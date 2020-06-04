class HazardCategory:
    def __init__(self):
        for k, v in dict.items():
            setattr(self, k, v)
