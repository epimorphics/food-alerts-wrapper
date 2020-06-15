class Status:
    """
    Attributes:

        label (string): name of the status of the Alert, normally this will be 'Published' but in rare cases may be changed to 'Withdrawn'
    """
    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        # id is written @id in the API
        self.id = dict["@id"]

    def __getattr__(self, attribute):
        return None