class PathogenRisk:
    def __init__(self):
        for k, v in dict.items():
            setattr(self, k, v)

        # id is written @id in the APi
        self.id = dict["@id"]
