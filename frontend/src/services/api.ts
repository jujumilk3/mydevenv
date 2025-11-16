import axios from 'axios';
import type {
  Bucket,
  CreateBucketRequest,
  ExportFormat,
  ScriptType,
} from '@/types';

const api = axios.create({
  baseURL: '/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Bucket API
export const bucketApi = {
  getAll: async (): Promise<Bucket[]> => {
    const { data } = await api.get('/bucket');
    return data;
  },

  getById: async (id: number): Promise<Bucket> => {
    const { data } = await api.get(`/bucket/${id}`);
    return data;
  },

  create: async (bucket: CreateBucketRequest): Promise<Bucket> => {
    const { data } = await api.post('/bucket', bucket);
    return data;
  },

  update: async (id: number, bucket: Partial<CreateBucketRequest>): Promise<Bucket> => {
    const { data } = await api.patch(`/bucket/${id}`, bucket);
    return data;
  },

  delete: async (id: number): Promise<void> => {
    await api.delete(`/bucket/${id}`);
  },

  export: async (id: number, format: ExportFormat): Promise<string> => {
    const { data } = await api.get(`/bucket/${id}/export`, {
      params: { format },
    });
    return data;
  },

  getInstallScript: async (id: number, scriptType: ScriptType): Promise<string> => {
    const { data } = await api.get(`/bucket/${id}/install-script`, {
      params: { script_type: scriptType },
    });
    return data;
  },

  exportAll: async (id: number): Promise<Record<string, string>> => {
    const { data } = await api.get(`/bucket/${id}/export-all`);
    return data;
  },
};

// Tool API
export const toolApi = {
  getAll: async () => {
    const { data } = await api.get('/tool');
    return data;
  },

  getById: async (id: number) => {
    const { data } = await api.get(`/tool/${id}`);
    return data;
  },
};

// Tag API
export const tagApi = {
  getAll: async () => {
    const { data } = await api.get('/tag');
    return data;
  },
};

export default api;
