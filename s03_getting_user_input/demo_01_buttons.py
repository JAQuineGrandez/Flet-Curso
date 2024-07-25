import flet
from flet import ElevatedButton, Page


def main(page: Page):
    btn_accion = ElevatedButton('¡Click!')
    btn_cancelar = flet.Ref[ElevatedButton]()

    page.add(btn_accion, ElevatedButton(ref= btn_cancelar, text="Cancelar"))


# Modo Web:
flet.app(target=main, view=flet.WEB_BROWSER)
