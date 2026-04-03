<script setup lang="ts">
  import { useLogoutMutation } from '@/api/UserApi/hooks/useLogoutMutation';
  import DropdownList from '@/components/ui/DropdownList.vue';
  import ConfirmModal from '@/components/ui/modal/ConfirmModal.vue';
  import { useUserNavigationRoutes } from '@/hooks/useRoutes';
  import { DropdownItem } from '@/models/components/DropdownItem';
  import { ref, watch } from 'vue';
  import { useRoute } from 'vue-router';

  defineProps<{
    isOpen: boolean;
    handleNode?: HTMLElement;
  }>();

  const emit = defineEmits<{
    (e: 'update:isOpen', isOpen: boolean): void;
  }>();

  const route = useRoute();
  const routes = useUserNavigationRoutes();
  const { mutate: logout } = useLogoutMutation();

  watch(
    () => route.path,
    () => emit('update:isOpen', false),
  );

  const items = routes.map<DropdownItem>((route) => ({
    content: route.meta.title || '',
    location: { name: route.name },
    type: 'link',
  }));

  const isShowModal = ref<boolean>(false);

  items.push({
    content: 'Выйти',
    type: 'button',
    action: () => (isShowModal.value = true),
  });
</script>

<template>
  <DropdownList
    :handle-node="handleNode"
    :is-open="isOpen"
    :item-list="items"
    @update:is-open="(value) => emit('update:isOpen', value)"
  />

  <ConfirmModal
    v-model:is-show="isShowModal"
    question="Вы уверены, что хотите выйти из аккаунта?"
    agreeAnswer="Выйти из аккаунта"
    disagree-answer="Остаться"
    :agreeAction="logout"
  />
</template>
