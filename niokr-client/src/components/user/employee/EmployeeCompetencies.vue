<script setup lang="ts">
  import { useUpdateUserInfo } from '@/api/UserApi/hooks/useUpdateUserInfo';
  import BaseButton from '@/components/ui/BaseButton.vue';
  import InputModal from '@/components/ui/modal/InputModal.vue';
  import { ref } from 'vue';

  defineProps<{
    competencies: string;
  }>();

  const isShowModal = ref<boolean>(false);

  const { mutate: updateCompetencies } = useUpdateUserInfo();
</script>

<template>
  <section class="section">
    <div class="title">
      <h1>Компетенции</h1>
      <BaseButton variant="text" @click="isShowModal = true"> Изменить </BaseButton>
      <InputModal
        v-model:isShow="isShowModal"
        title="Редактирование компетенций"
        :baseText="competencies"
        placeholder="Например, Умение работать в команде"
        :submitFunction="(text) => updateCompetencies({ competencies: text })"
        submit-text="Сохранить"
      />
    </div>
    <p v-if="competencies">{{ competencies }}</p>
    <p v-else class="competencies">Компетенции не выбраны</p>
  </section>
</template>

<style lang="scss" scoped>
  .section {
    margin-bottom: 3.125rem;
    &:last-child {
      margin-bottom: 0;
    }
  }

  .title {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1.0625rem;
    h1 {
      font-size: 1.125rem;
      font-weight: bold;
    }
  }

  .competencies {
    color: var(--dark-gray-color);
  }
</style>
