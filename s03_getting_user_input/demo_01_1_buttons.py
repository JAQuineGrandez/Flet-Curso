import flet
from flet import ElevatedButton, Page


def main(page: Page):
    btn_icon_house = flet.IconButton(icon=flet.icons.HOME)
    btn_icon_logout= flet.IconButton(icon=flet.icons.LOGOUT)
    btn_icon_menu= flet.IconButton(icon=flet.icons.MENU)

    page.add(btn_icon_house, btn_icon_logout, btn_icon_menu)


# Modo Web:
flet.app(target=main, view=flet.WEB_BROWSER)
