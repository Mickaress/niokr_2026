<script setup lang="ts">
  import { useAuthMutation } from '@/api/UserApi/hooks/useAuthMutation';
  import { useGetUserInfoQuery } from '@/api/UserApi/hooks/useGetUserInfoQuery';
  import arrowIconUrl from '@/assets/icons/dropdown-arrow.svg?url';
  import BaseButton from '@/components/ui/BaseButton.vue';
  import { computed, ref } from 'vue';
  import UserNavigationDropdown from './UserNavigationDropdown.vue';

  const { mutate: auth } = useAuthMutation();
  const { data: userInfo } = useGetUserInfoQuery();

  const fio = computed(() => {
    const [f, ...rest] = userInfo.value?.full_name.split(' ') || [];
    return `${f} ${rest.map((str: string) => str[0]).join('. ')}.`;
  });

  const handleMenuNode = ref<HTMLElement | undefined>(undefined);
  const isMenuOpen = ref(false);

  function toggleMenu() {
    isMenuOpen.value = !isMenuOpen.value;
  }
</script>

<template>
  <div class="actions" ref="handleMenuNode">
    <img src="@/assets/icons/user.svg" alt="" />
    <p v-if="userInfo" class="username">
      {{ fio }}
    </p>
    <button v-if="userInfo" :class="['menu-btn', { active: isMenuOpen }]" @click="toggleMenu">
      <img :src="arrowIconUrl" alt="↓" />
    </button>

    <UserNavigationDropdown v-model:is-open="isMenuOpen" :handle-node="handleMenuNode" />
    <BaseButton v-if="!userInfo" class="auth-btn" variant="text" @click="auth()">
      Авторизоваться
    </BaseButton>
  </div>
</template>

<style lang="scss" scoped>
  .actions {
    gap: 0.75rem;
    display: flex;
    align-items: center;
  }
  .username {
    font-size: 1.125rem;
    line-height: 1.4375em;
    color: var(--accent-color);
    white-space: nowrap;
    user-select: none;
  }
  .auth-btn {
    font-size: 1.125rem;
  }
  .menu-btn {
    width: 2.1875rem;
    height: 1.9375rem;
    padding: 0 0.5rem;
    cursor: pointer;
    background-color: transparent;
    border: 0;
    border-radius: 0.25rem;
    transform: rotate(180deg);
  }

  .menu-btn:hover {
    position: relative;
    background-color: var(--medium-gray-color);
  }

  .menu-btn.active {
    transform: rotate(0deg);
  }
</style>
