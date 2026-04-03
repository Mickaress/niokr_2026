import { describe, expect, it } from 'vitest';
import { declOfNum } from '../string';

describe('string.ts', () => {
  it('declOfNum()', () => {
    const words: [string, string, string] = ['слово', 'слова', 'слов'];
    expect(declOfNum(1, words)).toBe('слово');
    expect(declOfNum(2, words)).toBe('слова');
    expect(declOfNum(5, words)).toBe('слов');
  });
});
