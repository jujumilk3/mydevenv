# mydevenv Frontend

Modern web interface for the mydevenv platform built with React, TypeScript, Vite, and Tailwind CSS.

## Tech Stack

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **Lucide React** - Icon library

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Backend API running on `http://localhost:8000`

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

The app will be available at `http://localhost:3000`

### Build for Production

```bash
# Create production build
npm run build

# Preview production build
npm run preview
```

## Project Structure

```
frontend/
├── src/
│   ├── components/      # Reusable UI components
│   │   ├── Navbar.tsx
│   │   ├── Footer.tsx
│   │   └── BucketCard.tsx
│   ├── pages/           # Page components
│   │   ├── HomePage.tsx
│   │   ├── EnvironmentsPage.tsx
│   │   └── EnvironmentDetailPage.tsx
│   ├── services/        # API services
│   │   └── api.ts
│   ├── types/           # TypeScript types
│   │   └── index.ts
│   ├── App.tsx          # Main app component
│   ├── main.tsx         # Entry point
│   └── index.css        # Global styles
├── index.html           # HTML template
├── vite.config.ts       # Vite configuration
├── tailwind.config.js   # Tailwind configuration
└── tsconfig.json        # TypeScript configuration
```

## Features

### 🏠 Home Page
- Hero section with call-to-action
- Feature highlights
- How it works section

### 📦 Environments Page
- Browse all development environments
- Search and filter functionality
- Platform-based filtering

### 📄 Environment Detail Page
- View complete environment details
- Download installation scripts (Bash, PowerShell, Dockerfile)
- Quick install command
- Package, environment variable, and config file tabs

### 🎨 UI Components

#### Navbar
- Logo and branding
- Navigation links
- Search and GitHub buttons
- Create environment CTA

#### Footer
- About section
- Quick links
- Social media links

#### BucketCard
- Environment preview card
- Platform badge
- Package count
- Like button

## API Integration

The frontend communicates with the backend API through Axios:

```typescript
// Example API call
import { bucketApi } from '@/services/api';

const buckets = await bucketApi.getAll();
const bucket = await bucketApi.getById(1);
const script = await bucketApi.getInstallScript(1, 'bash');
```

## Styling

The project uses Tailwind CSS with custom utility classes:

```css
/* Button styles */
.btn
.btn-primary
.btn-secondary
.btn-outline

/* Card styles */
.card

/* Input styles */
.input

/* Badge styles */
.badge
.badge-blue
.badge-green
.badge-gray
```

## Development

### Running with Docker

```bash
# From project root
docker-compose up frontend

# Or run entire stack
docker-compose up
```

### Code Formatting

```bash
# Lint code
npm run lint
```

## Environment Variables

Create a `.env` file in the frontend directory (if needed):

```env
VITE_API_URL=http://localhost:8000
```

## Routes

- `/` - Home page
- `/environments` - Browse environments
- `/environments/:id` - Environment details
- `/create` - Create new environment (TODO)
- `/explore` - Explore page (TODO)
- `/docs` - Documentation (TODO)

## Contributing

1. Follow the existing code structure
2. Use TypeScript for type safety
3. Follow Tailwind CSS conventions
4. Keep components small and reusable

## License

MIT
