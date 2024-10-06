from model.split.split import Split

class PercentSplit(Split):
    def __init__(self, user, percent):
        super().__init__(user)
        self._percent = percent

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, percent):
        self._percent = percent
