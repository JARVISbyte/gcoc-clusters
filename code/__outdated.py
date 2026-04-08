def rotate(x: np.array, y: np.array, angle_tan: float, y_int: float = 0):
    cosine = 1/np.sqrt(1 + angle_tan**2)
    sinus = 1/np.sqrt(1 + (1/angle_tan)**2) * (-1 if angle_tan < 0 else 1)

    return x*cosine - y*sinus, x*sinus + y*cosine


x1, _ = rotate(bp_rp, g_mag, slope)
x1_min, x1_max = np.quantile((0.2, 0.8), x1)

x_min, x_max = rotate(())