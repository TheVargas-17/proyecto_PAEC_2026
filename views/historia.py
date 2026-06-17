import flet as ft

def mostrar_historia(page, volver_menu):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "CONCIENCIA HISTÓRICA III",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/historia.jpg",
                    width=450
                ),

                ft.Text(
                    """
Tema:
La evolución de la salud pública

A lo largo de la historia, las sociedades
han desarrollado estrategias para mejorar
la salud y la calidad de vida de las personas.
                    """,
                    size=18,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Divider(),

                ft.Text(
                    "LÍNEA DEL TIEMPO",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "SIGLO XIX",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                "Mejoras en los sistemas de drenaje, alcantarillado y saneamiento."
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.BLUE_300,
                    padding=15,
                    border_radius=10,
                    width=650
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "SIGLO XX",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                "Campañas de vacunación masiva y descubrimiento de antibióticos."
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.GREEN_300,
                    padding=15,
                    border_radius=10,
                    width=650
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "FINALES DEL SIGLO XX",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                "Promoción de hábitos saludables, nutrición y actividad física."
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.ORANGE_300,
                    padding=15,
                    border_radius=10,
                    width=650
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "ACTUALIDAD",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                "Uso de tecnología médica, prevención de enfermedades y educación para la salud."
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.PURPLE_300,
                    padding=15,
                    border_radius=10,
                    width=650
                ),

                ft.Divider(),

                ft.Text(
                    "IMPORTANCIA DE LA SALUD PÚBLICA",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Container(
                    content=ft.Text(
                        """
Gracias a estos avances, la esperanza de vida
ha aumentado considerablemente.

Actualmente contamos con vacunas, hospitales,
agua potable y programas de prevención que
ayudan a mejorar la calidad de vida de millones
de personas.
                        """,
                        size=18
                    ),
                    bgcolor=ft.Colors.BLUE_GREY_800,
                    padding=20,
                    border_radius=10,
                    width=700
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
La historia demuestra que los avances en la
medicina, la higiene y la prevención han sido
fundamentales para mejorar la salud de la población.

Gracias a estos cambios, las personas pueden
vivir más años y tener una mejor calidad de vida.
                    """,
                    size=18,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Button(
                    "Volver",
                    on_click=volver_menu
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            spacing=15
        )
    )

    page.update()