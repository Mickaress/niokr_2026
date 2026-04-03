export function askForUserRole(): string | undefined {
  const isCustomer = window.confirm('Зайти как заказчик?');
  if (isCustomer) return 'test_customer';

  const isEmployee = window.confirm('Зайти как сотрудник?');
  if (isEmployee) return 'test_employee';

  const isAdmin = window.confirm('Зайти как администратор?');
  if (isAdmin) return 'test_admin';

  return undefined;
}
