import flet as ft
from views.menu import MenuView

def InicioView(page):

    page.clean()

    page.add(
        ft.Container(
            content=ft.Column(
                [


                        ft.Text(
                        "PAEC CETIS 61",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.CYAN_300
                    ),

                    ft.Image(
                        src="assets/logo_cetis61.jpg",  # Tu logo aquí
                        width=180,
                        height=180
                    ),

                    ft.Text(
                        "PROYECTO VIDA SALUDABLE",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    ),

                    ft.Divider(color=ft.Colors.CYAN_300),

                    ft.Text(
                        """
¡Qué gusto tenerte aquí!

Este espacio está pensado para ayudarte a comprender
cómo la alimentación, el descanso, la actividad física,
la salud emocional y los hábitos saludables influyen
en tu rendimiento académico y bienestar personal.

Explora cada asignatura y descubre información,
actividades y ejemplos que te ayudarán a construir
un estilo de vida más saludable.

Recuerda:
Tu salud es tu mejor herramienta para alcanzar tus metas.
                        """,
                        size=18,
                        color=ft.Colors.WHITE,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Button(
                        "Entrar al Proyecto",
                        on_click=lambda e: MenuView(page)
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            padding=30
        )
    )

    page.update()