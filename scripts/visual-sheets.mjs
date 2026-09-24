import sharp from 'sharp';import fs from 'node:fs';
fs.mkdirSync('verification/review',{recursive:true});
const files=fs.readdirSync('verification/pages').filter(x=>x.endsWith('.png')).sort();
for(let start=0;start<files.length;start+=5){const batch=files.slice(start,start+5);const layers=[];let maxHeight=0;
 for(let i=0;i<batch.length;i++){const buf=await sharp('verification/pages/'+batch[i]).resize({width:360,height:2600,fit:'inside'}).toBuffer();const m=await sharp(buf).metadata();maxHeight=Math.max(maxHeight,m.height+45);layers.push({input:buf,left:i*380+10,top:45});layers.push({input:Buffer.from(`<svg width="380" height="40"><rect width="380" height="40" fill="white"/><text x="5" y="24" font-size="12">${batch[i]}</text></svg>`),left:i*380,top:0});}
 await sharp({create:{width:batch.length*380,height:maxHeight,channels:3,background:'#d4d4d4'}}).composite(layers).jpeg({quality:85}).toFile(`verification/review/sheet-${String(start/5+1).padStart(2,'0')}.jpg`);
}console.log(files.length+' screenshots assembled');
