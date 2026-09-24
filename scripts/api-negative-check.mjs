import {spawn} from 'node:child_process';
import {writeFileSync} from 'node:fs';
const results=[];
const routes=['book','contact','support','gift-card','newsletter'];
async function batch(name,run){
 const server=spawn(process.execPath,['dist/server/entry.mjs'],{env:{...process.env,HOST:'127.0.0.1',PORT:'4334',RESEND_API_KEY:''},stdio:'ignore'});
 try{let ready=false;for(let i=0;i<100;i++){try{await fetch('http://127.0.0.1:4334/');ready=true;break;}catch{await new Promise(r=>setTimeout(r,100));}}if(!ready)throw Error('Test server did not start');await run();}finally{server.kill();await new Promise(r=>server.once('exit',r));}
}
async function request(route,body,extra={}){return fetch('http://127.0.0.1:4334/api/'+route,{method:'POST',headers:{'content-type':'application/json',...extra},body:JSON.stringify(body)});}
await batch('invalid',async()=>{for(const route of routes){const r=await request(route,{});const body=await r.json();results.push({case:'invalid',route,status:r.status,passed:r.status===400&&!!body.errors});}});
await batch('honeypot',async()=>{for(const route of routes){const r=await request(route,{website:'bot.example',email:'demo@example.com'});results.push({case:'honeypot',route,status:r.status,passed:r.status===400});}});
await batch('rate',async()=>{for(let i=0;i<6;i++){const r=await request('newsletter',{});results.push({case:'rate-limit',attempt:i+1,status:r.status,passed:i<5?r.status===400:r.status===429&&Number(r.headers.get('retry-after'))>0});}});
await batch('boundaries',async()=>{for(const [name,body,headers,status]of [['origin',{}, {origin:'https://unrelated.example'},403],['media',{}, {'content-type':'text/plain'},403],['size',{message:'x'.repeat(17000)},{},413]]){const r=await request('contact',body,headers);results.push({case:name,status:r.status,passed:r.status===status});}});
writeFileSync('verification/api-negative.json',JSON.stringify(results,null,2));console.log(results);if(results.some(r=>!r.passed))process.exitCode=1;
