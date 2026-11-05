"""Contenido compartido por la memoria y la presentación."""
FECHA = '5 de noviembre de 2026'
OBJETIVO = ('Diseñar un magazine digital adaptable a escritorio, tablet y móvil que permita '
            'descubrir, guardar y comentar artículos y personalizar la lectura de forma accesible.')

SITIOS = [
    {
        'nombre': 'Xataka', 'url': 'https://www.xataka.com/', 'imagen': 'xataka_contenido.png',
        'articulo': 'https://www.xataka.com/empresas-y-economia/amd-va-a-adelantar-a-intel-primera-vez-su-historia',
        'ejemplo': 'AMD va a adelantar a Intel por primera vez en su historia',
        'descripcion': 'Publicación de tecnología con portada de actualidad y artículos agrupados por temas.',
        'soluciones': 'Combina titulares, imágenes y resúmenes con categorías, buscador, temas de interés y acceso a comentarios. En el artículo se identifican autora, fecha y etiquetas.',
        'patrones': 'A2, mosaico de noticias: varias entradas facilitan descubrir contenido. B1, varias vías de navegación: temas, categorías y búsqueda. D3, titulares y resúmenes: permiten anticipar el contenido.',
        'heuristicas': 'H6: categorías y enlaces a comentarios visibles reducen lo que hay que recordar. H4: las entradas repiten una estructura reconocible. H8: promociones, publicidad y numerosos módulos compiten con la lectura.',
        'conclusion': 'Su punto fuerte es facilitar el descubrimiento y la participación. Su punto débil es la densidad de estímulos. Para Pausa tomamos las tarjetas y las etiquetas, con una portada más breve y un artículo con menos interrupciones.',
        'tomamos': 'Tarjetas, etiquetas y comentarios.',
        'mejoramos': 'Menos módulos que interrumpan la lectura.',
    },
    {
        'nombre': 'Smashing Magazine', 'url': 'https://www.smashingmagazine.com/', 'imagen': 'smashing_portada.png',
        'articulo': 'https://www.smashingmagazine.com/2026/11/modern-css-might-make-your-front-end-more-complex/',
        'ejemplo': 'Modern CSS Might Make Your Front-End More Complex',
        'descripcion': 'Revista digital de diseño y desarrollo web, con artículos extensos y clasificación temática.',
        'soluciones': 'Muestra buscador, temas, autoría, fechas, resúmenes y comentarios. El artículo revisado anuncia 22 minutos de lectura y utiliza encabezados para separar el texto.',
        'patrones': 'J1, módulo de búsqueda: acceso directo en la cabecera. B8, páginas de categoría: agrupan artículos del mismo tema. D1, plantillas: mantienen la organización de los contenidos.',
        'heuristicas': 'H1: el tiempo anunciado ayuda a decidir si empezar a leer. H6: los temas permanecen a la vista. H8: las llamadas a newsletter y otros productos añaden competencia visual. H2: las etiquetas técnicas pueden resultar menos claras para lectores generales.',
        'conclusion': 'Su punto fuerte es orientar antes de una lectura larga mediante autoría, temas y tiempo estimado. Como límite, combina la lectura con promociones y lenguaje especializado. Para Pausa tomamos los metadatos y simplificamos las etiquetas y los elementos secundarios.',
        'tomamos': 'Autoría, temas y tiempo estimado.',
        'mejoramos': 'Lenguaje general y controles de lectura claros.',
    },
    {
        'nombre': 'Ethic', 'url': 'https://ethic.es/', 'imagen': 'ethic_contenido.png',
        'articulo': 'https://ethic.es/psicologia-ambiental',
        'ejemplo': 'Psicología ambiental',
        'descripcion': 'Revista de pensamiento y actualidad con secciones como Sociedad, Medio Ambiente y Entrevistas.',
        'soluciones': 'Organiza la portada con imágenes, titulares y entradillas. Ofrece buscador, categorías, contenidos relacionados, newsletter y un acceso a la edición en inglés. El artículo revisado identifica tema y autor.',
        'patrones': 'I1, retícula: ordena los bloques editoriales. D3, titulares y resúmenes: presentan cada propuesta. K2, barra de navegación: mantiene las secciones identificables. D10, localización: se observa un acceso a una edición en inglés, sin comprobar traducciones equivalentes.',
        'heuristicas': 'H2: los nombres de sección utilizan conceptos cotidianos. H6: los contenidos relacionados dan continuidad a la lectura. H8: el gran espacio promocional de la cabecera retrasa el acceso a las primeras historias; el aviso inicial de cookies añade un paso.',
        'conclusion': 'Su punto fuerte es la identidad de revista y la organización temática. Como punto débil, las promociones de cabecera desplazan el contenido. Para Pausa conservamos la jerarquía editorial y mostramos antes los artículos y sus herramientas de lectura.',
        'tomamos': 'Jerarquía editorial y secciones temáticas.',
        'mejoramos': 'Artículos visibles antes y cabecera compacta.',
    },
]

PERSONAS = [
    {
        'nombre': 'Laura Martín', 'edad': '22 años', 'foto': 'laura.jpg', 'tipo': 'Persona ficticia',
        'contexto': 'Estudiante de Comunicación · Madrid · Español e inglés intermedio.',
        'personalidad': 'Curiosa, espontánea e impaciente cuando una tarea tiene demasiados pasos.',
        'tecnologia': 'Alta: usa aplicaciones a diario, buscadores y marcadores; prefiere controles directos.',
        'plataformas': 'Móvil durante los trayectos y portátil para estudiar.',
        'objetivos': 'Encontrar temas de cultura y ciencia, decidir qué leer con poco tiempo y guardar lecturas para después. Quiere ampliar su formación y participar en conversaciones informadas.',
        'frustraciones': 'Perder un artículo, anuncios que cortan el texto y búsquedas sin filtros claros.',
        'cita': 'Si ahora no me da tiempo, quiero guardarlo y encontrarlo luego.',
        'impacto': 'Búsqueda visible, tiempo estimado y botón Guardar accesible desde las tarjetas.',
    },
    {
        'nombre': 'Miguel Navarro', 'edad': '34 años', 'foto': 'miguel.jpg', 'tipo': 'Persona ficticia',
        'contexto': 'Profesor de secundaria · Zaragoza · Español.',
        'personalidad': 'Reflexivo, organizado y paciente; valora la calma y las rutinas sencillas.',
        'tecnologia': 'Media: usa correo, navegador y herramientas educativas; agradece nombres claros.',
        'plataformas': 'Portátil en el trabajo y tablet en casa.',
        'objetivos': 'Leer artículos largos sin cansarse y recuperar lecturas útiles para preparar clases. Quiere mantener la curiosidad y transmitirla a su alumnado.',
        'frustraciones': 'Letra pequeña, fondos incómodos y tener que volver a ajustar la lectura cada vez.',
        'cita': 'Quiero concentrarme en lo que leo y poner la letra a mi gusto.',
        'impacto': 'Tamaños de letra explícitos, tema sepia, columna legible y preferencias persistentes.',
    },
    {
        'nombre': 'Siobhán Doyle', 'edad': '30 años', 'foto': 'siobhan.jpg', 'tipo': 'Persona del enunciado',
        'contexto': 'Creadora de contenido · Dublín, Irlanda · Inglés nativo y español. Deuteranopia (daltonismo rojo-verde).',
        'personalidad': 'Amigable, curiosa y perfeccionista con los pequeños detalles.',
        'tecnologia': 'Nativa digital, domina las herramientas web, pero puede tener problemas con las que están mal diseñadas.',
        'plataformas': 'Portátil y móvil.',
        'objetivos': 'Poder navegar de forma fluida e intuitiva por webs con consistencia visual sin sufrir fatiga visual.',
        'frustraciones': 'Necesidad de diseño: evitar estados que solo se distingan mediante rojo y verde.',
        'cita': 'Crear contenido me encanta, pero navegar por webs mal diseñadas me genera una fatiga visual enorme.',
        'impacto': 'Texto e iconos junto al color, estados con borde y marca, controles consistentes e idioma ES/EN.',
    },
]

FUNCIONES = [
    ('F01','Revista adaptable','Alta','Portada con categorías y tarjetas en escritorio, tablet y móvil.','Laura / Miguel'),
    ('F02','Artículo legible','Alta','Título, autoría, fecha, texto y contenido relacionado.','Las tres'),
    ('F03','Tres temas de color','Alta','Claro, oscuro y sepia; selección indicada también con texto.','Miguel / Siobhán'),
    ('F04','Tamaño de fuente','Alta','Pequeño, mediano y grande sin recortar el contenido.','Miguel'),
    ('F05','Guardar y recuperar','Alta','Botón Guardar, lista dedicada, quitar y deshacer.','Laura / Miguel'),
    ('F06','Buscar con resaltado','Alta','Filtrar por título o texto, contar resultados y destacar coincidencias.','Laura'),
    ('F07','Filtrar por etiquetas','Alta','Etiqueta pulsable, filtro activo visible y opción de quitarlo.','Laura'),
    ('F08','Índice automático','Alta','Listado generado desde la revista con enlace directo a cada artículo.','Miguel / Siobhán'),
    ('F09','Progreso de lectura','Alta','Barra superior que avanza al recorrer el cuerpo del artículo.','Las tres'),
    ('F10','Tiempo de lectura','Alta','Calcular al cargar o cambiar el texto: palabras / 200, redondeado al alza.','Laura'),
    ('F11','Accesibilidad','Alta','Teclado, foco visible, etiquetas claras y estados que no dependan solo del color.','Siobhán'),
    ('F12','Comentarios','Media','Alias y mensaje; validar campos y mostrar confirmación.','Laura / Siobhán'),
    ('F13','Recordar preferencias','Media','Conservar tema y tamaño en el dispositivo y permitir restablecerlos.','Miguel'),
    ('F14','Idioma de la interfaz','Media','Selector ES/EN para etiquetas y controles; indicar si un artículo no está traducido.','Siobhán'),
]

ESCENARIOS = [
    {
        'titulo': 'Escenario 1 · Laura encuentra y guarda una lectura',
        'contexto': 'Laura tiene diez minutos antes de entrar en clase y utiliza el móvil. Quiere encontrar una lectura sobre la vida en las ciudades para retomarla por la tarde.',
        'pasos': [
            'Abre Inicio, escribe «ciudad» y pulsa Buscar.',
            'Ve el número de resultados y las coincidencias resaltadas; activa la etiqueta Sociedad.',
            'Revisa el resumen y los 6 minutos estimados. Abre el artículo y pulsa Guardar.',
            'Ve «✓ Guardado». Por la tarde abre Guardados en el mismo móvil y recupera el artículo.',
        ],
        'exito': 'El artículo aparece una sola vez en Guardados y se puede abrir sin repetir la búsqueda.',
        'alternativa': 'Si no encuentra resultados, conserva la consulta y puede corregirla o quitar filtros.',
        'funciones': 'F01, F05, F06, F07 y F10.',
    },
    {
        'titulo': 'Escenario 2 · Siobhán lee y comenta con comodidad',
        'contexto': 'Siobhán lee un artículo en el portátil después de trabajar. Quiere usar los controles en inglés y distinguir las acciones sin depender de diferencias entre rojo y verde.',
        'pasos': [
            'Selecciona EN en el selector de idioma y abre un artículo desde el índice de la revista.',
            'En Lectura elige Sepia y letra Grande. Cada selección se marca con nombre, borde y estado activo.',
            'Lee con la barra de progreso visible y guarda el artículo; reconoce «✓ Saved» por su texto y marca.',
            'Escribe su alias y un comentario, lo publica y ve la confirmación junto a su mensaje.',
        ],
        'exito': 'Puede identificar controles y estados, ajustar la lectura y recibir una confirmación comprensible.',
        'alternativa': 'Si deja el comentario vacío, aparece un mensaje junto al campo y se conserva el alias.',
        'funciones': 'F03, F04, F05, F08, F09, F11, F12, F13 y F14.',
    },
]

JUSTIFICACIONES = [
    ('Portada y tarjetas','Laura encuentra temas rápido.','A2 + D3','H2 + H6'),
    ('Buscar, categorías e índice','Varias entradas al mismo artículo.','B1 + B8 + J1','H6 + H7'),
    ('Cabecera y controles comunes','Siobhán reconoce las acciones.','D1 + K2','H4'),
    ('Letra y temas con etiquetas','Miguel ajusta la lectura; Siobhán identifica el estado.','B9 + D11','H3 + H7'),
    ('Barra, minutos y Guardado','Laura conoce el avance y el resultado de su acción.','K4','H1'),
    ('Quitar filtros y deshacer','Recuperarse de una selección accidental.','K4 + K12','H3 + H5'),
    ('Errores junto al comentario','Conservar datos e indicar qué falta.','H10 + K13','H5 + H9'),
    ('Ayuda breve y estados vacíos','Mostrar cómo continuar en cada situación.','H8','H10'),
    ('Columna de lectura despejada','Miguel puede concentrarse en el texto.','I1 + I3','H8'),
    ('Interfaz ES/EN','Siobhán elige el idioma de los controles.','D10','H2'),
]

FUENTES = [
    ('Enunciado de la práctica, UC3M, curso 2026/2027, secciones 2 y 3.', 'cp-enunciado.pdf'),
    ('Xataka · portada', 'https://www.xataka.com/'),
    ('Xataka · artículo utilizado como muestra', SITIOS[0]['articulo']),
    ('Smashing Magazine · portada', 'https://www.smashingmagazine.com/'),
    ('Smashing Magazine · artículo utilizado como muestra', SITIOS[1]['articulo']),
    ('Ethic · portada', 'https://ethic.es/'),
    ('Ethic · artículo utilizado como muestra', SITIOS[2]['articulo']),
    ('Nielsen Norman Group · 10 heurísticas de usabilidad', 'https://www.nngroup.com/articles/ten-usability-heuristics/'),
    ('Van Duyne, Landay y Hong · The Design of Sites, 2.ª ed., Pearson, 2006; índice del catálogo.', 'https://www.oreilly.com/library/view/the-design-of/0131345559/'),
    ('Fotografías ilustrativas de Laura y Miguel · Random User / UI Faces', 'https://randomuser.me/photos'),
]
