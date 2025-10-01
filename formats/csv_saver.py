import csv
from data_saver import DataSaver

class CsvSaver(DataSaver):
    def save(self, data: dict, filename: str):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow(["Full Name", "Group", "Subject", "Grade", "Average", "Desired Grade", "Desired Average"])

            for subj, grade in zip(data["real_performance"]["subjects"], data["real_performance"]["grades"]):
                writer.writerow([
                    data["full_name"],
                    data["group_number"],
                    subj,
                    grade,
                    data["real_performance"]["average"],
                    ";".join(map(str, data["desired_performance"]["desired_grades"])),
                    data["desired_performance"]["desired_average"]
                ])