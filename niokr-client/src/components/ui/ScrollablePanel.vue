<script setup lang="ts"></script>

<template>
  <section class="scrollable-panel">
    <header class="scrollable-panel__header">
      <slot name="header"></slot>
    </header>
    <div class="scrollable-panel__content">
      <slot name="default"></slot>
    </div>
  </section>
</template>

<style scoped lang="scss">
  .scrollable-panel {
    display: flex;
    flex-direction: column;
    padding-bottom: 0.2rem;
    background: var(--gray-color-4);
    border: 1px solid var(--gray-color-1);
    border-radius: 0.3125rem;
    &__header {
      margin-bottom: 0.3125rem;
    }

    &__content {
      overflow: auto;
      scrollbar-color: var(--dark-gray-color) transparent;
      scrollbar-width: thin;
      &::-webkit-scrollbar {
        width: 0.375rem;
      }
      &::-webkit-scrollbar-thumb {
        border-radius: 0.625rem;
        background-color: var(--dark-gray-color);
      }
    }
  }
</style>
