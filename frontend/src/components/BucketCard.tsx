import { Link } from 'react-router-dom';
import { Package, Download, Heart, Calendar } from 'lucide-react';
import type { Bucket } from '@/types';

interface BucketCardProps {
  bucket: Bucket;
}

export default function BucketCard({ bucket }: BucketCardProps) {
  const platformColors: Record<string, string> = {
    linux: 'bg-yellow-100 text-yellow-800',
    macos: 'bg-gray-100 text-gray-800',
    windows: 'bg-blue-100 text-blue-800',
    all: 'bg-green-100 text-green-800',
  };

  return (
    <Link to={`/environments/${bucket.id}`} className="block">
      <div className="card hover:shadow-lg transition-shadow duration-200 cursor-pointer">
        {/* Header */}
        <div className="flex items-start justify-between mb-3">
          <div className="flex-1">
            <h3 className="text-lg font-semibold text-gray-900 mb-1">
              {bucket.name}
            </h3>
            <p className="text-sm text-gray-600 line-clamp-2">
              {bucket.description}
            </p>
          </div>
          <span
            className={`badge ${
              platformColors[bucket.platform] || platformColors.all
            }`}
          >
            {bucket.platform}
          </span>
        </div>

        {/* Stats */}
        <div className="flex items-center space-x-4 text-sm text-gray-500 mb-4">
          {bucket.packages && bucket.packages.length > 0 && (
            <div className="flex items-center space-x-1">
              <Package className="w-4 h-4" />
              <span>{bucket.packages.length} packages</span>
            </div>
          )}
          {bucket.like_num !== undefined && (
            <div className="flex items-center space-x-1">
              <Heart className="w-4 h-4" />
              <span>{bucket.like_num}</span>
            </div>
          )}
          <div className="flex items-center space-x-1">
            <Calendar className="w-4 h-4" />
            <span>v{bucket.version}</span>
          </div>
        </div>

        {/* Tags */}
        {bucket.packages && bucket.packages.length > 0 && (
          <div className="flex flex-wrap gap-2">
            {bucket.packages.slice(0, 3).map((pkg) => (
              <span
                key={pkg.id}
                className="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-gray-100 text-gray-700"
              >
                {pkg.name}
              </span>
            ))}
            {bucket.packages.length > 3 && (
              <span className="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-gray-100 text-gray-700">
                +{bucket.packages.length - 3} more
              </span>
            )}
          </div>
        )}

        {/* Footer */}
        <div className="mt-4 pt-4 border-t border-gray-200 flex items-center justify-between">
          <div className="flex items-center space-x-2">
            {bucket.user_info && (
              <span className="text-sm text-gray-600">
                by <span className="font-medium">{bucket.user_info.username}</span>
              </span>
            )}
          </div>
          <button
            onClick={(e) => {
              e.preventDefault();
              // Handle download
            }}
            className="text-primary-600 hover:text-primary-700 transition-colors"
          >
            <Download className="w-4 h-4" />
          </button>
        </div>
      </div>
    </Link>
  );
}
