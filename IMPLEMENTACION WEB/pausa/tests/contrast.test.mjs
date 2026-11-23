import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const css=readFileSync(new URL('../style/main.css',import.meta.url),'utf8');
function tokens(block){return Object.fromEntries(Array.from(block.matchAll(/--([a-z-]+):\s*(#[a-f\d]{6})/gi),m=>[m[1],m[2]]));}
function luminance(hex){const c=[1,3,5].map(i=>parseInt(hex.slice(i,i+2),16)/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4);return c[0]*.2126+c[1]*.7152+c[2]*.0722;}
test('primary text, muted text, labels, buttons and highlights meet 4.5:1 in all themes',()=>{
  const base=tokens(css.match(/:root\s*\{([^}]+)\}/)[1]);
  for(const theme of ['light','dark','sepia']){
    const overrides=theme==='light'?{}:tokens(css.match(new RegExp(':root\\[data-theme="'+theme+'"\\]\\s*\\{([^}]+)\\}'))[1]);
    const colors={...base,...overrides};
    for(const [fg,bg] of [['ink','paper'],['muted','paper'],['muted','surface'],['tag','paper'],['accent','paper'],['accent-text','accent'],['ink','mark'],['error','paper']]){
      const [a,b]=[luminance(colors[fg]),luminance(colors[bg])].sort((a,b)=>b-a),ratio=(a+.05)/(b+.05);
      assert(ratio>=4.5,`${theme}: ${fg}/${bg} = ${ratio.toFixed(2)}`);
    }
  }
});
