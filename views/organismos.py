import flet as ft

def mostrar_organismos(page, volver_menu):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "ORGANISMOS, ESTRUCTURAS Y PROCESOS",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/organismos.jpg",
                    width=400
                ),

                ft.Text(
                    """
Tema:
Proceso de alimentación y nutrición

El cuerpo humano necesita nutrientes,
agua, descanso y actividad física para
funcionar correctamente.
                    """,
                    size=18,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Divider(),

                ft.Text(
                    "ETAPAS DEL PROCESO DIGESTIVO",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "1. INGESTIÓN",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Text(
                                "Los alimentos entran por la boca y comienzan a triturarse con los dientes."
                            ),

                            ft.Text(
                                "Duración aproximada: 5 a 10 segundos"
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.ORANGE_300,
                    padding=10,
                    border_radius=10,
                    width=650
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "2. DIGESTIÓN",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Text(
                                "El estómago utiliza jugos gástricos para descomponer los alimentos."
                            ),

                            ft.Text(
                                "Duración aproximada: 2 a 4 horas"
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.RED_300,
                    padding=10,
                    border_radius=10,
                    width=650
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "3. ABSORCIÓN",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Text(
                                "Los nutrientes pasan al torrente sanguíneo a través del intestino delgado."
                            ),

                            ft.Text(
                                "Duración aproximada: 4 a 6 horas"
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.GREEN_300,
                    padding=10,
                    border_radius=10,
                    width=650
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "4. EGESTIÓN",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Text(
                                "El intestino grueso compacta los desechos que el cuerpo no puede aprovechar para su posterior eliminación."
                            ),

                            ft.Text(
                                "Duración aproximada: 12 a 48 horas"
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.BROWN_300,
                    padding=10,
                    border_radius=10,
                    width=650
                ),

                ft.Divider(),

                ft.Text(
                    "DATOS INTERESANTES",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Text(
                    """
• El intestino delgado mide aproximadamente 6 metros.

• El proceso digestivo completo puede durar entre 24 y 72 horas.

• Beber suficiente agua ayuda al sistema digestivo.

• Una alimentación saludable mejora el rendimiento escolar.

• El estómago puede expandirse hasta almacenar aproximadamente 1.5 litros de alimento.
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
El sistema digestivo transforma los alimentos
en nutrientes que el cuerpo utiliza para obtener
energía, crecer y mantenerse saludable.

Una alimentación equilibrada favorece el buen
funcionamiento del organismo y mejora el
rendimiento académico.
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
            scroll=ft.ScrollMode.AUTO
        )
    )

    page.update()