import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {HtmlValidate} from 'html-validate';
import axe from 'axe-core';
import {open,navigate,input} from './helpers.mjs';

test('home includes the original logo, six stories and automatically generated index',t=>{
  const c=open();t.after(c.close);
  assert.equal(c.d.querySelector('.brand img').getAttribute('src'),'../images/pausa-logo.png');
  assert.equal(c.d.querySelectorAll('[data-story]').length,6);assert.equal(c.d.querySelectorAll('.edition-index li').length,6);
  for(const img of c.d.querySelectorAll('img'))assert(existsSync(new URL('../src/'+img.getAttribute('src'),import.meta.url)));
});
test('Laura: query, category, article, save, revisit, reload, remove and undo',async t=>{
  const c=open();t.after(c.close);input(c,'#search-input','ciudad');
  c.d.querySelector('[data-category="sociedad"]').click();
  assert.equal(c.d.querySelectorAll('[data-story]').length,1);assert(c.d.querySelector('mark'));
  await navigate(c,'#/articulo/ciudad');c.d.querySelector('[data-action="save"]').click();
  assert.equal(c.d.querySelector('[data-action="save"]').getAttribute('aria-pressed'),'true');
  await navigate(c,'#/guardados');assert.equal(c.d.querySelectorAll('[data-story]').length,1);
  const reload=open({hash:'#/guardados',savedState:JSON.parse(c.w.localStorage.getItem('pausa:v1'))});t.after(reload.close);
  assert.equal(reload.d.querySelectorAll('[data-story]').length,1);
  c.d.querySelector('[data-action="save"]').click();assert(c.d.querySelector('.empty-state'));
  c.d.querySelector('[data-action="undo"]').click();assert.equal(c.d.querySelectorAll('[data-story]').length,1);
});
test('saved stories focus Undo on removal and return focus to the restored story',t=>{
  const saved = ['lluvia','ciudad','museo'];
  const c = open({hash:'#/guardados',savedState:{saved}});
  t.after(c.close);
  const saveSelector = '[data-action="save"][data-id="ciudad"]';
  const remove = c.d.querySelector(saveSelector);
  remove.focus();
  remove.click();
  const undo = c.d.querySelector('[data-action="undo"]');
  assert.equal(c.d.activeElement,undo);
  assert.equal(c.d.querySelector(saveSelector),null);

  undo.click();
  const restored = c.d.querySelector(saveSelector);
  assert.equal(c.d.activeElement,restored);
  assert.equal(restored.getAttribute('aria-pressed'),'true');
  assert.deepEqual([...c.d.querySelectorAll('[data-story]')].map(card=>card.dataset.story),saved);
  assert.deepEqual(JSON.parse(c.w.localStorage.getItem('pausa:v1')).saved,saved);
});
test('undo returns focus to search when a filter hides the restored story',t=>{
  const c = open({hash:'#/guardados',savedState:{saved:['ciudad','museo']}});
  t.after(c.close);
  c.d.querySelector('[data-action="save"][data-id="ciudad"]').click();
  c.d.querySelector('[data-category="cultura"]').click();
  c.d.querySelector('[data-action="undo"]').click();

  assert.equal(c.d.activeElement,c.d.querySelector('#search-input'));
  assert.equal(c.d.querySelector('[data-category="cultura"]').getAttribute('aria-pressed'),'true');
  assert.equal(c.d.querySelector('[data-story="ciudad"]'),null);
  c.d.querySelector('[data-category="all"]').click();
  assert(c.d.querySelector('[data-story="ciudad"]'));
});
test('dismissing Undo returns focus to search without restoring the story',t=>{
  const c = open({hash:'#/guardados',savedState:{saved:['ciudad']}});
  t.after(c.close);
  c.d.querySelector('[data-action="save"]').click();
  const close = c.d.querySelector('#toast [data-action="close-toast"]');
  close.focus();
  close.click();

  assert.equal(c.d.activeElement,c.d.querySelector('#search-input'));
  assert(c.d.querySelector('#toast').hidden);
  assert.equal(c.d.querySelector('[data-story]'),null);
});
test('query remains visible on no results, can be cleared and survives a deep link',t=>{
  const c=open({hash:'#/explorar?q=inexistente&tag=ciencia'});t.after(c.close);
  assert.equal(c.d.querySelector('#search-input').value,'inexistente');assert(c.d.querySelector('.empty-state'));
  c.d.querySelector('[data-action="clear"]').click();assert.equal(c.d.querySelectorAll('[data-story]').length,6);
});
test('search handles accented text and HTML-like input without creating elements',t=>{
  const c=open();t.after(c.close);input(c,'#search-input','cafe');assert.equal(c.d.querySelectorAll('[data-story]').length,1);
  input(c,'#search-input','<img src=x onerror=alert(1)>');assert.equal(c.d.querySelectorAll('[onerror]').length,0);assert(c.d.querySelector('.empty-state'));
});
test('Siobhán: English article, sepia, large text, preferences survive reload',async t=>{
  const c=open();t.after(c.close);const select=c.d.querySelector('#language');select.value='en';select.dispatchEvent(new c.w.Event('change',{bubbles:true}));
  await navigate(c,'#/articulo/ciudad');assert.match(c.d.querySelector('h1').textContent,/city can be read/);assert.equal(c.d.documentElement.lang,'en');
  c.d.querySelector('#sidebar-options [data-value="sepia"]').click();c.d.querySelector('#sidebar-options [data-value="large"]').click();
  assert.equal(c.d.documentElement.dataset.theme,'sepia');assert.equal(c.d.documentElement.dataset.font,'large');assert.equal(c.d.querySelector('#sidebar-options [data-value="large"]').getAttribute('aria-pressed'),'true');
  const reload=open({savedState:JSON.parse(c.w.localStorage.getItem('pausa:v1'))});t.after(reload.close);assert.equal(reload.d.documentElement.dataset.theme,'sepia');assert.equal(reload.d.documentElement.lang,'en');
});
test('comments preserve invalid drafts, validate, count characters and persist safely',t=>{
  const c=open({hash:'#/articulo/ciudad'});t.after(c.close);input(c,'#comment-alias','Siobhán');
  c.d.querySelector('#comment-form').dispatchEvent(new c.w.Event('submit',{bubbles:true,cancelable:true}));
  assert.equal(c.d.querySelector('#comment-alias').value,'Siobhán');assert.equal(c.d.querySelector('#comment-message').getAttribute('aria-invalid'),'true');
  input(c,'#comment-message','<img src=x onerror="alert(1)"> Una lectura tranquila.');assert.match(c.d.querySelector('#comment-counter').textContent,/500/);
  c.d.querySelector('#comment-form').dispatchEvent(new c.w.Event('submit',{bubbles:true,cancelable:true}));
  assert.equal(c.d.querySelectorAll('.comment').length,1);assert.equal(c.d.querySelectorAll('.comment img').length,0);assert.match(c.d.querySelector('.comment p').textContent,/<img/);
  assert.equal(c.d.querySelector('#comment-message').value,'');assert.equal(JSON.parse(c.w.localStorage.getItem('pausa:v1')).comments.ciudad.length,1);
});
test('blocked storage remains usable and explains session-only persistence',t=>{
  const c=open({blocked:true});t.after(c.close);assert.equal(c.d.querySelector('#storage-warning').hidden,false);
  c.d.querySelector('[data-action="save"]').click();assert.equal(c.d.querySelector('[data-action="save"]').getAttribute('aria-pressed'),'true');
});
test('reading time uses current language body at 200 wpm',t=>{
  const c=open({hash:'#/articulo/ciudad'});t.after(c.close);
  const expected=c.w.PausaCore.readingMinutes(c.d.querySelector('#article-body').textContent);
  assert.match(c.d.querySelector('.article-byline').textContent,new RegExp(expected+' min'));
});
test('reading time recalculates when the body changes; controls and comments are excluded',async t=>{
  const c=open({hash:'#/articulo/ciudad'});t.after(c.close);
  c.d.querySelector('#article-body').textContent='palabra '.repeat(401);
  await new Promise(resolve=>c.w.setTimeout(resolve,0));
  assert.equal(c.d.querySelector('[data-reading-time]').textContent,'3 min de lectura');
  assert.match(c.d.querySelector('[data-word-count]').textContent,/401 palabras/);
});
test('body-only search displays a matching excerpt, not an unhighlighted card',t=>{
  const c=open();t.after(c.close);input(c,'#search-input','marquesina');
  assert.equal(c.d.querySelectorAll('[data-story]').length,1);assert.equal(c.d.querySelector('.story-copy p mark').textContent.toLowerCase(),'marquesina');
});
test('progress is complete at the end of body before comments',t=>{
  const c=open({hash:'#/articulo/ciudad'});t.after(c.close);
  c.d.querySelector('#article-body').getBoundingClientRect=()=>({top:-2000,bottom:600});c.w.dispatchEvent(new c.w.Event('resize'));
  assert.equal(c.d.querySelector('#reading-progress').getAttribute('aria-valuenow'),'100');
});
test('skip link and section anchors preserve article routing and keyboard focus',t=>{
  const c=open({hash:'#/articulo/ciudad'});t.after(c.close);
  c.d.querySelector('.skip-link').click();assert.equal(c.d.activeElement.id,'main');assert.equal(c.w.location.hash,'#/articulo/ciudad');
  c.d.querySelector('[data-jump="section-1"]').click();assert.equal(c.d.activeElement.id,'section-1');assert.equal(c.w.location.hash,'#/articulo/ciudad');
});
test('mobile menu and reading dialog expose accurate open state; reset restores defaults',t=>{
  const c=open();t.after(c.close);c.d.querySelector('[data-action="menu"]').click();assert.equal(c.d.querySelector('#mobile-menu').hidden,false);
  c.d.dispatchEvent(new c.w.KeyboardEvent('keydown',{key:'Escape',bubbles:true}));assert.equal(c.d.querySelector('#mobile-menu').hidden,true);
  c.d.querySelector('[data-action="reading"]').click();assert(c.d.querySelector('#reading-dialog').open);
  c.d.querySelector('#dialog-options [data-value="dark"]').click();assert.equal(c.d.documentElement.dataset.theme,'dark');
  c.d.querySelector('#dialog-options [data-action="reset"]').click();assert.equal(c.d.documentElement.dataset.theme,'light');
  c.d.querySelector('[data-action="close-reading"]').click();assert(!c.d.querySelector('#reading-dialog').open);
});
test('unknown article displays a recovery link instead of an empty screen',t=>{
  const c=open({hash:'#/articulo/no-existe'});t.after(c.close);assert(c.d.querySelector('.not-found a'));assert(c.d.querySelector('#reading-progress').hidden);
});
test('HTML validity and accessible semantics across generated views',async t=>{
  // DOM serialization writes hidden="" and defer=""; both are valid HTML.
  const validator=new HtmlValidate({extends:['html-validate:recommended'],rules:{'no-inline-style':'off','prefer-native-element':'off','attribute-boolean-style':'off','attribute-empty-style':'off'}});
  const views=['#/inicio','#/explorar?q=ciudad','#/guardados','#/indice','#/articulo/ciudad','#/ayuda'].map(hash=>({hash}));
  views.push({hash:'#/inicio',savedState:{language:'en',theme:'dark'}},{hash:'#/articulo/ciudad',savedState:{language:'en',theme:'sepia'}});
  for(const view of views){
    const {hash}=view;const c=open(view);t.after(c.close);
    const report=await validator.validateString(c.dom.serialize());
    assert.equal(report.valid,true,hash+' HTML: '+JSON.stringify(report.results.flatMap(r=>r.messages.map(m=>m.message))));
    c.w.eval(axe.source);
    const results=await c.w.axe.run(c.d,{rules:{'color-contrast':{enabled:false}}});
    assert.equal(results.violations.length,0,hash+' axe: '+JSON.stringify(results.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)}))));
  }
});
