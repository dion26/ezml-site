import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import progress from 'vite-plugin-progress'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    progress(),
  ],
  build: {
    outDir: '../static/dist'
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  },
})
