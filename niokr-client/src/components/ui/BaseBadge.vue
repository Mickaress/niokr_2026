<template>
  <div class="badge">
    <slot></slot>
  </div>
</template>

<style scoped>
  .badge {
    padding: 0.5rem;
    text-align: center;
    font-size: 0.875rem;
    justify-self: end;
    font-weight: bold;
    text-transform: uppercase;
    border-radius: 6.25rem;
    white-space: nowrap;

    &.active {
      color: var(--green-color);
      border: 2px solid var(--green-color);
    }

    &.archived {
      color: var(--dark-gray-color);
      border: 2px solid var(--dark-gray-color);
    }

    &.review {
      color: var(--accent-color);
      border: 2px solid var(--accent-color);
    }
  }
</style>
