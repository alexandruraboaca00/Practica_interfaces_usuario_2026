# Validación de la web de Pausa

## Verificación del 28/11/2026

- `npm run check` completó 29 pruebas. En Chromium se verificaron el regreso al catálogo tras una recarga, la limpieza de filtros con teclado, el resaltado de autoría y la navegación móvil a 320, 390, 768 y 1440 px.
- Axe en Chromium revisó seis vistas móviles a 390 px, en español e inglés y con los tres temas. Las 36 combinaciones quedaron sin infracciones detectadas. En particular, el botón de lectura tiene un nombre accesible localizado.
- El servicio [W3C HTML Checker](https://validator.w3.org/nu/) devolvió cero errores y avisos en los ocho documentos de la versión revisada. Se enviaron las dos entradas HTML y seis vistas renderizadas en Chromium.

### Evaluación con la extensión WAVE

Se utilizó la extensión de WebAIM, versión 3.3.4.0, en Chromium y con la web servida en local. Se revisaron estas vistas y estados. [Extensión WAVE](https://wave.webaim.org/extension/)

| Vistas o estados | Casos | Errores | Errores de contraste | Alertas |
| --- | ---: | ---: | ---: | --- |
| Inicio, Explorar con filtro y coincidencia de autoría, búsqueda sin resultados | 3 | 0 | 0 | `noscript` en cada caso |
| Guardados lleno, Guardados vacío, Índice, Ayuda | 4 | 0 | 0 | `noscript` en cada caso |
| Artículo claro, oscuro y sepia en inglés con letra grande | 3 | 0 | 0 | `noscript` en cada caso |
| Comentario con error, botón Lectura en móvil | 2 | 0 | 0 | `noscript` en cada caso |

En la primera pasada se detectaron avisos de texto muy pequeño en la etiqueta de edición y en la cabecera de los ajustes de lectura. Se aumentó la etiqueta de edición a 12 px con el tamaño base del navegador y se retiró la cabecera redundante de los ajustes. La segunda pasada confirma que desaparecieron los avisos de texto pequeño. La alerta restante corresponde al mensaje que indica cómo habilitar JavaScript para abrir el catálogo. Las pruebas automáticas cubren los estados indicados. La revisión con lector de pantalla queda pendiente.

### Preparación del SUS con otro grupo

Dar a cada participante la misma tarea y un navegador con el estado inicial de la revista:

> Encuentra el artículo sobre la ciudad en la categoría Sociedad. Ajusta la lectura a sepia y letra grande, guárdalo y vuelve a abrirlo desde Guardados. Deja un comentario de prueba con un alias.

Después de la tarea, cada persona del otro grupo responde los diez ítems del SUS de clase, de 1 a 5. Registrar un identificador anónimo, rango de edad, género y las diez respuestas. Sumar las contribuciones de los ítems impares (respuesta menos 1) y pares (5 menos respuesta) y multiplicar por 2,5. Calcular la media de las puntuaciones individuales y resumir el perfil del grupo por rango de edad y género. La evaluación con participantes está pendiente. [Método de John Brooke](https://germanupa.de/sites/default/files/2021-12/brooke1996sus.pdf)

## Registro del 23/11/2026

## Comprobaciones realizadas

- `npm run check`: sintaxis JavaScript, validación local de las entradas HTML y 23 pruebas automáticas satisfactorias.
- Los recorridos de Laura y Siobhán se ejecutaron en JSDOM: búsqueda y filtro, lectura, guardado, recarga, retirada con deshacer, cambio a inglés, sepia y letra grande, comentarios inválidos y válidos, y persistencia.
- Se verificaron búsqueda por contenido y acentos, resaltado sin interpretar HTML, datos locales dañados o bloqueados, recuperación de enlaces desconocidos, controles de menú/lectura, salto al contenido y navegación por secciones.
- El tiempo usa el cuerpo a 200 palabras por minuto, redondea hacia arriba y cambia cuando se modifica el texto. La barra llega al 100 % antes de los comentarios.
- El servidor local responde con HTML, CSS, scripts e imágenes y rechaza rutas que salgan de su directorio.
- `axe-core` no detectó infracciones semánticas en ocho estados de la aplicación, incluidos inicio y artículo en inglés. Se desactivó únicamente la regla de contraste de axe porque JSDOM no tiene motor de renderizado.
- Se calculó por separado el contraste de los colores declarados para texto principal, secundario, etiquetas, acciones, errores y resaltado en los tres temas: las combinaciones comprobadas superan 4,5:1. Esta prueba de tokens no sustituye la inspección del resultado renderizado.

## W3C HTML Checker

Se enviaron al servicio `https://validator.w3.org/nu/?out=json` las dos entradas HTML y seis documentos con las vistas generadas: Inicio, Explorar con búsqueda, Guardados vacío, Índice, Artículo y Ayuda. Resultado: **0 errores y 0 avisos en los ocho documentos**. El servicio respondió con versión `26.11.20`.

El registro de las respuestas está en `W3C_2026-11-23.json`. Las vistas generadas se obtuvieron al ejecutar los mismos scripts de la aplicación en JSDOM; no son capturas de un navegador ni validan todos los estados posibles del contenido local.

## Alcance de la implementación

Es una aplicación estática. Guardados, preferencias y comentarios son locales a cada navegador. No existen cuentas, moderación central ni sincronización. Los artículos y firmas editoriales son ficticios. Las pruebas automatizadas no acreditan por sí solas el cumplimiento completo de WCAG ni sustituyen la evaluación con personas.
