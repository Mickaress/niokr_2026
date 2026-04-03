<script setup lang="ts">
  import { useGetAllTagsQuery } from '@/api/TagApi/hooks/useGetAllTagsQuery';
  import BaseButton from '@/components/ui/BaseButton.vue';
  import TagList from '@/components/ui/TagList.vue';
  import BaseModal from '@/components/ui/modal/BaseModal.vue';
  import { computed, ref, watch } from 'vue';
  import ChangeTags from './ChangeTags.vue';

  const props = defineProps<{
    isShow: boolean;
    tagIds: number[];
    saveFunction: (tagIds: number[]) => void;
  }>();

  const emit = defineEmits<{
    (event: 'update:isShow', isShow: boolean): void;
  }>();

  function onCloseModal() {
    emit('update:isShow', false);
  }

  const selectedTagIds = ref(props.tagIds);

  watch(
    () => props.isShow,
    () => {
      selectedTagIds.value = props.tagIds;
    },
  );

  const { data: allTags } = useGetAllTagsQuery();

  const notUserTags = computed(() =>
    allTags?.value?.results.filter((tag) => !selectedTagIds.value.includes(tag.id)),
  );

  function deleteTag(id: number) {
    selectedTagIds.value = selectedTagIds.value.filter((item) => item !== id);
  }

  function addTag(id: number) {
    if (selectedTagIds.value.includes(id)) {
      return;
    }

    selectedTagIds.value = [...selectedTagIds.value, id];
  }

  const saveTags = () => {
    props.saveFunction(selectedTagIds.value);
    onCloseModal();
  };
</script>

<template>
  <BaseModal class="tag-modal" :is-show="isShow" @close="onCloseModal">
    <h1>Редактирование тегов</h1>
    <div class="tag-modal__selected-tags">
      <h2>Выбранные теги</h2>

      <TagList
        v-if="selectedTagIds?.length"
        :tag-ids="selectedTagIds"
        :is-visible="true"
        deletable
        :deleteFunc="deleteTag"
      />

      <p v-else>Теги не выбраны</p>
    </div>

    <ChangeTags :tags="notUserTags" :addTagFunc="addTag" />

    <div class="tag-modal__save-button">
      <BaseButton @click="saveTags">Сохранить</BaseButton>
    </div>
  </BaseModal>
</template>

<style scoped lang="scss">
  .tag-modal {
    h1 {
      font-size: 1.875rem;
    }

    &__selected-tags {
      max-width: 40rem;
      border-bottom: 1px solid var(--medium-gray-color);
      padding-bottom: 1.25rem;
      margin: 1.25rem 0;
      h2 {
        margin-bottom: 0.5rem;
      }
      p {
        font-size: 0.625rem;
        text-transform: uppercase;
        color: var(--dark-gray-color);
      }
    }

    &__save-button {
      display: flex;
      justify-content: center;
      margin-top: 1.25rem;
    }
  }
</style>
