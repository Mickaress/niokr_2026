<script setup lang="ts">
  import { useGetAllTagsQuery } from '@/api/TagApi/hooks/useGetAllTagsQuery';
  import { declOfNum } from '@/helpers/string';
  import { computed, ref } from 'vue';
  import BaseButton from './BaseButton.vue';
  import BaseTag from './BaseTag.vue';

  const props = withDefaults(
    defineProps<{
      tagIds: number[];
      defaultVisible?: number;
      declWords?: [string, string, string];
      isVisible?: boolean;
      deletable?: boolean;
      deleteFunc?: (id: number) => void;
    }>(),
    {
      defaultVisible: 3,
      declWords: () => ['тег', 'тега', 'тегов'],
      isVisible: false,
    },
  );

  const { data: allTags } = useGetAllTagsQuery();
  const tags = computed(
    () => allTags.value?.results.filter((tag) => props.tagIds.includes(tag.id)) || [],
  );

  const isTagsVisible = ref(props.isVisible);

  const hiddenTagsCount = props.tagIds.length - props.defaultVisible;
  const BtnText = computed(() =>
    isTagsVisible.value
      ? props.isVisible
        ? ''
        : 'Скрыть'
      : `+${hiddenTagsCount} ${declOfNum(hiddenTagsCount, props.declWords)}`,
  );

  const visibleTags = computed(() =>
    isTagsVisible.value ? tags.value : tags.value.slice(0, props.defaultVisible),
  );
</script>

<template>
  <ul class="tag-list">
    <li v-for="tag of visibleTags" :key="tag.id">
      <BaseTag :deletable="props.deletable" @click="props.deleteFunc && props.deleteFunc(tag.id)">
        {{ tag.name }}
      </BaseTag>
    </li>
    <li v-if="hiddenTagsCount > 0" class="button">
      <BaseButton variant="text" @click="isTagsVisible = !isTagsVisible">
        {{ BtnText }}
      </BaseButton>
    </li>
  </ul>
</template>

<style scoped lang="scss">
  .tag-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    align-items: center;
  }
  .button {
    display: flex;
    align-items: center;
  }
</style>
