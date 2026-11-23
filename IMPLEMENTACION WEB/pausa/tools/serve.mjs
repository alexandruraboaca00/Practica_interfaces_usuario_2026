import {createServer} from 'node:http';
import {readFile,stat} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';

// No build step or runtime dependency is required. Paths also work on GitHub Pages.
export function makeServer(root = fileURLToPath(new URL('../',import.meta.url))) {
  root=path.resolve(root);
  const mime={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.png':'image/png','.jpg':'image/jpeg','.svg':'image/svg+xml','.json':'application/json; charset=utf-8','.txt':'text/plain; charset=utf-8'};
  return createServer(async(req,res)=>{
    try {
      const url=new URL(req.url,'http://localhost');
      let target=path.resolve(root,'.'+decodeURIComponent(url.pathname));
      if(target!==root&&!target.startsWith(root+path.sep)){res.writeHead(403);res.end('Forbidden');return;}
      if((await stat(target)).isDirectory())target=path.join(target,'index.html');
      const body=await readFile(target);res.writeHead(200,{'Content-Type':mime[path.extname(target)]||'application/octet-stream','X-Content-Type-Options':'nosniff'});res.end(body);
    }catch{res.writeHead(404,{'Content-Type':'text/plain; charset=utf-8'});res.end('Not found');}
  });
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
  const port=Number(process.env.PORT||3000),host=process.env.HOST||'127.0.0.1';
  makeServer().listen(port,host,()=>console.log(`Pausa: http://${host}:${port}/src/`));
}
