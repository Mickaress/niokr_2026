<script setup lang="ts">
  import { useUpdateUserInfo } from '@/api/UserApi/hooks/useUpdateUserInfo';
  import BaseButton from '@/components/ui/BaseButton.vue';
  import TagList from '@/components/ui/TagList.vue';
  import TagsModal from '@/components/ui/modal/editTagsModal/TagsModal.vue';
  import { ref } from 'vue';

  defineProps<{
    tags: number[];
  }>();

  const isShowModal = ref<boolean>(false);

  const { mutate: updateTags } = useUpdateUserInfo();
</script>

<template>
  <TagsModal
    :tag-ids="tags"
    v-model:isShow="isShowModal"
    :save-function="(tagIds) => updateTags({ tags: tagIds })"
  />

  <section class="section">
    <div class="title">
      <h1>Теги</h1>

      <BaseButton variant="text" @click="isShowModal = true"> Изменить </BaseButton>
    </div>
    <p v-if="tags.length === 0">Теги не выбраны</p>

    <TagList v-else is-visible :tag-ids="tags" />
  </section>
</template>

<style lang="scss" scoped>
  .section {
    margin-bottom: 1.625rem;
    p {
      color: var(--dark-gray-color);
    }
  }
  .title {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1.0625rem;
    h1 {
      font-size: 1.125rem;
      font-weight: bold;
    }
  }
</style>
