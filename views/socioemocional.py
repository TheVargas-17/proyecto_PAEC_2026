import flet as ft


def mostrar_socioemocional(page, volver_menu):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "DESARROLLO SOCIOEMOCIONAL",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/socioemocional.jpg",
                    width=400
                ),

                ft.Text(
                    """
Tema:
Salud emocional y bienestar personal

La salud socioemocional nos ayuda a reconocer,
comprender y manejar nuestras emociones para
mantener relaciones sanas y alcanzar nuestras metas.
                    """,
                    size=18,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Divider(),

                ft.Text(
                    "IMPORTANCIA DE LA SALUD EMOCIONAL",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "1. AUTOCONOCIMIENTO",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Text(
                                "Reconocer nuestras emociones y entender cómo influyen en nuestras acciones."
                            ),

                            ft.Text(
                                "Permite tomar mejores decisiones."
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.BLUE_300,
                    padding=10,
                    border_radius=10,
                    width=650
                ),

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "2. AUTOCONTROL",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Text(
                                "Aprender a manejar emociones como el enojo, la tristeza o la frustración."
                            ),

                            ft.Text(
                                "Ayuda a reaccionar de manera positiva."
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
                                "3. EMPATÍA",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Text(
                                "Comprender los sentimientos y necesidades de otras personas."
                            ),

                            ft.Text(
                                "Favorece la convivencia y el respeto."
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
                                "4. RELACIONES SALUDABLES",
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Text(
                                "Mantener una comunicación respetuosa y resolver conflictos pacíficamente."
                            ),

                            ft.Text(
                                "Fortalece amistades y trabajo en equipo."
                            ),
                        ]
                    ),
                    bgcolor=ft.Colors.PURPLE_300,
                    padding=10,
                    border_radius=10,
                    width=650
                ),

                ft.Divider(),

                ft.Text(
                    "CONSEJOS PARA CUIDAR TU SALUD EMOCIONAL",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Text(
                    """
• Dormir al menos 8 horas diarias.

• Realizar actividad física regularmente.

• Mantener una alimentación saludable.

• Hablar con personas de confianza cuando tengas problemas.

• Organizar tus tiempos de estudio y descanso.

• Practicar ejercicios de respiración y relajación.

• Evitar el estrés excesivo.
                    """,
                    size=18,
                    color=ft.Colors.WHITE
                ),

                ft.Divider(),

                ft.Text(
                    "BENEFICIOS EN EL RENDIMIENTO ACADÉMICO",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Text(
                    """
• Mayor concentración en clases.

• Mejor memoria y aprendizaje.

• Más motivación para estudiar.

• Menor ansiedad durante exámenes.

• Mejor convivencia escolar.
                    """,
                    size=18,
                    color=ft.Colors.WHITE
                ),

                ft.Divider(),

                ft.Text(
                    "REFLEXIÓN",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.CYAN
                ),

                ft.Text(
                    """
"Cuidar nuestras emociones es tan importante
como cuidar nuestro cuerpo. Una mente sana
nos ayuda a alcanzar nuestras metas y disfrutar
cada etapa de nuestra vida."
                    """,
                    size=18,
                    color=ft.Colors.WHITE,
                    italic=True,
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