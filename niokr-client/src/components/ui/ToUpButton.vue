<template>
  <transition name="btn">
    <BaseButton v-if="visible" class="btn" @click="scroll" />
  </transition>
</template>

<script setup lang="ts">
  import { onBeforeMount, onBeforeUnmount, ref } from 'vue';
  import BaseButton from './BaseButton.vue';

  const props = withDefaults(
    defineProps<{
      topOffset?: number;
    }>(),
    { topOffset: 0 },
  );

  const visible = ref(false);

  function scroll() {
    window.scrollTo({ behavior: 'smooth', left: 0, top: 0 });
  }

  function onScroll() {
    visible.value = Math.floor(scrollY) > props.topOffset;
  }

  onBeforeMount(() => {
    window.addEventListener('scroll', onScroll);
  });

  onBeforeUnmount(() => {
    window.removeEventListener('scroll', onScroll);
  });
</script>

<style lang="scss" scoped>
  .btn {
    position: fixed;
    right: 5rem;
    bottom: 4rem;
    z-index: 999;
    width: 4rem;
    height: 4rem;
    padding: 0;
    background-image: url('@/assets/icons/dropdown-arrow.svg');
    background-repeat: no-repeat;
    background-position: 50% 45%;
    background-size: 50%;
    border-radius: 50%;
    box-shadow: 0 0 0.3125rem rgb(0 0 0 / 18%);
  }

  .btn-enter-active,
  .btn-leave-active {
    transition: opacity 0.3s ease;
  }

  .btn-enter-from,
  .btn-leave-to {
    opacity: 0;
  }
</style>
