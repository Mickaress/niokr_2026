<template>
  <header class="sidebar-layout__header">
    <slot name="header"></slot>
  </header>
  <div class="sidebar-layout__wrapper">
    <aside class="sidebar-layout__wrapper-aside">
      <slot name="sidebar"></slot>
    </aside>
    <main>
      <slot name="main"></slot>
    </main>
  </div>
</template>

<style lang="scss">
  .sidebar-layout {
    &__header {
      margin-bottom: 1rem;
      h1 {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
      }
      h2 {
        font-size: 1.125rem;
        font-weight: normal;
        margin-bottom: 2rem;
      }
      input {
        max-width: 43.375rem;
      }
    }

    &__wrapper {
      display: grid;
      grid-template-columns: 23.75rem auto;
      gap: 2.125rem;
    }
  }
</style>
