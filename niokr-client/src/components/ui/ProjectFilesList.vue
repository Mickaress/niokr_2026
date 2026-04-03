<script setup lang="ts">
  import type { ProjectFileType } from '@/models/Project';

  type AnyProjectFile = File | ProjectFileType;

  defineProps<{
    files: AnyProjectFile[];
    removable?: boolean;
  }>();

  const emit = defineEmits<{
    (event: 'remove', index: number): void;
  }>();

  const VIEWABLE_TYPES = new Set([
    'application/pdf',
    'image/png',
    'image/jpeg',
    'image/gif',
    'image/webp',
    'image/svg+xml',
    'video/mp4',
    'video/webm',
    'audio/mpeg',
    'audio/wav',
    'audio/ogg',
    'text/plain',
    'text/html',
    'text/xml',
    'application/json',
  ]);

  function isLocalFile(file: AnyProjectFile): file is File {
    return file instanceof File;
  }

  function buildServerUrl(filePath: string) {
    if (!filePath) return '';

    const baseFileUrl = import.meta.env.VITE_FILE_URL;
    return `${baseFileUrl}${filePath}`;
  }

  function getDisplayName(file: AnyProjectFile) {
    if (isLocalFile(file)) return file.name;

    if (file.original_filename) return file.original_filename;
    if (file.file) {
      const parts = file.file.split('/');
      return parts[parts.length - 1] || file.file;
    }

    return `file-${file.id}`;
  }

  function openLocalFile(file: File) {
    const url = URL.createObjectURL(file);

    if (VIEWABLE_TYPES.has(file.type)) {
      window.open(url, '_blank');
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      return;
    }

    const a = document.createElement('a');
    a.href = url;
    a.download = file.name;
    a.click();
    URL.revokeObjectURL(url);
  }

  function openFile(file: AnyProjectFile) {
    if (isLocalFile(file)) {
      openLocalFile(file);
      return;
    }

    const url = buildServerUrl(file.file);
    if (url) window.open(url, '_blank');
  }

  function removeAt(index: number) {
    emit('remove', index);
  }
</script>

<template>
  <ul class="file-list">
    <li
      v-for="(file, index) in files"
      :key="isLocalFile(file) ? file.name : file.id"
      class="file-list-item"
    >
      <button class="file-list-item-content" type="button" @click.stop="openFile(file)">
        <img src="@/assets/icons/file.svg" alt="" />

        <p class="file-list-item-content-label" :data-tooltip="getDisplayName(file)">
          <span>{{ getDisplayName(file) }}</span>
        </p>
      </button>

      <button v-if="removable" class="file-remove" type="button" @click.stop="removeAt(index)">
        ✕
      </button>
    </li>
  </ul>
</template>

<style scoped lang="scss">
  .file-list {
    display: flex;
    flex-direction: row;
    gap: 0.375rem;

    &-item {
      position: relative;
      width: 10rem;
      height: 10rem;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid var(--medium-gray-color);
      border-radius: 0.625rem;

      &:hover {
        border-color: var(--accent-color);
      }

      &-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        flex: 1;
        background: none;
        border: none;
        padding: 0;
        cursor: pointer;

        &-label {
          position: relative;
          max-width: 8rem;
          font-size: 0.9375rem;
          text-align: center;

          span {
            display: block;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
          }

          &::after {
            content: attr(data-tooltip);
            position: absolute;
            left: 50%;
            top: calc(100% + 0.375rem);
            transform: translateX(-50%);
            max-width: 16rem;
            padding: 0.25rem 0.5rem;
            border-radius: 0.375rem;
            background-color: rgb(17 24 39 / 94%);
            color: #fff;
            font-size: 0.75rem;
            line-height: 1.2;
            white-space: normal;
            text-align: left;
            pointer-events: none;
            opacity: 0;
            visibility: hidden;
            transition:
              opacity 0.12s ease,
              visibility 0.12s ease;
            z-index: 2;
          }

          &:hover::after,
          &:focus-visible::after {
            opacity: 1;
            visibility: visible;
          }
        }
      }
    }
  }

  .file-name {
    flex: 1;
    min-width: 0;
    font-size: 0.9375rem;
  }

  .file-open {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: none;
    border: none;
    cursor: pointer;
    color: var(--accent-color);
    text-align: left;
    padding: 0;
    text-decoration: none;
    transition: opacity 0.2s ease;

    &:focus-visible {
      outline: 2px solid var(--accent-color);
      outline-offset: 2px;
      border-radius: 0.375rem;
    }

    &:hover {
      opacity: 0.8;
      text-decoration: underline;
      text-underline-offset: 2px;
    }
  }

  .file-remove {
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 1.625rem;
    height: 1.625rem;
    background-color: transparent;
    border: 1px solid transparent;
    cursor: pointer;
    color: var(--dark-gray-color);
    font-size: 1rem;
    padding: 0;
    border-radius: 0.5rem;
    line-height: 1;
    transition:
      color 0.2s ease,
      background-color 0.2s ease,
      border-color 0.2s ease;

    &:hover {
      color: #dc2626;
      background-color: rgb(220 38 38 / 10%);
      border-color: rgb(220 38 38 / 18%);
    }

    &:focus-visible {
      outline: 2px solid #dc2626;
      outline-offset: 1px;
    }
  }
</style>
