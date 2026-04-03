<script setup lang="ts">
  import { useGetUserInfoQuery } from '@/api/UserApi/hooks/useGetUserInfoQuery';
  import { useUpdateUserInfo } from '@/api/UserApi/hooks/useUpdateUserInfo';
  import BaseButton from '@/components/ui/BaseButton.vue';
  import BaseInput from '@/components/ui/BaseInput.vue';
  import BasePanel from '@/components/ui/BasePanel.vue';
  import BaseTextarea from '@/components/ui/BaseTextarea.vue';
  import FormSection from '@/components/ui/FormSection.vue';
  import { useCheckRole } from '@/hooks/useCheckRole';
  import { CustomerType, UserFormType, UserRole } from '@/models/User';
  import { RouteNames } from '@/router/types/routeNames';
  import { computed, ref } from 'vue';

  const isCustomer = useCheckRole([UserRole.CUSTOMER]);
  const { mutate: updateUserInfo } = useUpdateUserInfo();
  const userInfo = useGetUserInfoQuery();

  const customerData = computed(() => userInfo.data.value as CustomerType);

  const defaultUserFormValue: UserFormType = {
    full_name: userInfo.data.value?.full_name || '',
    email: userInfo.data.value?.email || '',
    phone: userInfo.data.value?.phone || '',
    company_name: customerData.value?.company?.name || '',
    company_address: customerData.value?.company?.address || '',
    company_description: customerData.value?.company?.description || '',
  };

  const userFormValue = ref<UserFormType>({
    ...defaultUserFormValue,
  });

  const onSubmit = () => {
    const data: UserFormType = {
      full_name: userFormValue.value.full_name,
      email: userFormValue.value.email,
      phone: userFormValue.value.phone,
    };

    if (isCustomer) {
      data.company_name = userFormValue.value.company_name;
      data.company_address = userFormValue.value.company_address;
      data.company_description = userFormValue.value.company_description;
    }

    updateUserInfo(userFormValue.value);
  };
</script>

<template>
  <BasePanel class="panel">
    <FormSection tag="1" title="Основная информация" :divider="isCustomer">
      <div class="block">
        <div>
          <h1 class="header">Название проекта</h1>

          <BaseInput v-model="userFormValue.full_name" placeholder="ФИО" />
        </div>

        <div>
          <h1 class="header">Почта</h1>
          <BaseInput v-model="userFormValue.email" placeholder="Почта" />
        </div>

        <div>
          <h1 class="header">Телефон</h1>
          <BaseInput v-model="userFormValue.phone" placeholder="Телефон" />
        </div>
      </div>
    </FormSection>

    <FormSection v-if="isCustomer" tag="2" title="Компания">
      <div class="block">
        <div>
          <h1 class="header">Название компании</h1>
          <BaseInput v-model="userFormValue.company_name" placeholder="Название компании" />
        </div>

        <div>
          <h1 class="header">Адрес компании</h1>
          <BaseInput v-model="userFormValue.company_address" placeholder="Адрес компании" />
        </div>

        <div>
          <h1 class="header">Описание компании</h1>
          <BaseTextarea
            v-model="userFormValue.company_description"
            placeholder="Например, Компания занимается разработкой интерактивных веб-приложений."
          />
        </div>
      </div>
    </FormSection>
  </BasePanel>
  <div class="buttons">
    <BaseButton
      variant="outlined"
      color="red"
      is="router-link"
      :to="{ name: RouteNames.USER_INFO }"
    >
      Сбросить и выйти
    </BaseButton>

    <BaseButton @click="onSubmit">
      {{ 'Сохранить' }}
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

  .buttons {
    display: flex;
    justify-content: end;
    gap: 1rem;
    margin-top: 2.5rem;
  }
</style>
