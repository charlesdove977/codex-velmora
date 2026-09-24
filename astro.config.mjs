import { defineConfig } from 'astro/config';
import node from '@astrojs/node';
import react from '@astrojs/react';
import {site} from './src/config/site.ts';
import sitemap from '@astrojs/sitemap';
export default defineConfig({
  site: site.url,
  image: {service: {entrypoint: 'astro/assets/services/noop'}},
  adapter: node({mode: 'standalone'}),
  integrations: [react(), sitemap({filter: p => !p.includes('styleguide') && !p.includes('confirmed') && !p.endsWith('/404')})],
  vite: {
    resolve: {dedupe: ['react', 'react-dom']},
    build: {chunkSizeWarningLimit: 900},
  },
});
