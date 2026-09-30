const CACHE = 'minna-kotoba-v120';
const ASSETS = [
  './', './index.html', './styles.css', './app.js', './vocab.json', './kaiwa.json', './listening-n5.json', './mock-tests-n5.json', './mock_tests/2018_N5_Mondai.pdf', './mock_tests/2018_N5_Kaitou.pdf', './manifest.webmanifest', './bg_pixel_cinema.jpg', './bg_cinema_wall.jpg', './bg_grammar.jpg', './bg_home.jpg', './bg_kanji.jpg', './bg_learn.jpg', './bg_lesson_1.jpg', './bg_lesson_2.jpg', './bg_lesson_3.jpg', './bg_more.jpg', './bg_more_new.jpg', './bg_practice.jpg', './bg_practice_new.jpg', './fuji.jpg', './fuji_wide.jpg', './icon_grammar.png', './icon_home.png', './icon_kanji.png', './icon_lessons.png', './icon_listening.png', './icon_mocktest.png', './icon_vocabulary.png', './icons/icon-180.png', './icons/icon-192.png', './icons/icon-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE).then(cache => 
      Promise.all(ASSETS.map(url => 
        fetch(url, { cache: 'no-cache' }).then(response => {
          if (!response.ok) throw new Error('Network response was not ok for ' + url);
          return cache.put(url, response);
        }).catch(err => console.error('Failed to cache', url, err))
      ))
    ).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => 
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  
  event.respondWith(
    caches.match(event.request).then(cached => {
      return cached || fetch(event.request).then(response => {
        const copy = response.clone();
        // ONLY cache valid responses (not 404s)
        if (response.ok && new URL(event.request.url).origin === self.location.origin) {
          caches.open(CACHE).then(c => c.put(event.request, copy));
        }
        return response;
      }).catch(() => {
        // Only return index.html for navigation requests, not images!
        if (event.request.mode === 'navigate') {
          return caches.match('./index.html');
        }
        return null;
      });
    })
  );
});

