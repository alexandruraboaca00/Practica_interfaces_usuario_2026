import test from 'node:test';
import assert from 'node:assert/strict';
import {makeServer} from '../tools/serve.mjs';
test('static server serves HTML, assets and deep-link entry without a build',async t=>{
  const server=makeServer();await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));t.after(()=>server.close());
  const base='http://127.0.0.1:'+server.address().port;
  for(const p of ['/','/src/','/style/main.css','/script/app.js','/images/pausa-logo.png','/images/ciudad.png'])assert.equal((await fetch(base+p)).status,200,p);
  const missing=await fetch(base+'/src/absent');assert.equal(missing.status,404);
  const bad=await fetch(base+'/%2e%2e%2fpackage.json');assert.equal(bad.status,403);
});
