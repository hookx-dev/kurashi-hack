// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Thin, template-only articles kept online but excluded from indexing while
// they await a proper content rewrite (see CLAUDE.md / AdSense review notes).
const NOINDEX_SLUGS = [
  'kitchen-setup', 'storage-setup', 'desk-setup', 'bath-mat', 'bath-storage',
  'bed-storage', 'cable-box', 'cushion', 'footrest', 'gap-wagon',
  'hanger-rack', 'monitor-arm', 'stove-cover', 'trash-can', 'vacuum-stand',
];
const NOINDEX_PATHS = new Set(NOINDEX_SLUGS.map((slug) => `/article-${slug}/`));

// https://astro.build/config
export default defineConfig({
  site: 'https://kurashi-hack.pages.dev',
  integrations: [
    sitemap({
      filter: (page) => !NOINDEX_PATHS.has(new URL(page).pathname),
    }),
  ]
});
