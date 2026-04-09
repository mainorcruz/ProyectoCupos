"""Punto de entrada de la aplicación de Proyección de Cupos.

Bachillerato en Informática Empresarial — Universidad de Costa Rica
Planes de estudio 01 y 07.
"""

from views.main_view import MainView


def main():
    app = MainView()
    app.run()


if __name__ == "__main__":
    main()
