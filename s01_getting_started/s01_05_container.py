import flet
from flet import Page, Row, Text


def main(page: Page):
    lenguajes = ['Python', 'Flet', 'Flutter']
    etiquetas = []

    for e in lenguajes:
        etiquetas.append(Text(value=e, size= 30, weight= flet.FontWeight.BOLD, color= flet.colors.AMBER_ACCENT, bgcolor= flet.colors.PINK))

    row_datos = Row(controls=etiquetas)

    page.add(row_datos)


# Ejecución en el escritorio:
flet.app(target=main)
