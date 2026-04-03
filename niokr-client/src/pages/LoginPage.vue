<script setup lang="ts">
  import { useAuthMutation } from '@/api/UserApi/hooks/useAuthMutation';
  import BaseButton from '@/components/ui/BaseButton.vue';

  const { mutate: auth } = useAuthMutation();
</script>

<template>
  <div class="login-page">
    <BaseButton @click="auth()"> Авторизоваться </BaseButton>
  </div>
</template>

<style lang="scss" scoped>
  .login-page {
    position: absolute;
    top: calc(50vh - 150px);
    left: 50%;
    transform: translateX(-50%);
  }
</style>
