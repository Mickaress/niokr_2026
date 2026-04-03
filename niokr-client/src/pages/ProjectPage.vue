<script setup lang="ts">
  import { useGetSingleProjectQuery } from '@/api/ProjectApi/hooks/useGetSingleProjectQuery';
  import AppList from '@/components/ui/AppList/AppList.vue';
  import BaseBadge from '@/components/ui/BaseBadge.vue';
  import BasePanel from '@/components/ui/BasePanel.vue';
  import BaseStub from '@/components/ui/BaseStub.vue';
  import GridLayout from '@/components/ui/GridLayout.vue';
  import { STATUS_LABELS } from '@/models/Status';
  import { useRoute } from 'vue-router';
  import TagList from '@/components/ui/TagList.vue';
  import ProjectFilesList from '@/components/ui/ProjectFilesList.vue';

  const route = useRoute();

  const projectId = Number(route.params.id);
  const projectQuery = useGetSingleProjectQuery(projectId);
</script>

<template>
  <BaseStub v-if="projectQuery.isLoading.value" title="Загрузка..."></BaseStub>
  <BaseStub
    v-if="projectQuery.isError.value"
    title="Ошибка сервера"
    subtitle="В данный момент сервер не отвечает"
  ></BaseStub>

  <template v-if="projectQuery.data.value">
    <header class="header">
      <h1>{{ projectQuery.data.value?.name }}</h1>

      <div class="header-actions">
        <BaseBadge :class="projectQuery.data.value.status">
          {{ STATUS_LABELS[projectQuery.data.value.status] }}
        </BaseBadge>
      </div>
    </header>

    <BasePanel v-if="projectQuery.data.value">
      <AppList
        :width="16"
        :items="[
          {
            title: 'Название компании',
            content: `${projectQuery.data.value.company.name}`,
          },
          {
            title: 'Адрес компании',
            content: `${projectQuery.data.value.company.address}`,
          },
          {
            title: 'Описание компании',
            content: `${projectQuery.data.value.company.description}`,
          },
        ]"
      />
    </BasePanel>

    <BasePanel class="panel" v-if="projectQuery.data.value">
      <GridLayout cols="1fr 1fr 1fr">
        <AppList
          :items="[
            {
              title: 'ФИО заказчика',
              content: projectQuery.data.value.company.customer.full_name,
            },
            {
              title: 'Email заказчика',
              content: projectQuery.data.value.company.customer.email,
            },
            {
              title: 'Телефон заказчика',
              content: projectQuery.data.value.company.customer.phone,
            },
          ]"
        />
        <div class="info">
          <h1>Теги</h1>

          <TagList
            v-if="projectQuery.data.value.tags?.length"
            isVisible
            :tag-ids="projectQuery.data.value.tags"
          />

          <p v-else class="empty-skills">Теги не указаны</p>
        </div>
        <AppList
          :items="[
            {
              title: 'Дата размещения',
              content: projectQuery.data.value.created_at,
            },
            {
              title: 'Количество просмотров',
              content: projectQuery.data.value.views.toString(),
            },
            {
              title: 'Количество откликов',
              content: projectQuery.data.value.applications_count.toString(),
            },
          ]"
        />
      </GridLayout>
    </BasePanel>

    <BasePanel v-if="projectQuery.data.value">
      <AppList
        :width="16"
        :items="[
          {
            title: 'Описание',
            content: `${projectQuery.data.value.description}`,
          },
          {
            title: 'Сроки реализации',
            content: projectQuery.data.value.period,
          },
        ]"
      />
    </BasePanel>

    <BasePanel v-if="projectQuery.data.value.files?.length">
      <h1 class="files-title">Файлы проекта</h1>
      <ProjectFilesList :files="projectQuery.data.value.files!" />
    </BasePanel>
  </template>
</template>

<style lang="scss" scoped>
  .header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    justify-content: space-between;
    margin-top: 1.6875rem;
    margin-bottom: 1.875rem;

    h1 {
      font-size: 2.25rem;
      font-weight: bold;
    }
  }

  .header-actions {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .footer {
    margin-top: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1.25rem;
  }

  .panel {
    margin-bottom: 1rem;
  }

  .files-title {
    font-size: 1.25rem;
    font-weight: bold;
    margin-bottom: 0.75rem;
  }

  .info {
    h1 {
      font-size: 1.125rem;
      margin-bottom: 0.625rem;
    }
    p {
      font-size: 1.125rem;
      font-weight: 700;
    }
  }

  .skills {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
    h1 {
      min-width: 16rem;
      font-weight: 600;
      font-size: 1.125rem;
    }
  }

  .empty-skills {
    font-size: 1rem;
    font-weight: 400;
    color: var(--dark-gray-color);
  }
</style>
