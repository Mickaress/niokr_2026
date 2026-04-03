<script setup lang="ts">
  import { computed, watch } from 'vue';
  import { useRoute, useRouter } from 'vue-router';

  const props = defineProps<{
    totalItems: number;
    pageSize: number;
  }>();

  const route = useRoute();
  const router = useRouter();

  const currentPage = computed(() => Number(route.query.page) || 1);

  const pagesVisible = 7;

  const totalPages = computed(() => Math.ceil(props.totalItems / props.pageSize));

  // генерирует видимые ссылки пагинации
  const pages = computed(() => {
    const pages = [1];
    let startPage = 1;
    let endPage = 1;

    const half = Math.floor((pagesVisible - 2) / 2);

    if (currentPage.value <= Math.ceil(pagesVisible / 2)) {
      startPage = 2;
      endPage = pagesVisible - 1;
    } else if (totalPages.value - currentPage.value < Math.ceil(pagesVisible / 2)) {
      startPage = totalPages.value - pagesVisible + 2;
      endPage = totalPages.value;
    } else {
      startPage = currentPage.value - half;
      endPage = currentPage.value + half;
    }

    if (startPage < 2) {
      startPage = 2;
    }

    if (endPage > totalPages.value) {
      endPage = totalPages.value;
    }

    for (let i = startPage; i <= endPage; i++) {
      pages.push(i);
    }

    if (endPage < totalPages.value) {
      pages.push(totalPages.value);
    }

    return pages;
  });

  function setPage(page: number) {
    router.replace({
      ...route,
      query: {
        ...route.query,
        page: page,
      },
    });
  }

  watch(
    () => props.totalItems,
    () => {
      if (currentPage.value > totalPages.value) {
        setPage(currentPage.value - 1);
      }
    },
    { immediate: true },
  );
</script>

<template>
  <nav class="pagination">
    <ul class="pagination-list">
      <li :class="['pagination-item', { 'disabled-item': currentPage <= 1 }]">
        <button
          :disabled="currentPage <= 1"
          :class="['pagination-btn', 'pagination-arrow']"
          @click="setPage(currentPage - 1)"
        >
          &lt;
        </button>
      </li>
      <li
        v-for="pageLink in pages"
        :key="pageLink"
        :class="['pagination-item', { active: pageLink === currentPage }]"
      >
        <button
          :disabled="pageLink === currentPage"
          class="pagination-btn"
          @click="setPage(pageLink)"
        >
          {{ pageLink }}
        </button>
      </li>
      <li :class="['pagination-item', { 'disabled-item': currentPage >= totalPages }]">
        <button
          :disabled="currentPage >= totalPages"
          :class="['pagination-btn', 'pagination-arrow']"
          @click="setPage(currentPage + 1)"
        >
          &gt;
        </button>
      </li>
    </ul>
  </nav>
</template>

<style lang="scss" scoped>
  .pagination {
    margin: 1rem 0;
    background: var(--light-color);
    border-radius: 0.625rem;
    box-shadow: 0 0 0.3125rem rgb(0 0 0 / 18%);
  }

  .pagination-list {
    display: flex;
    gap: 2.25rem;
    justify-content: center;
  }

  .pagination-item {
    width: 2.5625rem;
    height: 3.3125rem;
  }

  .disabled-item {
    pointer-events: none;
    opacity: 0.4;
  }

  .pagination-btn {
    display: inline-block;
    width: 100%;
    height: 100%;
    font-size: 1.25rem;
    color: var(--dark-gray-color);
    cursor: pointer;
    border-bottom: 0.25rem solid transparent;
  }

  .pagination-btn:hover,
  .pagination-item.active .pagination-btn {
    border-bottom-color: var(--orange-color);
  }

  .pagination-arrow:hover {
    color: var(--orange-color);
    border-bottom-color: transparent;
  }
</style>
