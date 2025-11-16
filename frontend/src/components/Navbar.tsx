import { Link } from 'react-router-dom';
import { Search, Plus, Github } from 'lucide-react';

export default function Navbar() {
  return (
    <nav className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-gradient-to-br from-primary-500 to-primary-700 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-xl">M</span>
            </div>
            <span className="text-xl font-bold text-gray-900">mydevenv</span>
          </Link>

          {/* Navigation Links */}
          <div className="hidden md:flex items-center space-x-8">
            <Link
              to="/environments"
              className="text-gray-600 hover:text-gray-900 font-medium transition-colors"
            >
              Environments
            </Link>
            <Link
              to="/explore"
              className="text-gray-600 hover:text-gray-900 font-medium transition-colors"
            >
              Explore
            </Link>
            <Link
              to="/docs"
              className="text-gray-600 hover:text-gray-900 font-medium transition-colors"
            >
              Docs
            </Link>
          </div>

          {/* Action Buttons */}
          <div className="flex items-center space-x-4">
            <button className="p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors">
              <Search className="w-5 h-5" />
            </button>
            <a
              href="https://github.com/jujumilk3/mydevenv"
              target="_blank"
              rel="noopener noreferrer"
              className="p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <Github className="w-5 h-5" />
            </a>
            <Link
              to="/create"
              className="btn btn-primary flex items-center space-x-2"
            >
              <Plus className="w-5 h-5" />
              <span>Create Environment</span>
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}
