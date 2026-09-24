// Test-only Node preload. Never sends external requests.
import {appendFileSync} from 'node:fs';
globalThis.fetch=async(input,init={})=>{
 const url=String(input);if(!url.startsWith('https://api.resend.com/'))throw Error('Unexpected external request in email test');
 appendFileSync(process.env.MOCK_MAIL_LOG,JSON.stringify({url,body:JSON.parse(init.body||'{}')})+'\n');
 return new Response(JSON.stringify(process.env.MOCK_MAIL_FAILURE?{name:'validation_error',message:'Simulated failure'}:{id:'synthetic-test-id'}),{status:process.env.MOCK_MAIL_FAILURE?400:200,headers:{'Content-Type':'application/json'}});
};
