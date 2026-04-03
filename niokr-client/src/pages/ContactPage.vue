<script setup lang="ts">
  import DG from '2gis-maps';
  import { onMounted } from 'vue';

  onMounted(() => {
    const map = DG.map('map', {
      center: [52.262672, 104.262],
      zoom: 16.5,
      dragging: false,
      touchZoom: false,
      scrollWheelZoom: false,
      doubleClickZoom: false,
      boxZoom: false,
      fullscreenControl: false,
    });
    DG.marker([52.262, 104.26254])
      .addTo(map)
      .bindPopup('Кабинет И-114 • Начальник научно-исследовательской части')
      .openPopup();
  });
</script>

<template>
  <header class="header">
    <h1>Контакты</h1>
  </header>
  <div class="row">
    <div class="contact-content">
      <h2>Адрес</h2>
      <p>
        664074, г. Иркутск, ул. Лермонтова, 83 <br />
        ИРНИТУ, Каб. И-114
      </p>
      <div class="contact-content-block">
        <h3>Режим работы</h3>
        <p>
          Пн-Пт с 9:00 до 16:00 <br />
          Перерыв с 12:30 до 13:00
        </p>
      </div>
    </div>
    <div class="contact-content">
      <h2>Контакты</h2>
      <div class="contact-content-block">
        <h3>Научно-исследовательская часть</h3>
        <a class="link" href="tel:+73952405736">
          <svg
            class="icon"
            width="23"
            height="23"
            viewBox="0 0 23 23"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M14.0499 5C15.0267 5.19057 15.9243 5.66826 16.628 6.37194C17.3317 7.07561 17.8094 7.97326 17.9999 8.95M14.0499 1C16.0792 1.22544 17.9715 2.13417 19.4162 3.57701C20.8608 5.01984 21.7719 6.91101 21.9999 8.94M20.9999 16.92V19.92C21.0011 20.1985 20.944 20.4742 20.8324 20.7293C20.7209 20.9845 20.5572 21.2136 20.352 21.4019C20.1468 21.5901 19.9045 21.7335 19.6407 21.8227C19.3769 21.9119 19.0973 21.9451 18.8199 21.92C15.7428 21.5856 12.7869 20.5341 10.1899 18.85C7.77376 17.3147 5.72527 15.2662 4.18993 12.85C2.49991 10.2412 1.44818 7.27099 1.11993 4.18C1.09494 3.90347 1.12781 3.62476 1.21643 3.36162C1.30506 3.09849 1.4475 2.85669 1.6347 2.65162C1.82189 2.44655 2.04974 2.28271 2.30372 2.17052C2.55771 2.05833 2.83227 2.00026 3.10993 2H6.10993C6.59524 1.99522 7.06572 2.16708 7.43369 2.48353C7.80166 2.79999 8.04201 3.23945 8.10993 3.72C8.23656 4.68007 8.47138 5.62273 8.80993 6.53C8.94448 6.88792 8.9736 7.27691 8.89384 7.65088C8.81408 8.02485 8.6288 8.36811 8.35993 8.64L7.08993 9.91C8.51349 12.4135 10.5864 14.4864 13.0899 15.91L14.3599 14.64C14.6318 14.3711 14.9751 14.1858 15.3491 14.1061C15.723 14.0263 16.112 14.0555 16.4699 14.19C17.3772 14.5286 18.3199 14.7634 19.2799 14.89C19.7657 14.9585 20.2093 15.2032 20.5265 15.5775C20.8436 15.9518 21.0121 16.4296 20.9999 16.92Z"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          +7 (3952) 40-50-53
        </a>

        <a class="link" href="mailto:e-project@ex.istu.edu">
          <svg
            class="icon"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M4 4H20C21.1 4 22 4.9 22 6V18C22 19.1 21.1 20 20 20H4C2.9 20 2 19.1 2 18V6C2 4.9 2.9 4 4 4Z"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
            <path
              d="M22 6L12 13L2 6"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          kaloshinia@ex.istu.edu</a
        >
        <h3>Технические вопросы по работе сайта</h3>
        <a class="link" href="tel:+73952405164">
          <svg
            class="icon"
            width="23"
            height="23"
            viewBox="0 0 23 23"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M14.0499 5C15.0267 5.19057 15.9243 5.66826 16.628 6.37194C17.3317 7.07561 17.8094 7.97326 17.9999 8.95M14.0499 1C16.0792 1.22544 17.9715 2.13417 19.4162 3.57701C20.8608 5.01984 21.7719 6.91101 21.9999 8.94M20.9999 16.92V19.92C21.0011 20.1985 20.944 20.4742 20.8324 20.7293C20.7209 20.9845 20.5572 21.2136 20.352 21.4019C20.1468 21.5901 19.9045 21.7335 19.6407 21.8227C19.3769 21.9119 19.0973 21.9451 18.8199 21.92C15.7428 21.5856 12.7869 20.5341 10.1899 18.85C7.77376 17.3147 5.72527 15.2662 4.18993 12.85C2.49991 10.2412 1.44818 7.27099 1.11993 4.18C1.09494 3.90347 1.12781 3.62476 1.21643 3.36162C1.30506 3.09849 1.4475 2.85669 1.6347 2.65162C1.82189 2.44655 2.04974 2.28271 2.30372 2.17052C2.55771 2.05833 2.83227 2.00026 3.10993 2H6.10993C6.59524 1.99522 7.06572 2.16708 7.43369 2.48353C7.80166 2.79999 8.04201 3.23945 8.10993 3.72C8.23656 4.68007 8.47138 5.62273 8.80993 6.53C8.94448 6.88792 8.9736 7.27691 8.89384 7.65088C8.81408 8.02485 8.6288 8.36811 8.35993 8.64L7.08993 9.91C8.51349 12.4135 10.5864 14.4864 13.0899 15.91L14.3599 14.64C14.6318 14.3711 14.9751 14.1858 15.3491 14.1061C15.723 14.0263 16.112 14.0555 16.4699 14.19C17.3772 14.5286 18.3199 14.7634 19.2799 14.89C19.7657 14.9585 20.2093 15.2032 20.5265 15.5775C20.8436 15.9518 21.0121 16.4296 20.9999 16.92Z"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          +7 (3952) 40-51-64</a
        >
        <a class="link" href="mailto:arshinskyv@istu.edu">
          <svg
            class="icon"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M4 4H20C21.1 4 22 4.9 22 6V18C22 19.1 21.1 20 20 20H4C2.9 20 2 19.1 2 18V6C2 4.9 2.9 4 4 4Z"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
            <path
              d="M22 6L12 13L2 6"
              stroke="black"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          arshinskyv@istu.edu</a
        >
      </div>
    </div>
    <div class="contact-content">
      <h2>Персоналии</h2>
      <div class="contact-content-block">
        <h3>Руководитель центра проектного обучения</h3>
        <a
          class="link"
          href="https://www.istu.edu/ob_irnitu/person/chimitov_pavel_evgenevich"
          target="_blank"
        >
          Калошин Игорь Александрович
        </a>
      </div>
      <div class="contact-content-block">
        <h3>Администратор сайта</h3>
        <a
          class="link"
          href="https://www.istu.edu/ob_irnitu/person/arshinskiy_vadim_leonidovich"
          target="_blank"
        >
          Аршинский Вадим Леонидович
        </a>
      </div>
    </div>
  </div>

  <div id="map" class="map"></div>
</template>

<style lang="scss" scoped>
  .header {
    margin-bottom: 0.5rem;

    h1 {
      font-size: 2.5rem;
      font-weight: bold;
    }
  }

  .row {
    display: flex;
    flex-wrap: wrap;
    gap: 2.75rem;

    & > * {
      flex: 1 12.5rem;
    }
  }

  .contact-content {
    width: 100%;
  }

  .icon {
    width: 1.1em;
    min-width: 1.1em;
    height: 1.1em;
  }

  .contact-content h2 {
    margin-bottom: 1.7525rem;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 1.9375rem;
    color: var(--dark-gray-color);
  }

  .contact-content p {
    margin-bottom: 1.0531rem;
    font-size: 1.25rem;
    font-weight: normal;
    line-height: 1.625rem;
    color: var(--text-color);
  }

  .link {
    display: flex;
    gap: 0.75rem;
    align-items: center;
    margin-bottom: 1.0531rem;
    font-size: 1.25rem;
    font-weight: normal;
    line-height: 1.625rem;
    color: var(--text-color);
    text-decoration: none;
  }

  .link:hover {
    text-decoration: underline;
  }

  .contact-content-block {
    display: inline-block;
  }

  .contact-content-block h3 {
    margin-bottom: 12px;
    font-size: 1.25rem;
    font-weight: 600;
    line-height: 1.625rem;
    color: var(--text-color);
  }

  .contact-content-block p {
    margin: 0;
  }

  .map {
    width: 100%;
    height: 60vh;
    min-height: 12.5rem;
    margin-top: 0.5rem;
    background-color: var(--medium-gray-color);
    border-radius: 0.625rem;
  }

  :deep(.dg-popup__container) {
    color: var(--light-color);
  }
</style>
