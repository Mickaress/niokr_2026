<script setup lang="ts">
  import type { Ref } from 'vue';

  withDefaults(
    defineProps<{
      modelValue?: string;
      icon?: string;
      inputRef?: Ref<HTMLInputElement | null>;
    }>(),
    {
      modelValue: '',
      icon: undefined,
      inputRef: undefined,
    },
  );

  const emit = defineEmits<{
    (e: 'update:modelValue', value: string): void;
  }>();

  function onInput(e: Event) {
    const target = e.target as HTMLInputElement;
    emit('update:modelValue', target.value);
  }
</script>

<template>
  <input
    v-bind="$attrs"
    :ref="inputRef"
    :value="modelValue"
    :class="['input', { 'with-icon': icon }]"
    :style="{
      backgroundImage: icon && `url(${icon})`,
    }"
    @input="onInput"
  />
</template>

<style lang="scss" scoped>
  .input {
    width: 100%;
    padding-left: 0.8rem;
    font-size: 1.125rem;
    height: 2.75rem;
    border: 1px solid var(--medium-gray-color);
    border-radius: 0.3125rem;
    transition: border 100ms ease;
    outline: none;
  }

  .input.with-icon {
    background: calc(100% - 1rem) center / 1.5rem no-repeat #fff;
  }

  .input::placeholder {
    color: var(--dark-gray-color);
  }

  .input:disabled {
    color: var(--dark-gray-color);
    cursor: default;
    background-color: var(--light-gray-color);
  }

  .input:focus-visible {
    border-color: var(--accent-color);
  }
</style>
