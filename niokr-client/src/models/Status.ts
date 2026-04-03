export const enum Status {
  Review = 'review',
  Active = 'active',
  Archived = 'archived',
}

export const STATUS_LABELS: Record<Status, string> = {
  [Status.Active]: 'Активный',
  [Status.Review]: 'На рассмотрении',
  [Status.Archived]: 'Архивный',
};
