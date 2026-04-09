# Proyección de Cupos — Bachillerato en Informática Empresarial (UCR)

Aplicación de escritorio para proyectar la demanda de cupos en cursos del Bachillerato en Informática Empresarial de la Universidad de Costa Rica, basada en los planes de estudio 01 y 07.

## Requisitos

- Python 3.10 o superior
- Windows 10/11 (tkinter viene incluido con Python en Windows)

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Uso

1. **Cargar Excel de notas**: Seleccione el archivo `.xlsx` con las columnas: Carné, Apellido 1, Apellido 2, Nombre, Recinto, Sigla, Grupo, Nombre del curso, Créditos, Nota, Modalidad, Pertenece a plan, Período, Año.
2. **Seleccionar plan de estudios**: Plan 01 (1997) o Plan 07 (Rediseño).
3. **Seleccionar cursos**: Filtre por ciclo y seleccione los cursos a proyectar.
4. **Proyectar cupos**: Genera la demanda proyectada basada en los requisitos aprobados.
5. **Exportar**: Reporte resumen o detallado (con lista de estudiantes elegibles por curso).

## Lógica de proyección

- Un estudiante es **elegible** para un curso si:
  - Ha aprobado **todos** los requisitos (o sus equivalentes)
  - No ha aprobado ni tiene matriculado el curso
- **Aprobado**: Nota ≥ 7.0
- **Retirado**: Modalidad contiene RJ, RET o similar
- **Matriculado**: Modalidad PI o sin nota asignada

## Arquitectura

```
cupos_app/
├── main.py                  # Punto de entrada
├── models/                  # Capa de datos
│   ├── course.py            # Modelo de curso
│   ├── student.py           # Modelo de estudiante y expediente
│   ├── study_plan.py        # Modelo de plan de estudios
│   └── plan_data.py         # Datos de planes 01 y 07
├── views/                   # Capa de presentación (tkinter)
│   └── main_view.py         # Ventana principal
├── controllers/             # Capa de lógica de negocio
│   ├── file_controller.py   # Carga de archivos Excel
│   ├── projection_controller.py  # Motor de proyección
│   └── report_controller.py # Generación de reportes
└── requirements.txt
```
# ProyectoCupos
