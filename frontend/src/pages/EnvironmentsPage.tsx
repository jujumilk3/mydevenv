import { useState, useEffect } from 'react';
import { Search, Filter } from 'lucide-react';
import BucketCard from '@/components/BucketCard';
import { bucketApi } from '@/services/api';
import type { Bucket } from '@/types';

export default function EnvironmentsPage() {
  const [buckets, setBuckets] = useState<Bucket[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [platformFilter, setPlatformFilter] = useState('all');

  useEffect(() => {
    loadBuckets();
  }, []);

  const loadBuckets = async () => {
    try {
      setLoading(true);
      const data = await bucketApi.getAll();
      setBuckets(data);
    } catch (error) {
      console.error('Failed to load buckets:', error);
    } finally {
      setLoading(false);
    }
  };

  const filteredBuckets = buckets.filter((bucket) => {
    const matchesSearch =
      bucket.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      bucket.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesPlatform =
      platformFilter === 'all' || bucket.platform === platformFilter;
    return matchesSearch && matchesPlatform;
  });

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Development Environments
          </h1>
          <p className="text-lg text-gray-600">
            Browse and discover development environments shared by the community
          </p>
        </div>

        {/* Filters */}
        <div className="bg-white rounded-lg shadow-sm p-6 mb-8">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {/* Search */}
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
              <input
                type="text"
                placeholder="Search environments..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="input pl-10"
              />
            </div>

            {/* Platform Filter */}
            <div className="relative">
              <Filter className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
              <select
                value={platformFilter}
                onChange={(e) => setPlatformFilter(e.target.value)}
                className="input pl-10"
              >
                <option value="all">All Platforms</option>
                <option value="linux">Linux</option>
                <option value="macos">macOS</option>
                <option value="windows">Windows</option>
              </select>
            </div>
          </div>
        </div>

        {/* Results Count */}
        <div className="mb-4">
          <p className="text-gray-600">
            {loading ? (
              'Loading...'
            ) : (
              <>
                Showing <span className="font-semibold">{filteredBuckets.length}</span>{' '}
                {filteredBuckets.length === 1 ? 'environment' : 'environments'}
              </>
            )}
          </p>
        </div>

        {/* Buckets Grid */}
        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[...Array(6)].map((_, i) => (
              <div key={i} className="card animate-pulse">
                <div className="h-6 bg-gray-200 rounded w-3/4 mb-2"></div>
                <div className="h-4 bg-gray-200 rounded w-full mb-4"></div>
                <div className="h-4 bg-gray-200 rounded w-5/6"></div>
              </div>
            ))}
          </div>
        ) : filteredBuckets.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-600 text-lg">No environments found</p>
            <p className="text-gray-500 mt-2">
              Try adjusting your search or filters
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredBuckets.map((bucket) => (
              <BucketCard key={bucket.id} bucket={bucket} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
