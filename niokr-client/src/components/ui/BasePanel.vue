<template>
  <div class="panel">
    <slot></slot>
  </div>
</template>

<style scoped>
  .panel {
    padding: 1.375rem;
    background: var(--light-color);
    border-radius: 0.625rem;
    box-shadow: 0 0 0.3125rem rgb(0 0 0 / 18%);
  }
</style>
