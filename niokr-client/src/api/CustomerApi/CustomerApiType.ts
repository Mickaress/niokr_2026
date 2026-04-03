import { ProjectFormType } from '@/models/Project';

export default interface CustomerApiType {
  createProject(data: ProjectFormType): Promise<void>;
}
