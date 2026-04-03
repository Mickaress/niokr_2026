<script setup lang="ts">
  import searchIconUrl from '@/assets/icons/search.svg?url';
  import BaseInput from '@/components/ui/BaseInput.vue';
  import ScrollablePanel from '@/components/ui/ScrollablePanel.vue';
  import { TagType } from '@/models/Filters';
  import { computed, ref } from 'vue';

  const props = defineProps<{
    tags?: TagType[];
    addTagFunc: (id: number) => void;
  }>();

  const searchText = ref('');

  const filteredTags = computed(() =>
    searchText.value
      ? props.tags?.filter(
          (tag) =>
            searchText.value && tag.name.toLowerCase().includes(searchText.value.toLowerCase()),
        )
      : props.tags,
  );
</script>

<template>
  <div>
    <h1>Выберите теги из списка</h1>
    <ScrollablePanel class="block">
      <template #header>
        <BaseInput
          v-model="searchText"
          :icon="searchIconUrl"
          placeholder="Поиск по тегам..."
          type="text"
          inputmode="email"
          maxlength="100"
        />
      </template>

      <template #default>
        <ul class="lists">
          <li v-for="tag of filteredTags" :key="tag.id">
            <button @click="addTagFunc(tag.id)">
              {{ tag.name }}
            </button>
          </li>
        </ul>
      </template>
    </ScrollablePanel>
  </div>
</template>

<style lang="scss" scoped>
  h1 {
    font-size: 1.25rem;
    margin-bottom: 0.75rem;
  }
  .block {
    background-color: var(--gray-color);
    width: 40rem;
    padding: 0.875rem;
    border: 1px solid var(--medium-gray-color);
    border-radius: 0.3125rem;
    height: 32rem;
    display: flex;
    flex-direction: column;
  }
  .lists {
    li {
      button {
        color: var(--dark-color);
        cursor: pointer;
        &:hover {
          text-decoration: underline;
        }
      }
      padding: 0.625rem 0;
    }
  }
</style>
