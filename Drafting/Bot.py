class Bot:
    _default_order = [5, 4, 3, 1, 2]
    _off_lane_priority_order = [5, 1, 2, 4, 3]
    _safe_lane_priority_order = [4, 3, 2, 5, 1]
    _early_cores_order = [1, 2, 3, 4, 5]
    _mid_lane_priority_order = [3, 4, 5, 1, 2]

    def __init__(self):
        self.positions = [1, 2, 3, 4, 5]