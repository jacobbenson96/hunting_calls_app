const CACHE_NAME = 'hunting-calls-cache-v1';

// Files to cache
const ASSETS = [
    '/',
    '/calls',
    '/static/hp_background.jpg',
    '/static/turkey_icon.jpg',
    '/static/deer_icon.jpg',
    '/static/crow_icon.jpg',
    '/static/Cluck_and_Purr.mp3',
    '/static/Clucks.mp3',
    '/static/Cutting.mp3',
    '/static/Excited_Hen_Yelps.mp3',
    '/static/Fly_Down_Cackles.mp3',
    '/static/Gobbling.mp3',
    '/static/Kee_Kee_Run.mp3',
    '/static/Old_Hen_Assembly_Yelp.mp3',
    '/static/Plain_Hen_Yelp.mp3',
    '/static/Purrs.mp3',
    '/static/Putts.mp3',
    '/static/Tree_Calling.mp3'
];

// Install Service Worker and cache assets
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            console.log('Caching assets');
            return cache.addAll(ASSETS);
        })
    );
});

// Activate Service Worker and remove old caches
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
            );
        })
    );
});

// Fetch files from cache or network
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
