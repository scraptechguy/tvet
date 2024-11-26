    def light_curve(self, n=100):
        s = self.s
        x, y, z = s
        total = []

        for i in range(n+1):
            gamma = 0 + 2.0*np.pi * i/n
            print("gamma = ", gamma/np.pi*180.0, " deg")

            x_ = x * np.cos(gamma) + y * np.sin(gamma)
            y_ = -x * np.sin(gamma) + y * np.cos(gamma)
            z_ = z

            s_ = np.array([x_, y_, z_])

            self.get_cosines(s=s_)
            self.get_fluxes()
            total.append((gamma, self.total))