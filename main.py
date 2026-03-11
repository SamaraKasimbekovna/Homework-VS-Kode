from datetime import datetime

# Запрос имени один раз
name = input("Введите имя: ")

# Получение текущей даты и времени
now = datetime.now()
formatted_time = now.strftime("%Y:%m:%d - %H:%M:%S")

# Вывод сообщения один раз
print(f"{formatted_time} - Привет, {name}!")
