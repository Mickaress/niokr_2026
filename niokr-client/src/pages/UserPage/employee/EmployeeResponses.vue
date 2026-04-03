<script setup lang="ts">
  import { useGetAppliedProjectListQuery } from '@/api/ProjectApi/hooks/useGetAppliedProjectListQuery';
  import ProjectsList from '@/components/ui/ProjectsList.vue';
  import { onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';

  const projectsQuery = useGetAppliedProjectListQuery();

  const route = useRoute();
  const router = useRouter();

  onMounted(() => {
    router.replace({ ...route, query: { ...route.query, is_applied: 'true' } });
  });
</script>

<template>
  <ProjectsList :projects-query="projectsQuery" />
</template>
