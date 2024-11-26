    def get_fluxes(self):
        phi_s = 1361. # W/m^2
        self.phi_i = phi_s * self.mu_i * self.nu_i

        f = []
        A_w = 0.23
        self.f_L = A_w/(4.0*np.pi)
        for i in range(len(self.mu_e)):
            f.append(self.f_func(self.f_L, self.mu_i[i], self.mu_e[i], self.alpha))
        self.f = np.array(f)

        self.I = self.f * self.phi_i
        self.phi_e = self.I * self.mu_e * self.nu_e

        self.total = np.sum(self.phi_e)