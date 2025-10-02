from student import Student
from performance import Performance
from desired_performance import DesiredPerformance

class StudentData:
    def __init__(self, student: Student, real_performance: Performance, desired_performance: DesiredPerformance):
        self.__student = student
        self.__real_performance = real_performance
        self.__desired_performance = desired_performance

    def to_dict(self):
        return {
            "full_name": self.__student.get_full_name(),
            "group_number": self.__student.get_group_number(),
            "real_performance": {
                "subjects": self.__real_performance.get_subjects(),
                "grades": self.__real_performance.get_grades(),
                "average_per_subject": self.__real_performance.average_grade_per_subject(),
                "overall_average": self.__real_performance.overall_average()
            },
            "desired_performance": {
                "desired_grades": self.__desired_performance.get_grades(),
                "average_per_subject": self.__desired_performance.average_grade_per_subject(),
                "overall_average": self.__desired_performance.overall_average()
            }
        }