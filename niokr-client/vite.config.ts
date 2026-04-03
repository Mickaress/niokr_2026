import vueJsx from '@vitejs/plugin-vue-jsx';
import { fileURLToPath, URL } from 'node:url';

import vue from '@vitejs/plugin-vue';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [vue(), vueJsx()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      '@styles': fileURLToPath(new URL('./src/styles', import.meta.url)),
    },
  },
});

// https://vitejs.dev/config/
// export default ({ mode }) => {
//   const env = loadEnv(mode, process.cwd());

//   process.env = { ...process.env, ...env };

//   return defineConfig({
//     plugins: [vue(), vueJsx()],
//     resolve: {
//       alias: {
//         '@': fileURLToPath(new URL('./src', import.meta.url)),
//         '@styles': fileURLToPath(new URL('./src/styles', import.meta.url)),
//       },
//     },
//     base: process.env.VITE_BASE_URL,
//   });
// };
