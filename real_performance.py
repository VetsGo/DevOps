from performance import Performance

class RealPerformance(Performance):
    def average_grade_per_subject(self):
        averages = {}
        for subject in self.get_subjects():
            grades = self.get_grades()[subject]
            averages[subject] = sum(grades) / len(grades) if grades else 0
        return averages

    def overall_average(self):
        all_averages = self.average_grade_per_subject()
        if not all_averages:
            return 0
        return sum(all_averages.values()) / len(all_averages)