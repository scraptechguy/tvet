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