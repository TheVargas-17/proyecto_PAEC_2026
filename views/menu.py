import flet as ft

from views.socioemocional import mostrar_socioemocional
from views.humanidades import mostrar_humanidades
from views.organismos import mostrar_organismos
from views.historia import mostrar_historia
from views.matematicas import mostrar_matematicas
from views.movimiento import mostrar_movimiento


def MenuView(page):

    page.clean()

    def volver_menu(e):
        MenuView(page)

    def crear_tarjeta(titulo, imagen, accion):

        return ft.Container(
            content=ft.Column(
                [
                    ft.Image(
                        src=f"assets/{imagen}",
                        width=150,
                        height=120
                    ),

                    ft.Text(
                        titulo,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Button(
                        "Abrir",
                        on_click=accion
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            bgcolor=ft.Colors.BLUE_700,
            border_radius=15,
            padding=15,
            width=220
        )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "MENÚ PRINCIPAL",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Row(
                    [
                        crear_tarjeta(
                            "Socioemocional",
                            "socioemocional.jpg",
                            lambda e: mostrar_socioemocional(
                                page,
                                volver_menu
                            )
                        ),

                        crear_tarjeta(
                            "Humanidades",
                            "humanidades.jpg",
                            lambda e: mostrar_humanidades(
                                page,
                                volver_menu
                            )
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),

                ft.Row(
                    [
                        crear_tarjeta(
                            "Organismos",
                            "organismos.jpg",
                            lambda e: mostrar_organismos(
                                page,
                                volver_menu
                            )
                        ),

                        crear_tarjeta(
                            "Historia",
                            "historia.jpg",
                            lambda e: mostrar_historia(
                                page,
                                volver_menu
                            )
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),

                ft.Row(
                    [
                        crear_tarjeta(
                            "Matemáticas",
                            "matematicas.jpg",
                            lambda e: mostrar_matematicas(
                                page,
                                volver_menu
                            )
                        ),

                        crear_tarjeta(
                            "Movimiento",
                            "movimiento.jpg",
                            lambda e: mostrar_movimiento(
                                page,
                                volver_menu
                            )
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

    page.update()