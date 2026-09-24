async page=>{
const results=[];
for(const width of [1440,390]){
 await page.setViewportSize({width,height:900});await page.goto('http://127.0.0.1:4322/styleguide');
 for(let y=0;y<await page.evaluate(()=>document.body.scrollHeight);y+=750){await page.evaluate(y=>window.scrollTo(0,y),y);await page.waitForTimeout(120);}
 await page.evaluate(()=>window.scrollTo(0,0));await page.waitForTimeout(600);
 await page.screenshot({path:`/Users/user/Desktop/Development-Charlie-2/Charlieautomates/websites/Codex-Velmora/verification/styleguide-${width}.png`,fullPage:true});
 results.push({width,overflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),h1:await page.locator('h1').count()});
}
await page.emulateMedia({reducedMotion:'reduce'});await page.reload();await page.locator('[data-scene=hero]').scrollIntoViewIfNeeded();await page.waitForTimeout(1000);results.push({reducedMotionCanvas:await page.locator('canvas').count(),posterVisible:await page.locator('[data-scene=hero] .scene-poster').isVisible()});await page.screenshot({path:'/Users/user/Desktop/Development-Charlie-2/Charlieautomates/websites/Codex-Velmora/verification/reduced-motion.png'});return results;
}
