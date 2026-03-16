
import flet as ft
from datetime import datetime


def main(page: ft.Page):

    def hello(e):
        if name.value:
            time = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
            result.value = f"{time} - Привет, {name.value}!"
            page.update()

    name = ft.TextField(label="Введите имя", on_submit=hello)
    btn = ft.ElevatedButton("OK", on_click=hello)
    result = ft.Text()

    page.add(name, btn, result)


ft.run(main, view=ft.AppView.WEB_BROWSER)