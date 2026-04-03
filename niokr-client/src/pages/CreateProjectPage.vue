<script setup lang="ts">
  import BaseButton from '@/components/ui/BaseButton.vue';
  import BasePanel from '@/components/ui/BasePanel.vue';
  import BaseTextarea from '@/components/ui/BaseTextarea.vue';
  import FormSection from '@/components/ui/FormSection.vue';
  import { ProjectFileType, ProjectFormType } from '@/models/Project';
  import { RouteNames } from '@/router/types/routeNames';
  import { computed, onMounted, ref } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { toast } from 'vue3-toastify';
  import TagList from '@/components/ui/TagList.vue';
  import { UserRole } from '@/models/User';
  import { useCheckRole } from '@/hooks/useCheckRole';
  import TagsModal from '@/components/ui/modal/editTagsModal/TagsModal.vue';
  import { useCreateProjectMutation } from '@/api/CustomerApi/hooks/useCreateProjectMutation';
  import ProjectFilesList from '@/components/ui/ProjectFilesList.vue';
  import { useUpdateProjectMutation } from '@/api/ProjectApi/hooks/useUpdateProjectMutation';
  import { projectApi } from '@/api/ProjectApi';
  import { ProjectType } from '@/models/Project';
  import { Status } from '@/models/Status';

  const defaultProjectFormValue: ProjectFormType = {
    name: '',
    description: '',
    dateStart: undefined,
    dateEnd: undefined,
    tagIds: [],
    files: [],
  };

  const projectFormValue = ref<ProjectFormType>({
    ...defaultProjectFormValue,
  });

  const { mutate: createProject } = useCreateProjectMutation();
  const { mutate: updateProject } = useUpdateProjectMutation();
  const route = useRoute();
  const router = useRouter();

  const projectId = computed(() => Number(route.params.id));
  const isEditMode = computed(() => Number.isFinite(projectId.value) && projectId.value > 0);
  const isProjectLoading = ref(false);

  const isAdmin = useCheckRole([UserRole.ADMIN]);

  const isShowModal = ref(false);

  const fileInputRef = ref<HTMLInputElement | null>(null);
  const isDragOver = ref(false);
  const existingFiles = ref<ProjectFileType[]>([]);
  const displayFiles = computed(() => [
    ...existingFiles.value,
    ...(projectFormValue.value.files ?? []),
  ]);

  function addFiles(newFiles: File[]) {
    console.log(newFiles);
    projectFormValue.value.files = [...(projectFormValue.value.files ?? []), ...newFiles];
  }

  function onFileChange(event: Event) {
    const input = event.target as HTMLInputElement;
    if (!input.files) return;
    addFiles(Array.from(input.files));
    input.value = '';
  }

  function onDrop(event: DragEvent) {
    isDragOver.value = false;
    const files = event.dataTransfer?.files;
    if (files) addFiles(Array.from(files));
  }

  function removeFile(index: number) {
    if (index < existingFiles.value.length) {
      existingFiles.value = existingFiles.value.filter((_, i) => i !== index);
      return;
    }

    const newFileIndex = index - existingFiles.value.length;
    projectFormValue.value.files = projectFormValue.value.files?.filter(
      (_, i) => i !== newFileIndex,
    );
  }

  function toInputDate(value?: string) {
    if (!value) return undefined;

    const isoMatch = value.match(/^(\d{4})-(\d{2})-(\d{2})/);
    if (isoMatch) return `${isoMatch[1]}-${isoMatch[2]}-${isoMatch[3]}`;

    const rusMatch = value.match(/^(\d{2})\.(\d{2})\.(\d{4})$/);
    if (rusMatch) return `${rusMatch[3]}-${rusMatch[2]}-${rusMatch[1]}`;

    return undefined;
  }

  type ProjectWithOptionalDates = ProjectType & {
    dateStart?: string;
    dateEnd?: string;
  };

  function getDatesFromProject(project: ProjectWithOptionalDates) {
    const dateStart = toInputDate(project.dateStart);
    const dateEnd = toInputDate(project.dateEnd);

    if (dateStart || dateEnd) return { dateStart, dateEnd };

    const period = typeof project.period === 'string' ? project.period : '';
    const dateMatches = period.match(/\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2}/g);

    return {
      dateStart: toInputDate(dateMatches?.[0]),
      dateEnd: toInputDate(dateMatches?.[1]),
    };
  }

  onMounted(async () => {
    if (!isEditMode.value) return;

    isProjectLoading.value = true;
    try {
      const project = (await projectApi.getSingleProject(
        projectId.value,
      )) as ProjectWithOptionalDates;
      const { dateStart, dateEnd } = getDatesFromProject(project);

      projectFormValue.value = {
        ...projectFormValue.value,
        name: project.name,
        description: project.description,
        dateStart,
        dateEnd,
        tagIds: project.tags,
      };
      existingFiles.value = project.files ?? [];
    } catch {
      toast.error('Не удалось загрузить проект');
    } finally {
      isProjectLoading.value = false;
    }
  });

  const onSubmit = () => {
    if (!projectFormValue.value.name) {
      toast.warning('Заполните название проекта');
      return;
    }

    if (!projectFormValue.value.description) {
      toast.warning('Заполните описание проекта');
      return;
    }

    if (isEditMode.value) {
      updateProject(
        {
          id: projectId.value,
          data: {
            ...projectFormValue.value,
            status: Status.Active,
          },
        },
        {
          onSuccess: () => {
            router.replace({
              name: RouteNames.USER_PROJECTS,
            });
          },
        },
      );
      return;
    }

    createProject(projectFormValue.value);
  };
</script>

<template>
  <TagsModal
    :tag-ids="projectFormValue.tagIds"
    v-model:isShow="isShowModal"
    :save-function="(tagIds) => (projectFormValue.tagIds = tagIds)"
  />

  <BasePanel v-if="!isProjectLoading" class="panel">
    <FormSection tag="1" title="Основная информация" divider>
      <div class="block">
        <div>
          <h1 class="header">Название проекта</h1>
          <BaseTextarea
            v-model="projectFormValue.name"
            placeholder="Например, Разработка интерактивных веб-приложений"
          />
        </div>

        <div>
          <h1 class="header">Описание проекта</h1>
          <BaseTextarea
            v-model="projectFormValue.description"
            placeholder="Например, В этом проекте вы будете заниматься разработкой интерактивных веб-приложений. Это отличная возможность применить свои навыки веб-разработки и создать увлекательные веб-приложения."
          />
        </div>

        <div>
          <h1 class="header">Сроки реализации</h1>

          <div class="date">
            <input v-model="projectFormValue.dateStart" type="date" />

            <span>—</span>

            <input v-model="projectFormValue.dateEnd" type="date" />
          </div>
        </div>
      </div>
    </FormSection>

    <FormSection tag="2" title="Файлы проекта" :divider="isAdmin">
      <div class="block">
        <div>
          <h1 class="header">Прикреплённые файлы</h1>
          <input
            ref="fileInputRef"
            type="file"
            multiple
            class="file-input"
            @change="onFileChange"
          />

          <div
            class="drop-zone"
            :class="{ 'drop-zone--active': isDragOver }"
            @click="fileInputRef?.click()"
            @dragover.prevent="isDragOver = true"
            @dragleave.prevent="isDragOver = false"
            @drop.prevent="onDrop"
          >
            <span class="drop-zone__icon">📎</span>
            <span>Перетащите файлы сюда или выберите вручную</span>
          </div>

          <ProjectFilesList
            v-if="displayFiles.length"
            :files="displayFiles"
            removable
            @remove="removeFile"
          />
        </div>
      </div>
    </FormSection>

    <FormSection v-if="isAdmin" tag="3" title="Теги">
      <div class="block">
        <div>
          <h1 class="header">Теги</h1>
        </div>

        <div class="wrapper">
          <TagList :tagIds="projectFormValue.tagIds" />

          <BaseButton variant="text" @click="isShowModal = true"> Редактировать теги + </BaseButton>
        </div>
      </div>
    </FormSection>
  </BasePanel>
  <div class="buttons">
    <BaseButton
      variant="outlined"
      color="red"
      is="router-link"
      :to="{ name: RouteNames.USER_PROJECTS }"
    >
      Сбросить и выйти
    </BaseButton>

    <BaseButton @click="onSubmit">
      {{ isEditMode ? 'Разместить проект' : 'Создать проект' }}
    </BaseButton>
  </div>
</template>

<style lang="scss" scoped>
  .panel {
    margin-top: 3.625rem;
  }

  .block {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
  }

  .header {
    font-weight: bold;
    font-size: 1.125rem;
    line-height: 2.375rem;
  }

  .date {
    display: flex;
    gap: 0.5rem;
    align-items: center;
    input {
      font-size: 1.125rem;
      border: 1px solid var(--medium-gray-color);
      border-radius: 0.3125rem;
      padding: 0.75rem;
      outline: none;
      &:focus {
        border-color: var(--accent-color);
      }
    }
  }
  .buttons {
    display: flex;
    justify-content: end;
    gap: 1rem;
    margin-top: 2.5rem;
  }
  .file-input {
    display: none;
  }
  .drop-zone {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 1.5rem;
    margin-bottom: 0.75rem;
    border: 2px dashed var(--medium-gray-color);
    border-radius: 0.5rem;
    cursor: pointer;
    color: var(--dark-gray-color);
    font-size: 0.9375rem;
    transition:
      border-color 0.2s,
      background-color 0.2s;
    &:hover {
      border-color: var(--accent-color);
      background-color: #f1f4fe;
    }
    &--active {
      border-color: var(--accent-color);
      background-color: #f1f4fe;
    }
  }
  .drop-zone__icon {
    font-size: 1.25rem;
  }
  .wrapper {
    display: flex;
    gap: 0.5rem;
  }
</style>
