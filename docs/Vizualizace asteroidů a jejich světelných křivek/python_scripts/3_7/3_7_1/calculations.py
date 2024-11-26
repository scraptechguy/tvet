    # Stredy stran
    a = np.array(abs(B - C))
    b = np.array(abs(C - A))
    c = np.array(abs(A - B))

    # Teziste a normala
    T = 1.0/3.0 * (A + B + C)
    n = np.cross(a, b)
    n = n / np.sqrt(np.dot(n, n))