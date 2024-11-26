def f_lambert(f_L, mu_i, mu_e, alpha):
    return f_L

def f_lommel(f_L, mu_i, mu_e, alpha):
    if mu_i + mu_e > 0.0:
        return f_L / (mu_i + mu_e)
    else:
        return 0.0

def f_hapke(f_L, mu_i, mu_e, alpha):
    return Hapke.f_hapke(f_L, mu_i, mu_e, alpha)