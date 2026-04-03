<script setup lang="ts">
  import { useMainNavigationRoutes } from '@/hooks/useRoutes';
  import AppLogo from '../ui/AppLogo.vue';
  import BaseContainer from '../ui/BaseContainer.vue';

  const mainRoutes = useMainNavigationRoutes();

  const adminContacts = [
    {
      name: 'Телефон:',
      content: '+7 (3952) 40-51-64',
      href: 'tel:+73952405164',
    },
    {
      name: 'E-MAIL:',
      content: 'ARSHINSKYV@ISTU.EDU',
      href: 'mailto:arshinskyv@istu.edu',
    },
  ];

  const mainContacts = [
    {
      name: 'Телефон:',
      content: '+7 (3952) 405-000',
      href: 'tel:+73952405164',
    },
    {
      name: 'СПРАВОЧНАЯ:',
      content: '+7 (3952) 405-009',
      href: 'tel:+73952405009',
    },
    {
      name: 'E-MAIL:',
      content: 'INFO@ISTU.EDU',
      href: 'mailto:info@istu.edu',
    },
  ];
</script>

<template>
  <footer class="footer">
    <BaseContainer class="footer__container">
      <div>
        <AppLogo is-footer />

        <a class="footer__initials" href="https://www.istu.edu/" target="_blank">
          Федеральное Государственное Бюджетное Образовательное Учреждение высшего образования
          <br />
          <span> "Иркутский Национальный Исследовательский Технический Университет" </span>
        </a>
      </div>

      <nav>
        <ul class="footer__nav-list">
          <li v-for="link in mainRoutes" :key="link.name">
            <RouterLink :to="{ name: link.name }">
              {{ link.meta.title }}
            </RouterLink>
          </li>
        </ul>
      </nav>

      <div class="footer__divider"></div>

      <section>
        <h1 class="footer__info-title">Техническая поддержка:</h1>
        <ul class="footer__info-list">
          <li v-for="contact in adminContacts" :key="contact.name" class="footer__info-list-item">
            <p>{{ contact.name }}</p>
            <a :href="contact.href" target="_blank">{{ contact.content }}</a>
          </li>
        </ul>
      </section>

      <section>
        <h1 class="footer__info-title">Контакты организации:</h1>
        <ul class="footer__info-list">
          <li class="footer__info-list-item"><p>664074, г. Иркутск ул. Лермонтова 83</p></li>
          <li v-for="contact in mainContacts" :key="contact.name" class="footer__info-list-item">
            <p>{{ contact.name }}</p>
            <a :href="contact.href" target="_blank">{{ contact.content }}</a>
          </li>
        </ul>
      </section>
    </BaseContainer>
  </footer>
</template>

<style lang="scss" scoped>
  .footer {
    padding: 3.5rem 0 2.25rem;
    margin-top: 8.75rem;
    background-color: var(--dark-color);

    &__container {
      display: grid;
      grid-template-columns: 1fr repeat(4, auto);
      column-gap: 4.375rem;
      max-width: 112.5rem;
    }

    &__initials {
      display: block;
      max-width: 30em;
      margin-top: 7em;
      color: var(--light-color);
      font-size: 0.875rem;
      line-height: 1.5;
      font-weight: normal;

      &:hover {
        text-decoration: underline;
      }
      span {
        font-weight: bold;
        color: var(--light-color);
        font-size: 0.875rem;
        line-height: 1.5;
      }
    }

    &__nav-list {
      display: flex;
      flex-direction: column;
      align-items: start;
      gap: 1.25rem;
      a {
        color: var(--light-color);
        &:hover {
          text-decoration: underline;
        }
      }
    }

    &__divider {
      width: 1px;
      height: 100%;
      background-color: var(--light-color);
    }

    &__info-title {
      color: #fff;
      margin-bottom: 1.25rem;
    }

    &__info-list {
      display: flex;
      flex-direction: column;
      gap: 0.625rem;
    }

    &__info-list-item {
      display: flex;
      gap: 0.25rem;
      p {
        font-size: 0.875rem;
        font-weight: normal;
        white-space: nowrap;
        color: var(--dark-gray-color);
        text-transform: uppercase;
      }
      a {
        color: var(--dark-gray-color);
        font-size: 0.875rem;
        &:hover {
          text-decoration: underline;
        }
      }
    }
  }
</style>
