<script setup lang="ts">
  import { useApplyMutation } from '@/api/EmployeeApi/hooks/useApplyMutation';
  import { useWithdrawMutation } from '@/api/EmployeeApi/hooks/useWithdrawMutation';
  import { useUpdateProjectMutation } from '@/api/ProjectApi/hooks/useUpdateProjectMutation';
  import BaseButton from '@/components/ui/BaseButton.vue';
  import BaseCard from '@/components/ui/BaseCard.vue';
  import BaseList from '@/components/ui/BaseList.vue';
  import TagList from '@/components/ui/TagList.vue';
  import ConfirmModal from '@/components/ui/modal/ConfirmModal.vue';
  import { useCheckRole } from '@/hooks/useCheckRole';
  import { ListDTO, ProjectType } from '@/models/Project';
  import { Status } from '@/models/Status';
  import { UserRole } from '@/models/User';
  import { RouteNames } from '@/router/types/routeNames';
  import { UseQueryReturnType } from '@tanstack/vue-query';
  import { ref, watch } from 'vue';
  import VMultiselect from '@vueform/multiselect';
  import { useGetProjectApplicantsQuery } from '@/api/ProjectApi/hooks/useGetProjectApplicantsQuery';

  defineProps<{
    projectsQuery: UseQueryReturnType<ListDTO<ProjectType>, unknown>;
  }>();

  const { mutate: closeProject } = useUpdateProjectMutation();
  const { mutate: apply } = useApplyMutation();
  const { mutate: withdraw } = useWithdrawMutation();
  const isCustomer = useCheckRole([UserRole.CUSTOMER]);
  const isAdmin = useCheckRole([UserRole.ADMIN]);
  const isEmployee = useCheckRole([UserRole.EMPLOYEE]);

  const deletableProjectId = ref<number>(0);
  const isShowDeleteModal = ref<boolean>(false);
  const selectedEmployeeId = ref<number | null>(null);
  const applicantsQuery = useGetProjectApplicantsQuery(
    deletableProjectId,
    isShowDeleteModal,
    isAdmin,
  );

  const projectRoute = (id: number) => {
    return { name: RouteNames.PROJECT_DETAILS, params: { id } };
  };

  const onCloseProject = (projectId: number) => {
    deletableProjectId.value = projectId;
    isShowDeleteModal.value = true;
  };

  watch(isShowDeleteModal, (isOpen) => {
    if (!isOpen) {
      deletableProjectId.value = 0;
      selectedEmployeeId.value = null;
    }
  });
</script>

<template>
  <ConfirmModal
    v-model:is-show="isShowDeleteModal"
    question="Вы уверены, что хотите закрыть этот проект?"
    :agree-action="
      () =>
        closeProject({
          id: deletableProjectId,
          data: { status: Status.Archived, employee_id: selectedEmployeeId },
        })
    "
    agree-answer="Закрыть"
    disagree-answer="Отмена"
  >
    <template #content v-if="applicantsQuery.data.value">
      <VMultiselect
        class="applicant-select"
        v-model="selectedEmployeeId"
        mode="single"
        placeholder="Выберите пользователя"
        no-results-text="Пользователь не найден"
        no-options-text="Пользователи не найдены"
        :close-on-select="true"
        :searchable="true"
        :options="applicantsQuery.data.value"
        :disabled="applicantsQuery.isFetching.value"
        :loading="applicantsQuery.isFetching.value"
        label="full_name"
        track-by="id"
        value-prop="id"
      />
    </template>
  </ConfirmModal>

  <BaseList
    :is-loading="projectsQuery.isLoading.value"
    :is-mini="false"
    :is-error="projectsQuery.isError.value"
    empty-title="У вас нет проектов"
    empty-subtitle="Пока у вас нет ни одного проекта"
    :total-items="projectsQuery.data.value?.count || 0"
  >
    <template #list>
      <li v-for="project in projectsQuery.data.value?.results" :key="project.id">
        <BaseCard
          :title="project.name"
          :link="projectRoute(project.id)"
          :status="project.status"
          is-divide
        >
          <template #header>
            <p>{{ project.company.name }}</p>
          </template>

          <template #main>
            <p>
              Описание:
              <span>{{ project.description }}</span>
            </p>

            <p>
              Сроки реализации:
              <span> {{ project.period }} </span>
            </p>

            <p>
              Дата размещения:
              <span> {{ project.created_at }} </span>
            </p>
          </template>

          <template #footer>
            <TagList :tagIds="project.tags" />
          </template>

          <template #buttons>
            <template v-if="isEmployee && project.status === Status.Active">
              <BaseButton
                v-if="project.is_applied"
                color="red"
                variant="outlined"
                @click="withdraw(project.id)"
              >
                Отменить отклик
              </BaseButton>

              <BaseButton v-else variant="outlined" @click="apply(project.id)">
                Откликнуться
              </BaseButton>
            </template>

            <BaseButton
              v-if="
                [Status.Active, Status.Review].includes(project.status) && (isCustomer || isAdmin)
              "
              color="red"
              variant="outlined"
              @click="onCloseProject(project.id)"
            >
              Закрыть
            </BaseButton>

            <BaseButton
              v-if="isAdmin && project.status === Status.Review"
              variant="outlined"
              is="router-link"
              :to="{ name: RouteNames.ADD_EDIT_PROJECT, params: { id: project.id } }"
            >
              Рассмотреть
            </BaseButton>

            <BaseButton is="router-link" :to="projectRoute(project.id)"> Подробнее </BaseButton>
          </template>
        </BaseCard>
      </li>
    </template>
  </BaseList>
</template>

<style scoped lang="scss">
  .applicant-select {
    margin-bottom: 2rem;
  }
</style>
