<script setup lang="ts">
  import { AppListItemType } from '@/models/components/AppList';
  import AppListItem from './AppListItem.vue';

  withDefaults(
    defineProps<{
      items?: AppListItemType[];
      width?: number;
    }>(),
    {
      items: () => [],
      width: 16,
    },
  );
</script>

<template>
  <ul class="info-list">
    <slot>
      <template v-for="{ title, content } in items" :key="title + content">
        <AppListItem :width="width">
          <template #title>{{ title }}</template>
          <template #default>
            {{ content || '-' }}
          </template>
        </AppListItem>
      </template>
    </slot>
  </ul>
</template>

<style scoped>
  .info-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }
</style>
