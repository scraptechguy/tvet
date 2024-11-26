    def get_cosines(self, s=(1, 0, 0), o=(0, 0, 1)):
        self.s = np.array(s)
        self.o = np.array(o)
        self.alpha = np.arccos(np.dot(s, o))

        mu_i = []
        mu_e = []