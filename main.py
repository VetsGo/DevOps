from student import Student
from performance import Performance
from desired_performance import DesiredPerformance
from student_data import StudentData
from formats.json_saver import JsonSaver
from formats.xml_saver import XmlSaver
from formats.csv_saver import CsvSaver

class RealPerformance(Performance):
    def average_grade(self):
        grades = self.get_grades()
        if not grades:
            return 0
        return sum(grades) / len(grades)

def main():
    # Студент
    student = Student("Ridkovets Serhii", "PD-51")

    # Успішність
    subjects = ["Math", "Physics", "DevOps", "C#"]
    grades = [85, 90, 84, 96]
    real_perf = RealPerformance(subjects, grades)

    # Бажана успішність
    desired_grades = [95, 100, 92, 100]
    desired_average = 98
    desired_perf = DesiredPerformance(subjects, desired_grades, desired_average)

    # Отримання даних
    student_data = StudentData(student, real_perf, desired_perf)
    data_dict = student_data.to_dict()

    # Створення файлів з даними трьох форматів
    base_filename = f"{student.get_full_name().replace(' ', '_')}_{student.get_group_number()}"
    JsonSaver().save(data_dict, base_filename + ".json")
    XmlSaver().save(data_dict, base_filename + ".xml")
    CsvSaver().save(data_dict, base_filename + ".csv")

if __name__ == "__main__":
    main()