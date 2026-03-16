import flet as ft
from datetime import datetime

history = []

def main(page: ft.Page):
    input_field = ft.TextField(label="Введите имя", width=300)
    plain_text = ft.Text()

    def update():
        plain_text.value = "\n".join(history)
        page.update()

    send_btn = ft.ElevatedButton("OK", on_click=lambda e: add_name())
    delete_btn = ft.ElevatedButton("Удалить последнее", on_click=lambda e: delete_last())
    sort_btn = ft.ElevatedButton("Сортировать по алфавиту", on_click=lambda e: sort_history())

    def add_name():
        name = input_field.value.strip()
        if name:
            history.append(f"{datetime.now():%Y:%m:%d - %H:%M:%S} - Привет, {name}!")
            input_field.value = ""
        update()

    def delete_last():
        if history: history.pop()
        else: plain_text.value = "История пуста!"
        update()

    def sort_history():
        if history: history.sort()
        else: plain_text.value = "История пуста!"
        update()

    page.add(ft.Row([input_field, send_btn]), ft.Row([delete_btn, sort_btn]), plain_text)

ft.run(main, view=ft.AppView.WEB_BROWSER)