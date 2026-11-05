# Pausa · Práctica de Interfaces de Usuario

Diseño de un magazine digital para la parte 3 del enunciado del curso 2026/2027.

- `doc/Pausa_Memoria_Puntos_1_a_5.docx`: memoria sencilla con los puntos 1 a 5.
- `doc/Pausa_Presentacion_Punto_6.pptx`: presentación para la defensa del punto 6.
- `diseno/`: diagramas y wireframes SVG editables e importables en Figma.
- `doc/recursos/`: capturas de las webs analizadas y fotografías de las personas.
- `scripts/`: fuentes para generar los documentos y los bocetos.

El repositorio se ha reinicializado localmente con `git init`. No se ha realizado ningún push.

Los perfiles de Laura y Miguel son ficticios. El de Siobhán Doyle procede del enunciado. Las fotografías son ilustrativas. Las observaciones de las webs se realizaron el 5 de noviembre de 2026, sin iniciar sesión ni publicar contenido.

Los bocetos se entregan en SVG, con textos y formas editables, y se reproducen en el Word y el PowerPoint. **No se ha creado un archivo nativo ni un enlace de Figma**: para esa parte de la entrega, hay que importar los SVG siguiendo `diseno/LEEME_FIGMA.md`.

## Regenerar los archivos

Crear un entorno de Python e instalar `scripts/requirements.txt`. Ejecutar desde la raíz del repositorio:

```sh
python scripts/generar_diseno.py
python scripts/generar_documentos.py
```

Las capturas y fotografías ya se incluyen, por lo que no hace falta descargarlas de nuevo.

