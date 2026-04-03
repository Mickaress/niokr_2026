<script setup lang="ts">
  import { useGetUserInfoQuery } from '@/api/UserApi/hooks/useGetUserInfoQuery';
  import BaseButton from '@/components/ui/BaseButton.vue';
  import BasePanel from '@/components/ui/BasePanel.vue';
  import { AdminType, CustomerType, EmployeeType, UserRole } from '@/models/User';
  import AdminInfo from './admin/AdminInfo.vue';
  import CustomerInfo from './customer/CustomerInfo.vue';
  import EmployeeInfo from './employee/EmployeeInfo.vue';
  import { computed } from 'vue';
  import { RouteNames } from '@/router/types/routeNames';

  const { data: userData } = useGetUserInfoQuery();

  const customerData = computed(() => userData.value as CustomerType);
  const employeeData = computed(() => userData.value as EmployeeType);
  const adminData = computed(() => userData.value as AdminType);

  const isCustomer = computed(() => userData.value?.role === UserRole.CUSTOMER);
  const isEmployee = computed(() => userData.value?.role === UserRole.EMPLOYEE);
  const isAdmin = computed(() => userData.value?.role === UserRole.ADMIN);
</script>

<template>
  <BasePanel class="info">
    <h1 class="fio">{{ userData?.full_name }}</h1>

    <CustomerInfo v-if="isCustomer" :user-info="customerData" />

    <EmployeeInfo v-if="isEmployee" :user-info="employeeData" />

    <AdminInfo v-if="isAdmin" :user-info="adminData" />

    <BaseButton variant="outlined" is="router-link" :to="{ name: RouteNames.USER_EDIT_INFO }">
      Редактировать профиль
    </BaseButton>
  </BasePanel>
</template>

<style lang="scss" scoped>
  .info {
    display: flex;
    flex-direction: column;
    h1 {
      font-size: 1.875rem;
      font-weight: bold;
      margin-bottom: 1.5rem;
      padding-bottom: 1.5rem;
      white-space: pre-wrap;
    }
    a {
      align-self: flex-end;
      margin-top: 1.5rem;
    }
  }
</style>
