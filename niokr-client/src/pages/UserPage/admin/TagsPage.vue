<script setup lang="ts">
  import { useDeleteTagMutation } from '@/api/AdminApi/hooks/useDeleteTagMutation';
  import { useGetAllTagsQuery } from '@/api/TagApi/hooks/useGetAllTagsQuery';
  import BaseButton from '@/components/ui/BaseButton.vue';
  import BaseCard from '@/components/ui/BaseCard.vue';
  import BaseList from '@/components/ui/BaseList.vue';
  import ConfirmModal from '@/components/ui/modal/ConfirmModal.vue';
  import { ref } from 'vue';

  const tagListQuery = useGetAllTagsQuery(true);

  const { mutate: deleteTag } = useDeleteTagMutation();

  const isShowDeleteModal = ref(false);
  const deletableId = ref<number>(0);

  const onDeleteTag = (id: number) => {
    deletableId.value = id;
    isShowDeleteModal.value = true;
  };
</script>

<template>
  <ConfirmModal
    v-model:is-show="isShowDeleteModal"
    question="Вы уверены, что хотите удалить этот тег?"
    :agree-action="() => deleteTag(deletableId)"
    agree-answer="Удалить"
    disagree-answer="Отмена"
  />

  <BaseList
    :is-loading="tagListQuery.isLoading.value"
    :is-error="tagListQuery.isError.value"
    empty-title="Нет тегов"
    empty-subtitle="Пока нет ни одного тега"
    :total-items="tagListQuery.data.value?.count || 0"
  >
    <template #list>
      <li v-for="tag in tagListQuery.data.value?.results" :key="tag.id">
        <BaseCard :title="tag.name">
          <template #main><slot name="main"></slot></template>
          <template #footer><slot name="footer"></slot></template>
          <template #buttons>
            <BaseButton variant="outlined" color="red" @click="onDeleteTag(tag.id)">
              Удалить
            </BaseButton>
          </template>
        </BaseCard>
      </li>
    </template>
  </BaseList>
</template>
