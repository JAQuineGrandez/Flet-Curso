import flet
from flet import Column, ElevatedButton, Page, Text, TextField


def main(page: Page):
    txt_first_name = flet.Ref[TextField]()
    txt_last_name  = flet.Ref[TextField]()
    col_controles  = flet.Ref[Column]()
    btn_saludar    = flet.Ref[ElevatedButton]()
    

    def saludar_clicked(event):
        col_controles.current.controls.append(Text(f'¡Hola, {txt_first_name.current.value} {txt_last_name.current.value}!'))

        txt_first_name.current.value = ''
        txt_last_name.current.value = ''
        btn_saludar.current.data += 1
        btn_saludar.current.text = str(btn_saludar.current.data)

        page.update()
        txt_first_name.current.focus()


    page.add(
        TextField(ref=txt_first_name, label='Nombre', autofocus=True),
        TextField(ref=txt_last_name, label='Apellido'),
        ElevatedButton(ref = btn_saludar, text= "Saludar", on_click= saludar_clicked, data= 1),
        Column(ref=col_controles)
    )


# Ejecución de la aplicación en modo escritorio:
flet.app(target=main)
