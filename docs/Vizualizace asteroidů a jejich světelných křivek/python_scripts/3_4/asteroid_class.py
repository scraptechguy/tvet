class Asteroid(object):
    def __init__(self, args=None, filename=None):
        self.args = args
        self.filename = filename
        
        self.vertices, self.faces = Load.load_obj(self.filename)
        self.size = np.max(self.vertices) - np.min(self.vertices)
        self.vertices *= 1.9 / self.size
        self.f_func = f_lambert

        self.get_geometry()
        self.get_cosines()
        self.get_fluxes()
        self.plot()