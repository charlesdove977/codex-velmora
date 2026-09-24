async page=>{
const out=[];
await page.emulateMedia({reducedMotion:'reduce'});
for(const width of [1440,390]){
 await page.setViewportSize({width,height:900});await page.goto('http://127.0.0.1:4322/book');await page.evaluate(()=>sessionStorage.clear());await page.goto('http://127.0.0.1:4322/book?treatment=hydrafacial&provider=maya-chen');await page.waitForTimeout(350);
 if(!await page.getByLabel('HydraFacial',{exact:true}).isChecked())throw Error('Treatment prefill failed');
 await page.getByRole('button',{name:'Continue'}).click();await page.getByRole('button',{name:'Continue'}).click();if(!await page.getByText('Choose an open date within').isVisible())throw Error('Missing date validation');
 await page.locator('#book-date').selectOption({index:2});await page.locator('#book-time').selectOption({index:1});await page.reload();await page.waitForTimeout(350);if(!await page.locator('#book-date').inputValue())throw Error('State lost on refresh');
 await page.getByRole('button',{name:'Continue'}).click();await page.getByRole('button',{name:'Continue'}).click();if(!await page.getByText('Enter your full name.').isVisible())throw Error('Missing detail validation');
 await page.getByLabel('Full name',{exact:true}).fill('Demo Test');await page.getByLabel('Email address',{exact:true}).first().fill('demo@example.com');await page.getByLabel('Phone number',{exact:true}).fill('4805550100');await page.getByLabel('I am 18 or older').check();await page.getByRole('button',{name:'Continue'}).click();
 await page.screenshot({path:`/Users/user/Desktop/Development-Charlie-2/Charlieautomates/websites/Codex-Velmora/verification/booking-review-${width}.png`,fullPage:true});
 await page.getByRole('button',{name:'Confirm consultation request'}).click();await page.waitForURL('**/book/confirmed');await page.locator('[data-reference]').waitFor();const ref=await page.locator('[data-reference]').innerText();
 const downloadPromise=page.waitForEvent('download');await page.getByRole('button',{name:'Download tentative calendar'}).click();const download=await downloadPromise;await download.saveAs(`/Users/user/Desktop/Development-Charlie-2/Charlieautomates/websites/Codex-Velmora/verification/booking-${width}.ics`);
 await page.screenshot({path:`/Users/user/Desktop/Development-Charlie-2/Charlieautomates/websites/Codex-Velmora/verification/booking-confirmed-${width}.png`,fullPage:true});out.push({width,ref,download:download.suggestedFilename(),passed:true});
}
return out;
}
