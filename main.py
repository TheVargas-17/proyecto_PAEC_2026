import flet as ft
from views.inicio import InicioView

def main(page: ft.Page):

    page.title = "PAEC CETIS 61"
    page.window_width = 1000
    page.window_height = 700
    page.bgcolor = "#0F172A"
    page.scroll = ft.ScrollMode.AUTO

    InicioView(page)

ft.app(target=main)