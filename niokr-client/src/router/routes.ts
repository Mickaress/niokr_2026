import ContactPage from '@/pages/ContactPage.vue';
import CreateProjectPage from '@/pages/CreateProjectPage.vue';
import FaqPage from '@/pages/FaqPage.vue';
import NotFoundPage from '@/pages/NotFoundPage.vue';
import ProjectsPage from '@/pages/ProjectsPage.vue';
import UserInfo from '@/pages/UserPage/UserInfo.vue';
import UserPage from '@/pages/UserPage/UserPage.vue';
import type { RouteRecordRaw } from 'vue-router';
import { RouteNames } from './types/routeNames';
import LoginPage from '@/pages/LoginPage.vue';
import { UserRole } from '@/models/User';
import EmployeeResponses from '@/pages/UserPage/employee/EmployeeResponses.vue';
import { NavType } from './types/navTypes';
import ProjectPage from '@/pages/ProjectPage.vue';
import UserProjects from '@/pages/UserPage/UserProjects.vue';
import TagsPage from '@/pages/UserPage/admin/TagsPage.vue';
import EditUserPage from '@/pages/UserPage/EditUserPage.vue';

export const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: LoginPage,
    name: RouteNames.LOGIN,
    meta: {
      requiresGuest: true,
    },
  },
  {
    path: '/projects',
    component: ProjectsPage,
    name: RouteNames.ACTIVE_PROJECTS,
    meta: {
      title: 'Проекты',
      roles: [UserRole.EMPLOYEE],
      type: NavType.MAIN_NAV,
      order: 0,
    },
  },
  {
    path: '/faq',
    component: FaqPage,
    name: RouteNames.FAQ,
    meta: {
      title: 'Вопрос-ответ',
      type: NavType.MAIN_NAV,
      roles: [UserRole.EMPLOYEE, UserRole.CUSTOMER, UserRole.ADMIN],
      order: 1,
    },
  },
  {
    path: '/contacts',
    component: ContactPage,
    name: RouteNames.CONTACTS,
    meta: {
      title: 'Контакты',
      type: NavType.MAIN_NAV,
      roles: [UserRole.EMPLOYEE, UserRole.CUSTOMER, UserRole.ADMIN],
      order: 2,
    },
  },
  {
    path: '/project/:id',
    component: ProjectPage,
    name: RouteNames.PROJECT_DETAILS,
    meta: {
      roles: [UserRole.EMPLOYEE, UserRole.CUSTOMER, UserRole.ADMIN],
    },
  },
  {
    path: '/project/create',
    name: RouteNames.CUSTOMER_PROJECT_CREATE,
    component: CreateProjectPage,
    meta: {
      roles: [UserRole.CUSTOMER],
    },
  },
  {
    path: '/project/:id/edit',
    name: RouteNames.ADD_EDIT_PROJECT,
    component: CreateProjectPage,
    meta: {
      roles: [UserRole.CUSTOMER, UserRole.ADMIN],
    },
  },
  {
    path: '/profile/edit',
    name: RouteNames.USER_EDIT_INFO,
    component: EditUserPage,
    meta: {
      roles: [UserRole.EMPLOYEE, UserRole.CUSTOMER, UserRole.ADMIN],
    },
  },
  {
    path: '/profile',
    component: UserPage,
    name: RouteNames.USER_PAGE,
    redirect: { name: RouteNames.USER_INFO },
    children: [
      {
        path: 'info',
        name: RouteNames.USER_INFO,
        component: UserInfo,
        meta: {
          title: 'Мой профиль',
          roles: [UserRole.EMPLOYEE, UserRole.CUSTOMER, UserRole.ADMIN],
          type: NavType.USER_NAV,
          order: 0,
        },
      },
      {
        path: 'applications',
        name: RouteNames.EMPLOYEE_APPLICATIONS,
        component: EmployeeResponses,
        meta: {
          title: 'Мои отклики',
          type: NavType.USER_NAV,
          order: 1,
          roles: [UserRole.EMPLOYEE],
        },
      },
      {
        path: 'projects',
        name: RouteNames.USER_PROJECTS,
        component: UserProjects,
        meta: {
          title: 'Проекты',
          type: NavType.USER_NAV,
          order: 3,
          roles: [UserRole.CUSTOMER, UserRole.EMPLOYEE, UserRole.ADMIN],
        },
      },
      {
        path: 'tags',
        name: RouteNames.ADMIN_TAGS,
        component: TagsPage,
        meta: {
          title: 'Теги',
          roles: [UserRole.ADMIN],
          type: NavType.USER_NAV,
          order: 4,
        },
      },
    ],
  },
  {
    path: '/:pathMatch(.*)*',
    component: NotFoundPage,
    name: RouteNames.NOT_FOUND,
    meta: {
      roles: [UserRole.EMPLOYEE, UserRole.CUSTOMER, UserRole.ADMIN],
    },
  },
];
