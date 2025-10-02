import xml.etree.ElementTree as ET
from data_saver import DataSaver

class XmlSaver(DataSaver):
    def save(self, data: dict, filename: str):
        student_elem = ET.Element("student")
        ET.SubElement(student_elem, "full_name").text = data["full_name"]
        ET.SubElement(student_elem, "group_number").text = data["group_number"]

        real_perf_elem = ET.SubElement(student_elem, "real_performance")
        for subj in data["real_performance"]["subjects"]:
            subj_elem = ET.SubElement(real_perf_elem, "subject", name=subj)
            grades_elem = ET.SubElement(subj_elem, "grades")
            for grade in data["real_performance"]["grades"][subj]:
                ET.SubElement(grades_elem, "grade").text = str(grade)
            ET.SubElement(subj_elem, "average").text = str(data["real_performance"]["average_per_subject"][subj])
        ET.SubElement(real_perf_elem, "overall_average").text = str(data["real_performance"]["overall_average"])

        desired_elem = ET.SubElement(student_elem, "desired_performance")
        for subj in data["real_performance"]["subjects"]:
            subj_elem = ET.SubElement(desired_elem, "subject", name=subj)
            grades_elem = ET.SubElement(subj_elem, "desired_grades")
            for grade in data["desired_performance"]["desired_grades"][subj]:
                ET.SubElement(grades_elem, "grade").text = str(grade)
            ET.SubElement(subj_elem, "average").text = str(data["desired_performance"]["average_per_subject"][subj])
        ET.SubElement(desired_elem, "overall_average").text = str(data["desired_performance"]["overall_average"])

        tree = ET.ElementTree(student_elem)
        tree.write(filename, encoding="utf-8", xml_declaration=True)