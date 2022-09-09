class Distance:
    def __init__(self, km):
        self._km = km
    @property
    def km(self):
        return self._km
    @property
    def miles(self):
        return self._km / 1.609

distance2 = Distance(3)
print(str(distance2.km))
print(str(distance2.miles))
