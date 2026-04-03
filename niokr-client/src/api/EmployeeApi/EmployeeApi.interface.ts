export default interface EmployeeApiType {
  apply(projectId: number): Promise<void>;
  withdraw(projectId: number): Promise<void>;
}
