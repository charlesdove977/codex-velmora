import {site} from '../config/site';
export function GET(){return new Response(`User-agent: *
Allow: /
Disallow: /api/
Disallow: /book/confirmed
Disallow: /styleguide
Sitemap: ${site.url}/sitemap-index.xml
`,{headers:{'Content-Type':'text/plain; charset=utf-8'}});}
