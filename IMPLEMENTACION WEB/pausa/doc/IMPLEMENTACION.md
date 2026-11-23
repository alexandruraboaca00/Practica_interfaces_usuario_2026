# Implementación de Pausa

Versión del 23/11/2026. Equipo: Chao Chen, Alvaro Enrique Arnaiz, Alexandru David Raboaca y Marcos Rodriguez.

La web implementa los recorridos definidos en la memoria con un acabado editorial inspirado en la portada: logo propio junto al nombre, fondo marfil, azul oscuro, titulares serif e imágenes. Conserva los documentos de diseño y la presentación existentes.

## Abrir y comprobar

La aplicación usa HTML, CSS y JavaScript sin framework ni compilación. Se puede abrir `src/index.html` directamente en un navegador moderno. Se recomienda usar un servidor local para obtener un origen estable para el almacenamiento:

```sh
npm start
```

Abrir `http://127.0.0.1:3000/src/`. El servidor solo necesita Node.js; no hay que instalar paquetes para usar la web. Para ejecutar la verificación automática, usar Node.js 24 y:

```sh
npm ci
npm run check
```

La entrada raíz `index.html` lleva a `src/`. Las rutas con fragmentos (`#/articulo/ciudad`) funcionan en alojamiento estático, incluido GitHub Pages, sin reglas especiales de reescritura. Esta implementación no activa ni configura el alojamiento del repositorio.

## Funciones implementadas

| Función de la memoria | Resultado |
|---|---|
| F01 · Revista adaptable | Retícula de escritorio, reorganización en tablet y menú móvil. |
| F02 · Artículos legibles | Seis artículos completos con fotografía, autoría ficticia, fecha, secciones y contenido relacionado; disponibles en ES y EN. |
| F03 · Temas | Claro, oscuro y sepia, con nombre, borde y estado seleccionado. |
| F04 · Tamaño | Pequeño, mediano y grande sobre el cuerpo del artículo. |
| F05 · Guardados | Añadir, consultar, quitar y deshacer la última retirada. |
| F06 · Buscador | Consulta en título, descripción, autoría, etiquetas y cuerpo; búsqueda sin distinguir mayúsculas ni acentos, contador, resaltado y fragmento contextual. |
| F07 · Etiquetas | Categorías combinables con la consulta, estado pulsado y limpieza de filtros. |
| F08 · Índice | Se genera desde el catálogo y enlaza directamente a todos los artículos. El artículo incluye además enlaces a sus secciones. |
| F09 · Progreso | Barra superior calculada con el desplazamiento dentro del cuerpo; llega al 100 % antes de los comentarios. |
| F10 · Tiempo | Palabras del cuerpo y sus epígrafes / 200, redondeado al alza. Se recalcula al cambiar el idioma o el texto. Excluye menús, controles y comentarios. |
| F11 · Accesibilidad | HTML semántico, salto al contenido, foco visible, teclado nativo, textos alternativos, movimiento reducido y estados textuales. |
| F12 · Comentarios | Alias de 2–40 caracteres y mensaje de 1–500, validación por campo, contador y confirmación. |
| F13 · Persistencia | Preferencias, guardados y comentarios locales, datos validados al cargar y funcionamiento en memoria cuando se bloquea el almacenamiento. |
| F14 · Idioma | Interfaz y seis artículos completos en español e inglés; preferencia recordada. |

## Archivos

- `src/index.html`: entrada, cabecera, logo, navegación y diálogo de lectura.
- `style/main.css`: diseño adaptable, tres temas y tamaños.
- `images/`: recursos gráficos locales y sus créditos.
- `script/data.js`: catálogo y textos bilingües de demostración.
- `script/core.js`: búsqueda, resaltado seguro, cómputo de palabras, progreso y validación.
- `script/app.js`: rutas, vistas, acciones, comentarios y persistencia.
- `tools/serve.mjs`: servidor local sin dependencias de ejecución.
- `tests/`: pruebas de funciones, recorridos en DOM, semántica, contraste de la paleta y servidor.

## Estado y límites

La clave de almacenamiento es `pausa:v1`. Guardados, comentarios y preferencias permanecen en ese navegador y dispositivo. No existen cuentas, servidor de comentarios ni sincronización entre usuarios. La interfaz informa de ello antes de publicar un comentario. El contenido de los campos se escapa antes de insertarlo en HTML; no se interpreta como código.

Los textos y las firmas editoriales son ficticios y sirven para demostrar el proyecto. Los recursos se identifican en `images/CREDITOS.txt`.

La memoria de diseño original mantiene su alcance de puntos 1 a 5. Este documento añade la implementación; no sustituye los informes finales de accesibilidad y usabilidad. La evidencia disponible y las comprobaciones pendientes están en `VALIDACION_WEB.md`.
