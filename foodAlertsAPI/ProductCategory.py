class ProductCategory:
    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        # id is written @id in the API
        try:
            self.id = dict["@id"]
        except KeyError:
            pass