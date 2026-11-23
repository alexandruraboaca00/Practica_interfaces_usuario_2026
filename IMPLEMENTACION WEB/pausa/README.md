# Pausa

Revista digital para Interfaces de Usuario, curso 2026/2027. Incluye los productos de diseño, la presentación y una implementación web con logo propio, fotografías y contenido en español e inglés.

## Abrir la web

Abrir `src/index.html` en un navegador moderno o, preferiblemente, ejecutar desde la raíz:

```sh
npm start
```

Visitar `http://127.0.0.1:3000/src/`. No necesita compilación ni instalar dependencias para funcionar. Los paquetes de desarrollo se utilizan únicamente para verificar:

```sh
npm ci
npm run check
```

Las comprobaciones se han ejecutado con Node.js 24. La web incorpora búsqueda con resaltado y filtros, índice automático, guardados con deshacer, comentarios, temas claro/oscuro/sepia, tres tamaños de lectura, progreso, cálculo a 200 palabras por minuto y traducción ES/EN. Los datos se guardan en el mismo navegador; no hay cuentas ni sincronización.

La estructura sigue el enunciado: `src/` para HTML, `style/` para CSS, `images/` para gráficos y `script/` para JavaScript. [Descripción de la implementación](doc/IMPLEMENTACION.md) · [Validación y pendientes de evaluación](doc/VALIDACION_WEB.md).

## Documentación

- `doc/Pausa_Memoria_Puntos_1_a_5.docx`: memoria revisada con análisis, personas, funciones, escenarios, diagramas y justificación.
- `doc/Pausa_Presentacion_Punto_6.pptx`: 13 diapositivas con enlaces a Figma y notas de exposición repartidas entre cuatro integrantes.
- `doc/Guion_Defensa_4_Personas.docx`: guion para ensayar, tiempos, recorridos y preguntas previsibles.
- `diseno/`: 28 SVG editables con pantallas, estados y diagramas.
- `doc/recursos/`: capturas, fotografías ilustrativas y versiones PNG de los diseños.

## Figma

[Abrir el documento editable](https://www.figma.com/design/vP3kau1ExbjhCdFqqS9xCn)

[Escenario móvil de Laura](https://www.figma.com/proto/vP3kau1ExbjhCdFqqS9xCn?node-id=4-47&starting-point-node-id=4-47)

[Escenario de Siobhán](https://www.figma.com/proto/vP3kau1ExbjhCdFqqS9xCn?node-id=3-46&starting-point-node-id=3-46)

Los diseños están creados en Figma como formas, texto y botones editables. Hay dos puntos de inicio y 37 conexiones. Los recorridos usan entradas predefinidas, por ejemplo la consulta ciudad y un comentario de muestra. La guía de uso y las comprobaciones pendientes están en [diseno/LEEME_FIGMA.md](diseno/LEEME_FIGMA.md). Los enlaces directos de cada frame están en `diseno/figma.json`.

El plan Starter alcanzó su límite después de crear las conexiones e impidió completar la exportación visual del archivo desde las herramientas. Antes de exponer, abrir ambos recorridos, revisar su aspecto y comprobar Compartir para que el profesorado pueda acceder. Quedan cinco ajustes de texto solo en Figma: acortar el botón de cabecera en WF14, WF17, WF23 y WF26 y corregir el contador de WF27 a 44/500. Los SVG y las figuras locales ya están corregidos. LEEME_FIGMA.md contiene los enlaces directos y el texto exacto.

## Reparto de la defensa

Propuesta de ensayo de 10 minutos. El enunciado no establece duración.

| Integrante | Diapositivas | Tiempo | Contenido |
|---|---|---|---|
| Chao Chen | 1 a 3 | 2 min 20 s | Proyecto, análisis de publicaciones y personas |
| Alvaro Enrique Arnaiz | 4 a 6 | 2 min 20 s | Funciones priorizadas y escenarios |
| Alexandru David Raboaca | 7 a 9 | 2 min 20 s | Estructura, navegación y demostración de Laura |
| Marcos Rodriguez | 10 a 12 | 2 min 20 s | Lectura, comentarios y justificación teórica |

La diapositiva 13 queda como consulta de fuentes. Los 40 segundos restantes son margen para las transiciones y los enlaces. Las notas del PowerPoint incluyen el turno, tiempo y texto de cada diapositiva.

## Fuentes y alcance

Laura y Miguel son perfiles ficticios. Siobhán Doyle procede del enunciado. Las fotografías de los dos primeros perfiles son ilustrativas.

El análisis inicial y las capturas de portada son del 05/11/2026. Las capturas de los artículos y esta revisión son del 15/11/2026. `doc/recursos/capturas.json` distingue fechas, páginas y recursos. No se han realizado entrevistas ni evaluaciones con usuarios.

La implementación del 23/11/2026 añade comportamiento real a los bocetos: búsquedas, tiempos, progreso, preferencias, comentarios y guardados. La comprobación HTML del W3C y las pruebas automáticas constan en `doc/VALIDACION_WEB.md`. La revisión con la extensión WAVE y la evaluación SUS con otro grupo siguen pendientes; no se atribuyen resultados de pruebas a usuarios inexistentes.

## Subir estos cambios al repositorio

La implementación no cambia la configuración de alojamiento. Si se habilita GitHub Pages desde la rama `main` y la raíz del repositorio, `index.html` abre la web en `src/`. Para la entrega de clase, conservar también `doc/` y `diseno/`, y usar el nombre de ZIP que corresponda al grupo según el enunciado.
