import flet
from flet import Column, ElevatedButton, Page, Text, TextField


def main(page: Page):
    
    txt_first_name = flet.Ref[TextField]()
    txt_last_name  = flet.Ref[TextField]()
    btn_saludar    = flet.Ref[ElevatedButton]()
    col_controles  = flet.Ref[Column]()
    
    def submit_firstname(event):
        if not txt_first_name.current.value :
            txt_first_name.current.focus()
            return
        
        txt_last_name.current.focus()
        
    def submit_lastname(event):
        if not txt_last_name.current.value :
            txt_last_name.current.focus()
            return
        
        btn_saludar.current.focus()
    


    def saludar_clicked(event):
        col_controles.current.controls.append(Text(f'¡Hola, {txt_first_name.current.value} {txt_last_name.current.value}!'))

        txt_first_name.current.value = ''
        txt_last_name.current.value = ''

        page.update()
        txt_first_name.current.focus()


    page.add(
        TextField(ref=txt_first_name, label='Nombre', autofocus=True, on_submit= submit_firstname),
        TextField(ref=txt_last_name, label='Apellido', on_submit= submit_lastname),
        ElevatedButton(ref=btn_saludar,text='Saludar', on_click=saludar_clicked),
        Column(ref=col_controles)
    )


# Ejecución de la aplicación en modo escritorio:
flet.app(target=main)
