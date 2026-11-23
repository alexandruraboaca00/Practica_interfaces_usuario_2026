import test from 'node:test';
import assert from 'node:assert/strict';
import '../script/core.js';
import '../script/data.js';
const C=globalThis.PausaCore;
test('reading time: real body words, rounded up at 200 wpm',()=>{
  assert.equal(C.readingMinutes(''),0);assert.equal(C.readingMinutes('hola'),1);
  assert.equal(C.readingMinutes('hola '.repeat(200)),1);assert.equal(C.readingMinutes('hola '.repeat(201)),2);
  assert.equal(C.readingMinutes('hola '.repeat(1200)),6);assert.equal(C.wordCount('¿Qué tal? café, don’t, 2026.'),5);
});
test('literal accent-insensitive search and safe highlighting',()=>{
  assert.equal(C.highlight('Un café y otro CAFÉ','cafe'),'Un <mark>café</mark> y otro <mark>CAFÉ</mark>');
  assert.equal(C.highlight('<script>alert(1)</script>','alert'),'&lt;script&gt;<mark>alert</mark>(1)&lt;/script&gt;');
  assert.equal(C.highlight('Texto [raro].','[raro]'),'Texto <mark>[raro]</mark>.');
  assert.equal(C.highlight('a & b','&'),'a <mark>&amp;</mark> b');
});
test('query and category intersect and include full article bodies',()=>{
  const a={...globalThis.PausaData[0],...globalThis.PausaData[0].es};
  assert(C.matches(a,'MARQUESINA','sociedad'));assert(!C.matches(a,'marquesina','cultura'));assert(!C.matches(a,'<img','all'));
});
test('progress measures only article body and clamps both ends',()=>{
  assert.equal(C.progress(100,2100,800),0);assert.equal(C.progress(-600,1400,800),50);assert.equal(C.progress(-1200,800,800),100);assert.equal(C.progress(-2000,0,800),100);
  assert.equal(C.progress(30,400,800),0);assert.equal(C.progress(-20,400,800),100);
});
test('persisted data is validated, bounded and deduplicated',()=>{
  const s=C.sanitizeState({saved:['ciudad','unknown','ciudad'],theme:'invalid',font:'large',language:'en',comments:{ciudad:[{alias:'ab',message:'Hi',date:'wrong'},null]}},['ciudad']);
  assert.deepEqual(s.saved,['ciudad']);assert.equal(s.theme,'light');assert.equal(s.font,'large');assert.deepEqual(s.comments.ciudad,[]);
  assert.equal(C.sanitizeState(null,[]).language,'es');
});
test('comments reject whitespace and enforce both length limits',()=>{
  assert.deepEqual(C.validateComment('a',' '),{alias:true,message:true});assert.deepEqual(C.validateComment('Siobhán','Buen artículo'),{alias:false,message:false});
  assert(C.validateComment('x'.repeat(41),'a').alias);assert(C.validateComment('ab','x'.repeat(501)).message);
});
