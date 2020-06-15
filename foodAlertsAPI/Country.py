class Country:
    """
    Attributes:

        label (string): name of country for which the alert applies
    """

    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        # id is written @id in the API
        self.id = dict["@id"]

    def __getattr__(self, attribute):
        return None