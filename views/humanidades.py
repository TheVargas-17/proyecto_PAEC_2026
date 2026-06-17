import flet as ft

def mostrar_humanidades(page, volver_menu):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "HUMANIDADES",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/humanidades.jpg",
                    width=400
                ),

                ft.Text(
                    """
Tema:
Valores para una vida saludable

Las humanidades permiten reflexionar sobre
la importancia de los valores en nuestra vida
diaria y en la convivencia con otras personas.
                    """,
                    size=18,
                    color=ft.Colors.WHITE
                ),

                ft.Divider(),

                ft.Text(
                    "VALORES FUNDAMENTALES",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Container(
                    content=ft.Text(
                        "RESPETO\n\nReconocer y valorar a todas las personas."
                    ),
                    bgcolor=ft.Colors.BLUE_300,
                    padding=10,
                    border_radius=10,
                    width=600
                ),

                ft.Container(
                    content=ft.Text(
                        "EMPATÍA\n\nComprender los sentimientos y necesidades de los demás."
                    ),
                    bgcolor=ft.Colors.GREEN_300,
                    padding=10,
                    border_radius=10,
                    width=600
                ),

                ft.Container(
                    content=ft.Text(
                        "SOLIDARIDAD\n\nApoyar a quienes necesitan ayuda y trabajar en equipo."
                    ),
                    bgcolor=ft.Colors.ORANGE_300,
                    padding=10,
                    border_radius=10,
                    width=600
                ),

                ft.Container(
                    content=ft.Text(
                        "RESPONSABILIDAD\n\nCumplir con nuestras obligaciones y cuidar nuestra salud."
                    ),
                    bgcolor=ft.Colors.PURPLE_300,
                    padding=10,
                    border_radius=10,
                    width=600
                ),

                ft.Divider(),

                ft.Text(
                    "IMPORTANCIA EN LA VIDA SALUDABLE",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Text(
                    """
Los valores ayudan a crear ambientes sanos
en la escuela, la familia y la comunidad.

Cuando practicamos el respeto, la empatía,
la solidaridad y la responsabilidad, mejoramos
nuestra convivencia y bienestar.
                    """,
                    size=18,
                    color=ft.Colors.WHITE
                ),

                ft.Divider(),

                ft.Text(
                    "CONCLUSIÓN",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Text(
                    """
Una vida saludable no depende solamente de la
alimentación o el ejercicio, también requiere
valores que favorezcan la convivencia y el
desarrollo personal.
                    """,
                    size=18,
                    color=ft.Colors.WHITE
                ),

                ft.Button(
                    "Volver",
                    on_click=volver_menu
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO
        )
    )

    page.update()