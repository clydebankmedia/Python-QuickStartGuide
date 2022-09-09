class Distance:
    def __init__(self, km):
        self._km = km

    @property
    def km(self):
        return self._km

    @km.setter
    def km(self, value):
        self._km = value

    @property
    def miles(self):
        return self._km / 1.609

    @miles.setter
    def miles(self, value):
        self._km = value * 1.609
