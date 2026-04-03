<script setup lang="ts">
  import AppLogo from '../../ui/AppLogo.vue';
  import BaseContainer from '../../ui/BaseContainer.vue';
  import HeaderNavigation from './HeaderNavigation.vue';
  import HeaderUserActions from './UserActions/HeaderUserActions.vue';
</script>

<template>
  <header class="header">
    <BaseContainer class="container">
      <AppLogo />

      <HeaderNavigation />

      <HeaderUserActions />
    </BaseContainer>
  </header>
</template>

<style lang="scss" scoped>
  .header {
    background: var(--light-color);
    border-bottom: 1px solid var(--medium-gray-color);
    margin-bottom: 2rem;
  }
  .container {
    display: flex;
    max-width: 112.5rem;
    justify-content: space-between;
    align-items: center;
    height: 7rem;
  }
</style>
