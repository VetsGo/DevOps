from student import Student
from real_performance import RealPerformance
from desired_performance import DesiredPerformance
from student_data import StudentData
from formats.json_saver import JsonSaver
from formats.xml_saver import XmlSaver
from formats.csv_saver import CsvSaver

def main():
    student = Student("Ridkovets Serhii", "PD-51")

    subjects = ["Math", "Physics", "DevOps", "C#"]
    grades = {
        "Math": [85, 90, 88, 95],
        "Physics": [90, 92, 89, 95],
        "DevOps": [84, 86, 56, 76],
        "C#": [96, 98, 94, 100, 100]
    }
    real_perf = RealPerformance(subjects, grades)

    desired_grades = {
        "Math": [95, 98],
        "Physics": [100, 98],
        "DevOps": [92, 95],
        "C#": [100, 100]
    }
    desired_averages = {
        "Math": 96,
        "Physics": 99,
        "DevOps": 93,
        "C#": 100
    }
    desired_overall = 97
    desired_perf = DesiredPerformance(subjects, desired_grades, desired_averages, desired_overall)

    student_data = StudentData(student, real_perf, desired_perf)
    data_dict = student_data.to_dict()

    base_filename = f"{student.get_full_name().replace(' ', '_')}_{student.get_group_number()}"
    JsonSaver().save(data_dict, base_filename + ".json")
    XmlSaver().save(data_dict, base_filename + ".xml")
    CsvSaver().save(data_dict, base_filename + ".csv")

if __name__ == "__main__":
    main()