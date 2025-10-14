# DevOps CLI Tools

Невеликий набір CLI-інструментів для демонстрації трьох підходів:

1) sys.argv `sys_tool.py`: Простий скрипт, що друкує повідомлення лише при прямому запуску
2) Click `click_tool.py`: CLI-команда `say` з опцією `--name`
3) Fire `fire_expose.py`: Автоматичний CLI для функцій з `utils.py`

## Приклади

# 1. sys_tool
python src/sys_tool.py: командна строка
python src/sys_tool.py --help: При використанні інструменту python src/sys_tool.py Друкує 'командна строка' лише при запуску напряму.

# 2. click_tool
python src/click_tool.py say --name Alice: Alice
python src/click_tool.py say --name peter: Ім’я не підходить

# 3. fire_expose
python src/fire_expose.py greet Alice: Привіт, Alice!
python src/fire_expose.py goodbye Bob: До побачення, Bob!