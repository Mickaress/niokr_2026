<template>
  <BasePanel v-if="isOpen" ref="root" :style="{ ...position }" class="dropdown">
    <slot></slot>
  </BasePanel>
</template>

<script setup lang="ts">
  import { isPartOfNode } from '@/helpers/dom';
  import { onClickOutside } from '@vueuse/core';
  import { ref, watch } from 'vue';
  import BasePanel from './BasePanel.vue';

  export type Position = {
    left?: string;
    right?: string;
    top?: string;
    bottom?: string;
  };

  const props = withDefaults(
    defineProps<{
      isOpen: boolean;
      handleNode?: HTMLElement;
      position?: Position;
    }>(),
    {
      position: () => ({}),
      handleNode: undefined,
    },
  );
  const emit = defineEmits<{
    (e: 'update:isOpen', isOpen: boolean): void;
  }>();
  const root = ref(null);

  watch(
    () => props.handleNode,
    (handleNode, prevHandleNode) => {
      if (!handleNode) return;
      if (handleNode === prevHandleNode) return;
      handleNode.style.position = 'relative';
    },
    { immediate: true },
  );

  onClickOutside(root, (evt) => {
    if (isPartOfNode(evt.target as HTMLElement, props.handleNode)) return;
    emit('update:isOpen', false);
  });
</script>

<style scoped>
  .dropdown {
    position: absolute;
    top: 150%;
    right: 0;
    width: 15rem;
    padding: 0.6rem 0 !important;
  }
</style>
