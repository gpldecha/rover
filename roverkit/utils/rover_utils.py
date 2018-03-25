class Rc:

    def __init__(self, rc_min, rc_max):
        self.rc_min = rc_min
        self.rc_max = rc_max
        self.v_min = -1.0
        self.v_max = 1.0
        self.rc_value = None
        self.set_value(0.0)

    def set_value(self, value):
        self.rc_value = int(linear_scaling(value, self.v_min, self.v_max,  self.rc_min, self.rc_max))


def linear_scaling(v, vmin, vmax, dmin, dmax):
    if v < vmin: return dmin
    if v > vmax: return dmax
    return (v - vmin)/(vmax - vmin)*(dmax - dmin) + dmin
