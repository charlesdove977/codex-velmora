import {site,addressLine} from '../config/site';
export function GET(){return new Response(`# ${site.name}
> ${site.tagline}

Location: ${addressLine}.
${site.demo?site.demoNotice:''}

## Explore
- [Treatments](${site.url}/treatments): Educational guides, risks and starting prices.
- [Book a consultation](${site.url}/book): Request a time; await confirmation.
- [Pricing](${site.url}/pricing): Prices and consultation terms.
- [Membership](${site.url}/membership): Three care tiers.
- [Support](${site.url}/support): FAQs, aftercare and practice policies.
- [Journal](${site.url}/journal): General educational articles.
- [Medical disclaimer](${site.url}/medical-disclaimer): Clinical limitations and emergency guidance.

${site.demo?'All provider identities and testimonials are fictional. Images are licensed stock. Comparison sliders are interface demonstrations, not clinical evidence.':''}
Booking creates a request only. Consult a qualified clinician for personal medical advice.
`,{headers:{'Content-Type':'text/plain; charset=utf-8'}});}
