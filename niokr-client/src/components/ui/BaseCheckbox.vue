<template>
  <label :aria-disabled="disabled" class="label">
    <input
      :disabled="disabled"
      class="checkbox"
      :checked="checked"
      type="checkbox"
      :value="value"
      @change="onChange"
    />
    <slot></slot>
  </label>
</template>

<script setup lang="ts">
  import { computed } from 'vue';

  const props = defineProps<{
    modelValue?: unknown[];
    value: unknown;
    disabled?: boolean;
  }>();
  const emit = defineEmits<{
    (e: 'update:modelValue', value: unknown): void;
  }>();

  const checked = computed(includesValue);
  defineExpose({ checked });

  function onChange(e: Event) {
    const target = e.target as HTMLInputElement;
    if (!props.modelValue) return;
    if (props.disabled) return;
    if (target.checked) addValue(props.modelValue, props.value);
    else removeValue(props.modelValue, props.value);
  }

  function addValue(arr: unknown[], value: unknown) {
    emit('update:modelValue', [...arr, value]);
  }

  function removeValue(arr: unknown[], value: unknown) {
    emit(
      'update:modelValue',
      arr.filter((i) => i !== value),
    );
  }

  function includesValue(): boolean {
    return Boolean(props.modelValue?.includes(props.value));
  }
</script>

<style lang="scss" scoped>
  .label[aria-disabled='true'] {
    color: var(--gray-color-2) !important;
    cursor: default !important;
  }

  .label {
    display: flex;
    gap: 0.9375rem;
    align-items: center;
    font-size: 1.125rem;
    font-weight: normal;
    user-select: none;

    &:not(:last-child) {
      margin-bottom: 0.8125rem;
    }
  }

  .label:hover {
    color: var(--accent-color);
    cursor: pointer;
  }

  .checkbox {
    position: relative;
    width: 1.25rem;
    height: 1.25rem;
    border: 0.0625rem solid var(--dark-gray-color);
    border-radius: 0.1875rem;
    appearance: none;
    cursor: pointer;
  }

  .checkbox:checked {
    background-color: var(--accent-color);
    border: none;
  }

  .checkbox:checked::before {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
    line-height: normal;
    color: #fff;
    content: '\2713';
  }
</style>
