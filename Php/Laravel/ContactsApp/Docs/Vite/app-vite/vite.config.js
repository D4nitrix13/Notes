import laravel from 'laravel-vite-plugin';
import { defineConfig } from 'vite';

export default defineConfig({
    plugins: [
        laravel({
            input: ['resources/css/app.css', 'resources/js/app.js'], // Files to compile (entry points)
            refresh: true, // Enables automatic browser refresh on file changes
        }),
    ],
    server: {
        host: '0.0.0.0',                   // Listen on all network interfaces (useful for Docker)
        port: 5174,                        // Port for the Vite dev server
        origin: 'http://172.17.0.2:5174',  // URL used for HMR and CORS
        cors: true,                        // Enable CORS to allow external access
        hmr: {
            host: '172.17.0.2',              // Host/IP used by Hot Module Replacement (HMR)
        },
    },
});
