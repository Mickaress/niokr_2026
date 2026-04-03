<script setup lang="ts">
  import BaseButton from '../BaseButton.vue';
  import BaseModal from './BaseModal.vue';

  const props = defineProps<{
    isShow: boolean;
    question: string;
    agreeAnswer: string;
    disagreeAnswer: string;
    agreeAction: () => void;
  }>();

  const emit = defineEmits<{
    (event: 'update:isShow', isShow: boolean): void;
  }>();

  function onCloseModal() {
    emit('update:isShow', false);
  }

  const onSubmit = () => {
    props.agreeAction();
    onCloseModal();
  };
</script>

<template>
  <BaseModal :is-show="isShow" @close="onCloseModal">
    <div class="content">
      <h1>{{ question }}</h1>

      <slot name="content"></slot>

      <div class="buttons">
        <BaseButton @click="onSubmit" variant="outlined" color="red">
          {{ agreeAnswer }}
        </BaseButton>
        <BaseButton @click="onCloseModal">{{ disagreeAnswer }}</BaseButton>
      </div>
    </div>
  </BaseModal>
</template>

<style lang="scss" scoped>
  .content {
    min-width: 100%;
    margin-top: 2.5rem;

    h1 {
      font-size: 2.5rem;
      max-width: 31.25rem;
      text-align: center;
      margin-bottom: 2rem;
      font-weight: bold;
    }
  }
  .buttons {
    display: flex;
    justify-content: center;
    gap: 1.25rem;
  }
</style>
