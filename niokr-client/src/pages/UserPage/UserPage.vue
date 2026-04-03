<script setup lang="ts">
  import SidebarLayout from '@/components/layout/SidebarLayout.vue';
  import BaseButton from '@/components/ui/BaseButton.vue';
  import BaseInput from '@/components/ui/BaseInput.vue';
  import UserTabs from '@/components/ui/UserTabs.vue';
  import ConfirmModal from '@/components/ui/modal/ConfirmModal.vue';
  import { RouteNames } from '@/router/types/routeNames';
  import { RouterView } from 'vue-router';
  import { UserRole } from '@/models/User';
  import { useCheckRole } from '@/hooks/useCheckRole';
  import { computed, ref } from 'vue';
  import { useRoute } from 'vue-router';
  import { useAddTagMutation } from '@/api/AdminApi/hooks/useAddTagMutation';

  const { mutate: addTag } = useAddTagMutation();

  const route = useRoute();
  const isCustomer = useCheckRole([UserRole.CUSTOMER]);

  const isUserProjectPage = computed(() => {
    return route.name === RouteNames.USER_PROJECTS;
  });

  const isTagsPage = computed(() => {
    return route.name === RouteNames.ADMIN_TAGS;
  });

  const isShowTagModal = ref(false);
  const tagName = ref('');

  const onAddTag = () => {
    addTag(tagName.value);
    tagName.value = '';
    isShowTagModal.value = false;
  };
</script>

<template>
  <SidebarLayout>
    <template #header>
      <div class="user__header">
        <h1>Профиль пользователя</h1>

        <BaseButton
          v-if="isCustomer && isUserProjectPage"
          is="router-link"
          :to="{ name: RouteNames.CUSTOMER_PROJECT_CREATE }"
        >
          Создать проект
        </BaseButton>

        <BaseButton v-if="isTagsPage" @click="isShowTagModal = true"> Создать тег </BaseButton>
      </div>
    </template>

    <template #sidebar>
      <UserTabs />
    </template>

    <template #main>
      <RouterView />
    </template>
  </SidebarLayout>

  <ConfirmModal
    v-model:is-show="isShowTagModal"
    question="Введите название тега"
    :agree-action="onAddTag"
    agree-answer="Добавить"
    disagree-answer="Отмена"
  >
    <template #content>
      <BaseInput class="input" v-model="tagName" placeholder="Название тега" maxlength="100" />
    </template>
  </ConfirmModal>
</template>

<style lang="scss" scoped>
  .user__header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1.5rem;

    h1 {
      font-size: 2.5rem;
      font-weight: bold;
    }
  }

  .input {
    margin-bottom: 2rem;
  }
</style>
