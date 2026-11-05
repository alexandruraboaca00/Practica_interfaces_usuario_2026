"""Genera diagramas y wireframes vectoriales editables para Pausa."""
from pathlib import Path
from html import escape
import textwrap
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'diseno'
PNG = ROOT / 'doc/recursos/diseno'
OUT.mkdir(exist_ok=True)
PNG.mkdir(parents=True, exist_ok=True)
INK, MUTED, BLUE = '#202833', '#596574', '#244D72'
LINE, PALE, WHITE = '#B8C0C8', '#F1F3F5', '#FFFFFF'


class SVG:
    def __init__(self, w, h, title):
        self.w, self.h = w, h
        self.items = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
                      f'<title>{escape(title)}</title>']
        self.rect(0, 0, w, h, fill=WHITE, stroke='none')

    def rect(self, x, y, w, h, fill=WHITE, stroke=LINE, r=5, sw=1):
        self.items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def text(self, x, y, content, size=20, color=INK, bold=False, anchor='start'):
        family = 'DejaVu Sans' if any(c in str(content) for c in '✓→') else 'Arial, Liberation Sans, sans-serif'
        self.items.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}" text-anchor="{anchor}">{escape(str(content))}</text>')

    def wrap(self, x, y, content, width=60, size=20, leading=None, color=INK, bold=False):
        lines = textwrap.wrap(content, width=width, break_long_words=False)
        for i, line in enumerate(lines):
            self.text(x, y + i * (leading or size*1.45), line, size, color, bold)
        return y + len(lines) * (leading or size*1.45)

    def line(self, x1, y1, x2, y2, color=LINE, sw=1):
        self.items.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"/>')

    def path(self, points, arrow=False, color=BLUE, sw=2):
        s = ' '.join(f'{x},{y}' for x, y in points)
        self.items.append(f'<polyline points="{s}" fill="none" stroke="{color}" stroke-width="{sw}"/>')
        if arrow:
            (x0,y0),(x,y)=points[-2:]
            if x == x0:
                dy = 1 if y > y0 else -1
                self.path([(x-6,y-10*dy),(x,y),(x+6,y-10*dy)], color=color, sw=sw)
            else:
                dx = 1 if x > x0 else -1
                self.path([(x-10*dx,y-6),(x,y),(x-10*dx,y+6)], color=color, sw=sw)

    def button(self, x, y, w, label, selected=False, h=44, size=17):
        self.rect(x,y,w,h,fill=BLUE if selected else WHITE,stroke=BLUE if selected else LINE)
        self.text(x+w/2,y+h/2+size*.35,label,size,WHITE if selected else INK,selected,'middle')

    def placeholder(self, x, y, w, h, label='Imagen del artículo'):
        self.rect(x,y,w,h,fill=PALE)
        self.line(x,y,x+w,y+h)
        self.line(x+w,y,x,y+h)
        self.rect(x+w/2-95,y+h/2-15,190,30,fill=PALE,stroke='none')
        self.text(x+w/2,y+h/2+6,label,17,MUTED,anchor='middle')

    def bars(self, x, y, width, n=3, step=25):
        for i in range(n):
            self.rect(x,y+i*step,width*(.76 if i==n-1 else 1),8,fill='#D9DEE3',stroke='none',r=2)

    def label(self, x, y, n, content):
        self.rect(x,y-20,27,27,fill=BLUE,stroke=BLUE,r=14)
        self.text(x+13.5,y-1,n,16,WHITE,True,'middle')
        self.text(x+37,y,content,17,BLUE)

    def save(self, name):
        source='\n'.join(self.items+['</svg>'])
        (OUT/f'{name}.svg').write_text(source,encoding='utf-8')
        cairosvg.svg2png(bytestring=source.encode(),write_to=str(PNG/f'{name}.png'),scale=1.35)
        print(name)


def header(s, active='Inicio', progress=False):
    if progress:
        s.rect(0,0,1440,7,fill='#E0E4E8',stroke='none',r=0)
        s.rect(0,0,504,7,fill=BLUE,stroke='none',r=0)
    s.text(48,60,'PAUSA',36,BLUE,True)
    for x, label in [(260,'Inicio'),(360,'Explorar'),(495,'Índice de la revista'),(750,'Guardados')]:
        s.text(x,58,label,21,BLUE if active==label else INK,active==label)
        if active==label:
            s.line(x,72,x+len(label)*10,72,BLUE,3)
    s.button(1100,26,135,'Lectura')
    s.button(1255,26,135,'ES / EN v')
    s.line(0,92,1440,92)


def footer(s, y):
    s.line(48,y-30,1392,y-30)
    s.text(48,y,'PAUSA · Cultura, ciencia y vida cotidiana',17,MUTED)
    s.text(1120,y,'Ayuda · Accesibilidad',17,BLUE)


def article_card(s,x,y,w,title,category='Cultura',saved=False):
    s.rect(x,y,w,330)
    s.placeholder(x+15,y+15,w-30,110)
    s.text(x+20,y+155,category.upper(),15,BLUE,True)
    s.wrap(x+20,y+188,title,width=max(22,int(w/12)),size=24,bold=True,leading=29)
    s.text(x+20,y+267,'6 min · 1200 palabras',16,MUTED)
    s.button(x+20,y+283,105,'Leer',h=32,size=16)
    s.button(x+w-160,y+283,140,'✓ Guardado' if saved else '+ Guardar',saved,h=32,size=16)


def home():
    s=SVG(1440,1000,'WF01 · Inicio de Pausa · Escritorio 1440 px')
    header(s)
    s.text(48,146,'Una pausa para entender el mundo',34,bold=True)
    s.text(48,180,'Artículos de cultura, ciencia y vida cotidiana. Lee a tu ritmo.',21,MUTED)
    s.rect(48,211,730,52,fill=PALE)
    s.text(68,245,'Buscar por título o contenido…',20,MUTED)
    s.button(795,211,140,'Buscar',True,h=52,size=20)
    for x,w,label in [(48,100,'Todas'),(160,120,'Cultura'),(292,120,'Ciencia'),(424,140,'Sociedad')]:
        s.button(x,286,w,label,label=='Todas')
    s.text(48,380,'Destacado',24,bold=True)
    s.placeholder(48,401,470,235)
    s.text(545,432,'SOCIEDAD',16,BLUE,True)
    s.wrap(545,478,'La ciudad también se puede leer despacio',width=23,size=31,bold=True,leading=39)
    s.wrap(545,574,'Pequeños cambios que nos ayudan a mirar de otra forma lo cotidiano.',width=36,size=20,color=MUTED)
    s.text(545,647,'Ana Ruiz · 05/11/2026 · 6 min',18,MUTED)
    s.button(545,673,160,'Leer artículo',True)
    s.button(725,673,160,'+ Guardar')
    s.rect(986,211,406,508,fill=PALE)
    s.text(1010,254,'Índice de la revista',26,bold=True)
    s.text(1010,285,'Todas las historias de esta revista',17,MUTED)
    for i,title in enumerate(['La ciudad también se puede leer despacio','Lo que cuenta un museo de barrio','Ciencia para una tarde de lluvia','Ideas para una vida con menos ruido']):
        s.text(1010,335+i*88,f'0{i+1}',17,BLUE,True)
        s.wrap(1050,335+i*88,title,width=25,size=20,color=BLUE)
        s.line(1010,391+i*88,1368,391+i*88)
    s.text(48,772,'Más historias',24,bold=True)
    for x,t in [(48,'Cultura y memoria'),(505,'Ciencia cotidiana'),(962,'Sociedad y futuro')]:
        s.rect(x,795,430,95,fill=PALE)
        s.text(x+20,837,t,23,bold=True)
        s.text(x+20,869,'Resumen · Tiempo de lectura · Guardar',17,MUTED)
    footer(s,965)
    s.save('01_inicio_escritorio')


def article():
    s=SVG(1440,1120,'WF02 · Artículo y controles de lectura · Escritorio')
    header(s,active='Explorar',progress=True)
    s.text(48,130,'Inicio  /  Sociedad  /  Artículo',17,BLUE)
    s.text(960,130,'Progreso de lectura: 35 %',17,BLUE)
    s.wrap(48,190,'La ciudad también se puede leer despacio',width=40,size=41,bold=True,leading=48)
    s.text(48,296,'Ana Ruiz · 05/11/2026 · 1200 palabras · 6 min de lectura',19,MUTED)
    s.button(48,320,160,'+ Guardar')
    s.button(225,320,190,'Ver comentarios')
    s.rect(48,388,900,618,fill=WHITE)
    s.placeholder(74,410,848,170)
    s.text(86,624,'Una forma distinta de mirar',29,bold=True)
    y=s.wrap(86,668,'Las calles cuentan historias que a menudo pasan desapercibidas. Una plaza, una biblioteca o un paseo de barrio pueden convertirse en una oportunidad para detenernos y observar.',width=65,size=22,leading=33)
    y=s.wrap(86,y+22,'Leer con calma permite relacionar ideas y encontrar preguntas nuevas. Por eso, cada persona puede elegir la apariencia que le resulte más cómoda.',width=65,size=22,leading=33)
    s.bars(86,y+25,760,3,step=28)
    s.rect(986,167,406,412,fill=PALE)
    s.text(1010,207,'Lectura',27,bold=True)
    s.text(1010,244,'Tema de color',18,bold=True)
    s.button(1010,261,110,'Claro',True)
    s.button(1128,261,113,'Oscuro')
    s.button(1249,261,115,'Sepia')
    s.text(1010,343,'Tamaño de letra',18,bold=True)
    for x,w,t in [(1010,110,'Pequeño'),(1128,113,'Mediano'),(1249,115,'Grande')]:
        s.button(x,360,w,t,t=='Mediano',size=16)
    s.text(1010,436,'Preferencias en este dispositivo',17,MUTED)
    s.button(1010,459,354,'Restablecer lectura',h=42)
    s.text(1010,544,'Tiempo estimado de lectura: 6 minutos',16,MUTED)
    s.rect(986,610,406,396,fill=PALE)
    s.text(1010,652,'Índice de la revista',26,bold=True)
    s.wrap(1010,697,'01 · La ciudad también se puede leer despacio',width=30,size=20,color=BLUE,bold=True)
    s.wrap(1010,778,'02 · Lo que cuenta un museo de barrio',width=30,size=20,color=BLUE)
    s.wrap(1010,859,'03 · Ciencia para una tarde de lluvia',width=30,size=20,color=BLUE)
    s.text(1010,969,'Cada enlace abre un artículo',17,MUTED)
    s.text(48,1047,'Al final del texto: etiquetas · comentarios · artículos relacionados',18,MUTED)
    footer(s,1092)
    s.save('02_articulo_escritorio')


def search():
    s=SVG(1440,960,'WF03 · Buscar, filtrar y resaltar coincidencias')
    header(s,'Explorar')
    s.text(48,155,'Explorar artículos',34,bold=True)
    s.rect(48,185,780,56,fill=PALE)
    s.text(68,221,'ciudad',24)
    s.button(845,185,130,'Buscar',True,h=56,size=20)
    s.button(995,185,145,'Limpiar',h=56,size=20)
    for x,w,t in [(48,120,'Todas'),(180,140,'Cultura'),(332,140,'Ciencia'),(484,150,'Sociedad')]:
        s.button(x,269,w,t,t=='Sociedad')
    s.text(48,355,'3 resultados para «ciudad»',27,bold=True)
    s.text(48,391,'Filtro activo: Sociedad  ×     ·     Quitar filtros',20,BLUE)
    titles=['La ciudad también se puede leer despacio','La ciudad y sus espacios compartidos','Aprender a escuchar una ciudad']
    for i,t in enumerate(titles):
        y=426+i*142
        s.rect(48,y,1344,124)
        s.placeholder(64,y+16,160,92,'Imagen')
        words=t.split('ciudad')
        # Segmentos separados para que el término resaltado siga siendo editable.
        x=250
        s.text(x,y+39,words[0],25,bold=True)
        x += len(words[0])*13.5
        s.rect(x-2,y+16,86,31,fill='#FFE49C',stroke=INK,r=1)
        s.text(x,y+39,'ciudad',25,bold=True)
        s.text(x+91,y+39,words[1],25,bold=True)
        s.text(250,y+77,'Extracto del contenido con coincidencias destacadas y etiqueta Sociedad.',19,MUTED)
        s.text(250,y+104,'6 min de lectura',17,MUTED)
        s.button(1190,y+67,175,'+ Guardar',h=36,size=18)
    footer(s,930)
    s.save('03_busqueda_escritorio')


def saved():
    s=SVG(1440,860,'WF04 · Guardados y deshacer')
    header(s,'Guardados')
    s.text(48,157,'Mis artículos guardados',36,bold=True)
    s.text(48,197,'Guardados en este dispositivo · 2 artículos',21,MUTED)
    article_card(s,48,236,650,'La ciudad también se puede leer despacio','Sociedad',True)
    article_card(s,742,236,650,'Lo que cuenta un museo de barrio','Cultura',True)
    s.rect(48,610,1344,90,fill=PALE,stroke=BLUE,sw=2)
    s.text(72,650,'Artículo eliminado de Guardados.',24,bold=True)
    s.text(72,680,'Puedes recuperarlo sin repetir la búsqueda.',18,MUTED)
    s.button(1180,633,180,'Deshacer',True)
    s.text(48,755,'Al pulsar «✓ Guardado», se elimina el artículo y aparece este aviso.',19,MUTED)
    footer(s,828)
    s.save('04_guardados_escritorio')


def mobile_header(s,progress=False):
    if progress:
        s.rect(0,0,390,6,fill=PALE,stroke='none',r=0)
        s.rect(0,0,137,6,fill=BLUE,stroke='none',r=0)
    s.text(18,51,'PAUSA',28,BLUE,True)
    s.button(213,17,72,'ES/EN',size=14)
    s.button(295,17,77,'Menú',size=15)
    s.line(0,78,390,78)


def mobile():
    s=SVG(390,1010,'WF05 · Inicio móvil · 390 px')
    mobile_header(s)
    s.wrap(18,120,'Una pausa para entender el mundo',width=21,size=29,bold=True,leading=34)
    s.rect(18,210,255,48,fill=PALE)
    s.text(29,241,'Buscar artículos…',18,MUTED)
    s.button(281,210,91,'Buscar',True,h=48,size=16)
    for x,w,t in [(18,92,'Todas'),(121,112,'Cultura'),(244,128,'Ciencia')]:
        s.button(x,279,w,t,t=='Todas',size=17)
    s.button(18,337,354,'Índice de la revista  v',h=48,size=20)
    s.text(18,430,'Destacado',23,bold=True)
    s.placeholder(18,453,354,161)
    s.wrap(18,659,'La ciudad también se puede leer despacio',width=24,size=29,bold=True,leading=35)
    s.text(18,766,'Sociedad · Ana Ruiz · 6 min',18,MUTED)
    s.button(18,793,168,'Leer artículo',True,h=48,size=18)
    s.button(199,793,173,'+ Guardar',h=48,size=18)
    s.text(18,894,'Más historias',24,bold=True)
    s.line(0,935,390,935)
    s.text(26,974,'Inicio',18,BLUE,True)
    s.text(132,974,'Explorar',18)
    s.text(260,974,'Guardados',18)
    s.save('05_inicio_movil')

    s=SVG(390,1270,'WF06 · Artículo móvil y lectura · 390 px')
    mobile_header(s,True)
    s.text(18,110,'< Resultados   ·   Progreso: 35 %',17,BLUE)
    s.wrap(18,157,'La ciudad también se puede leer despacio',width=22,size=30,bold=True,leading=36)
    s.text(18,285,'Ana Ruiz · 1200 palabras · 6 min',17,MUTED)
    s.button(18,310,168,'+ Guardar',h=48,size=18)
    s.button(199,310,173,'Lectura  v',True,h=48,size=18)
    s.rect(18,377,354,220,fill=PALE,stroke=BLUE)
    s.text(33,412,'Tema',18,bold=True)
    for x,w,t in [(33,95,'Claro'),(139,98,'Oscuro'),(248,109,'Sepia')]:
        s.button(x,428,w,t,t=='Sepia',h=44,size=16)
    s.text(33,508,'Letra',18,bold=True)
    for x,w,t in [(33,95,'Pequeño'),(139,98,'Mediano'),(248,109,'Grande')]:
        s.button(x,524,w,t,t=='Grande',h=44,size=14)
    s.button(18,614,354,'Índice de la revista  v',h=48,size=20)
    s.rect(18,681,354,445,fill='#F3E9D7',stroke='#998C79')
    s.wrap(33,718,'Una forma distinta de mirar',width=23,size=24,bold=True,leading=29)
    s.wrap(33,804,'Las calles cuentan historias que a menudo pasan desapercibidas. Una plaza o una biblioteca pueden convertirse en una oportunidad para detenernos y observar.',width=25,size=24,leading=35)
    s.text(18,1165,'Etiquetas: Sociedad · Ciudad',17,BLUE)
    s.button(18,1190,354,'Ver comentarios (2)',h=48,size=20)
    s.save('06_articulo_movil')


def tablet():
    s=SVG(768,1024,'WF07 · Artículo en tablet · 768 px')
    s.text(30,53,'PAUSA',31,BLUE,True)
    s.text(205,50,'Inicio',18)
    s.text(287,50,'Explorar',18)
    s.text(391,50,'Guardados',18)
    s.button(545,22,86,'Lectura',size=15)
    s.button(642,22,96,'ES / EN',size=15)
    s.rect(0,79,768,6,fill=PALE,stroke='none',r=0)
    s.rect(0,79,269,6,fill=BLUE,stroke='none',r=0)
    s.text(30,124,'Inicio / Sociedad / Artículo',17,BLUE)
    s.wrap(30,177,'La ciudad también se puede leer despacio',width=33,size=36,bold=True,leading=44)
    s.text(30,286,'Ana Ruiz · 1200 palabras · 6 min · Progreso: 35 %',19,MUTED)
    s.button(30,313,180,'+ Guardar',h=48,size=19)
    s.button(230,313,238,'Índice de la revista  v',h=48,size=18)
    s.button(489,313,249,'Lectura: Claro · Mediano',h=48,size=17)
    s.placeholder(30,391,708,230)
    s.text(62,674,'Una forma distinta de mirar',29,bold=True)
    s.wrap(62,722,'Las calles cuentan historias que a menudo pasan desapercibidas. Una plaza, una biblioteca o un paseo de barrio pueden convertirse en una oportunidad para detenernos y observar.',width=50,size=22,leading=33)
    s.bars(62,900,644,3,step=27)
    s.save('07_articulo_tablet')


def states():
    s=SVG(1440,880,'WF08 · Estados vacíos, validación y comentarios')
    s.text(40,56,'Estados y comentarios',34,bold=True)
    s.rect(40,92,650,310,fill=PALE)
    s.text(64,135,'Búsqueda sin resultados',25,bold=True)
    s.text(64,181,'0 resultados para «ciudadd»',23)
    s.wrap(64,224,'Revisa la palabra o elimina alguna etiqueta. La consulta se conserva para que puedas corregirla.',width=49,size=20)
    s.button(64,333,265,'Quitar filtros',True)
    s.button(350,333,315,'Editar búsqueda')
    s.rect(730,92,670,310,fill=PALE)
    s.text(754,135,'Guardados vacíos',25,bold=True)
    s.wrap(754,193,'Todavía no has guardado artículos. Pulsa «+ Guardar» en una tarjeta o en un artículo.',width=48,size=22)
    s.button(754,322,370,'Explorar artículos',True)
    s.rect(40,442,1360,390)
    s.text(64,487,'Comentarios',28,bold=True)
    s.text(64,527,'Nombre o alias *',18,bold=True)
    s.rect(64,542,590,45,fill=PALE)
    s.text(77,573,'Siobhán',20)
    s.text(64,622,'Comentario *',18,bold=True)
    s.rect(64,637,590,93,stroke=INK,sw=2)
    s.text(64,760,'! Escribe un comentario antes de enviarlo.',18,bold=True)
    s.text(599,760,'0/500',17,MUTED)
    s.button(64,779,255,'Publicar comentario',True,h=36)
    s.text(718,531,'Confirmación tras corregir:',21,bold=True)
    s.rect(718,552,650,98,fill=PALE,stroke=BLUE,sw=2)
    s.text(738,591,'✓ Comentario publicado',24,BLUE,True)
    s.text(738,625,'Tu mensaje aparece en la lista.',20)
    s.text(718,707,'Siobhán · ahora',19,bold=True)
    s.wrap(718,745,'Me ha gustado esta forma de mirar la ciudad.',width=46,size=22)
    s.save('08_estados_y_comentarios')


def structure():
    s=SVG(1440,800,'Diagrama de estructura del sitio Pausa')
    s.text(40,52,'Estructura del sitio',32,bold=True)
    s.rect(570,92,300,80,fill=BLUE,stroke=BLUE)
    s.text(720,142,'Pausa',32,WHITE,True,'middle')
    positions=[45,325,605,885,1165]
    titles=['Inicio','Explorar','Índice de la revista','Guardados','Ayuda']
    bodies=[['Destacado','Últimos artículos'],['Categorías y etiquetas','Búsqueda y resultados'],['Listado automático','Enlace a cada artículo'],['Lista de favoritos','Estado vacío'],['Cómo guardar y leer','Accesibilidad']]
    s.path([(720,172),(720,205),(165,205)])
    s.path([(720,205),(1285,205)])
    for x,t,body in zip(positions,titles,bodies):
        s.path([(x+120,205),(x+120,240)],True)
        s.rect(x,240,240,158,fill=PALE)
        s.text(x+120,282,t,22,BLUE,True,'middle')
        for i,b in enumerate(body):
            s.text(x+120,327+i*30,b,18,anchor='middle')
    for x in positions[:4]:
        s.path([(x+120,398),(x+120,440),(650,440)])
    s.path([(650,440),(650,480)],True)
    s.rect(350,480,600,160,fill=PALE,stroke=BLUE,sw=2)
    s.text(650,523,'Artículo',29,BLUE,True,'middle')
    s.text(650,564,'Texto · Autor · Etiquetas · Relacionados',21,anchor='middle')
    s.text(650,600,'Tiempo · Progreso · Guardar · Comentarios',20,anchor='middle')
    s.rect(40,690,1360,74,fill=PALE)
    s.text(62,720,'Controles globales: idioma ES/EN y lectura (tema y tamaño). No son páginas independientes.',20)
    s.text(62,750,'Un mismo artículo se abre desde Inicio, Explorar, Índice o Guardados.',19,MUTED)
    s.save('09_diagrama_estructura')


def node(s,x,y,w,label,detail='',h=82):
    s.rect(x,y,w,h,fill=PALE,stroke=BLUE)
    s.text(x+w/2,y+32,label,22,BLUE,True,'middle')
    if detail:
        s.text(x+w/2,y+61,detail,17,anchor='middle')


def navigation():
    s=SVG(1440,1020,'Diagrama de navegación: búsqueda, lectura, guardados y comentarios')
    s.text(40,50,'Navegación y respuesta de la interfaz',32,bold=True)
    node(s,40,96,235,'Inicio')
    node(s,365,96,280,'Buscar / etiqueta','Introducir o elegir')
    node(s,745,96,280,'Resultados','Abrir una tarjeta')
    node(s,1125,96,275,'Artículo','Leer y personalizar')
    for a,b in [(275,365),(645,745),(1025,1125)]:
        s.path([(a,137),(b,137)],True)
    node(s,365,238,280,'Índice de la revista','Elegir un artículo')
    s.path([(158,178),(158,279),(365,279)],True)
    s.path([(645,279),(1262,279),(1262,178)],True)
    node(s,745,338,280,'0 resultados','Revisar texto / quitar filtros')
    s.path([(885,178),(885,338)],True)
    s.path([(745,379),(700,379),(700,205),(505,205),(505,178)],True)
    s.text(910,312,'Si no hay coincidencias',16,MUTED)
    node(s,40,510,300,'Artículo','Pulsar «+ Guardar»')
    node(s,405,510,300,'✓ Guardado','Aviso y estado del botón')
    node(s,770,510,300,'Mis guardados','Abrir o quitar artículo')
    node(s,1135,510,265,'Deshacer','Recuperar lo eliminado')
    s.path([(340,551),(405,551)],True)
    s.path([(705,551),(770,551)],True)
    s.path([(1070,551),(1135,551)],True)
    s.path([(920,592),(920,637),(190,637),(190,592)],True)
    s.text(504,630,'Abrir artículo guardado',17,MUTED)
    s.path([(1267,592),(1267,663),(1060,663),(1060,592)],True)
    node(s,40,752,265,'Comentarios','Alias + mensaje')
    node(s,390,752,265,'Validar','Campos / 500 caracteres')
    node(s,740,752,265,'Error en campo','Conservar y corregir')
    node(s,1090,752,310,'Comentario publicado','Confirmación y lista')
    s.path([(305,793),(390,793)],True)
    s.path([(655,793),(740,793)],True)
    s.text(665,779,'Error',16,MUTED)
    s.path([(872,834),(872,881),(523,881),(523,834)],True)
    s.path([(523,752),(523,709),(1245,709),(1245,752)],True)
    s.text(815,701,'Datos válidos',17,MUTED)
    s.rect(40,928,1360,63,fill=PALE)
    s.text(62,966,'Tema, tamaño e idioma cambian en la misma pantalla. «Volver» conserva búsqueda y filtros.',20)
    s.save('10_diagrama_navegacion')


if __name__=='__main__':
    for create in [home,article,search,saved,mobile,tablet,states,structure,navigation]:
        create()
