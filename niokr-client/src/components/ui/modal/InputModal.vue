<script setup lang="ts">
  import BaseButton from '@/components/ui/BaseButton.vue';
  import BaseTextarea from '@/components/ui/BaseTextarea.vue';
  import BaseModal from '@/components/ui/modal/BaseModal.vue';
  import { ref, watch } from 'vue';

  const props = withDefaults(
    defineProps<{
      isShow: boolean;
      title: string;
      baseText?: string;
      placeholder: string;
      submitFunction: (text: string) => void;
      submitText: string;
    }>(),
    {
      baseText: '',
    },
  );

  const emit = defineEmits<{
    (event: 'update:isShow', isShow: boolean): void;
  }>();

  const onCloseModal = () => {
    emit('update:isShow', false);
  };

  const input = ref(props.baseText);

  watch(
    () => props.isShow,
    () => {
      input.value = props.baseText;
    },
  );

  const onSubmit = () => {
    props.submitFunction(input.value);
    onCloseModal();
  };
</script>

<template>
  <BaseModal :is-show="isShow" @close="onCloseModal">
    <h1>{{ title }}</h1>
    <div class="content">
      <BaseTextarea :placeholder="placeholder" v-model="input" :height="20" />
      <BaseButton class="button" @click="onSubmit"> {{ submitText }} </BaseButton>
    </div>
  </BaseModal>
</template>

<style scoped lang="scss">
  h1 {
    font-size: 1.875rem;
    margin-bottom: 1.25rem;
  }
  .content {
    min-width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.375rem;
  }
</style>
