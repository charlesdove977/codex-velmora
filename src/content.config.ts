import {defineCollection} from 'astro:content';import {z} from 'astro/zod';import {glob} from 'astro/loaders';
const journal=defineCollection({loader:glob({pattern:'**/*.md',base:'./src/content/journal'}),schema:z.object({title:z.string(),description:z.string(),date:z.date(),category:z.string(),image:z.string(),author:z.string()})});export const collections={journal};
