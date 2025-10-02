import csv
from data_saver import DataSaver

class CsvSaver(DataSaver):
    def save(self, data: dict, filename: str):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Full Name", "Group", "Subject", "Grades", "Average", "Desired Grades", "Desired Average", "Overall Average", "Desired Overall"])

            for subj in data["real_performance"]["subjects"]:
                writer.writerow([
                    data["full_name"],
                    data["group_number"],
                    subj,
                    ";".join(map(str, data["real_performance"]["grades"][subj])),
                    data["real_performance"]["average_per_subject"][subj],
                    ";".join(map(str, data["desired_performance"]["desired_grades"][subj])),
                    data["desired_performance"]["average_per_subject"][subj],
                    data["real_performance"]["overall_average"],
                    data["desired_performance"]["overall_average"]
                ])