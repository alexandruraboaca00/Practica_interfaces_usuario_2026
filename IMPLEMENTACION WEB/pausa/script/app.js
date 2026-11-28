(() => {
  'use strict';
  const C = globalThis.PausaCore, DATA = globalThis.PausaData;
  const $ = selector => document.querySelector(selector);
  const e = C.escapeHTML;
  const KEY = 'pausa:v1';
  const categories = ['all', 'cultura', 'ciencia', 'sociedad', 'vida'];
  const words = {
    es: {
      skip:'Saltar al contenido', home:'Inicio', explore:'Explorar', index:'Índice', saved:'Guardados', reading:'Lectura', language:'Idioma', help:'Ayuda', helpAccess:'Ayuda y accesibilidad',
      footerLine:'Menos ruido. Más historias que importan.', project:'Proyecto académico · Interfaces de Usuario · UC3M 2026/2027', localNote:'Tus lecturas, en este dispositivo.',
      readingPrefs:'A tu manera', prefsIntro:'Un espacio cómodo para cada lectura.', prefsSaved:'Recordaremos tus preferencias en este dispositivo.',
      all:'Todas', cultura:'Cultura', ciencia:'Ciencia', sociedad:'Sociedad', vida:'Vida cotidiana',
      eyebrow:'EL ARTE DE TOMARSE UN MOMENTO', heroTitle:'Una pausa para<br><em>entender el mundo.</em>', heroIntro:'Historias de cultura, ciencia y vida cotidiana. Sin prisa, con curiosidad.', edition:'EDICIÓN DE NOVIEMBRE · 2026',
      searchLabel:'Buscar en la revista', searchPlaceholder:'Busca una historia, un tema, una idea…', search:'Buscar', clear:'Limpiar filtros', categories:'Filtrar por categoría',
      featured:'La historia destacada', more:'Más historias, otras miradas', read:'Leer artículo', minute:'min de lectura', save:'Guardar', savedState:'Guardado', remove:'Quitar de guardados',
      contents:'En esta edición', contentsIntro:'Un pequeño mapa para tu próxima lectura.', viewIndex:'Ver todo el índice', allStories:'Todas las historias',
      exploreIntro:'Sigue tu curiosidad. Hay una historia para cada momento.', savedIntro:'Un lugar para las historias a las que quieres volver.',
      results:'historias', result:'historia', resultFor:'para', noResults:'Todavía no encontramos esa historia.', noResultsText:'Prueba con otra palabra o cambia la categoría. Tu consulta sigue aquí.',
      emptySaved:'Las buenas historias merecen una segunda lectura.', emptySavedText:'Toca Guardar en cualquier artículo. Lo encontrarás aquí cuando quieras volver.', discover:'Descubrir historias',
      savedToast:'Artículo guardado para después.', removedToast:'Artículo quitado de guardados.', undo:'Deshacer', restored:'Artículo recuperado.',
      theme:'Tema de color', light:'Claro', dark:'Oscuro', sepia:'Sepia', font:'Tamaño del texto', small:'Pequeño', medium:'Mediano', large:'Grande', reset:'Restablecer preferencias',
      onThisPage:'En este artículo', comments:'Conversación', commentIntro:'¿Qué te ha hecho pensar esta historia?', alias:'Tu alias', aliasHint:'Entre 2 y 40 caracteres.', message:'Tu comentario', commentHint:'Entre 1 y 500 caracteres. Se conserva solo en este navegador.',
      publish:'Publicar comentario', aliasError:'Escribe un alias de entre 2 y 40 caracteres.', messageError:'Escribe un comentario de entre 1 y 500 caracteres.',
      commentSuccess:'Tu comentario se ha guardado en este navegador.', noComments:'La conversación está por empezar. Puedes abrirla tú.', localComments:'Los comentarios son locales: no se envían a un servidor ni se comparten entre dispositivos.',
      back:'Volver a las historias', related:'Para seguir leyendo', words:'palabras', progress:'Progreso de lectura', end:'Has llegado al final. Gracias por hacer una pausa.',
      imageCredit:'Imagen ilustrativa generada con IA.', photoCredit:'Fotografía de Unsplash.', close:'Cerrar', openMenu:'Abrir menú', closeMenu:'Cerrar menú', navigation:'Navegación principal', homeLabel:'Pausa, inicio',
      storageWarning:'El navegador no permite guardar los datos. Puedes seguir leyendo; los cambios se conservarán solo durante esta sesión.', notFound:'Esta historia no está en la revista.', notFoundText:'Puede que el enlace esté incompleto. Puedes volver al inicio o consultar el índice.',
      helpTitle:'Un espacio para leer a tu manera', helpIntro:'Las herramientas de Pausa, sin letra pequeña.',
      helpRead:'Personaliza tu lectura', helpReadText:'Abre Lectura en la cabecera o los controles de un artículo. Elige Claro, Oscuro o Sepia y un tamaño Pequeño, Mediano o Grande. La barra superior muestra tu avance dentro del texto. El tiempo se calcula con las palabras del artículo, a 200 palabras por minuto, redondeando hacia arriba.',
      helpSearch:'Encuentra y guarda historias', helpSearchText:'Busca en títulos y textos, combina la consulta con una categoría y reconoce las coincidencias resaltadas. El índice se genera desde el catálogo de la revista. Guardar añade un artículo a Guardados; si lo quitas, puedes deshacer la acción.',
      helpKeyboard:'Navega con teclado', helpKeyboardText:'Usa Tab y Mayús + Tab para recorrer los controles y Entrar o Espacio para activarlos. El primer enlace permite saltar al contenido. Escape cierra el menú y el panel de lectura. La tecla / lleva al buscador cuando no estás escribiendo.',
      helpPrivacy:'Tus datos se quedan aquí', helpPrivacyText:'Los guardados, comentarios y preferencias se almacenan en este navegador mediante almacenamiento local. No hay cuentas ni sincronización. Borrar los datos del navegador elimina esta información. Si el almacenamiento está bloqueado, puedes usar la web durante la sesión.',
      helpAbout:'Sobre Pausa', helpAboutText:'Revista de demostración creada para Interfaces de Usuario, UC3M, curso 2026/2027. Los artículos y sus firmas son contenido editorial ficticio para el proyecto. Equipo: Chao Chen, Alvaro Enrique Arnaiz, Alexandru David Raboaca y Marcos Rodriguez.',
      helpPhotos:'Imágenes', helpPhotosText:'El símbolo de Pausa procede de la identidad del proyecto. La imagen de la calle es una ilustración generada con IA; las otras fotografías proceden de Unsplash. Sus enlaces originales están en images/CREDITOS.txt, en el repositorio.',
      categoryIndex:'Índice de la revista', indexIntro:'Todas las historias de esta edición, en un solo lugar.', section:'Sección', readingNow:'Tu momento de lectura', dateLocale:'es-ES'
    },
    en: {
      skip:'Skip to content', home:'Home', explore:'Explore', index:'Index', saved:'Saved', reading:'Reading', language:'Language', help:'Help', helpAccess:'Help and accessibility',
      footerLine:'Less noise. More stories that matter.', project:'Academic project · User Interfaces · UC3M 2026/2027', localNote:'Your reading, on this device.',
      readingPrefs:'Make it yours', prefsIntro:'A comfortable space for every story.', prefsSaved:'We will remember your preferences on this device.',
      all:'All', cultura:'Culture', ciencia:'Science', sociedad:'Society', vida:'Everyday life',
      eyebrow:'THE ART OF TAKING A MOMENT', heroTitle:'A pause to<br><em>understand the world.</em>', heroIntro:'Stories about culture, science and everyday life. Unhurried and curious.', edition:'NOVEMBER EDITION · 2026',
      searchLabel:'Search the magazine', searchPlaceholder:'Find a story, a topic, an idea…', search:'Search', clear:'Clear filters', categories:'Filter by category',
      featured:'The featured story', more:'More stories, fresh perspectives', read:'Read article', minute:'min read', save:'Save', savedState:'Saved', remove:'Remove from saved',
      contents:'In this edition', contentsIntro:'A small map for your next read.', viewIndex:'See the full index', allStories:'All stories',
      exploreIntro:'Follow your curiosity. There is a story for every moment.', savedIntro:'A home for the stories you want to return to.',
      results:'stories', result:'story', resultFor:'for', noResults:'We have not found that story yet.', noResultsText:'Try another word or change the category. Your search is still here.',
      emptySaved:'Good stories deserve a second reading.', emptySavedText:'Choose Save on any article. You will find it here whenever you want to return.', discover:'Discover stories',
      savedToast:'Article saved for later.', removedToast:'Article removed from saved.', undo:'Undo', restored:'Article restored.',
      theme:'Colour theme', light:'Light', dark:'Dark', sepia:'Sepia', font:'Text size', small:'Small', medium:'Medium', large:'Large', reset:'Reset preferences',
      onThisPage:'In this article', comments:'Conversation', commentIntro:'What did this story make you think about?', alias:'Your alias', aliasHint:'Between 2 and 40 characters.', message:'Your comment', commentHint:'Between 1 and 500 characters. Kept in this browser only.',
      publish:'Post comment', aliasError:'Enter an alias between 2 and 40 characters.', messageError:'Enter a comment between 1 and 500 characters.',
      commentSuccess:'Your comment has been saved in this browser.', noComments:'The conversation has not started yet. You can open it.', localComments:'Comments are local: they are not sent to a server or shared across devices.',
      back:'Back to stories', related:'Keep reading', words:'words', progress:'Reading progress', end:'You have reached the end. Thank you for taking a pause.',
      imageCredit:'Illustrative image generated with AI.', photoCredit:'Photograph from Unsplash.', close:'Close', openMenu:'Open menu', closeMenu:'Close menu', navigation:'Main navigation', homeLabel:'Pausa, home',
      storageWarning:'Your browser cannot store data. You can keep reading; changes will last for this session only.', notFound:'This story is not in the magazine.', notFoundText:'The link may be incomplete. Return home or browse the index.',
      helpTitle:'A space to read your way', helpIntro:'The tools in Pausa, without the small print.',
      helpRead:'Make reading comfortable', helpReadText:'Open Reading in the header or use the article controls. Choose Light, Dark or Sepia and Small, Medium or Large text. The top bar tracks progress through the article body. Reading time uses the article’s word count at 200 words per minute, rounded up.',
      helpSearch:'Find and save stories', helpSearchText:'Search titles and article text, combine your query with a category and find highlighted matches. The index is generated from the magazine catalogue. Save adds an article to Saved; if you remove it, you can undo the action.',
      helpKeyboard:'Use your keyboard', helpKeyboardText:'Use Tab and Shift + Tab to move through controls, then Enter or Space to activate them. The first link skips to the content. Escape closes the menu and reading panel. Press / to reach search when you are not typing.',
      helpPrivacy:'Your data stays here', helpPrivacyText:'Saved articles, comments and preferences use local storage in this browser. There are no accounts or synchronisation. Clearing browser data removes them. If storage is blocked, you can still use the website during the session.',
      helpAbout:'About Pausa', helpAboutText:'A demonstration magazine for User Interfaces, UC3M, 2026/2027. Articles and bylines are fictional editorial content for the project. Team: Chao Chen, Alvaro Enrique Arnaiz, Alexandru David Raboaca and Marcos Rodriguez.',
      helpPhotos:'Images', helpPhotosText:'The Pausa symbol comes from the project’s visual identity. The street image was generated with AI; other photographs come from Unsplash. Original links are recorded in images/CREDITOS.txt in the repository.',
      categoryIndex:'Magazine index', indexIntro:'Every story in this edition, all in one place.', section:'Section', readingNow:'Your reading moment', dateLocale:'en-GB'
    }
  };
  let storageOK = true;
  let raw;
  try { const stored=localStorage.getItem(KEY);try{raw=JSON.parse(stored);}catch{raw=null;} } catch { storageOK = false; }
  let state = C.sanitizeState(raw, DATA.map(a => a.id));
  let query = '', category = 'all', route = 'inicio', currentId = null, undo = null, progressFrame = 0;
  let lastDialogTrigger = null, articleObserver = null;
  const t = key => words[state.language][key] || key;
  const article = item => ({...item, ...item[state.language]});
  const articles = () => DATA.map(article);
  const href = id => '#/articulo/' + id;
  const date = value => new Intl.DateTimeFormat(t('dateLocale'), {day:'numeric',month:'short',year:'numeric'}).format(new Date(value + (value.length === 10 ? 'T12:00:00' : '')));
  const icon = name => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${({bookmark:'<path d="M6 4h12v17l-6-4-6 4V4Z"/>',check:'<path d="m5 12 4 4L19 6"/>',search:'<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',clock:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',book:'<path d="M12 5v16M12 5C8 2 3 3 3 3v15s5-1 9 3c4-4 9-3 9-3V3s-5-1-9 2Z"/>'})[name] || ''}</svg>`;
  function persist() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch { storageOK = false; }
    $('#storage-warning').hidden = storageOK;
    $('#storage-warning').textContent = t('storageWarning');
  }
  function applyPreferences() {
    document.documentElement.dataset.theme = state.theme;
    document.documentElement.dataset.font = state.font;
    document.documentElement.lang = state.language;
    $('meta[name="theme-color"]').content = ({light:'#f8f7f3',dark:'#17222b',sepia:'#f1e7d5'})[state.theme];
    document.querySelectorAll('[data-i18n]').forEach(el => { el.textContent = t(el.dataset.i18n); });
    document.querySelectorAll('[data-home-label]').forEach(el => el.setAttribute('aria-label',t('homeLabel')));
    document.querySelectorAll('[data-nav-label]').forEach(el => el.setAttribute('aria-label',t('navigation')));
    $('#language').value = state.language; $('#language').setAttribute('aria-label',t('language'));
    $('#reading-progress').setAttribute('aria-label',t('progress'));
    $('[data-action="close-reading"]').setAttribute('aria-label',t('close'));
    $('[data-action="menu"]').setAttribute('aria-label',t('openMenu'));
    $('#dialog-options').innerHTML = options('dialog');
    $('#storage-warning').hidden = storageOK; $('#storage-warning').textContent = t('storageWarning');
  }
  function options(context) {
    return `<div class="preference-group" role="group" aria-labelledby="${context}-theme"><h3 id="${context}-theme">${t('theme')}</h3><div class="option-buttons">${['light','dark','sepia'].map(v=>`<button type="button" data-preference="theme" data-value="${v}" aria-pressed="${state.theme===v}"><span class="swatch swatch-${v}" aria-hidden="true"></span>${t(v)}</button>`).join('')}</div></div>
      <div class="preference-group" role="group" aria-labelledby="${context}-font"><h3 id="${context}-font">${t('font')}</h3><div class="option-buttons">${['small','medium','large'].map(v=>`<button type="button" data-preference="font" data-value="${v}" aria-pressed="${state.font===v}">${t(v)}</button>`).join('')}</div></div><button class="text-button reset-preferences" type="button" data-action="reset">${t('reset')}</button>`;
  }
  function saveButton(a, compact = false) {
    const saved = state.saved.includes(a.id);
    return `<button type="button" class="save-button ${compact?'compact':''} ${saved?'is-saved':''}" data-action="save" data-id="${a.id}" aria-pressed="${saved}" aria-label="${e((saved?t('remove'):t('save'))+': '+a.title)}">${icon(saved?'check':'bookmark')}<span${compact?' class="sr-only"':''}>${saved?t('savedState'):t('save')}</span></button>`;
  }
  function tag(a) { return `<button class="story-category" type="button" data-category-link="${a.category}">${t(a.category)}</button>`; }
  function metadata(a) { return `<span>${e(a.author)}</span><span class="meta-dot" aria-hidden="true">·</span><span>${C.readingMinutes(C.bodyText(a))} ${t('minute')}</span>`; }
  function card(a, featured = false) {
    let excerpt=a.excerpt;
    if(query&&!C.normalize(excerpt).includes(C.normalize(query))){
      const body=C.bodyText(a),at=C.normalize(body).indexOf(C.normalize(query));
      if(at>=0){const start=Math.max(0,at-55),end=Math.min(body.length,at+query.length+100);excerpt=(start?'…':'')+body.slice(start,end)+(end<body.length?'…':'');}
    }
    return `<article class="${featured?'hero-story':'story-card'}" data-story="${a.id}">
      <div class="story-image-wrap"><a class="story-image-link" href="${href(a.id)}" aria-label="${e(a.title)}"><img src="../images/${a.image}" alt="${e(a.alt[state.language])}" width="900" height="600" ${featured?'fetchpriority="high"':'loading="lazy"'}></a>${saveButton(a,true)}</div>
      <div class="story-copy">${tag(a)}<h2><a href="${href(a.id)}">${C.highlight(a.title,query)}</a></h2><p>${C.highlight(excerpt,query)}</p><div class="story-meta">${metadata(a)}</div>${featured?`<a class="primary-button" href="${href(a.id)}">${t('read')}</a>`:''}</div>
    </article>`;
  }
  function contents() {
    return `<aside class="edition-index" aria-labelledby="edition-title"><p class="eyebrow">PAUSA · 01</p><h2 id="edition-title">${t('contents')}</h2><p class="muted index-intro">${t('contentsIntro')}</p><ol>${articles().map(a=>`<li><a href="${href(a.id)}"><span>${e(a.title)}</span><span class="index-meta">${t(a.category)} · ${C.readingMinutes(C.bodyText(a))} min</span></a></li>`).join('')}</ol><a class="text-link" href="#/indice">${t('viewIndex')}</a><div class="editor-note"><span class="quote-mark" aria-hidden="true">“</span><p>${state.language==='es'?'No se trata de leer más.<br>Se trata de encontrar<br>algo que te acompañe.':'It is not about reading more.<br>It is about finding something<br>that stays with you.'}</p><span class="eyebrow">${state.language==='es'?'EL EQUIPO DE PAUSA':'THE PAUSA TEAM'}</span></div></aside>`;
  }
  function searchControls() {
    return `<form id="search-form" class="search-form" role="search"><label class="sr-only" for="search-input">${t('searchLabel')}</label><div class="search-input-wrap">${icon('search')}<input id="search-input" type="search" maxlength="120" placeholder="${t('searchPlaceholder')}" value="${e(query)}" autocomplete="off"><span class="search-shortcut" aria-hidden="true">/</span></div><button class="primary-button" type="submit">${t('search')}</button></form><div class="filter-row" role="group" aria-label="${t('categories')}">${categories.map(c=>`<button type="button" class="filter-button" data-category="${c}" aria-pressed="${c===category}">${t(c)}</button>`).join('')}</div>`;
  }
  function catalog() {
    const home = route === 'inicio', saved = route === 'guardados';
    const title = home ? t('heroTitle') : saved ? t('saved') : t('allStories');
    $('#app').innerHTML = `<div class="page-shell"><section class="welcome ${home?'':'welcome-small'}" aria-labelledby="page-title"><div><p class="eyebrow">${home?t('eyebrow'):'PAUSA · '+t(saved?'readingNow':'explore').toUpperCase()}</p><h1 id="page-title">${title}</h1><p class="welcome-intro">${t(home?'heroIntro':saved?'savedIntro':'exploreIntro')}</p></div>${home?`<span class="edition-label">${t('edition')}</span>`:''}</section><div class="catalog-layout"><section class="catalog-main" aria-label="${t('searchLabel')}">${searchControls()}<div id="catalog-results"></div></section>${contents()}</div></div>`;
    renderResults();
  }
  function renderResults() {
    const base = route === 'guardados' ? state.saved.map(id=>articles().find(a=>a.id===id)).filter(Boolean) : articles();
    const visible = base.filter(a => C.matches(a,query,category));
    const isHome = route === 'inicio' && !query && category==='all';
    const count = `${visible.length} ${t(visible.length===1?'result':'results')}${query?' '+t('resultFor')+' «'+e(query)+'»':''}`;
    let html = `<p class="results-count" role="status">${count}</p>`;
    if (!visible.length) {
      const empty = route === 'guardados' && !base.length;
      html += `<div class="empty-state">${icon(empty?'bookmark':'search')}<h2>${t(empty?'emptySaved':'noResults')}</h2><p>${t(empty?'emptySavedText':'noResultsText')}</p>${empty?`<a class="primary-button" href="#/explorar">${t('discover')}</a>`:`<button class="primary-button" type="button" data-action="clear">${t('clear')}</button>`}</div>`;
    } else if (isHome) {
      html += card(visible[0],true) + `<div class="section-heading"><h2>${t('more')}</h2><span>${String(visible.length-1).padStart(2,'0')} ${t('results')}</span></div><div class="story-grid">${visible.slice(1).map(a=>card(a)).join('')}</div>`;
    } else html += `<div class="story-grid result-grid">${visible.map(a=>card(a)).join('')}</div>`;
    $('#catalog-results').innerHTML = html;
    document.querySelectorAll('[data-category]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.category===category)));
    updateSaveButtons();
  }
  function updateSaveButtons() {
    document.querySelectorAll('[data-action="save"]').forEach(button=>{
      const saved=state.saved.includes(button.dataset.id),a=article(DATA.find(a=>a.id===button.dataset.id));
      button.setAttribute('aria-pressed',String(saved));button.setAttribute('aria-label',(saved?t('remove'):t('save'))+': '+a.title);
      button.classList.toggle('is-saved',saved);button.querySelector('span').textContent=t(saved?'savedState':'save');
      button.querySelector('svg').outerHTML=icon(saved?'check':'bookmark');
    });
    document.querySelectorAll('[data-saved-count]').forEach(el=>{el.textContent=state.saved.length;el.hidden=!state.saved.length;});
  }
  function showToast(message, canUndo = false) {
    $('#toast').innerHTML = `<span>${e(message)}</span>${canUndo?`<button type="button" data-action="undo">${t('undo')}</button>`:''}<button type="button" class="toast-close" aria-label="${t('close')}" data-action="close-toast">×</button>`;
    $('#toast').hidden = false;
  }
  function save(id) {
    const index = state.saved.indexOf(id);
    if (index<0) { state.saved.push(id); undo=null; showToast(t('savedToast')); }
    else { state.saved.splice(index,1);undo={id,index};showToast(t('removedToast'),true); }
    persist();
    if (route === 'guardados') {
      renderResults();
      $('#toast [data-action="undo"]')?.focus({preventScroll:true});
    } else {
      updateSaveButtons();
    }
  }
  function articleView(id) {
    const raw = DATA.find(a=>a.id===id);
    if (!raw) { notFound();return; }
    const a=article(raw);
    document.title=a.title+' · Pausa';
    $('#reading-progress').hidden=false;
    $('#app').innerHTML=`<div class="page-shell article-shell"><a class="back-link" href="#/explorar">${t('back')}</a><article class="full-article" aria-labelledby="article-title" lang="${state.language}"><header class="article-heading">${tag(a)}<h1 id="article-title">${e(a.title)}</h1><p class="article-deck">${e(a.excerpt)}</p><div class="article-byline"><div><strong>${e(a.author)}</strong><span>${date(a.date)} <span aria-hidden="true">·</span> ${C.readingMinutes(C.bodyText(a))} ${t('minute')}</span></div><div class="article-top-actions">${saveButton(a)}<a class="text-link" href="#comments" data-jump="comments">${t('comments')}</a></div></div></header><figure class="article-image"><img src="../images/${a.image}" alt="${e(a.alt[state.language])}" width="1400" height="850"><figcaption>${t(id==='ciudad'?'imageCredit':'photoCredit')}</figcaption></figure><div class="article-layout"><div class="reading-column"><div id="article-body" class="article-body">${a.sections.map((s,i)=>`<section id="section-${i}" aria-labelledby="section-heading-${i}"><h2 id="section-heading-${i}">${e(s.title)}</h2>${s.paragraphs.map(p=>`<p>${e(p)}</p>`).join('')}</section>`).join('')}</div><p class="reading-end">${icon('book')}${t('end')}</p><div class="article-bottom-actions">${saveButton(a)}<span>${C.wordCount(C.bodyText(a))} ${t('words')} · 200 ${state.language==='es'?'palabras/min':'words/min'}</span></div>${commentForm(id)}</div><aside class="reading-sidebar" aria-label="${t('readingPrefs')}"><div class="reader-tools"><p class="eyebrow">${t('readingNow')}</p><h2>${t('readingPrefs')}</h2><div id="sidebar-options">${options('sidebar')}</div></div><nav class="article-toc" aria-labelledby="article-toc-title"><h2 id="article-toc-title">${t('onThisPage')}</h2>${a.sections.map((s,i)=>`<a href="#section-${i}" data-jump="section-${i}">${e(s.title)}</a>`).join('')}<a href="#comments" data-jump="comments">${t('comments')}</a></nav></aside></div></article><section class="related-stories" aria-labelledby="related-title"><div class="section-heading"><h2 id="related-title">${t('related')}</h2></div><div class="story-grid">${articles().filter(x=>x.id!==id).slice(0,3).map(a=>card(a)).join('')}</div></section></div>`;
    const byline=$('.article-byline>div:first-child>span');
    byline.innerHTML=`${date(a.date)} <span aria-hidden="true">·</span> <span data-reading-time></span>`;
    $('.article-bottom-actions>span').setAttribute('data-word-count','');
    recalculateReading();
    articleObserver=new MutationObserver(()=>{recalculateReading();updateProgress();});
    articleObserver.observe($('#article-body'),{subtree:true,childList:true,characterData:true});
    renderComments(id);updateSaveButtons();updateProgress();
  }
  function recalculateReading(){
    const body=$('#article-body');if(!body)return;
    const nodes=Array.from(body.querySelectorAll('h2,p'));
    const text=nodes.length?nodes.map(n=>n.textContent).join(' '):body.textContent;
    $('[data-reading-time]').textContent=C.readingMinutes(text)+' '+t('minute');
    $('[data-word-count]').textContent=C.wordCount(text)+' '+t('words')+' · 200 '+(state.language==='es'?'palabras/min':'words/min');
  }
  function commentForm(id) {
    return `<section id="comments" class="comments-section" aria-labelledby="comments-title"><p class="eyebrow">PAUSA · ${t('comments')}</p><h2 id="comments-title">${t('commentIntro')}</h2><p class="local-comments">${t('localComments')}</p><div id="comments-list"></div><form id="comment-form" data-id="${id}" novalidate><div class="form-field"><label for="comment-alias">${t('alias')}</label><p id="alias-hint" class="field-hint">${t('aliasHint')}</p><input id="comment-alias" name="alias" type="text" minlength="2" maxlength="40" required autocomplete="nickname" aria-describedby="alias-hint alias-error"><p class="field-error" id="alias-error" hidden></p></div><div class="form-field"><label for="comment-message">${t('message')}</label><p id="message-hint" class="field-hint">${t('commentHint')}</p><textarea id="comment-message" name="message" rows="5" maxlength="500" required aria-describedby="message-hint message-error comment-counter"></textarea><div class="message-meta"><p class="field-error" id="message-error" hidden></p><span id="comment-counter">0 / 500</span></div></div><p id="comment-status" role="status"></p><button class="primary-button" type="submit">${t('publish')}</button></form></section>`;
  }
  function renderComments(id) {
    const list = state.comments[id] || [];
    $('#comments-list').innerHTML=list.length?list.slice().reverse().map(c=>`<article class="comment"><div class="comment-avatar" aria-hidden="true">${e(Array.from(c.alias)[0].toUpperCase())}</div><div><h3>${e(c.alias)}</h3><time datetime="${e(c.date)}">${date(c.date)}</time><p>${e(c.message)}</p></div></article>`).join(''):`<p class="muted no-comments">${t('noComments')}</p>`;
  }
  function submitComment(form) {
    const alias=$('#comment-alias'),message=$('#comment-message'),errors=C.validateComment(alias.value,message.value);
    for (const [key,failed] of Object.entries(errors)) {
      const input=key==='alias'?alias:message, error=$('#'+key+'-error');
      input.setAttribute('aria-invalid',String(failed));error.hidden=!failed;error.textContent=failed?t(key==='alias'?'aliasError':'messageError'):'';
    }
    if(errors.alias||errors.message){(errors.alias?alias:message).focus();return;}
    const id=form.dataset.id;
    if(!state.comments[id]) state.comments[id]=[];
    state.comments[id].push({alias:alias.value.trim(),message:message.value.trim(),date:new Date().toISOString()});
    // Keep local history bounded, consistently with the state loader.
    state.comments[id]=state.comments[id].slice(-100);
    persist();renderComments(id);message.value='';$('#comment-counter').textContent='0 / 500';$('#comment-status').textContent=t('commentSuccess');message.focus();
  }
  function indexView() {
    $('#app').innerHTML=`<div class="page-shell"><section class="welcome welcome-small"><p class="eyebrow">PAUSA · ${t('edition')}</p><h1 id="page-title">${t('categoryIndex')}</h1><p class="welcome-intro">${t('indexIntro')}</p></section><div class="index-page">${categories.slice(1).map(c=>{const group=articles().filter(a=>a.category===c);return `<section class="index-category" aria-labelledby="index-${c}"><h2 id="index-${c}">${t(c)}<span>${group.length}</span></h2><ul>${group.map(a=>`<li><a href="${href(a.id)}"><img src="../images/${a.image}" alt="" width="160" height="120" loading="lazy"><div><h3>${e(a.title)}</h3><p>${e(a.excerpt)}</p><span>${e(a.author)} · ${C.readingMinutes(C.bodyText(a))} ${t('minute')}</span></div></a>${saveButton(a,true)}</li>`).join('')}</ul></section>`;}).join('')}</div></div>`;
  }
  function helpView() {
    $('#app').innerHTML=`<div class="page-shell help-page"><section class="welcome welcome-small"><p class="eyebrow">PAUSA · ${t('help')}</p><h1 id="page-title">${t('helpTitle')}</h1><p class="welcome-intro">${t('helpIntro')}</p></section><div class="help-sections">${['Read','Search','Keyboard','Privacy','About','Photos'].map(s=>`<section><h2>${t('help'+s)}</h2><p>${t('help'+s+'Text')}</p></section>`).join('')}</div><a class="primary-button" href="#/inicio">${t('home')}</a></div>`;
  }
  function notFound(){ $('#app').innerHTML=`<div class="page-shell empty-state not-found"><h1 id="page-title">${t('notFound')}</h1><p>${t('notFoundText')}</p><a class="primary-button" href="#/indice">${t('viewIndex')}</a></div>`; }
  function render(focus = false) {
    articleObserver?.disconnect();articleObserver=null;
    const fragment=location.hash.slice(1)||'/inicio';
    const [path, search='']=fragment.split('?'), parts=path.split('/').filter(Boolean);
    route=parts[0]||'inicio';currentId=parts[1]||null;
    const params=new URLSearchParams(search);query=(params.get('q')||'').slice(0,120);category=categories.includes(params.get('tag'))?params.get('tag'):'all';
    $('#reading-progress').hidden=true;document.title='Pausa · '+(state.language==='es'?'Una revista para leer a tu ritmo':'A magazine to read at your own pace');
    if(['inicio','explorar','guardados'].includes(route))catalog();
    else if(route==='articulo')articleView(currentId);
    else if(route==='indice')indexView();
    else if(route==='ayuda')helpView();
    else notFound();
    document.querySelectorAll('[data-route]').forEach(el=>{if(el.dataset.route===route)el.setAttribute('aria-current','page');else el.removeAttribute('aria-current');});
    updateSaveButtons();closeMenu();
    if(focus){$('#main').focus({preventScroll:true});window.scrollTo({top:0,behavior:'instant'});}
  }
  function syncFilters() {
    const params=new URLSearchParams();if(query)params.set('q',query);if(category!=='all')params.set('tag',category);
    const hash='#/'+route+(params.size?'?'+params.toString():'');
    // file:// browsers can reject history writes; filtering still works there.
    try{history.replaceState(null,'',hash);}catch{/* Memory-only URL state. */}
    renderResults();
  }
  function updateProgress() {
    const body=$('#article-body');if(!body)return;
    const box=body.getBoundingClientRect();
    // The reader's viewport starts below the sticky site header.
    const offset=$('.site-header').getBoundingClientRect().height;
    const value=C.progress(box.top-offset,box.bottom-offset,window.innerHeight-offset);
    $('#reading-progress').style.setProperty('--progress',value+'%');$('#reading-progress').setAttribute('aria-valuenow',String(value));
  }
  function closeMenu(){ $('#mobile-menu').hidden=true;$('[data-action="menu"]').setAttribute('aria-expanded','false');$('[data-action="menu"]').setAttribute('aria-label',t('openMenu')); }
  function setPreference(key,value) {
    state[key]=value;persist();applyPreferences();
    if($('#sidebar-options'))$('#sidebar-options').innerHTML=options('sidebar');
    // Replaced controls should retain keyboard focus in their original group.
    updateProgress();
  }
  document.addEventListener('click',event=>{
    if(event.target.closest('.skip-link')){event.preventDefault();$('#main').focus();return;}
    const jump=event.target.closest('[data-jump]');
    if(jump){event.preventDefault();const target=$('#'+jump.dataset.jump);target.scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});target.setAttribute('tabindex','-1');target.focus({preventScroll:true});return;}
    const cat=event.target.closest('[data-category]');if(cat){category=cat.dataset.category;syncFilters();return;}
    const tagLink=event.target.closest('[data-category-link]');if(tagLink){location.hash='/explorar?tag='+tagLink.dataset.categoryLink;return;}
    const pref=event.target.closest('[data-preference]');if(pref){const context=pref.closest('#dialog-options')?'#dialog-options':'#sidebar-options';const key=pref.dataset.preference,value=pref.dataset.value;setPreference(key,value);document.querySelector(`${context} [data-preference="${key}"][data-value="${value}"]`)?.focus({preventScroll:true});return;}
    const button=event.target.closest('[data-action]');if(!button)return;
    switch(button.dataset.action){
      case 'save':save(button.dataset.id);break;
      case 'undo': {
        if (!undo) break;
        const {id, index} = undo;
        state.saved = state.saved.filter(savedId => savedId !== id);
        state.saved.splice(index, 0, id);
        undo = null;
        persist();
        if (route === 'guardados') {
          renderResults();
          const restoredButton = $(`#catalog-results [data-action="save"][data-id="${id}"]`);
          const focusTarget = restoredButton ?? $('#search-input');
          // Leave room for the fixed confirmation on short screens.
          focusTarget.scrollIntoView({block:'center'});
          focusTarget.focus({preventScroll:true});
        } else {
          updateSaveButtons();
        }
        showToast(t('restored'));
        break;
      }
      case 'close-toast': {
        const toast = $('#toast');
        const returnFocus = route === 'guardados' && toast.contains(document.activeElement);
        toast.hidden = true;
        if (returnFocus) $('#search-input').focus();
        break;
      }
      case 'clear':query='';category='all';$('#search-input').value='';syncFilters();$('#search-input').focus();break;
      case 'reading':lastDialogTrigger=button;$('#reading-dialog').showModal();break;
      case 'close-reading':$('#reading-dialog').close();break;
      case 'menu':{const open=$('#mobile-menu').hidden;$('#mobile-menu').hidden=!open;button.setAttribute('aria-expanded',String(open));button.setAttribute('aria-label',t(open?'closeMenu':'openMenu'));break;}
      case 'reset':{const context=button.closest('#dialog-options')?'#dialog-options':'#sidebar-options';state.theme='light';state.font='medium';persist();applyPreferences();if($('#sidebar-options'))$('#sidebar-options').innerHTML=options('sidebar');document.querySelector(context+' [data-action="reset"]')?.focus();updateProgress();break;}
    }
  });
  document.addEventListener('submit',event=>{
    if(event.target.id==='search-form'){event.preventDefault();query=$('#search-input').value.trim();syncFilters();}
    if(event.target.id==='comment-form'){event.preventDefault();submitComment(event.target);}
  });
  document.addEventListener('input',event=>{
    if(event.target.id==='search-input'){query=event.target.value.trim();syncFilters();}
    if(event.target.id==='comment-message')$('#comment-counter').textContent=event.target.value.length+' / 500';
  });
  $('#language').addEventListener('change',event=>{state.language=event.target.value;persist();applyPreferences();render();});
  $('#reading-dialog').addEventListener('close',()=>lastDialogTrigger?.focus());
  document.addEventListener('keydown',event=>{
    if(event.key==='Escape'){if(!$('#mobile-menu').hidden){closeMenu();$('[data-action="menu"]').focus();}}
    if(event.key==='/'&&!event.ctrlKey&&!event.metaKey&&!event.altKey&&!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)&&!$('#reading-dialog').open){if($('#search-input')){event.preventDefault();$('#search-input').focus();}}
  });
  window.addEventListener('hashchange',()=>render(true));
  window.addEventListener('scroll',()=>{if(!progressFrame)progressFrame=requestAnimationFrame(()=>{progressFrame=0;updateProgress();});},{passive:true});
  window.addEventListener('resize',updateProgress);
  window.addEventListener('storage',event=>{if(event.key!==KEY)return;try{state=C.sanitizeState(JSON.parse(event.newValue),DATA.map(a=>a.id));applyPreferences();render();}catch{/* Keep current state if another tab writes invalid JSON. */}});
  applyPreferences();render();
})();
