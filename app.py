import flet as ft

def app(page: ft.Page):
    page.title = "История приветствий"
    
    try:
        history = [line.strip() for line in open("history.txt").readlines()]
    except FileNotFoundError:
        history = []

    history = history[-5:]
    
    history_text = ft.Text("\n".join(history))

    def save_and_update(e):
        name = input_field.value.strip()
        if name:
            history.append(name)
           
            history[:] = history[-5:]
            open("history.txt", "w").write("\n".join(history))
            history_text.value = "\n".join(history)
            input_field.value = ""
        page.update()

    input_field = ft.TextField(hint_text="Имя", on_submit=save_and_update, width=200)
    send_btn = ft.IconButton(ft.Icons.SEND, on_click=save_and_update)

    page.add(ft.Row([input_field, send_btn]), history_text)

ft.run(app, view=ft.AppView.WEB_BROWSER)

