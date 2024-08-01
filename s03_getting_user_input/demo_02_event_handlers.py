import flet
from flet import IconButton, Page, Row, TextField, icons


def main(page: Page):
    page.title = 'Contador'
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER

    txt_numero = TextField(value='0', text_align='right', width=100)

    def reducir_clicked(event):
        
        numero = event.control.data - 1
        txt_numero.value = str(numero)
        event.control.data = numero 
        page.update()
    
    def aumentar_clicked(event):
        numero = event.control.data +  1
        txt_numero.value = str(numero)
        event.control.data = numero 
        page.update()
    
    page.add(
        Row(
            controls=[
                IconButton(icons.REMOVE, icon_color=flet.colors.AMBER, on_click=reducir_clicked, data= 0),
                txt_numero,
                IconButton(icons.ADD, icon_color= flet.colors.AMBER, on_click=aumentar_clicked, data= 0)
            ],
            alignment= flet.MainAxisAlignment.CENTER,
        )
    )


# Modo escritorio:
flet.app(target=main)
