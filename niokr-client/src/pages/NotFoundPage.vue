<script setup lang="ts">
  import BaseButton from '@/components/ui/BaseButton.vue';
  import BaseStub from '@/components/ui/BaseStub.vue';
  import { RouteNames } from '@/router/types/routeNames';
</script>

<template>
  <div class="wrapper">
    <img src="@/assets/icons/404.svg" alt="" />
    <BaseStub
      title="Страница не найдена
"
      subtitle="Возможно, она была перемещена, или вы, просто, неверно указали адрес страницы.

"
    >
      <template #button>
        <BaseButton is="router-link" :to="{ name: RouteNames.USER_PAGE }"> В профиль </BaseButton>
      </template>
    </BaseStub>
  </div>
</template>

<style lang="scss" scoped>
  .wrapper {
    position: absolute;
    top: calc(50vh - 370px);
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
