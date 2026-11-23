# Validación de la web de Pausa

Revisión del 23/11/2026 sobre la implementación añadida al repositorio. Este registro distingue los controles automáticos de las evaluaciones que aún requieren navegador o personas.

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

## Comprobaciones pendientes antes de entregar

1. Abrir la web en navegadores reales y revisar anchuras de 320, 390, 768, 1024 y 1440 px, zoom al 200 %, teclado, lector de pantalla, cuadros de diálogo y los tres temas. El entorno de trabajo no ofreció la herramienta de navegador compartido necesaria para completar esa comprobación visual.
2. Instalar y ejecutar la extensión **WAVE**, como exige el enunciado. Revisar los errores, avisos y contrastes en Inicio, Artículo, búsqueda, Guardados y comentarios; conservar capturas y redactar el informe. No se ha ejecutado la extensión WAVE en esta revisión.
3. Realizar la evaluación **SUS con otro grupo**, recoger rango de edad y género según el enunciado y calcular puntuaciones individuales y media. No se han realizado entrevistas ni inventado respuestas SUS.
4. Integrar los resultados reales de estas evaluaciones en la memoria final de los puntos 7 a 9 y comprobar el acceso a Figma desde el equipo de la defensa.

## Alcance de la implementación

Es una aplicación estática. Guardados, preferencias y comentarios son locales a cada navegador. No existen cuentas, moderación central ni sincronización. Los artículos y firmas editoriales son ficticios. Las pruebas automatizadas no acreditan por sí solas el cumplimiento completo de WCAG ni sustituyen la evaluación con personas.
