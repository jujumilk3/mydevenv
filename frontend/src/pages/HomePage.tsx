import { Link } from 'react-router-dom';
import { ArrowRight, Package, Download, Share2, Code, Zap, Shield } from 'lucide-react';

export default function HomePage() {
  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-primary-50 to-blue-50 py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
              Share Your Dev Environment
              <br />
              <span className="text-primary-600">Anywhere, Anytime</span>
            </h1>
            <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
              The platform for sharing, managing, and deploying development environments.
              Save your setup once, use it everywhere.
            </p>
            <div className="flex justify-center space-x-4">
              <Link to="/environments" className="btn btn-primary text-lg px-8 py-3">
                Explore Environments
                <ArrowRight className="w-5 h-5 ml-2 inline" />
              </Link>
              <Link to="/create" className="btn btn-outline text-lg px-8 py-3">
                Create Environment
              </Link>
            </div>
          </div>

          {/* Feature Cards */}
          <div className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white rounded-xl p-6 shadow-lg">
              <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mb-4">
                <Package className="w-6 h-6 text-primary-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Package Management</h3>
              <p className="text-gray-600">
                Support for pip, npm, brew, apt, and more. Manage all your dependencies in one place.
              </p>
            </div>

            <div className="bg-white rounded-xl p-6 shadow-lg">
              <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4">
                <Download className="w-6 h-6 text-green-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">One-Click Install</h3>
              <p className="text-gray-600">
                Generate installation scripts for Bash, PowerShell, or Dockerfile automatically.
              </p>
            </div>

            <div className="bg-white rounded-xl p-6 shadow-lg">
              <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
                <Share2 className="w-6 h-6 text-purple-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Easy Sharing</h3>
              <p className="text-gray-600">
                Share your environment with team members or the community with a simple link.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">How It Works</h2>
            <p className="text-xl text-gray-600">
              Get started in three simple steps
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
            <div className="text-center">
              <div className="w-16 h-16 bg-primary-600 text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-4">
                1
              </div>
              <h3 className="text-xl font-semibold mb-2">Create or Scan</h3>
              <p className="text-gray-600">
                Create a new environment from scratch or scan your current system to capture your setup.
              </p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-primary-600 text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-4">
                2
              </div>
              <h3 className="text-xl font-semibold mb-2">Configure & Share</h3>
              <p className="text-gray-600">
                Add packages, environment variables, and config files. Share it publicly or keep it private.
              </p>
            </div>

            <div className="text-center">
              <div className="w-16 h-16 bg-primary-600 text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-4">
                3
              </div>
              <h3 className="text-xl font-semibold mb-2">Deploy Anywhere</h3>
              <p className="text-gray-600">
                Download installation scripts and deploy your environment on any machine with one command.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Powerful Features</h2>
            <p className="text-xl text-gray-600">
              Everything you need to manage development environments
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="bg-white p-6 rounded-lg">
              <Code className="w-10 h-10 text-primary-600 mb-4" />
              <h3 className="text-lg font-semibold mb-2">Multi-Platform Support</h3>
              <p className="text-gray-600">
                Linux, macOS, Windows - deploy anywhere with platform-specific configurations.
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg">
              <Zap className="w-10 h-10 text-primary-600 mb-4" />
              <h3 className="text-lg font-semibold mb-2">CLI Tool</h3>
              <p className="text-gray-600">
                Powerful command-line interface for quick environment management and deployment.
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg">
              <Shield className="w-10 h-10 text-primary-600 mb-4" />
              <h3 className="text-lg font-semibold mb-2">Docker Ready</h3>
              <p className="text-gray-600">
                Automatically generate Dockerfile and docker-compose configurations.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-primary-600">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-4xl font-bold text-white mb-4">
            Ready to Get Started?
          </h2>
          <p className="text-xl text-primary-100 mb-8">
            Join developers who are streamlining their development workflow
          </p>
          <div className="flex justify-center space-x-4">
            <Link
              to="/create"
              className="bg-white text-primary-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors"
            >
              Create Your First Environment
            </Link>
            <a
              href="https://github.com/jujumilk3/mydevenv"
              target="_blank"
              rel="noopener noreferrer"
              className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-primary-700 transition-colors"
            >
              View on GitHub
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}
