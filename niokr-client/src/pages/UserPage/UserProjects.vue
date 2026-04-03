<script setup lang="ts">
  import { useGetUserProjectListQuery } from '@/api/ProjectApi/hooks/useGetUserProjectListQuery';
  import ProjectsList from '@/components/ui/ProjectsList.vue';
  import { useCheckRole } from '@/hooks/useCheckRole';
  import { Status, STATUS_LABELS } from '@/models/Status';
  import { UserRole } from '@/models/User';
  import { computed, onMounted } from 'vue';
  import { RouterLink, useRoute, useRouter } from 'vue-router';

  const projectsQuery = useGetUserProjectListQuery();

  const route = useRoute();
  const router = useRouter();

  const currentStatus = computed(() => String(route.query.status));
  const statusTabs = [Status.Active, Status.Review, Status.Archived];

  const isEmployee = useCheckRole([UserRole.EMPLOYEE]);

  onMounted(() => {
    if (!route.query.status && !isEmployee) {
      router.replace({ ...route, query: { ...route.query, status: Status.Active } });
    }
  });
</script>

<template>
  <div v-if="!isEmployee" class="wrapper">
    <RouterLink
      v-for="tab in statusTabs"
      :key="tab"
      class="tab"
      :class="{ active: currentStatus === tab }"
      :to="{ ...route, query: { status: tab } }"
    >
      {{ STATUS_LABELS[tab] }}
    </RouterLink>
  </div>

  <ProjectsList :projects-query="projectsQuery" />
</template>

<style scoped lang="scss">
  .wrapper {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }

  .tab {
    background-color: white;
    text-transform: uppercase;
    padding: 0.75rem 1rem;
    border: 0.0625rem solid var(--medium-gray-color);
    border-radius: 0.625rem;

    &.active {
      background-color: var(--accent-color);
      color: var(--light-color);
      border: none;
    }
  }
</style>
