"""Crea el Word (puntos 1–5) y el PowerPoint (punto 6) de la práctica."""
from pathlib import Path
from datetime import datetime
from docx import Document
from docx.shared import Cm, Pt, RGBColor as WordColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx import Presentation
from pptx.util import Inches, Pt as PPt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from PIL import Image
from lxml import etree
from contenido import FECHA, OBJETIVO, SITIOS, PERSONAS, FUNCIONES, ESCENARIOS, JUSTIFICACIONES, FUENTES

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'doc'
ASSETS = OUT / 'recursos'
DESIGN = ASSETS / 'diseno'
BLUE, INK, MUTED, PALE, LINE = '244D72', '202833', '596574', 'F1F3F5', 'B8C0C8'
OUT.mkdir(exist_ok=True)


def hyperlink(p, title, url):
    rel=p.part.relate_to(url,RT.HYPERLINK,is_external=True)
    link=OxmlElement('w:hyperlink')
    link.set(qn('r:id'),rel)
    run=OxmlElement('w:r')
    props=OxmlElement('w:rPr')
    color=OxmlElement('w:color'); color.set(qn('w:val'),BLUE); props.append(color)
    underline=OxmlElement('w:u'); underline.set(qn('w:val'),'single'); props.append(underline)
    run.append(props)
    t=OxmlElement('w:t'); t.text=title; run.append(t)
    link.append(run); p._p.append(link)


def shade(cell,fill):
    tcPr=cell._tc.get_or_add_tcPr()
    shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),fill); tcPr.append(shd)


def paragraph(doc, text='', label=None, style=None, size=None):
    p=doc.add_paragraph(style=style)
    if label:
        p.add_run(label+' ').bold=True
    p.add_run(text)
    if size:
        for r in p.runs: r.font.size=Pt(size)
    return p


def heading(doc,title,level=1):
    return doc.add_heading(title,level)


def page(doc,title):
    doc.add_page_break()
    return heading(doc,title)


def caption(doc,text):
    p=paragraph(doc,text,size=8.5)
    p.paragraph_format.space_after=Pt(5)
    for r in p.runs: r.font.color.rgb=WordColor.from_string(MUTED)
    return p


def picture(doc,path,width=16.8):
    p=doc.add_paragraph()
    p.paragraph_format.space_before=Pt(2)
    p.paragraph_format.space_after=Pt(3)
    p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(path),width=Cm(width))
    return p


def table(doc,headers,rows,widths=None,size=9.5):
    t=doc.add_table(rows=1,cols=len(headers))
    t.alignment=WD_TABLE_ALIGNMENT.CENTER
    t.style='Table Grid'
    t.autofit=False
    for c,h in zip(t.rows[0].cells,headers):
        c.text=h; shade(c,BLUE)
        for r in c.paragraphs[0].runs:
            r.bold=True; r.font.color.rgb=WordColor(255,255,255)
    repeat=OxmlElement('w:tblHeader'); t.rows[0]._tr.get_or_add_trPr().append(repeat)
    for row in rows:
        cells=t.add_row().cells
        for c,txt in zip(cells,row): c.text=str(txt)
    for row in t.rows:
        trpr=row._tr.get_or_add_trPr()
        cant=OxmlElement('w:cantSplit'); trpr.append(cant)
        for i,c in enumerate(row.cells):
            if widths: c.width=Cm(widths[i])
            c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            for p in c.paragraphs:
                p.paragraph_format.space_after=Pt(4)
                p.paragraph_format.space_before=Pt(4)
                p.paragraph_format.line_spacing=1.02
                for r in p.runs: r.font.size=Pt(size)
    if widths:
        for c,w in zip(t.columns,widths): c.width=Cm(w)
    return t


def persona(doc,person,large=False):
    t=doc.add_table(rows=1,cols=2)
    t.alignment=WD_TABLE_ALIGNMENT.LEFT
    t.columns[0].width=Cm(2.6 if large else 2.0)
    t.columns[1].width=Cm(14.2 if large else 14.8)
    p=t.cell(0,0).paragraphs[0]
    p.add_run().add_picture(str(ASSETS/person['foto']),width=Cm(2.35 if large else 1.6))
    c=t.cell(0,1)
    p=c.paragraphs[0]
    r=p.add_run(f"{person['nombre']} · {person['edad']}")
    r.bold=True; r.font.size=Pt(14); r.font.color.rgb=WordColor.from_string(BLUE)
    p=c.add_paragraph(person['contexto']); p.paragraph_format.space_after=Pt(3)
    p=c.add_paragraph(person['tipo']); p.paragraph_format.space_after=Pt(3)
    for r in p.runs: r.font.size=Pt(8.5); r.italic=True
    for key,label in [('personalidad','Personalidad.'),('tecnologia','Experiencia tecnológica.'),('plataformas','Plataformas.'),('objetivos','Objetivos y motivaciones.'),('frustraciones','Necesidad / frustración.'),('cita','Lema personal.')]:
        text=f'«{person[key]}»' if key=='cita' else person[key]
        p=paragraph(doc,text,label=label,size=10.5)
        p.paragraph_format.space_after=Pt(4)


def create_word():
    doc=Document()
    sec=doc.sections[0]
    sec.page_width=Cm(21); sec.page_height=Cm(29.7)
    sec.top_margin=Cm(1.6); sec.bottom_margin=Cm(1.5)
    sec.left_margin=Cm(1.7); sec.right_margin=Cm(1.7)
    sec.header_distance=Cm(.65); sec.footer_distance=Cm(.65)
    normal=doc.styles['Normal']
    normal.font.name='Arial'; normal.font.size=Pt(10.5)
    normal.font.color.rgb=WordColor.from_string(INK)
    normal.paragraph_format.line_spacing=1.10
    normal.paragraph_format.space_after=Pt(6)
    for name,size in [('Title',36),('Heading 1',19),('Heading 2',13.5),('Heading 3',11)]:
        st=doc.styles[name]; st.font.name='Arial'; st.font.size=Pt(size)
        st.font.color.rgb=WordColor.from_string(BLUE)
        st.paragraph_format.space_before=Pt(8)
        st.paragraph_format.space_after=Pt(8)
    sec.header.paragraphs[0].text='PAUSA  |  Interfaces de Usuario · Parte 3'
    sec.header.paragraphs[0].runs[0].font.size=Pt(8)
    sec.header.paragraphs[0].runs[0].font.color.rgb=WordColor.from_string(MUTED)
    foot=sec.footer.paragraphs[0]; foot.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    r=foot.add_run('Pausa · '); r.font.size=Pt(8)
    field=OxmlElement('w:fldSimple'); field.set(qn('w:instr'),'PAGE'); foot._p.append(field)
    lang=OxmlElement('w:lang'); lang.set(qn('w:val'),'es-ES')
    normal.element.get_or_add_rPr().append(lang)
    core=doc.core_properties
    core.title='Pausa · Memoria de diseño · Puntos 1 a 5'
    core.subject='Interfaces de Usuario · Parte 3 · Curso 2026/2027'
    core.author=''; core.keywords='magazine, personas, wireframes, Nielsen, Van Duyne'

    # 1. Portada, introducción e índice.
    paragraph(doc,'UNIVERSIDAD CARLOS III DE MADRID',size=11)
    paragraph(doc,'Grado en Ingeniería Informática · Interfaces de Usuario',size=10)
    paragraph(doc,'Curso 2026/2027',size=10)
    p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(4)
    r=p.add_run('Pausa'); r.font.name='Arial'; r.font.size=Pt(44); r.bold=True; r.font.color.rgb=WordColor.from_string(BLUE)
    paragraph(doc,'Diseño de un magazine digital',size=22)
    paragraph(doc,'Parte 3 · Metodología de diseño · Puntos 1 a 5',size=13)
    paragraph(doc,FECHA,size=10)
    heading(doc,'Introducción',2)
    paragraph(doc,'Pausa es una propuesta de revista digital de cultura, ciencia y vida cotidiana. El diseño parte de tres publicaciones de referencia y de tres perfiles de uso para facilitar el descubrimiento de artículos y una lectura cómoda.')
    paragraph(doc,'Esta memoria recoge el análisis, las personas, el objetivo y las funciones, los escenarios, los diagramas y los bocetos. Las pantallas son una propuesta de baja fidelidad. La defensa del punto 6 se entrega en un PowerPoint independiente.')
    heading(doc,'Índice',2)
    for text in [
        '1. Análisis de tres sitios similares .............................................. 2',
        '2. Personas ................................................................................ 5',
        '3. Objetivo, funciones y escenarios ............................................. 7',
        '4. Estructura y navegación .......................................................... 9',
        '5. Bocetos y justificación del diseño .......................................... 11',
        'Conclusiones y fuentes ............................................................. 16',
    ]: paragraph(doc,text)

    # 2–4. Referencias reales.
    for i,site in enumerate(SITIOS):
        page(doc,'1. Análisis de sitios similares' if i==0 else f"1.{i+1}. {site['nombre']}")
        if i==0:
            paragraph(doc,'Se han revisado las portadas y un artículo de cada sitio el 05/11/2026, con capturas de escritorio a 1440 px. Es una revisión exploratoria de interfaces públicas, sin iniciar sesión ni realizar pruebas con usuarios. Las relaciones con patrones y heurísticas son una interpretación de diseño propia.')
            caption(doc,'H1–H10: heurísticas de Nielsen. Las letras y números de patrones corresponden a Van Duyne, Landay y Hong, 2.ª edición [8–9].')
            heading(doc,'1.1. Xataka',2)
        paragraph(doc,site['descripcion'])
        picture(doc,ASSETS/site['imagen'],width=16.2 if i==0 else 16.8)
        p=caption(doc,f"Figura {i+1}. Captura real de {site['nombre']} · 05/11/2026. ")
        hyperlink(p,'Portada',site['url']); p.add_run(' · '); hyperlink(p,'Artículo de muestra',site['articulo'])
        paragraph(doc,site['soluciones'],label='Soluciones y funciones.')
        paragraph(doc,site['patrones'],label='Patrones de Van Duyne.')
        paragraph(doc,site['heuristicas'],label='Heurísticas de Nielsen.')
        paragraph(doc,site['conclusion'],label='Conclusión.')
        if i==2:
            heading(doc,'Conclusión del análisis',2)
            paragraph(doc,'La propuesta combina la exploración temática de Xataka, los metadatos de lectura de Smashing Magazine y la jerarquía editorial de Ethic. La mejora buscada es reunir búsqueda, guardados y personalización en una interfaz breve y consistente. No se atribuyen a los sitios funciones que no se hayan podido observar.')

    # 5–6. Personas.
    page(doc,'2. Personas')
    caption(doc,'Laura y Miguel son perfiles inventados para este ejercicio, no participantes de una investigación. Sus fotografías son ilustrativas [10].')
    persona(doc,PERSONAS[0])
    paragraph(doc,'')
    persona(doc,PERSONAS[1])

    page(doc,'2.3. Siobhán Doyle')
    caption(doc,'Perfil proporcionado por el enunciado. Se mantienen sus datos, rasgos y lema; la imagen procede del PDF facilitado [1].')
    persona(doc,PERSONAS[2],large=True)
    heading(doc,'Necesidades que guían el diseño',2)
    table(doc,['Persona','Necesidad principal','Respuesta de Pausa'],[
        ('Laura','Encontrar y recuperar lecturas con poco tiempo.',PERSONAS[0]['impacto']),
        ('Miguel','Leer durante más tiempo con comodidad.',PERSONAS[1]['impacto']),
        ('Siobhán','Distinguir estados y evitar fatiga visual.',PERSONAS[2]['impacto']),
    ],widths=[2.5,5.5,9.6],size=10)
    paragraph(doc,'La deuteranopia no implica un único tema de color preferido. Por eso, se permite elegir el tema y se acompañan los estados con texto, iconos y bordes. La selección no depende únicamente de distinguir rojo y verde.')

    # 7–8. Definición y escenarios.
    page(doc,'3. Objetivo, funciones y escenarios')
    paragraph(doc,OBJETIVO,label='Objetivo en una frase.')
    heading(doc,'3.1. Funcionalidades por prioridad',2)
    paragraph(doc,'El orden marca la importancia para la primera versión. Las funciones de prioridad alta cubren el núcleo de la revista, los requisitos de lectura y el acceso inclusivo; después se añaden participación y comodidad.')
    table(doc,['Orden','Función','Prioridad','Comportamiento previsto'],[(str(i+1)+' · '+f[0],f[1],f[2],f[3]) for i,f in enumerate(FUNCIONES)],widths=[2.0,3.5,1.9,10.2],size=9.5)
    paragraph(doc,'Se usa el número de palabras del cuerpo del artículo, sin menús ni comentarios. Tiempo = techo(palabras / 200), con mínimo 1 minuto para un texto no vacío; 1200 palabras son 6 minutos. Se recalcula si cambia el texto, no al cambiar el tamaño de letra.',label='Criterio de lectura.')
    paragraph(doc,'La barra mide el desplazamiento dentro del artículo y llega al 100 % al final del texto. Los guardados y las preferencias se conservan en el mismo dispositivo; no se promete sincronización entre equipos.',label='Criterio de estado.')

    page(doc,'3.2. Escenarios de usuario')
    for scenario in ESCENARIOS:
        heading(doc,scenario['titulo'],2)
        paragraph(doc,scenario['contexto'],label='Contexto y objetivo.')
        for j,step in enumerate(scenario['pasos'],1): paragraph(doc,f'{j}. {step}')
        paragraph(doc,scenario['exito'],label='Resultado esperado.')
        paragraph(doc,scenario['alternativa'],label='Si surge un problema.')
        caption(doc,'Funciones relacionadas: '+scenario['funciones'])
    paragraph(doc,'Los escenarios son hipótesis para orientar el diseño y las tareas de una evaluación posterior; todavía no representan resultados de pruebas de usabilidad.')

    # 9–10. Diagramas.
    page(doc,'4. Estructura y navegación')
    heading(doc,'4.1. Estructura del sitio',2)
    paragraph(doc,'El contenido se organiza en cinco entradas principales. Los artículos constituyen un tipo de página compartido: una misma lectura se puede abrir desde distintos lugares sin duplicar el contenido.')
    picture(doc,DESIGN/'09_diagrama_estructura.png')
    caption(doc,'Figura 4. Mapa de páginas y agrupaciones. Fuente: elaboración propia.')
    for label,text in [
        ('Inicio.','Presenta el destacado y las publicaciones recientes.'),
        ('Explorar.','Reúne categorías, etiquetas y búsqueda. Los resultados conservan los criterios elegidos.'),
        ('Índice de la revista.','Se genera con el catálogo y enlaza directamente a cada artículo. En escritorio aparece como columna; en tablet y móvil se despliega.'),
        ('Guardados.','Muestra los artículos guardados en el dispositivo y permite recuperarlos o quitarlos.'),
        ('Ayuda.','Explica de forma breve los controles de lectura, los guardados y las opciones de accesibilidad.'),
    ]: paragraph(doc,text,label=label)
    paragraph(doc,'El idioma y las preferencias de lectura se cambian desde controles comunes. No requieren abandonar el artículo ni se modelan como páginas separadas.')

    page(doc,'4.2. Navegación del sitio')
    picture(doc,DESIGN/'10_diagrama_navegacion.png')
    caption(doc,'Figura 5. Recorridos y alternativas de recuperación. Fuente: elaboración propia.')
    paragraph(doc,'Inicio → búsqueda o etiqueta → resultados → artículo. La consulta y los filtros se mantienen al volver. Si no hay coincidencias, se conserva lo escrito y se ofrecen quitar filtros o editar la búsqueda.',label='Encontrar.')
    paragraph(doc,'Artículo → Guardar → confirmación → Guardados → artículo. Al quitar un guardado se ofrece Deshacer. El acceso al índice de la revista es una alternativa para abrir una lectura conocida.',label='Recuperar.')
    paragraph(doc,'Artículo → comentarios → validar → confirmar. Si faltan datos o se supera el límite, se explica el problema junto al campo y se conserva el contenido para corregirlo.',label='Participar.')

    # 11–15. Bocetos y justificación.
    page(doc,'5. Bocetos y justificación del diseño')
    paragraph(doc,'Se proponen pantallas de baja fidelidad para fijar jerarquía, controles y recorridos antes de implementar. Los recuadros con diagonales representan imágenes pendientes, no contenido definitivo.')
    heading(doc,'5.1. Inicio en escritorio',2)
    picture(doc,DESIGN/'01_inicio_escritorio.png')
    caption(doc,'Figura 6. WF01 · Inicio · 1440 px. Elaboración propia; SVG editable en diseno/.')
    paragraph(doc,'El buscador y las etiquetas se colocan antes del destacado para que Laura encuentre contenido con rapidez. Las tarjetas muestran una idea del contenido, tiempo estimado y un acceso directo a Guardar.')
    paragraph(doc,'El índice lateral enlaza a todos los artículos del catálogo. Su contenido se generará a partir de los datos de la revista para que no dependa de actualizar manualmente una lista. La cabecera mantiene Inicio, Explorar, Índice y Guardados.')
    paragraph(doc,'Los bocetos se entregan como SVG importables en Figma. No se ha creado un archivo nativo ni un enlace de Figma desde esta sesión: queda pendiente importarlos al documento de Figma y conectar los frames. El procedimiento y los enlaces previstos están en diseno/LEEME_FIGMA.md.',label='Formato del boceto.')

    page(doc,'5.2. Artículo y personalización')
    picture(doc,DESIGN/'02_articulo_escritorio.png')
    caption(doc,'Figura 7. WF02 · Artículo en escritorio · 1440 px. Elaboración propia.')
    paragraph(doc,'Miguel dispone de una columna de texto estable y controles explícitos de tema y tamaño. Las opciones se agrupan en Lectura y se pueden restablecer. Se prevén temas claro, oscuro y sepia, y tamaños pequeño, mediano y grande.')
    paragraph(doc,'Siobhán puede identificar la opción seleccionada mediante el nombre y el estado del botón. Guardar cambia a «✓ Guardado»; la barra superior y el porcentaje muestran el avance. El tiempo estimado aparece cerca de la autoría y se calcula con 200 palabras por minuto.')
    paragraph(doc,'El índice de la revista conserva enlaces a los artículos. Los comentarios se sitúan después del cuerpo del texto, con un acceso desde la cabecera para quien quiera participar.')

    page(doc,'5.3. Adaptación a móvil y tablet')
    t=doc.add_table(rows=1,cols=3)
    t.autofit=False; t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for c,w in zip(t.columns,[4.1,4.1,9.4]): c.width=Cm(w)
    for c,name,w in zip(t.rows[0].cells,['05_inicio_movil','06_articulo_movil','07_articulo_tablet'],[3.75,3.75,8.8]):
        c.paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.CENTER
        c.paragraphs[0].add_run().add_picture(str(DESIGN/f'{name}.png'),width=Cm(w))
    caption(doc,'Figura 8. WF05: inicio móvil; WF06: artículo móvil; WF07: artículo en tablet. Elaboración propia.')
    table(doc,['Formato','Organización','Decisión centrada en la persona'],[
        ('Escritorio · 1440 px','Retícula y columna lateral.','Índice y controles visibles para lecturas largas de Miguel.'),
        ('Tablet · 768 px','Texto en una columna; controles compactos.','Mantener la comodidad en la tablet de Miguel.'),
        ('Móvil · 390 px','Tarjetas apiladas, menú e índice plegables.','Laura puede buscar y guardar; Siobhán mantiene los mismos nombres y estados.'),
    ],widths=[3.4,5.3,8.9],size=9.5)
    paragraph(doc,'Los controles táctiles se plantean con una altura de al menos 44 px. La futura implementación deberá permitir ampliar el texto, mostrar el foco al usar el teclado y evitar desplazamiento horizontal en la lectura. El tema sepia con letra grande se ilustra en el artículo móvil.')

    page(doc,'5.4. Buscar y recuperar artículos')
    picture(doc,DESIGN/'03_busqueda_escritorio.png',width=15.9)
    caption(doc,'Figura 9. WF03 · Consulta, coincidencias resaltadas, contador y filtro activo.')
    picture(doc,DESIGN/'04_guardados_escritorio.png',width=15.9)
    caption(doc,'Figura 10. WF04 · Guardados y aviso de eliminación con Deshacer. Elaboración propia.')
    paragraph(doc,'Laura reconoce lo que ha buscado y los filtros activos. Desde Guardados puede volver al artículo; el texto y la marca del botón comunican su estado también a Siobhán.')

    page(doc,'5.5. Estados y criterios de diseño')
    picture(doc,DESIGN/'08_estados_y_comentarios.png',width=13.6)
    caption(doc,'Figura 11. WF08 · Sin resultados, guardados vacíos y validación de comentarios.')
    table(doc,['Decisión','Justificación','Patrón','Heurística'],JUSTIFICACIONES,widths=[3.7,8.0,2.5,3.4],size=9)
    caption(doc,'H1 estado; H2 lenguaje del usuario; H3 control; H4 consistencia; H5 prevención; H6 reconocimiento; H7 flexibilidad; H8 simplicidad; H9 recuperación de errores; H10 ayuda. Numeración de Nielsen [8].')
    caption(doc,'Los códigos de patrones proceden de la 2.ª edición de Van Duyne, Landay y Hong [9]. H8 en la columna Patrón identifica ayuda contextual; H8 en Heurística identifica simplicidad visual.')
    paragraph(doc,'La relación entre persona, pantalla y criterio expresa una decisión de diseño, no una evaluación ya realizada. En el tema oscuro y en el resto de variantes se deberán comprobar los contrastes durante la implementación.')

    # 16. Cierre y bibliografía.
    page(doc,'Conclusiones y fuentes')
    heading(doc,'Conclusiones',2)
    paragraph(doc,'Pausa reúne descubrimiento, lectura y recuperación en una estructura corta. Laura orienta la búsqueda y el guardado; Miguel, la comodidad del texto; y Siobhán, la consistencia y la identificación de estados sin depender solo del color. Los escenarios conectan estas necesidades con recorridos concretos y con estados de recuperación.')
    paragraph(doc,'La propuesta deja definidos los contenidos de diseño de los puntos 1 a 5. Para cumplir el requisito de herramienta del punto 5 queda pendiente importar los SVG y conectar el boceto en Figma. La presentación del punto 6 resume los resultados. La implementación y las evaluaciones posteriores quedan fuera del alcance de estos archivos.')
    heading(doc,'Fuentes consultadas',2)
    caption(doc,'Consulta de las webs y obtención de capturas: 05/11/2026. El análisis se limita a las páginas enlazadas y a las funciones visibles sin cuenta.')
    for i,(title,url) in enumerate(FUENTES,1):
        p=paragraph(doc,f'[{i}] ',size=9.5)
        if url.startswith('http'): hyperlink(p,title,url)
        else: p.add_run(title+' Archivo local: '+url)
    paragraph(doc,'Laura: randomuser.me/api/portraits/women/44.jpg. Miguel: randomuser.me/api/portraits/men/52.jpg. Los nombres y datos de esos perfiles son inventados y no describen a las personas fotografiadas. La foto y el perfil de Siobhán proceden del enunciado.',label='Créditos de fotografías.',size=9)
    paragraph(doc,'Los diagramas y bocetos son de elaboración propia. Las capturas se incluyen como ejemplos de análisis académico y conservan la apariencia observada en la visita.',size=9)
    dest=OUT/'Pausa_Memoria_Puntos_1_a_5.docx'
    doc.save(dest)
    print(dest)


def rgb(value): return RGBColor.from_string(value)


class Deck:
    def __init__(self):
        self.p=Presentation()
        self.p.slide_width=Inches(13.333)
        self.p.slide_height=Inches(7.5)
        self.p.core_properties.title='Pausa · Defensa de los puntos 1 a 5'
        self.p.core_properties.subject='Parte 3 · Punto 6 · Interfaces de Usuario'
        self.p.core_properties.author=''

    def text(self,s,x,y,w,h,txt,size=21,color=INK,bold=False,align=None):
        box=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
        tf=box.text_frame; tf.word_wrap=True
        tf.margin_left=Inches(.02); tf.margin_right=Inches(.02)
        tf.margin_top=Inches(.01); tf.margin_bottom=Inches(.01)
        for i,line in enumerate(txt.split('\n')):
            p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
            p.text=line; p.font.name='Arial'; p.font.size=PPt(size)
            p.font.bold=bold; p.font.color.rgb=rgb(color)
            p.space_after=PPt(8)
            if align is not None: p.alignment=align
        return box

    def rect(self,s,x,y,w,h,fill=PALE,stroke=None):
        sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h))
        sh.adjustments[0]=.04
        sh.fill.solid(); sh.fill.fore_color.rgb=rgb(fill)
        etree.SubElement(sh._element.spPr,'{http://schemas.openxmlformats.org/drawingml/2006/main}effectLst')
        if stroke: sh.line.color.rgb=rgb(stroke)
        else: sh.line.fill.background()
        return sh

    def line(self,s,x1,y1,x2,y2):
        sh=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,Inches(x1),Inches(y1),Inches(x2),Inches(y2))
        sh.line.color.rgb=rgb(BLUE); sh.line.width=PPt(1.5)
        return sh

    def picture(self,s,path,x,y,w,h):
        with Image.open(path) as im: iw,ih=im.size
        factor=min(w/iw,h/ih)
        aw,ah=iw*factor,ih*factor
        return s.shapes.add_picture(str(path),Inches(x+(w-aw)/2),Inches(y+(h-ah)/2),width=Inches(aw),height=Inches(ah))

    def slide(self,title,kicker=''):
        s=self.p.slides.add_slide(self.p.slide_layouts[6])
        bg=s.background.fill; bg.solid(); bg.fore_color.rgb=rgb('FFFFFF')
        self.rect(s,0,0,13.333,.10,BLUE)
        self.text(s,.48,.27,12.35,.6,title,size=29,color=BLUE,bold=True)
        if kicker: self.text(s,.5,.92,12.3,.45,kicker,size=15,color=MUTED)
        self.text(s,.5,7.14,11,.2,'PAUSA · Interfaces de Usuario · Parte 3 / punto 6',size=10,color=MUTED)
        self.text(s,12.05,7.10,.75,.25,str(len(self.p.slides)),size=11,color=MUTED,align=PP_ALIGN.RIGHT)
        return s

    def notes(self,s,text): s.notes_slide.notes_text_frame.text=text

    def link(self,s,x,y,w,title,url):
        sh=self.text(s,x,y,w,.35,title,size=13,color=BLUE)
        sh.text_frame.paragraphs[0].runs[0].hyperlink.address=url

    def functions(self,s,items):
        colwidths=[.8,2.55,7.9,.98]
        x=[.5,1.3,3.85,11.75]
        self.rect(s,.48,1.42,12.37,.43,BLUE)
        for xx,w,t in zip(x,colwidths,['Orden','Función','Comportamiento','Prioridad']):
            self.text(s,xx,1.48,w,.3,t,size=15,color='FFFFFF',bold=True)
        for i,f in enumerate(items):
            y=1.94+i*.65
            if i%2==0: self.rect(s,.48,y-.03,12.37,.61)
            for xx,w,t in zip(x,colwidths,[f[0],f[1],f[3],f[2]]):
                self.text(s,xx,y,w,.58,t,size=16)


def create_ppt():
    d=Deck()
    s=d.slide('Pausa')
    d.text(s,.8,1.75,7.0,1.4,'Un magazine digital\npara leer a tu ritmo',size=38,bold=True)
    d.text(s,.8,3.55,6.8,1.15,'Análisis, personas, funciones, escenarios,\nestructura y bocetos de la propuesta.',size=24)
    d.text(s,.8,5.15,6.8,.6,'Defensa de los puntos 1 a 5 · Punto 6',size=20,color=BLUE)
    d.text(s,.8,5.92,7.0,.5,'Curso 2026/2027 · '+FECHA,size=17,color=MUTED)
    d.picture(s,DESIGN/'05_inicio_movil.png',8.8,1.3,3.4,5.55)
    d.notes(s,'Presentar Pausa como revista de cultura, ciencia y vida cotidiana. Esta defensa resume las primeras cinco fases. Las pantallas son bocetos de baja fidelidad y las dos primeras personas son ficticias. Duración orientativa total: 8–10 minutos.')

    s=d.slide('1 · Tres publicaciones de referencia','Qué tomamos y qué simplificamos para Pausa')
    for i,site in enumerate(SITIOS):
        x=.5+i*4.15
        d.rect(s,x,1.45,4.0,5.45)
        d.text(s,x+.14,1.62,3.72,.5,site['nombre'],size=23,bold=True)
        d.picture(s,ASSETS/site['imagen'],x+.13,2.18,3.74,2.35)
        d.text(s,x+.16,4.62,3.66,.95,site['tomamos'],size=20,bold=True)
        d.text(s,x+.16,5.61,3.66,.8,site['mejoramos'],size=18)
        d.link(s,x+.16,6.45,3.6,'Abrir web analizada',site['url'])
    d.notes(s,'Fuentes: portadas y artículos enlazados en la memoria, consultados el 05/11/2026. Xataka: mosaico A2, navegación B1 y reconocimiento H6; densidad visual H8. Smashing: búsqueda J1, categorías B8 y tiempo anunciado H1. Ethic: retícula I1, navegación K2 y lenguaje H2; cabecera promocional H8. Son observaciones exploratorias, no resultados de pruebas con usuarios.')

    s=d.slide('2 · Tres personas, necesidades diferentes','Dos perfiles ficticios y el perfil de Siobhán proporcionado por el enunciado')
    needs=[['Buscar en pocos pasos.','Saber cuánto tarda una lectura.','Guardar para después.'],['Leer artículos largos.','Elegir letra y tema.','Recordar sus ajustes.'],['Identificar estados sin rojo/verde.','Mantener controles consistentes.','Elegir interfaz ES/EN.']]
    for i,(person,bullets) in enumerate(zip(PERSONAS,needs)):
        x=.5+i*4.15
        d.rect(s,x,1.48,4.0,5.43)
        d.picture(s,ASSETS/person['foto'],x+.17,1.7,1.05,1.05)
        d.text(s,x+1.37,1.77,2.42,.9,person['nombre']+'\n'+person['edad'],size=21,bold=True)
        context=['Estudiante · Madrid\nTecnología alta · móvil y portátil','Profesor · Zaragoza\nTecnología media · portátil y tablet','Creadora de contenido · Dublín\nNativa digital · portátil y móvil']
        d.text(s,x+.17,2.99,3.66,1.0,context[i],size=18,color=MUTED)
        d.text(s,x+.17,4.23,3.66,2.1,'\n'.join('• '+b for b in bullets),size=20)
        d.text(s,x+.17,6.42,3.66,.25,person['tipo'],size=12,color=MUTED)
    d.notes(s,'Laura es curiosa, espontánea y busca rapidez. Miguel es reflexivo y organizado y busca comodidad para preparar clases. Siobhán tiene deuteranopia, habla inglés nativo y español y valora la consistencia. No se ha entrevistado a estos perfiles. Fotografías ilustrativas: Random User para Laura y Miguel; enunciado para Siobhán.')

    s=d.slide('3 · Objetivo y funciones prioritarias','Funciones F01–F07 · Ordenadas por importancia')
    d.functions(s,FUNCIONES[:7])
    d.text(s,.5,6.61,12.2,.36,'Objetivo: descubrir, guardar y comentar artículos con una lectura personalizable y accesible.',size=17,color=BLUE,bold=True)
    d.notes(s,OBJETIVO+' Las funciones de prioridad alta cubren el núcleo. La revista debe adaptarse a escritorio, tablet y móvil. Destacar que cada artículo tiene autoría y que el guardado ofrece una lista dedicada y la opción Deshacer.')

    s=d.slide('3 · Lectura, participación e idioma','Funciones F08–F14 · El tiempo se calcula a 200 palabras por minuto')
    d.functions(s,FUNCIONES[7:])
    d.text(s,.5,6.62,12.2,.36,'Ejemplo: 1200 palabras / 200 = 6 minutos · Índice con enlace directo a cada artículo.',size=17,color=BLUE,bold=True)
    d.notes(s,'El índice se genera desde los artículos del magazine; no se sustituye por un índice de apartados dentro de un solo texto. El progreso avanza al recorrer el cuerpo del artículo. El tiempo se recalcula al cambiar el contenido. El idioma cambia los controles; no se presume que todas las lecturas tengan traducción. Guardados y preferencias en el mismo dispositivo.')

    s=d.slide('3 · Dos escenarios de usuario','De una necesidad concreta a un recorrido verificable')
    for i,scenario in enumerate(ESCENARIOS):
        x=.5+i*6.33
        d.rect(s,x,1.52,6.12,5.3)
        d.text(s,x+.2,1.76,5.7,.65,'Laura · Encontrar y guardar' if i==0 else 'Siobhán · Leer y comentar',size=24,bold=True)
        context='Móvil, antes de clase. Busca una lectura sobre la ciudad para volver a ella por la tarde.' if i==0 else 'Portátil, al terminar de trabajar. Quiere una lectura cómoda y estados fáciles de distinguir.'
        d.text(s,x+.2,2.6,5.7,1.0,context,size=21)
        flow='Buscar «ciudad» → Sociedad → Artículo\n→ Guardar → Mis guardados' if i==0 else 'EN → Índice → Artículo → Sepia + Grande\n→ Guardar → Comentar'
        d.text(s,x+.2,3.94,5.7,1.1,flow,size=23,color=BLUE,bold=True)
        recovery='Si no hay resultados: corregir la búsqueda o quitar filtros.' if i==0 else 'Si falta el comentario: mensaje junto al campo y alias conservado.'
        d.text(s,x+.2,5.45,5.7,1.02,recovery,size=20)
    d.notes(s,'Escenario de Laura: la confirmación de Guardado permite recuperar el artículo en el mismo móvil sin repetir búsqueda. Escenario de Siobhán: no dependemos solo del color; hay nombre, estado y marca. Los escenarios son hipótesis de diseño para una evaluación futura.')

    s=d.slide('4 · Estructura del sitio','Cinco entradas principales y un tipo de página de artículo compartido')
    d.rect(s,5.25,1.42,2.8,.65,BLUE)
    d.text(s,5.35,1.54,2.6,.4,'Pausa',size=24,color='FFFFFF',bold=True,align=PP_ALIGN.CENTER)
    d.line(s,6.65,2.07,6.65,2.38)
    d.line(s,1.7,2.38,11.65,2.38)
    labels=[('Inicio','Destacado y últimos'),('Explorar','Categorías y búsqueda'),('Índice','Lista de artículos'),('Guardados','Lista y estado vacío'),('Ayuda','Controles y accesibilidad')]
    for i,(title,body) in enumerate(labels):
        x=.5+i*2.5
        d.line(s,x+1.15,2.38,x+1.15,2.78)
        d.rect(s,x,2.78,2.3,1.35,PALE,BLUE)
        d.text(s,x+.1,2.98,2.1,.45,title,size=22,color=BLUE,bold=True,align=PP_ALIGN.CENTER)
        d.text(s,x+.1,3.5,2.1,.55,body,size=16,align=PP_ALIGN.CENTER)
        if i<4:
            d.line(s,x+1.15,4.13,x+1.15,4.6)
    d.line(s,1.65,4.6,9.15,4.6); d.line(s,5.45,4.6,5.45,4.98)
    d.rect(s,3.1,4.98,6.7,.92,PALE,BLUE)
    d.text(s,3.25,5.18,6.4,.5,'Artículo · Lectura · Guardar · Comentarios',size=23,bold=True,align=PP_ALIGN.CENTER)
    d.text(s,.7,6.39,12,.4,'Controles comunes: idioma ES/EN, tema y tamaño de letra.',size=21,color=BLUE)
    d.notes(s,'El diagrama detallado aparece en la memoria. El artículo es el mismo aunque se abra desde Inicio, Explorar, Índice o Guardados. El índice lateral de escritorio se pliega en tablet y móvil. Las opciones de lectura actúan en la pantalla actual.')

    s=d.slide('4 · Navegación y recuperación','El usuario puede continuar y corregir una acción sin perder el contexto')
    for i,label in enumerate(['Inicio','Buscar / etiqueta','Resultados','Artículo','Guardar']):
        x=.5+i*2.51
        d.rect(s,x,1.75,2.12,.9,PALE,BLUE)
        d.text(s,x+.05,1.93,2.02,.66,label,size=19,bold=True,align=PP_ALIGN.CENTER)
        if i<4: d.text(s,x+2.15,1.98,.34,.5,'→',size=21,color=BLUE)
    d.text(s,5.18,3.03,2.7,.5,'0 resultados ↓',size=20,color=BLUE,bold=True)
    d.rect(s,4.55,3.62,4.0,1.05)
    d.text(s,4.7,3.80,3.7,.8,'Editar consulta / quitar filtros\nConservar lo escrito',size=17,align=PP_ALIGN.CENTER)
    d.text(s,10.08,3.08,2.7,.9,'✓ Guardado\n→ Mis guardados',size=21,color=BLUE,bold=True)
    d.text(s,.5,5.0,12.1,.4,'Artículo → Lectura → Mismo texto con nuevos ajustes',size=24,bold=True)
    d.text(s,.5,5.75,12.1,.4,'Artículo → Comentario → Validar → Confirmación o corrección',size=22)
    d.text(s,.5,6.48,12.1,.4,'Quitar un guardado → aviso + Deshacer · Volver conserva búsqueda y filtros.',size=19,color=BLUE)
    d.notes(s,'Explicar el caso sin resultados y la validación de comentarios. Un error conserva los datos y ofrece la acción para resolverlo. No hay que repetir toda la tarea. Guardar cambia el texto del botón; quitar un guardado ofrece Deshacer. El flujo completo está dibujado en la memoria.')

    s=d.slide('5 · Boceto: portada y búsqueda','Buscar y reconocer contenido antes de empezar a leer')
    d.picture(s,DESIGN/'01_inicio_escritorio.png',.48,1.5,7.5,5.2)
    d.rect(s,8.27,1.55,4.55,5.12)
    d.text(s,8.47,1.88,4.15,1.0,'Laura necesita encontrar y guardar en pocos pasos.',size=23,bold=True)
    d.text(s,8.47,3.22,4.15,2.55,'• Buscador visible.\n• Etiquetas con estado activo.\n• Resumen y minutos.\n• Guardar desde cada tarjeta.\n• Índice de todos los artículos.',size=21)
    d.text(s,8.47,6.03,4.15,.45,'A2 · B1 · D3 · J1 / H6',size=17,color=BLUE,bold=True)
    d.notes(s,'Las cajas cruzadas son imágenes pendientes. A2: mosaico editorial. B1: varias vías de acceso. D3: titulares y resúmenes. J1: búsqueda. H6: reconocer las opciones. El índice de la revista se genera con todos los artículos. Los SVG se entregan editables e importables en Figma; no se ha creado un archivo nativo.')

    s=d.slide('5 · Boceto: lectura en tres formatos','Escritorio, tablet y móvil comparten los mismos controles')
    d.picture(s,DESIGN/'02_articulo_escritorio.png',.4,1.53,6.4,4.98)
    d.picture(s,DESIGN/'07_articulo_tablet.png',6.95,1.58,3.55,4.85)
    d.picture(s,DESIGN/'06_articulo_movil.png',10.78,1.58,1.97,4.85)
    d.text(s,.5,6.59,12.2,.35,'Miguel: tema y letra · Siobhán: estados con texto · Laura: minutos, progreso y Guardar.',size=18,color=BLUE,bold=True)
    d.notes(s,'Escritorio de 1440 px, tablet de 768 px y móvil de 390 px. El índice se pliega para liberar espacio. La lectura ofrece Claro, Oscuro y Sepia, y tres tamaños de fuente. B9 accesibilidad y D11 presentación mediante estilos; H3 control, H4 consistencia y H7 flexibilidad. Botones táctiles planteados con al menos 44 px de alto. En este boceto móvil se representa sepia y letra grande.')

    s=d.slide('5 · Boceto: estados y comentarios','Confirmaciones, errores y alternativas para continuar')
    d.picture(s,DESIGN/'08_estados_y_comentarios.png',.45,1.48,8.05,5.1)
    d.text(s,8.83,1.8,4.0,1.0,'El color se acompaña siempre de texto o marcas.',size=23,bold=True)
    d.text(s,8.83,3.17,4.0,2.52,'• Sin resultados: editar o quitar filtros.\n• Sin guardados: explorar.\n• Comentario: corregir y confirmar.\n• Quitar guardado: deshacer.',size=21)
    d.text(s,8.83,6.13,4.0,.4,'K12 · K13 / H1 · H3 · H9',size=17,color=BLUE,bold=True)
    d.notes(s,'K12 prevención y K13 mensajes de error comprensibles. H1 feedback, H3 control y H9 recuperación. El formulario conserva el alias y lo escrito. La confirmación aparece en la misma zona. Se muestran estados alternativos de un boceto, no un sitio ya implementado. La pantalla de Guardados aparece completa en la memoria.')

    s=d.slide('5 · Decisiones justificadas y cierre','Cada decisión responde a una necesidad de las personas')
    rows=[('Necesidad','Decisión','Patrones / heurísticas'),('Laura · rapidez','Buscar, filtrar y guardar.','B1 + J1 / H6 + H7'),('Miguel · comodidad','Temas, letra y texto despejado.','B9 + I3 + D11 / H3 + H8'),('Siobhán · claridad','Texto e iconos, ES/EN y consistencia.','D1 + D10 / H2 + H4'),('Las tres · recuperarse','Errores claros, ayuda y deshacer.','H8 + K13 / H3 + H9 + H10')]
    for i,row in enumerate(rows):
        y=1.55+i*.77
        d.rect(s,.5,y,12.3,.67,BLUE if i==0 else PALE)
        for x,w,t in zip([.65,3.6,8.3],[2.75,4.45,4.2],row):
            d.text(s,x,y+.12,w,.51,t,size=17,color='FFFFFF' if i==0 else INK,bold=i==0)
    d.text(s,.6,5.73,12.1,.8,'Una estructura sencilla para descubrir, leer con comodidad y volver a lo guardado.',size=24,color=BLUE,bold=True)
    d.text(s,.6,6.70,12.1,.3,'Bocetos SVG preparados para importar y conectar en Figma.',size=16,color=MUTED)
    d.notes(s,'Los códigos se refieren a la segunda edición de The Design of Sites y a las diez heurísticas de Nielsen. H8 en la columna de patrones es ayuda contextual; H8 entre heurísticas es simplicidad visual. El catálogo se cita en la memoria. La importación y conexión en Figma queda pendiente por no tener acceso a la aplicación. No se han implementado ni evaluado todavía las pantallas.')

    s=d.slide('Fuentes','Referencias del análisis y de los criterios de diseño · Consulta: 05/11/2026')
    entries=[
        ('Enunciado de la práctica','PDF del repositorio · Secciones 2 y 3',''),
        ('Xataka','Portada y artículo de muestra',SITIOS[0]['url']),
        ('Smashing Magazine','Portada y artículo de muestra',SITIOS[1]['url']),
        ('Ethic','Portada y artículo de muestra',SITIOS[2]['url']),
        ('Nielsen Norman Group','10 heurísticas de usabilidad',FUENTES[7][1]),
        ('Van Duyne, Landay y Hong','The Design of Sites · 2.ª edición, 2006',FUENTES[8][1]),
        ('Fotografías de perfiles','Random User / UI Faces y enunciado',FUENTES[9][1]),
    ]
    for i,(title,detail,url) in enumerate(entries):
        y=1.55+i*.69
        box=d.text(s,.6,y,4.5,.44,title,size=20,bold=True)
        d.text(s,5.4,y,7.1,.44,detail,size=19,color=MUTED)
        if url: box.text_frame.paragraphs[0].runs[0].hyperlink.address=url
    d.text(s,.6,6.63,12,.33,'Los enlaces a cada artículo y los créditos completos están en la memoria.',size=16,color=BLUE)
    d.notes(s,'Las capturas son reales y se obtuvieron en escritorio. El texto del análisis distingue observaciones de decisiones propias. Laura y Miguel son perfiles ficticios; la fotografía no identifica a esos personajes. Siobhán procede del enunciado. Todos los diagramas y bocetos son de elaboración propia.')
    dest=OUT/'Pausa_Presentacion_Punto_6.pptx'
    d.p.save(dest)
    print(dest)
    print(f'{len(d.p.slides)} diapositivas')


if __name__=='__main__':
    create_word()
    create_ppt()
