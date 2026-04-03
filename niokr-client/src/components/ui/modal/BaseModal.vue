<template>
  <div v-if="isShow" class="modal-background" @click="closeModal">
    <BasePanel class="modal-content" @click.stop>
      <button class="close-btn" @click="closeModal">
        <img :src="closeIconUrl" alt="x" />
      </button>
      <slot></slot>
    </BasePanel>
  </div>
</template>

<script setup lang="ts">
  import closeIconUrl from '@/assets/icons/close.svg?url';
  import BasePanel from '../BasePanel.vue';

  defineProps<{
    isShow: boolean;
  }>();

  const emit = defineEmits<{
    (e: 'close'): void;
  }>();

  function closeModal() {
    emit('close');
  }
</script>

<style lang="scss" scoped>
  .modal-content {
    margin: 0 1rem;
    position: relative;
    max-width: 62.5rem;
    overflow: auto;
    scrollbar-color: var(--dark-gray-color) transparent;
    scrollbar-width: thin;
    &::-webkit-scrollbar {
      width: 0.375rem;
      border-radius: 0.625rem;
    }
    &::-webkit-scrollbar-thumb {
      border-radius: 0.625rem;
      background-color: var(--dark-gray-color);
    }
  }

  .modal-background {
    position: fixed;
    inset: 0;
    z-index: 100000;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgb(0 0 0 / 40%);
  }

  .close-btn {
    position: absolute;
    top: 1rem;
    right: 1.125rem;
    width: 3rem;
    height: 3rem;
    cursor: pointer;
  }

  .close-btn:hover {
    opacity: 0.8;
  }
</style>
