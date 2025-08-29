from abc import abstractmethod, ABC


class GraderBase(ABC):
    def __init__(self):
        self._grade = "NORMAL"

    @abstractmethod
    def set_grade(self, points):
        pass

    @abstractmethod
    def is_removed(self):
        pass

    @property
    def grade(self):
        return self._grade

class GraderNormal(GraderBase):
    def __init__(self):
        super().__init__()

    def set_grade(self, points):
        if points >= 50:
            self._grade = "GOLD"
        elif points >= 30:
            self._grade = "SILVER"
        else:
            self._grade = "NORMAL"

    def is_removed(self):
        return self.grade not in ("GOLD", "SILVER")