import xml.etree.ElementTree as ET
from data_saver import DataSaver

class XmlSaver(DataSaver):
    def save(self, data: dict, filename: str):
        student_elem = ET.Element("student")

        ET.SubElement(student_elem, "full_name").text = data["full_name"]
        ET.SubElement(student_elem, "group_number").text = data["group_number"]

        real_perf_elem = ET.SubElement(student_elem, "real_performance")
        for subj, grade in zip(data["real_performance"]["subjects"], data["real_performance"]["grades"]):
            subj_elem = ET.SubElement(real_perf_elem, "subject", name=subj)
            subj_elem.text = str(grade)
        ET.SubElement(real_perf_elem, "average").text = str(data["real_performance"]["average"])

        desired_elem = ET.SubElement(student_elem, "desired_performance")
        for grade in data["desired_performance"]["desired_grades"]:
            grade_elem = ET.SubElement(desired_elem, "desired_grade")
            grade_elem.text = str(grade)
        ET.SubElement(desired_elem, "desired_average").text = str(data["desired_performance"]["desired_average"])

        tree = ET.ElementTree(student_elem)
        tree.write(filename, encoding="utf-8", xml_declaration=True)