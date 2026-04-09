"""Datos de los planes de estudio 01 y 07 del Bachillerato en Informática Empresarial.

Fuente: Sistema de Aplicaciones Estudiantiles SAE, UCR.
Plan 01: Plan de 1997 (Resolución VD-13456-2025)
Plan 07: Rediseño de carrera (Resolución VD-13456-2025)
"""

from models.course import Course
from models.study_plan import StudyPlan


def _build_plan_01() -> StudyPlan:
    plan = StudyPlan(plan_id="01", name="Plan de 1997", total_credits=139)
    courses = [
        # Ciclo 1 (18 créditos)
        Course("ART100", "Curso de Arte", 2, 1),
        Course("CIH100", "Curso Integrado de Humanidades I", 6, 1),
        Course("IF1300", "Introducción a la Computación e Informática", 4, 1),
        Course("IF1400", "Lógica para Informáticos", 2, 1),
        Course("LM1030", "Estrategias de Lectura en Inglés I", 4, 1),
        # Ciclo 2 (18 créditos)
        Course("CIH200", "Curso Integrado de Humanidades II", 6, 2),
        Course("DEP100", "Actividad Deportiva", 0, 2),
        Course("IF2000", "Programación I", 4, 2, prerequisites=["IF1300"]),
        Course("LM1032", "Estrategias de Lectura en Inglés II", 4, 2,
               prerequisites=["LM1030"], prerequisite_equivalents={"LM1030": "LM1004"}),
        Course("MA0320", "Estructuras Matemáticas Discretas", 4, 2),
        # Ciclo 3 (18 créditos)
        Course("IF3000", "Programación II", 4, 3,
               prerequisites=["IF2000"], corequisites=["IF3001"]),
        Course("IF3001", "Algoritmos y Estructuras de Datos", 4, 3,
               prerequisites=["IF2000"], prerequisite_equivalents={"IF2000": "IF0004"}),
        Course("IF3100", "Introducción a Sistemas de Información", 3, 3,
               prerequisites=["IF1300"]),
        Course("MA0321", "Cálculo Diferencial e Integral", 4, 3),
        Course("XS0105", "Estadística para Informáticos", 3, 3),
        # Ciclo 4 (18 créditos)
        Course("IF4000", "Arquitectura de Computadores", 3, 4,
               prerequisites=["IF3000"]),
        Course("IF4001", "Sistemas Operativos", 4, 4,
               prerequisites=["IF3000", "IF3001"]),
        Course("IF4100", "Fundamentos de Bases de Datos", 4, 4,
               prerequisites=["IF3000"]),
        Course("IF5200", "Fundamentos de las Organizaciones", 3, 4,
               prerequisites=["IF3100"]),
        Course("MA0322", "Álgebra Lineal", 4, 4,
               prerequisites=["MA0320", "MA0321"]),
        # Ciclo 5 (18 créditos)
        Course("IF4101", "Lenguajes para Aplicaciones Comerciales", 4, 5,
               prerequisites=["IF3100", "IF4100"]),
        Course("IF5000", "Redes y Comunicaciones de Datos", 4, 5,
               prerequisites=["IF4001"]),
        Course("IF5100", "Administración de Bases de Datos", 4, 5,
               prerequisites=["IF4100"]),
        Course("MA0323", "Métodos Numéricos", 4, 5,
               prerequisites=["MA0322"]),
        Course("SRN100", "Seminario de Realidad Nacional I", 2, 5),
        # Ciclo 6 (16 créditos)
        Course("IF6000", "Redes en los Negocios", 4, 6,
               prerequisites=["IF5000"]),
        Course("IF6100", "Análisis y Diseño de Sistemas", 4, 6,
               prerequisites=["IF5100"]),
        Course("IF6200", "Economía de la Computación", 3, 6,
               prerequisites=["MA0323"]),
        Course("IF6201", "Informática Aplicada a los Negocios", 3, 6,
               prerequisites=["IF5200"], prerequisite_equivalents={"IF5200": "IF0015"}),
        Course("SRN200", "Seminario de Realidad Nacional II", 2, 6),
        # Ciclo 7 (16 créditos)
        Course("IF7100", "Ingeniería de Software", 4, 7,
               prerequisites=["IF6100"], prerequisite_equivalents={"IF6100": "IF0009"}),
        Course("IF7101", "Compromiso Social de la Informática", 2, 7,
               prerequisites=["IF7100"]),
        Course("IF7200", "Métodos Cuantitativos para la Toma de Decisiones", 4, 7,
               prerequisites=["IF6000", "IF6200"]),
        Course("IF7201", "Gestión de Proyectos", 3, 7,
               prerequisites=["IF6200"], prerequisite_equivalents={"IF6200": "IF0015"}),
        Course("OPT453", "Optativo de Temas Especiales", 3, 7),
        # Ciclo 8 (17 créditos)
        Course("IF8100", "Práctica Empresarial Supervisada", 6, 8,
               prerequisites=["IF7100", "IF7201"]),
        Course("IF8200", "Auditoría Informática", 4, 8,
               prerequisites=["IF7100", "IF7201"]),
        Course("IF8201", "Planificación Informática", 4, 8,
               prerequisites=["IF7201"]),
        Course("REP100", "Repertorio", 3, 8),
    ]
    for c in courses:
        plan.add_course(c)
    return plan


def _build_plan_07() -> StudyPlan:
    plan = StudyPlan(plan_id="07", name="Bachillerato en Informática Empresarial (Rediseño)", total_credits=144)
    courses = [
        # Ciclo 1 (16 créditos)
        Course("CIH100", "Curso Integrado de Humanidades I", 6, 1),
        Course("IF0001", "Desarrollo de Software I", 4, 1),
        Course("IF0002", "Introducción a la Informática Empresarial", 3, 1),
        Course("IF0003", "Matemática Básica para Informática Empresarial", 3, 1),
        # Ciclo 2 (16 créditos)
        Course("ART100", "Curso de Arte", 2, 2),
        Course("CIH200", "Curso Integrado de Humanidades II", 6, 2),
        Course("DEP100", "Actividad Deportiva", 0, 2),
        Course("IF0004", "Desarrollo de Software II", 4, 2,
               prerequisites=["IF0001"], prerequisite_equivalents={"IF0001": "IF2000"}),
        Course("IF0005", "Matemáticas Discretas para Informática Empresarial", 4, 2,
               prerequisites=["IF0003"], prerequisite_equivalents={"IF0003": "IF1400"}),
        # Ciclo 3 (18 créditos)
        Course("IF0006", "Desarrollo de Software III", 4, 3,
               prerequisites=["IF0004"]),
        Course("IF0007", "Bases de Datos I", 4, 3,
               prerequisites=["IF0004"]),
        Course("IF0008", "Cálculo I para Informática Empresarial", 4, 3,
               prerequisites=["IF0003"], prerequisite_equivalents={"IF0003": "IF1400"}),
        Course("IF3001", "Algoritmos y Estructuras de Datos", 4, 3,
               prerequisites=["IF0004"], prerequisite_equivalents={"IF0004": "IF2000"}),
        Course("SRN100", "Seminario de Realidad Nacional I", 2, 3),
        # Ciclo 4 (18 créditos)
        Course("IF0009", "Desarrollo de Software IV", 4, 4,
               prerequisites=["IF0006"], prerequisite_equivalents={"IF0006": "IF3000"}),
        Course("IF0010", "Bases de Datos II", 4, 4,
               prerequisites=["IF0007"], prerequisite_equivalents={"IF0007": "IF4100"}),
        Course("IF0011", "Redes de Computadoras", 4, 4,
               prerequisites=["IF0006"], prerequisite_equivalents={"IF0006": "IF3000"}),
        Course("IF0012", "Álgebra Lineal para Informática Empresarial", 4, 4,
               prerequisites=["IF0008"], prerequisite_equivalents={"IF0008": "MA0321"}),
        Course("SRN200", "Seminario de Realidad Nacional II", 2, 4),
        # Ciclo 5 (4 créditos)
        Course("IF0013", "Inglés I para Informática Empresarial", 4, 5),
        # Ciclo 6 (19 créditos)
        Course("IF0014", "Inglés II para Informática Empresarial", 4, 6,
               prerequisites=["IF0013"]),
        Course("IF0015", "Introducción a la Administración de Negocios", 4, 6,
               prerequisites=["IF0002"], prerequisite_equivalents={"IF0002": "IF1300"}),
        Course("IF0016", "Introducción a la Estadística y Análisis de Datos", 4, 6,
               prerequisites=["IF0010"], prerequisite_equivalents={"IF0010": "IF5100"}),
        Course("IF0017", "Métodos Numéricos y Análisis Computacional", 3, 6,
               prerequisites=["IF0012"], prerequisite_equivalents={"IF0012": "MA0322"}),
        Course("OPT1320_C6", "Área de Tendencias de Arq. e Infraestructura (Ciclo 6)", 4, 6),
        # Ciclo 7 (16 créditos)
        Course("IF0018", "Inglés III para Informática Empresarial", 4, 7,
               prerequisites=["IF0014"]),
        Course("IF0019", "Seguridad en Sistemas Informáticos", 4, 7,
               prerequisites=["IF0029"], prerequisite_equivalents={"IF0029": "IF0030"}),
        Course("OPT1321_C7", "Área de Tendencias de Desarrollo de Software (Ciclo 7)", 4, 7),
        Course("OPT1322", "Área de Tendencias de Ingeniería de Datos", 4, 7),
        # Ciclo 8 (4 créditos)
        Course("IF0020", "Inglés IV para Informática Empresarial", 4, 8,
               prerequisites=["IF0018"]),
        # Ciclo 9 (17 créditos)
        Course("IF7201", "Gestión de Proyectos", 3, 9,
               prerequisites=["IF0015"], prerequisite_equivalents={"IF0015": "IF6200"}),
        Course("OPT1319_C9", "Área de Tendencias de Gestión (Ciclo 9)", 3, 9),
        Course("OPT1320_C9", "Área de Tendencias de Arq. e Infraestructura (Ciclo 9)", 4, 9),
        Course("OPT1321_C9", "Área de Tendencias de Desarrollo de Software (Ciclo 9)", 4, 9),
        Course("REP100", "Repertorio", 3, 9),
        # Ciclo 10 (16 créditos)
        Course("IF0021", "Ética y Responsabilidad Profesional", 2, 10,
               prerequisites=["IF0023"], prerequisite_equivalents={"IF0023": "IF0024"}),
        Course("IF0022", "Práctica Empresarial Supervisada", 11, 10,
               prerequisites=["IF0016", "IF0020", "IF0025", "IF7201"],
               prerequisite_equivalents={
                   "IF0025": "IF0026",
                   "IF0029": "IF0030",
               }),
        Course("OPT1319_C10", "Área de Tendencias de Gestión (Ciclo 10)", 3, 10),
    ]
    for c in courses:
        plan.add_course(c)
    return plan


# Bloques optativos Plan 01
OPTATIVES_PLAN_01 = {
    "OPT453": [
        Course("IF7102", "Multimedios", 3, 7),
        Course("IF7103", "Sistemas Expertos para la Administración", 3, 7),
    ]
}

# Bloques optativos Plan 07
OPTATIVES_PLAN_07 = {
    "OPT1319": [
        Course("IF0023", "Gobernanza de Tecnologías de Información", 3, 0),
        Course("IF0024", "Emprendimiento y Desarrollo de Negocios", 3, 0),
        Course("IF6201", "Informática Aplicada a los Negocios", 3, 0),
    ],
    "OPT1320": [
        Course("IF0029", "Sistemas Operativos y Distribuidos", 4, 0),
        Course("IF0030", "Diseño de Sistemas Automatizados", 4, 0),
    ],
    "OPT1321": [
        Course("IF0025", "Aseguramiento de la Calidad en la Ingeniería del Software", 4, 0),
        Course("IF0026", "Interacción Humano Computador", 4, 0),
        Course("IF7100", "Ingeniería de Software", 4, 0),
    ],
    "OPT1322": [
        Course("IF0027", "Inteligencia de Negocios", 4, 0),
        Course("IF0028", "Minería de Datos", 4, 0),
    ],
}

PLAN_01 = _build_plan_01()
PLAN_07 = _build_plan_07()
