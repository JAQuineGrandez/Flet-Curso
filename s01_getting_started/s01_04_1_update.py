import time

import flet
from flet import Page, Text


def make_text(value):
    return Text(
        value= value,
        size = 20,
        color= flet.colors.AMBER_800,
        bgcolor= flet.colors.RED_800,
        
    )

def main(page: Page):
    
    columna = flet.Column()

    for i in range(10):
        columna.controls.append(
             make_text( f'Step: {i}')
        )
    
    page.add(columna) 


#Ejecución en el escritorio:
flet.app(target=main)