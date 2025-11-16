export interface Bucket {
  id: number;
  name: string;
  path: string;
  description: string;
  memo: string;
  is_published: boolean;
  platform: string;
  version: string;
  readme: string;
  user_token: string;
  created_at?: string;
  updated_at?: string;
  like_num?: number;
  is_liked?: boolean;
  packages?: Package[];
  environments?: Environment[];
  config_files?: ConfigFile[];
  user_info?: User;
}

export interface Package {
  id: number;
  name: string;
  description: string;
  package_manager: string;
  version: string;
  install_command?: string;
  is_global: boolean;
  platform: string;
  is_required?: boolean;
  created_at?: string;
  updated_at?: string;
}

export interface Environment {
  id: number;
  key: string;
  value: string;
  description: string;
  is_secret: boolean;
  platform: string;
  is_required?: boolean;
  created_at?: string;
  updated_at?: string;
}

export interface ConfigFile {
  id: number;
  name: string;
  description: string;
  file_path: string;
  content: string;
  file_type: string;
  platform: string;
  is_required?: boolean;
  created_at?: string;
  updated_at?: string;
}

export interface User {
  id: number;
  username: string;
  email?: string;
  created_at?: string;
}

export interface Tool {
  id: number;
  name: string;
  description: string;
  image_url: string;
  is_open_source: boolean;
  site_url: string;
  github_url: string;
  like_num?: number;
  is_liked?: boolean;
  created_at?: string;
  updated_at?: string;
}

export interface Tag {
  id: number;
  name: string;
  description: string;
  created_at?: string;
  updated_at?: string;
}

export interface CreateBucketRequest {
  name: string;
  description: string;
  memo?: string;
  is_published?: boolean;
  platform?: string;
  version?: string;
  readme?: string;
}

export interface CreatePackageRequest {
  name: string;
  description: string;
  package_manager: string;
  version?: string;
  install_command?: string;
  is_global?: boolean;
  platform?: string;
}

export interface CreateEnvironmentRequest {
  key: string;
  value: string;
  description?: string;
  is_secret?: boolean;
  platform?: string;
}

export interface CreateConfigFileRequest {
  name: string;
  description: string;
  file_path: string;
  content: string;
  file_type?: string;
  platform?: string;
}

export type ExportFormat = 'json' | 'yaml';
export type ScriptType = 'bash' | 'powershell' | 'dockerfile' | 'docker-compose';
export type Platform = 'all' | 'linux' | 'macos' | 'windows';
export type PackageManager = 'pip' | 'npm' | 'apt' | 'brew' | 'cargo' | 'go' | 'custom';
