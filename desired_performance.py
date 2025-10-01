from performance import Performance

class DesiredPerformance(Performance):
    def __init__(self, subjects: list[str], grades: list[float], desired_average: float):
        super().__init__(subjects, grades)
        self.__desired_average = desired_average

    def average_grade(self):
        return self.__desired_average