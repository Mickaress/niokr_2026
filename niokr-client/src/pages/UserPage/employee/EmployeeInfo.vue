<script setup lang="ts">
  import AppList from '@/components/ui/AppList/AppList.vue';
  import GridLayout from '@/components/ui/GridLayout.vue';
  import EmployeeCompetencies from '@/components/user/employee/EmployeeCompetencies.vue';
  import EmployeeTags from '@/components/user/employee/EmployeeTags.vue';
  import { EmployeeType } from '@/models/User';

  const props = defineProps<{
    userInfo: EmployeeType;
  }>();

  const infoItems = [
    {
      title: 'E-Mail',
      content: `${props.userInfo.email}`,
    },
    {
      title: 'Телефон',
      content: `${props.userInfo.phone}`,
    },
  ];
</script>

<template>
  <GridLayout cols="1fr 1fr">
    <div>
      <section class="section">
        <h1>Контактная информация</h1>

        <AppList class="app-list" :width="10" :items="infoItems" />
      </section>
    </div>
    <div>
      <EmployeeTags :tags="userInfo.tags" />

      <EmployeeCompetencies :competencies="userInfo.competencies" />
    </div>
  </GridLayout>
</template>

<style lang="scss" scoped>
  .section {
    margin-bottom: 1.625rem;
    h1 {
      font-size: 1.125rem;
      font-weight: bold;
      margin-bottom: 1.0625rem;
    }
    &:last-child {
      margin-bottom: 0;
    }
  }
  .app-list {
    &:deep(h1) {
      color: var(--dark-gray-color);
    }
  }
</style>
