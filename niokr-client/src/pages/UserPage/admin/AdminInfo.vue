<script setup lang="ts">
  import AppList from '@/components/ui/AppList/AppList.vue';
  import { AdminType } from '@/models/User';

  const props = defineProps<{
    userInfo: AdminType;
  }>();

  const infoItems = [
    {
      title: 'E-Mail',
      content: `${props.userInfo.email}`,
    },
    {
      title: 'Телефон',
      content: `${props.userInfo.phone}`,
    },
  ];
</script>

<template>
  <section class="section">
    <h1>Контактная информация</h1>
    <AppList class="app-list" :width="10" :items="infoItems" />
  </section>
</template>

<style lang="scss" scoped>
  .section {
    margin-bottom: 1.625rem;
    h1 {
      font-size: 1.125rem;
      font-weight: bold;
      margin-bottom: 1.0625rem;
    }
    &:last-child {
      margin-bottom: 0;
    }
  }
  .app-list {
    &:deep(h1) {
      color: var(--dark-gray-color);
    }
  }
</style>
