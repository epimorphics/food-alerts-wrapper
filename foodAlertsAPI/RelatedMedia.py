class RelatedMedia:
    """
    Attributes:

        title (string, optional): title for the related media
    """

    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)

        # id is written @id in the API
        try:
            self.id = dict["@id"]
        except KeyError:
            pass

    def __getattr__(self, attribute):
        return None