<script setup lang="ts">
  defineProps<{
    title?: string;
    subtitle?: string;
  }>();
</script>

<template>
  <section class="panel">
    <h1 v-if="title" class="title">{{ title }}</h1>
    <p v-if="subtitle" class="subtitle">{{ subtitle }}</p>
    <slot name="button"></slot>
  </section>
</template>

<style lang="scss" scoped>
  .panel {
    text-align: center;
  }

  .title {
    font-weight: bold;
    font-size: 1.75rem;
    line-height: 2.25rem;
    color: var(--dark-gray-color);
  }

  .subtitle {
    color: var(--dark-gray-color);
    margin: 1rem auto 2.125rem;
    max-width: 28.125rem;
    font-size: 1.125rem;
    line-height: 150%;
  }
</style>
