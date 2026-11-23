import {readFileSync} from 'node:fs';
import {JSDOM} from 'jsdom';
const root=new URL('../',import.meta.url);
export function open({hash='#/inicio',savedState,blocked=false}={}) {
  const html=readFileSync(new URL('src/index.html',root),'utf8');
  const dom=new JSDOM(html,{url:'https://pausa.test/src/'+hash,runScripts:'outside-only',pretendToBeVisual:true});
  const w=dom.window;
  w.scrollTo=()=>{};
  w.matchMedia=()=>({matches:false});
  // JSDOM has no canvas/layout engine. Contrast is checked separately from axe.
  w.HTMLCanvasElement.prototype.getContext=()=>null;
  w.HTMLElement.prototype.scrollIntoView=function(){};
  w.HTMLDialogElement.prototype.showModal=function(){this.setAttribute('open','');};
  w.HTMLDialogElement.prototype.close=function(){this.removeAttribute('open');this.dispatchEvent(new w.Event('close'));};
  if(savedState)w.localStorage.setItem('pausa:v1',JSON.stringify(savedState));
  if(blocked)Object.defineProperty(w,'localStorage',{get(){throw new Error('Storage disabled');}});
  for(const file of ['data.js','core.js','app.js'])w.eval(readFileSync(new URL('script/'+file,root),'utf8'));
  return {dom,w,d:w.document,close:()=>w.close()};
}
export async function navigate(ctx,hash) {
  const ready=new Promise(resolve=>ctx.w.addEventListener('hashchange',resolve,{once:true}));
  ctx.w.location.hash=hash;await ready;
}
export function input(ctx,selector,value) {
  const el=ctx.d.querySelector(selector);el.value=value;el.dispatchEvent(new ctx.w.Event('input',{bubbles:true}));
}
