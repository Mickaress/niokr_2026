<script setup lang="ts">
  import { useGetUserInfoQuery } from '@/api/UserApi/hooks/useGetUserInfoQuery';
  import { RouteNames } from '@/router/types/routeNames';

  withDefaults(
    defineProps<{
      isFooter?: boolean;
    }>(),
    {
      isFooter: false,
    },
  );

  const { data: userData } = useGetUserInfoQuery();
</script>

<template>
  <RouterLink :to="{ name: userData ? RouteNames.USER_INFO : RouteNames.LOGIN }">
    <div class="logo">
      <img src="@/assets/icons/logo.svg" alt="" />

      <div>
        <h1 class="title" :class="isFooter ? 'footer-color' : 'header-color'">Ярмарка проектов</h1>

        <p class="sub-title" :class="isFooter ? 'footer-color' : 'header-color'">в ИРНИТУ</p>
      </div>
    </div>
  </RouterLink>
</template>

<style lang="scss" scoped>
  .logo {
    display: flex;
    align-items: center;
    gap: 1.25rem;
    user-select: none;
  }

  .title {
    font-size: 1.375rem;
    font-weight: bold;
  }

  .sub-title {
    font-size: 1.125rem;
  }

  .header-color {
    color: var(--accent-color);
  }

  .footer-color {
    color: var(--light-color);
  }
</style>
