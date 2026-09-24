import type {APIRoute} from 'astro';import {handle} from '../../lib/api';
export const prerender=false;
export const POST:APIRoute=context=>handle('book',context);
