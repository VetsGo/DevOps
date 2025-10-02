from performance import Performance

class DesiredPerformance(Performance):
    def __init__(self, subjects: list[str], grades: dict[str, list[float]], desired_averages: dict[str, float], desired_overall: float):
        super().__init__(subjects, grades)
        self.__desired_averages = desired_averages
        self.__desired_overall = desired_overall

    def average_grade_per_subject(self):
        return self.__desired_averages

    def overall_average(self):
        return self.__desired_overall