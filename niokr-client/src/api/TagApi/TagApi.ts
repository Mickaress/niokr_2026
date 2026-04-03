import { FilterType, TagType } from '@/models/Filters';
import { axiosInstance } from '../axiosInstance';
import TagApiType from './TagApiType';
import { ListDTO } from '@/models/Project';

export default class TagApi implements TagApiType {
  async getAllTags(filters?: Pick<FilterType, 'page'>): Promise<ListDTO<TagType>> {
    const response = await axiosInstance.get('tags', filters ? { params: filters } : undefined);

    return response.data;
  }
}
