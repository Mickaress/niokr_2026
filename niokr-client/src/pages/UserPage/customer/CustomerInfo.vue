<script setup lang="ts">
  import AppList from '@/components/ui/AppList/AppList.vue';
  import { CustomerType } from '@/models/User';

  const props = defineProps<{
    userInfo: CustomerType;
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

  const companyItems = [
    {
      title: 'Название',
      content: `${props.userInfo.company.name}`,
    },
    {
      title: 'Адрес',
      content: `${props.userInfo.company.address}`,
    },
    {
      title: 'Описание',
      content: `${props.userInfo.company.description}`,
    },
  ];
</script>

<template>
  <div>
    <section class="section">
      <h1>Контактная информация</h1>
      <AppList class="app-list" :width="10" :items="infoItems" />
    </section>
    <section class="section">
      <h1>Информация о компании</h1>
      <AppList class="app-list" :width="10" :items="companyItems" />
    </section>
  </div>
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
