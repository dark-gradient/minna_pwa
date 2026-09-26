const CACHE = 'minna-kotoba-v1';
const ASSETS = [
  './', './index.html', './styles.css', './app.js', './vocab.json', './kaiwa.json',
  './manifest.webmanifest', './icons/icon-192.png', './icons/icon-512.png', './icons/icon-180.png'
];
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  event.respondWith(caches.match(event.request).then(cached => cached || fetch(event.request).then(response => {
    const copy = response.clone();
    if (new URL(event.request.url).origin === self.location.origin) caches.open(CACHE).then(c => c.put(event.request, copy));
    return response;
  }).catch(() => caches.match('./index.html'))));
});
