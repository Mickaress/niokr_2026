<script setup lang="ts">
  import { Ref, TextareaHTMLAttributes, computed, useAttrs } from 'vue';

  withDefaults(
    defineProps<{
      modelValue?: string;
      textareaRef?: Ref<TextareaHTMLAttributes | null>;
      height?: number;
    }>(),
    {
      modelValue: '',
      height: 7,
    },
  );

  const emit = defineEmits<{
    (e: 'update:modelValue', value: string): void;
  }>();

  const attrs = useAttrs();
  const isMaxLength = computed(
    () => typeof attrs.maxlength === 'number' || typeof attrs.maxlength === 'string',
  );

  function onInput(e: Event) {
    const target = e.target as HTMLInputElement;
    emit('update:modelValue', target.value);
  }
</script>

<template>
  <label class="label">
    <textarea
      v-bind="$attrs"
      :value="modelValue"
      :class="['input', { 'with-maxlength': isMaxLength }]"
      @input="onInput"
      :style="{ height: height + 'rem' }"
    >
    </textarea>
    <span v-if="isMaxLength" class="maxlength">
      {{ modelValue.length || 0 }}/{{ $attrs.maxlength }}
    </span>
  </label>
</template>

<style scoped>
  .label {
    position: relative;
    display: inline-block;
    width: 100%;
  }

  .maxlength {
    position: absolute;
    right: 1.25rem;
    bottom: 0.625rem;
    font-size: 1rem;
    color: var(--dark-gray-color);
    user-select: none;
  }

  .label-text {
    margin-bottom: 0.75rem;
    font-size: 1.125rem;
    font-weight: bold;
    color: #fff;
  }

  .input {
    width: 100%;
    padding: 0.75rem 0.8rem;
    font-size: 1.125rem;
    color: var(--dark-color);
    background-color: #fff;
    border: 1px solid var(--medium-gray-color);
    border-radius: 0.3125rem;
    transition: border 100ms ease;
    resize: none;
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

  .input.with-maxlength {
    padding-bottom: 2.5rem;
  }

  .input::placeholder {
    font-size: 1.125rem;
    font-weight: normal;
    color: var(--dark-gray-color);
  }

  .input:focus {
    outline: none;
  }

  .input:disabled {
    color: var(--dark-gray-color);
    cursor: default;
    background-color: var(--light-gray-color);
  }

  .input:focus-visible {
    border: 1px solid var(--accent-color);
  }
</style>
