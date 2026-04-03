<script setup lang="ts">
  import { RouterLink } from 'vue-router';
  import { useUserNavigationRoutes } from '@/hooks/useRoutes';

  const routes = useUserNavigationRoutes();
</script>

<template>
  <div class="user-tabs">
    <ul class="user-tabs__list">
      <li class="user-tabs__list-item" v-for="link of routes" :key="link.name">
        <RouterLink class="user-tabs__action" :to="{ name: link.name }">
          {{ link.meta.title }}
        </RouterLink>
      </li>
    </ul>
  </div>
</template>

<style lang="scss" scoped>
  .user-tabs {
    border: 1px solid var(--medium-gray-color);
    background: var(--light-color);
    border-radius: 0.625rem;

    &__list {
      padding: 0 1.375rem;
      width: 100%;

      &-item {
        &:not(:empty) {
          border-bottom: 1px solid var(--medium-gray-color);
        }
      }
    }
    &__action {
      display: flex;
      width: 100%;
      padding: 1.25rem 0;
      font-size: 1.25rem;
      line-height: 1.625rem;
      color: var(--text-color);
      cursor: pointer;

      &:hover,
      &.router-link-active {
        color: var(--accent-color);
      }
    }
  }
</style>
