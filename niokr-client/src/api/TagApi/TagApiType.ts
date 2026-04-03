import type { FilterType, TagType } from '@/models/Filters';
import { ListDTO } from '@/models/Project';

export default interface TagApiType {
  getAllTags(filters: Pick<FilterType, 'page'>): Promise<ListDTO<TagType>>;
}
