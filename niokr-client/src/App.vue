<script setup lang="ts">
  import { RouterView } from 'vue-router';
  import { useGetUserInfoQuery } from './api/UserApi/hooks/useGetUserInfoQuery';
  import PageLayout from './components/layout/PageLayout.vue';
  import ToUpButton from './components/ui/ToUpButton.vue';

  const { isLoading } = useGetUserInfoQuery();
</script>

<template>
  <PageLayout v-if="!isLoading">
    <RouterView />
  </PageLayout>

  <ToUpButton />
</template>

<style lang="scss" scoped></style>
