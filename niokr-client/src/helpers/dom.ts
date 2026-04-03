export const isPartOfNode = (
  target: HTMLElement | null,
  root: HTMLElement | undefined,
): boolean => {
  if (!root || !target) return false;
  return root === target || root.contains(target);
};
