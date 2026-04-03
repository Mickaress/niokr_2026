<template>
  <component
    :is="is"
    :disabled="disabled"
    :class="['button', variant, color]"
    :style="{
      width: fullWidth ? '100%' : undefined,
    }"
  >
    <slot></slot>
  </component>
</template>

<script setup lang="ts">
  export type Variant = 'primary' | 'outlined' | 'text';
  export type Is = 'button' | 'router-link' | 'a';
  export type Color = 'red';

  withDefaults(
    defineProps<{
      variant?: Variant;
      is?: Is;
      disabled?: boolean;
      fullWidth?: boolean;
      color?: Color;
    }>(),
    {
      is: 'button',
      variant: 'primary',
      disabled: false,
      fullWidth: false,
    },
  );
</script>

<style scoped lang="scss">
  .button {
    --main-color: var(--accent-color);
    --dark-main-color: var(--dark-accent-color);
    --light-main-color: var(--light-accent-color);

    text-transform: uppercase;
    border-radius: 0.3125rem;
    white-space: nowrap;
    text-decoration: none;
    cursor: pointer;

    &.red {
      --main-color: var(--red-color);
      --dark-main-color: var(--dark-red-color);
      --light-main-color: var(--light-red-color);
    }
  }

  .primary {
    color: var(--light-color);
    background-color: var(--main-color);
    padding: 1rem 2rem;
    border: 0.125rem solid var(--main-color);

    &:hover {
      background-color: var(--dark-main-color);
      border-color: var(--dark-main-color);
    }

    &:active {
      background-color: var(--light-main-color);
      border-color: var(--light-main-color);
    }

    &:disabled {
      background-color: var(--dark-gray-color);
      border-color: var(--dark-gray-color);
      cursor: default;
    }
  }

  .outlined {
    color: var(--main-color);
    background-color: transparent;
    border: 0.125rem solid var(--main-color);
    padding: 1rem 2rem;

    &:hover {
      color: #fff;
      background-color: var(--dark-main-color);
      border-color: var(--dark-main-color);
    }

    &:active {
      color: #fff;
      background-color: var(--light-main-color);
      border-color: var(--light-main-color);
    }

    &:disabled {
      color: var(--dark-gray-color);
      border-color: var(--dark-gray-color);
    }
  }

  .text {
    color: var(--main-color);
    background-color: transparent;

    &:hover {
      color: var(--dark-main-color);
      text-decoration: underline;
    }

    &:active {
      color: var(--light-main-color);
    }

    &:disabled {
      color: var(--dark-gray-color);
    }
  }
  .tag {
    color: var(--light-color);
    background-color: var(--main-color);
    padding: 0.4375rem 1.25rem;
    border-radius: 1.875rem;
    text-transform: none;

    &:hover {
      background-color: var(--dark-main-color);
    }

    &:active {
      background-color: var(--light-main-color);
    }

    &:disabled {
      background-color: var(--dark-gray-color);
    }
  }
</style>
