        for normal in self.normals:
            mu_i.append(np.dot(s, normal))
            mu_e.append(np.dot(o, normal))
        
        self.mu_i = np.array(mu_i)
        self.mu_e = np.array(mu_e)

        self.mu_i = np.where(self.mu_i > 0.0, self.mu_i, 0.0)
        self.mu_e = np.where(self.mu_e > 0.0, self.mu_e, 0.0)

        self.nu_i = np.zeros((len(self.faces)))
        self.nu_e = np.zeros((len(self.faces)))

        Shadowing.shadowing_module.non(self.mu_i, self.mu_e, self.nu_i, self.nu_e)
        Shadowing.shadowing_module.nu(self.faces + 1, self.vertices, self.normals, self.centers, self.s, self.nu_i)
        Shadowing.shadowing_module.nu(self.faces + 1, self.vertices, self.normals, self.centers, self.o, self.nu_e)