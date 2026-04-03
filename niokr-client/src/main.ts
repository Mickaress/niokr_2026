import { VueQueryPlugin } from '@tanstack/vue-query';
import { createPinia } from 'pinia';
import { createApp } from 'vue';
import Vue3Toastify, { ToastContainerOptions } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import App from './App.vue';
import router from './router';
import { queryClient } from './api/queryClient';

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(VueQueryPlugin, {
  queryClient,
});
app.use(Vue3Toastify, {
  autoClose: 3000,
  clearOnUrlChange: false,
} as ToastContainerOptions);

app.mount('#app');
