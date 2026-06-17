import flet as ft

def mostrar_movimiento(page, volver_menu):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "MOVIMIENTO Y ESTABILIDAD",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/movimiento.jpg",
                    width=450
                ),

                ft.Text(
                    "CANCELACIÓN ACTIVA DE RUIDO (ANC)",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Text(
                    """
La cancelación activa de ruido (ANC) es una
tecnología utilizada en audífonos modernos
para disminuir los sonidos del entorno y
mejorar la experiencia auditiva.
                    """,
                    size=18,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Divider(),

                ft.Text(
                    "PROCESO PASO A PASO",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "1. Captura del sonido",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                "Los micrófonos externos detectan el ruido ambiental."
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
                                "2. Procesamiento",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                "El sistema analiza la frecuencia y amplitud del sonido detectado."
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.INDIGO_300,
                    padding=15,
                    border_radius=10,
                    width=650
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "3. Interferencia destructiva",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                "Se genera una onda opuesta con un desfase de 180° para cancelar el ruido."
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.PURPLE_300,
                    padding=15,
                    border_radius=10,
                    width=650
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "4. Resultado",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                "Las ondas se anulan entre sí y el usuario escucha menos ruido exterior."
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.GREEN_300,
                    padding=15,
                    border_radius=10,
                    width=650
                ),

                ft.Divider(),

                ft.Text(
                    "EXPLICACIÓN FÍSICA",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Container(
                    content=ft.Text(
                        """
La cancelación activa de ruido funciona gracias
al principio de superposición de ondas.

Cuando dos ondas sonoras poseen la misma
amplitud pero fases opuestas, se produce
una interferencia destructiva.

Como resultado, el ruido disminuye
considerablemente y mejora la calidad del sonido.
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
La cancelación activa de ruido es una aplicación
real de la física de ondas.

Gracias a la interferencia destructiva, los
audífonos modernos pueden reducir el ruido
ambiental y ofrecer una mejor experiencia
auditiva a los usuarios.
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