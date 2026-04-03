import type { FilterType } from '@/models/Filters';
import type { ProjectType, ListDTO, ProjectFormType } from '@/models/Project';

export default interface ProjectApiType {
  getFilteredProjectList(filters: FilterType): Promise<ListDTO<ProjectType>>;
  getSingleProject(id: number): Promise<ProjectType>;
  updateProject(id: number, data: Partial<ProjectType> | ProjectFormType): Promise<void>;
}
