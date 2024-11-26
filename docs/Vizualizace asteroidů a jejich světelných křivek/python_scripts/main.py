#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import tkinter
import tkinter.filedialog
import numpy as np
import vispy
import vispy.app
import vispy.scene
import vispy.visuals

def load_obj(filename, debug=False):
    '''Load a Wavefront OBJ file.''' 
    
    node = []
    face = []

    f = open(filename, "r")

    for line in f.readlines(): 
        if len(line) == 0:
            continue
        elif line[0] == '#': 
            continue

        l = line.split()
        
        if l[0] == 'v':
            node.append(list(map(float, l[1:])))
        elif l[0] == 'f':
            face.append(list(map(lambda x: int(x) - 1, l[1:])))

    f.close()

    if debug:
        print("number of nodes = " + str(len(node)) + ", beginning with node " + str(node[0]))
        print("number of faces = " + str(len(face)) + ", beginning with face " + str(face[0]))

    return np.array(node), np.array(face)

class Asteroid(object):
    def __init__(self, filename=None, args=None):
        self.args = args
        self.filename = filename
        self.vertices, self.faces = load_obj(self.filename)
        self.size = np.max(self.vertices) - np.min(self.vertices)
        self.vertices *= 2 / self.size

        self.get_properties()
        self.get_illumination(s=(0.5, 1, 0))
        self.plot()

    def get_properties(self):
        self.centers = []
        self.normals = []

        for face in self.faces:
            A = self.vertices[face[0]]
            B = self.vertices[face[1]]
            C = self.vertices[face[2]]

            T = 1/3 * (A + B + C)
            a = B - C
            b = C - A
            n = np.cross(a, b)
            n /= np.sqrt(np.dot(n, n))

            self.centers.append(T)
            self.normals.append(n)

        self.centers = np.array(self.centers)
        self.normals = np.array(self.normals)

    def get_illumination(self, s=(1, 0, 0)):
        self.s = s

        self.mu_i = []
        for normal in self.normals:
            self.mu_i.append(np.dot(s, normal))
        self.mu_i = np.array(self.mu_i)

        phi_s = 1361. # W/m^2
        self.phi_i = phi_s * self.mu_i
        self.phi_i = np.where(self.phi_i > 0.0, self.phi_i, 0.0)

    def plot(self):
        self.canvas = vispy.scene.SceneCanvas(keys='interactive')
        self.canvas.size = 1920, 1080
        self.view = self.canvas.central_widget.add_view()

        color = np.array([1, 1, 1]) / np.max(self.phi_i)
        face_colors = []
        for face in self.phi_i:
            face_colors.append(face * color)
        # mesh = vispy.scene.visuals.Mesh(self.vertices, self.faces, color='gray')
        mesh = vispy.scene.visuals.Mesh(self.vertices, self.faces, color='gray')
        mesh.transform = vispy.scene.transforms.MatrixTransform()
        self.view.add(mesh)

        '''
        n = np.size(self.centers, axis=0)
        connect = np.concatenate((np.arange(0, n), np.arange(n, 2 * n)))
        print(connect)
        pos = np.array([self.centers, self.centers + 1 * self.normals])
        print(pos)
        '''

        pos = np.array([self.centers, self.centers + 0.1 * self.normals])
        connect = []
        n = len(self.centers)
        for i in range(n):
            connect.append(np.array([i, n + i]))

        normals = vispy.scene.visuals.Line(pos=pos, connect=np.array(connect), color='white', parent=self.view.scene)
        normals.visible = False
        # text = vispy.scene.visuals.Text(str(i), pos=self.centers[i], font_size=10, color='white')
        # self.view.add(text)

        vispy.scene.visuals.Text("'e' to hide edges", anchor_x='left', pos=(20, 20), font_size=10,
                            color='white', parent=self.canvas.scene)
        vispy.scene.visuals.Text("'f' to hide faces", anchor_x='left', pos=(20, 40), font_size=10,
                            color='white', parent=self.canvas.scene)
        vispy.scene.visuals.Text("'s' to change scattering", anchor_x='left', pos=(20, 60), font_size=10,
                            color='white', parent=self.canvas.scene)
        vispy.scene.visuals.Text("'n' to show normals", anchor_x='left', pos=(20, 80), font_size=10,
                            color='white', parent=self.canvas.scene)
        vispy.scene.visuals.Text("'q' to quit", anchor_x='left', pos=(20, 100), font_size=10,
                            color='white', parent=self.canvas.scene)
        
        vispy.scene.visuals.Text("Number of vertices: %d" %(len(self.vertices)), anchor_x='left', pos=(20, 140), font_size=10,
                            color='white', parent=self.canvas.scene)
        vispy.scene.visuals.Text("Number of faces: %d" %(len(self.faces)), anchor_x='left', pos=(20, 160), font_size=10,
                            color='white', parent=self.canvas.scene)
        vispy.scene.visuals.Text("Asteroid size: %f" %(self.size), anchor_x='left', pos=(20, 180), font_size=10,
                            color='white', parent=self.canvas.scene)
        
        vispy.scene.visuals.XYZAxis(parent=self.view.scene)

        shading_filter = vispy.visuals.filters.ShadingFilter(\
            shading= 'smooth',
            shininess=self.args.shininess,\
            ambient_coefficient = 0.0,\
            diffuse_coefficient = 1.0,\
            specular_coefficient = 0.0,\
            ambient_light = 'white',\
            diffuse_light = 'white',\
            specular_light = 'white',\
            )
        mesh.attach(shading_filter)

        wireframe_filter = vispy.visuals.filters.WireframeFilter(\
            width=self.args.wireframe_width,\
            color='green',\
            wireframe_only = False,\
            faces_only = True,\
            enabled= False,\
            )
        mesh.attach(wireframe_filter)

        self.view.camera = vispy.scene.cameras.TurntableCamera(center=(0, 0, 0))
        self.view.camera.depth_value = 1e3

        light_dir = self.s
        shading_filter.light_dir = light_dir[:3]

        @self.canvas.events.key_press.connect
        def on_key_press(event):

            if event.key in ['q', 'Q']:
                vispy.app.quit()

            elif event.key == '1':
                shading_filter.shading = None
                wireframe_filter.enabled = False
                mesh.update()

            elif event.key == '2':
                shading_filter.shading = 'flat'
                wireframe_filter.enabled = True
                wireframe_filter.wireframe_only = True
                wireframe_filter.faces_only = False
                mesh.update()

            elif event.key == '3':
                shading_filter.shading = 'smooth'
                wireframe_filter.enabled = False
                mesh.update()

            elif event.key == '4':
                shading_filter.shading = 'flat'
                wireframe_filter.enabled = True
                wireframe_filter.wireframe_only = False
                wireframe_filter.faces_only = False
                normals.visible = True
                mesh.update()

        self.canvas.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shininess', default=100)
    parser.add_argument('--wireframe-width', default=1)
    args, _ = parser.parse_known_args()

    root = tkinter.Tk()
    root.withdraw()
    filename = tkinter.filedialog.askopenfilename()

    def check_filetype():
        for index, character in enumerate(filename):
            if character == ".":
                if filename[index+1:] == "obj":
                    return True
                else:
                    return False

    right_filetype = check_filetype()

    if filename == '':
        print("NO FILE WAS SELECTED")
        vispy.app.quit()
    elif right_filetype == False:
        print("NEEDS TO BE AN .OBJ FILE")
        vispy.app.quit()
    else:
        # filename = "src/sample_files/tri_file_octdecv_1.obj"
        asteroid = Asteroid(filename=filename, args=args)
        vispy.app.run()

if __name__ == "__main__":
    main()