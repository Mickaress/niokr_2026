export default interface AdminApiType {
  addTag(name: string): Promise<void>;
  deleteTag(id: number): Promise<void>;
}
