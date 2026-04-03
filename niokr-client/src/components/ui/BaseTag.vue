<script setup lang="ts">
  import closeIconUrl from '@/assets/icons/close.svg?url';

  defineProps<{
    deletable?: boolean;
  }>();
</script>

<template>
  <span class="tag" :class="deletable && 'deletable'">
    <slot></slot>
    <img v-if="deletable" :src="closeIconUrl" />
  </span>
</template>

<style scoped lang="scss">
  .tag {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.4375rem 1.25rem;
    font-size: 0.875rem;
    line-height: 1.125rem;
    color: var(--light-color);
    background-color: var(--accent-color);
    border-radius: 1.875rem;
  }
  .deletable {
    &:hover {
      background-color: var(--red-color);
      cursor: pointer;
    }

    img {
      height: 0.875rem;
      padding: 0.125rem;
      filter: brightness(0) invert(1);
      margin-left: 0.3125rem;
    }
  }
</style>
