from JsonReader import JsonReader
from CsvToJsonConverter import CsvToJsonConverter
from StudentFinder import StudentFinder

if __name__ == "__main__":
    csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
    json_path = "students_data.json"

    # Конвертація з CSV до JSON
    converter = CsvToJsonConverter()
    converter.read_and_convert(csv_url, json_path)

    # Створення об'єкта JsonReader та виклик методу для читання та відображення даних з JSON
    json_reader = JsonReader()

    # Пошук та виведення інформації про студентів
    finder = StudentFinder(json_reader)
    finder.load_data(json_path)
    surname_to_find = "Барченко"
    found_students = finder.find_students_by_surname(surname_to_find)
    finder.display_students_info(found_students)



