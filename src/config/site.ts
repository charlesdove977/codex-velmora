export const site = {
 name:'Velmora Aesthetics', shortName:'Velmora', tagline:'Medical precision. Hotel calm.',
 url:'https://velmora.example', email:'hello@velmora.example', phone:'(480) 555-0148', phoneHref:'tel:+14805550148',
 address:{street:'7100 East Main Street',city:'Scottsdale',region:'AZ',postalCode:'85251',country:'US'},
 geo:{latitude:33.4935,longitude:-111.927}, timezone:'America/Phoenix', timezoneLabel:'Arizona', regionName:'Arizona', utcOffset:'-07:00',
 hours:[{day:'Sunday',open:null,close:null},{day:'Monday',open:9,close:18},{day:'Tuesday',open:9,close:18},{day:'Wednesday',open:9,close:18},{day:'Thursday',open:9,close:18},{day:'Friday',open:9,close:17},{day:'Saturday',open:10,close:15}],
 socials:[{name:'Instagram',url:'https://www.instagram.com/'}],
 colors:{bone:'#F5F0E8',sand:'#E7DDCF',stone:'#BFB3A3',ink:'#221B17',gold:'#B8946A',sage:'#8E9A86',muted:'#65594F',goldText:'#80603C',white:'#FFFDF9',error:'#9B332B'},
 demo:true, demoNotice:'A concept practice. Providers, prices and appointments are for demonstration.',
 consultation:{virtual:0,inPerson:50,duration:20},
};
export const addressLine = `${site.address.street}, ${site.address.city}, ${site.address.region} ${site.address.postalCode}`;
export const brandStyle = Object.entries(site.colors).map(([k,v])=>`--${k.replace(/[A-Z]/g,m=>'-'+m.toLowerCase())}:${v}`).join(';');
