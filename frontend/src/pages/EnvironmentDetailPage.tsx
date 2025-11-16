import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import {
  Download,
  Copy,
  Heart,
  Share2,
  Package,
  Settings,
  FileText,
  ChevronLeft,
  Terminal,
} from 'lucide-react';
import { bucketApi } from '@/services/api';
import type { Bucket, ScriptType } from '@/types';

export default function EnvironmentDetailPage() {
  const { id } = useParams<{ id: string }>();
  const [bucket, setBucket] = useState<Bucket | null>(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'packages' | 'env' | 'config' | 'readme'>(
    'readme'
  );

  useEffect(() => {
    if (id) {
      loadBucket(parseInt(id));
    }
  }, [id]);

  const loadBucket = async (bucketId: number) => {
    try {
      setLoading(true);
      const data = await bucketApi.getById(bucketId);
      setBucket(data);
    } catch (error) {
      console.error('Failed to load bucket:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleDownloadScript = async (scriptType: ScriptType) => {
    if (!bucket) return;
    try {
      const script = await bucketApi.getInstallScript(bucket.id, scriptType);
      const blob = new Blob([script], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `install.${scriptType === 'bash' ? 'sh' : scriptType === 'powershell' ? 'ps1' : scriptType}`;
      a.click();
      URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Failed to download script:', error);
    }
  };

  const copyInstallCommand = () => {
    const command = `curl -fsSL https://mydevenv.com/api/v1/bucket/${bucket?.id}/install-script | bash`;
    navigator.clipboard.writeText(command);
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="animate-pulse">
            <div className="h-8 bg-gray-200 rounded w-1/4 mb-4"></div>
            <div className="h-64 bg-gray-200 rounded"></div>
          </div>
        </div>
      </div>
    );
  }

  if (!bucket) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <p className="text-center text-gray-600">Environment not found</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Back Link */}
        <Link
          to="/environments"
          className="inline-flex items-center text-primary-600 hover:text-primary-700 mb-6"
        >
          <ChevronLeft className="w-4 h-4 mr-1" />
          Back to Environments
        </Link>

        {/* Header */}
        <div className="bg-white rounded-lg shadow-sm p-8 mb-6">
          <div className="flex items-start justify-between mb-4">
            <div className="flex-1">
              <h1 className="text-3xl font-bold text-gray-900 mb-2">
                {bucket.name}
              </h1>
              <p className="text-lg text-gray-600 mb-4">{bucket.description}</p>
              <div className="flex items-center space-x-4">
                <span className="badge badge-blue">{bucket.platform}</span>
                <span className="badge badge-gray">v{bucket.version}</span>
                {bucket.like_num !== undefined && (
                  <div className="flex items-center space-x-1 text-gray-600">
                    <Heart className="w-4 h-4" />
                    <span>{bucket.like_num}</span>
                  </div>
                )}
              </div>
            </div>

            <div className="flex space-x-2">
              <button className="btn btn-outline">
                <Heart className="w-4 h-4 mr-2" />
                Like
              </button>
              <button className="btn btn-outline">
                <Share2 className="w-4 h-4 mr-2" />
                Share
              </button>
            </div>
          </div>

          {/* Quick Install */}
          <div className="bg-gray-900 rounded-lg p-4 mt-6">
            <div className="flex items-center justify-between mb-2">
              <span className="text-gray-400 text-sm font-medium">Quick Install</span>
              <button
                onClick={copyInstallCommand}
                className="text-gray-400 hover:text-white transition-colors"
              >
                <Copy className="w-4 h-4" />
              </button>
            </div>
            <code className="text-green-400 font-mono text-sm">
              curl -fsSL https://mydevenv.com/api/v1/bucket/{bucket.id}/install-script | bash
            </code>
          </div>

          {/* Download Options */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mt-4">
            <button
              onClick={() => handleDownloadScript('bash')}
              className="btn btn-secondary flex items-center justify-center"
            >
              <Terminal className="w-4 h-4 mr-2" />
              Bash Script
            </button>
            <button
              onClick={() => handleDownloadScript('powershell')}
              className="btn btn-secondary flex items-center justify-center"
            >
              <Terminal className="w-4 h-4 mr-2" />
              PowerShell
            </button>
            <button
              onClick={() => handleDownloadScript('dockerfile')}
              className="btn btn-secondary flex items-center justify-center"
            >
              <FileText className="w-4 h-4 mr-2" />
              Dockerfile
            </button>
            <button
              onClick={() => handleDownloadScript('docker-compose')}
              className="btn btn-secondary flex items-center justify-center"
            >
              <FileText className="w-4 h-4 mr-2" />
              Compose
            </button>
          </div>
        </div>

        {/* Tabs */}
        <div className="bg-white rounded-lg shadow-sm">
          <div className="border-b border-gray-200">
            <div className="flex space-x-8 px-8">
              <button
                onClick={() => setActiveTab('readme')}
                className={`py-4 border-b-2 font-medium transition-colors ${
                  activeTab === 'readme'
                    ? 'border-primary-600 text-primary-600'
                    : 'border-transparent text-gray-600 hover:text-gray-900'
                }`}
              >
                <FileText className="w-4 h-4 inline mr-2" />
                README
              </button>
              <button
                onClick={() => setActiveTab('packages')}
                className={`py-4 border-b-2 font-medium transition-colors ${
                  activeTab === 'packages'
                    ? 'border-primary-600 text-primary-600'
                    : 'border-transparent text-gray-600 hover:text-gray-900'
                }`}
              >
                <Package className="w-4 h-4 inline mr-2" />
                Packages ({bucket.packages?.length || 0})
              </button>
              <button
                onClick={() => setActiveTab('env')}
                className={`py-4 border-b-2 font-medium transition-colors ${
                  activeTab === 'env'
                    ? 'border-primary-600 text-primary-600'
                    : 'border-transparent text-gray-600 hover:text-gray-900'
                }`}
              >
                <Settings className="w-4 h-4 inline mr-2" />
                Environment ({bucket.environments?.length || 0})
              </button>
              <button
                onClick={() => setActiveTab('config')}
                className={`py-4 border-b-2 font-medium transition-colors ${
                  activeTab === 'config'
                    ? 'border-primary-600 text-primary-600'
                    : 'border-transparent text-gray-600 hover:text-gray-900'
                }`}
              >
                <FileText className="w-4 h-4 inline mr-2" />
                Config Files ({bucket.config_files?.length || 0})
              </button>
            </div>
          </div>

          {/* Tab Content */}
          <div className="p-8">
            {activeTab === 'readme' && (
              <div className="prose max-w-none">
                <pre className="whitespace-pre-wrap">{bucket.readme || 'No README available'}</pre>
              </div>
            )}

            {activeTab === 'packages' && (
              <div className="space-y-4">
                {bucket.packages && bucket.packages.length > 0 ? (
                  bucket.packages.map((pkg) => (
                    <div key={pkg.id} className="border border-gray-200 rounded-lg p-4">
                      <div className="flex items-start justify-between">
                        <div className="flex-1">
                          <h3 className="font-semibold text-gray-900">{pkg.name}</h3>
                          <p className="text-sm text-gray-600 mt-1">{pkg.description}</p>
                          <div className="flex items-center space-x-4 mt-2 text-sm text-gray-500">
                            <span>Manager: {pkg.package_manager}</span>
                            <span>Version: {pkg.version}</span>
                            <span>Platform: {pkg.platform}</span>
                          </div>
                        </div>
                        {pkg.is_global && (
                          <span className="badge badge-blue">Global</span>
                        )}
                      </div>
                    </div>
                  ))
                ) : (
                  <p className="text-gray-600">No packages defined</p>
                )}
              </div>
            )}

            {activeTab === 'env' && (
              <div className="space-y-4">
                {bucket.environments && bucket.environments.length > 0 ? (
                  bucket.environments.map((env) => (
                    <div key={env.id} className="border border-gray-200 rounded-lg p-4">
                      <div className="flex items-start justify-between">
                        <div className="flex-1">
                          <h3 className="font-semibold text-gray-900">{env.key}</h3>
                          <p className="text-sm text-gray-600 mt-1">{env.description}</p>
                          <code className="block mt-2 p-2 bg-gray-100 rounded text-sm">
                            {env.is_secret ? '***' : env.value}
                          </code>
                        </div>
                        {env.is_secret && (
                          <span className="badge badge-gray">Secret</span>
                        )}
                      </div>
                    </div>
                  ))
                ) : (
                  <p className="text-gray-600">No environment variables defined</p>
                )}
              </div>
            )}

            {activeTab === 'config' && (
              <div className="space-y-4">
                {bucket.config_files && bucket.config_files.length > 0 ? (
                  bucket.config_files.map((config) => (
                    <div key={config.id} className="border border-gray-200 rounded-lg p-4">
                      <h3 className="font-semibold text-gray-900 mb-2">{config.name}</h3>
                      <p className="text-sm text-gray-600 mb-2">{config.description}</p>
                      <p className="text-sm text-gray-500 mb-2">Path: {config.file_path}</p>
                      <pre className="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto text-sm">
                        {config.content}
                      </pre>
                    </div>
                  ))
                ) : (
                  <p className="text-gray-600">No config files defined</p>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
