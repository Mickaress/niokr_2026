<script setup lang="ts">
  import { useGetActiveProjectListQuery } from '@/api/ProjectApi/hooks/useGetActiveProjectListQuery';
  import { useGetAllTagsQuery } from '@/api/TagApi/hooks/useGetAllTagsQuery';
  import searchIconUrl from '@/assets/icons/search.svg?url';
  import SidebarLayout from '@/components/layout/SidebarLayout.vue';
  import BaseButton from '@/components/ui/BaseButton.vue';
  import BaseInput from '@/components/ui/BaseInput.vue';
  import ProjectsList from '@/components/ui/ProjectsList.vue';
  import { useFilters } from '@/hooks/useFilters';
  import VMultiselect from '@vueform/multiselect';
  import { watch } from 'vue';

  const projectListQuery = useGetActiveProjectListQuery();
  const tagListQuery = useGetAllTagsQuery();

  const { clearFilter, filter, filters, debouncedInput } = useFilters();

  watch(
    () => filters.value.name,
    () => {
      debouncedInput();
    },
  );
</script>

<template>
  <SidebarLayout>
    <template #header>
      <h1>Все проекты</h1>

      <h2>На этой странице размещены все активные проекты</h2>

      <div class="test">
        <BaseInput
          v-model="filters.name"
          :icon="searchIconUrl"
          placeholder="Поиск по проектам..."
          type="text"
          inputmode="email"
          maxlength="100"
        />
      </div>
    </template>
    <template #sidebar>
      <form class="filter" @submit.prevent="filter">
        <div>
          <h1 class="filter__title">Теги</h1>
          <VMultiselect
            v-model="filters.tags"
            mode="tags"
            placeholder="Введите тег"
            no-results-text="Тег не найден"
            no-options-text="Теги не найдены"
            :close-on-select="false"
            :searchable="true"
            :options="tagListQuery.data.value?.results"
            :disabled="tagListQuery.isFetching.value"
            :loading="tagListQuery.isFetching.value"
            label="name"
            track-by="name"
            value-prop="id"
          />
        </div>

        <div class="filter__divider"></div>

        <footer class="filter__footer">
          <BaseButton full-width type="submit"> Найти </BaseButton>

          <BaseButton variant="text" type="button" @click="clearFilter" full-width>
            Сбросить фильтры
          </BaseButton>
        </footer>
      </form>
    </template>
    <template #main>
      <ProjectsList :projects-query="projectListQuery" />
    </template>
  </SidebarLayout>
</template>

<style lang="scss" scoped>
  .test {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
  }
  .filter {
    background-color: var(--light-color);
    padding: 1.25rem;
    border-radius: 0.625rem;
    border: 0.0625rem solid var(--medium-gray-color);

    &__title {
      font-size: 1.25rem;
      font-weight: bold;
      margin-bottom: 1rem;
    }

    &__divider {
      width: 100%;
      background: var(--medium-gray-color);
      height: 0.0625rem;
      margin: 1.25rem 0;
    }

    &__footer {
      display: flex;
      flex-direction: column;
      gap: 0.625rem;
    }
  }
</style>
