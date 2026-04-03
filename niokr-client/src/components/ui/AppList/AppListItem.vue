<script setup lang="ts">
  defineProps<{
    width: number;
  }>();
</script>

<template>
  <li class="item">
    <h1 class="title" :style="{ minWidth: width + 'rem' }">
      <slot name="title"></slot>
    </h1>
    <span class="value">
      <slot name="default"></slot>
    </span>
  </li>
</template>

<style lang="scss" scoped>
  .item {
    display: flex;
    gap: 1em;
  }

  .title {
    font-size: 1.125rem;
  }

  .value {
    font-weight: bold;
    font-size: 1.125rem;
  }
</style>
