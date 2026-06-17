import flet as ft
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import tempfile

def mostrar_matematicas(page, volver_menu):

    page.clean()

    alumnos = []

    nombre = ft.TextField(
        label="Nombre del alumno",
        width=300
    )

    horas = ft.TextField(
        label="Horas de sueño",
        width=300
    )

    promedio = ft.TextField(
        label="Promedio escolar",
        width=300
    )

    resultado = ft.Text(
        "",
        color=ft.Colors.YELLOW
    )

    tabla = ft.Column()

    def mostrar_grafica(e):

        if len(alumnos) < 2:

            resultado.value = (
                "Debes registrar al menos 2 alumnos"
            )

            page.update()
            return

        horas_sueno = []
        promedios = []

        for alumno in alumnos:

            horas_sueno.append(alumno["horas"])
            promedios.append(alumno["promedio"])

        plt.figure(figsize=(6,4))

        plt.plot(
            horas_sueno,
            promedios,
            marker="o"
        )

        plt.title(
            "Horas de Sueño vs Promedio"
        )

        plt.xlabel(
            "Horas de Sueño"
        )

        plt.ylabel(
            "Promedio Escolar"
        )

        plt.grid(True)

        archivo = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        plt.savefig(archivo.name)

        plt.close()

        ruta_imagen = archivo.name

        page.clean()

        page.add(
            ft.Column(
                [
                    ft.Text(
                        "GRÁFICA DE RESULTADOS",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    ),

                    ft.Image(
                        src=ruta_imagen,
                        width=700
                    ),

                    ft.Button(
                        "Volver",
                        on_click=lambda e: mostrar_matematicas(
                            page,
                            volver_menu
                        )
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        page.update()

        

    def actualizar_tabla():

        tabla.controls.clear()

        tabla.controls.append(
            ft.Row(
                [
                    ft.Text("Nombre", width=150, weight=ft.FontWeight.BOLD),
                    ft.Text("Horas", width=80, weight=ft.FontWeight.BOLD),
                    ft.Text("Promedio", width=100, weight=ft.FontWeight.BOLD),
                ]
            )
        )

        for alumno in alumnos:

            tabla.controls.append(
                ft.Row(
                    [
                        ft.Text(alumno["nombre"], width=150),
                        ft.Text(str(alumno["horas"]), width=80),
                        ft.Text(str(alumno["promedio"]), width=100),
                    ]
                )
            )

    def agregar_alumno(e):

        try:

            alumnos.append(
                {
                    "nombre": nombre.value,
                    "horas": float(horas.value),
                    "promedio": float(promedio.value)
                }
            )

            actualizar_tabla()

            nombre.value = ""
            horas.value = ""
            promedio.value = ""

            resultado.value = "Alumno agregado correctamente"

            page.update()

        except:

            resultado.value = "Datos inválidos"

            page.update()

    def calcular_tasa(e):

        if len(alumnos) < 2:

            resultado.value = (
                "Debes registrar al menos 2 alumnos"
            )

            page.update()
            return

        x1 = alumnos[0]["horas"]
        y1 = alumnos[0]["promedio"]

        x2 = alumnos[-1]["horas"]
        y2 = alumnos[-1]["promedio"]

        try:

            tasa = (y2 - y1) / (x2 - x1)

            resultado.value = (
                f"Tasa de variación = {tasa:.2f}\n\n"
                f"Interpretación:\n"
                f"Por cada hora adicional de sueño,\n"
                f"el promedio cambia aproximadamente {tasa:.2f} puntos."
            )

        except:

            resultado.value = "No se puede calcular la tasa"

        page.update()


    def mostrar_conclusion(e):

        if len(alumnos) == 0:

            resultado.value = "Registra alumnos primero"
            page.update()
            return

        mejor = max(alumnos, key=lambda x: x["promedio"])

        resultado.value = (
            f"Conclusión:\n\n"
            f"Según los datos registrados, el mejor rendimiento "
            f"académico fue de {mejor['promedio']}.\n\n"
            f"Este resultado se obtuvo con "
            f"{mejor['horas']} horas de sueño.\n\n"
            f"Se observa que dormir adecuadamente "
            f"puede favorecer el desempeño escolar."
        )

    page.update()


    def mostrar_recomendacion(e):

        resultado.value = (
            "Recomendación personal:\n\n"
            "• Dormir entre 8 y 9 horas.\n"
            "• Evitar usar el celular antes de dormir.\n"
            "• Mantener horarios de descanso constantes.\n"
            "• Realizar actividad física regularmente.\n"
            "• Mantener una alimentación saludable."
        )

        page.update()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "TEMAS SELECTOS DE MATEMÁTICAS",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/matematicas.jpg",
                    width=400
                ),

                ft.Text(
                    """
Tema:
Hábitos de sueño y rendimiento académico

Propósito:

Analizar la relación entre las horas de sueño
(variable independiente x) y el rendimiento
académico (variable dependiente y).

La tasa de variación permite observar
cómo influyen los hábitos de sueño
en el desempeño escolar.
                    """,
                    size=18,
                    color=ft.Colors.WHITE
                ),

                ft.Divider(),

                ft.Text(
                    "Registro de alumnos",
                    size=22,
                    color=ft.Colors.CYAN,
                    weight=ft.FontWeight.BOLD
                ),

                nombre,
                horas,
                promedio,

                ft.Button(
                    "Agregar Alumno",
                    on_click=agregar_alumno
                ),

                ft.Container(
                    content=tabla,
                    bgcolor=ft.Colors.BLUE_GREY_800,
                    padding=10,
                    border_radius=10,
                    width=500
                ),

                ft.Button(
                    "Calcular Tasa de Variación",
                    on_click=calcular_tasa
                ),

                resultado,
                ft.Button(
                        "Ver Conclusión",
                        on_click=mostrar_conclusion
                    ),

                    ft.Button(
                        "Ver Recomendación",
                        on_click=mostrar_recomendacion
                    ),

                    ft.Button(
                        "Ver Gráfica",
                        on_click=mostrar_grafica
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