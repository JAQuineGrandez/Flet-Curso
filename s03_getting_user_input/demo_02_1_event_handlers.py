import flet as ft

def main(page: ft.Page):
    page.title = "Identify Control Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    # Función que maneja el evento de clic
    def handle_click(event):
        clicked_button = event.control.data
        print(clicked_button)

    # Crear dos botones con diferentes IDs
    button1 = ft.IconButton(
        icon=ft.icons.ADD,
        on_click=handle_click,
        data=1
    )
    
    button2 = ft.IconButton(
        icon=ft.icons.REMOVE,
        on_click=handle_click,
        data = 2
    )

    # Agregar los botones a la página
    page.add(button1)
    page.add(button2)
    page.update()

ft.app(target=main)
