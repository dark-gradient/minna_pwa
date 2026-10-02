const CACHE = 'minna-kotoba-v156';
const ASSETS = [
  './', './index.html', './css/styles.css', './js/app.js', './data/vocab.json', './data/kaiwa.json', './data/listening-n5.json', './data/mock-tests-n5.json', './mock_tests/2018_N5_Mondai.pdf', './mock_tests/2018_N5_Kaitou.pdf', './data/grammar/lessons-01-25.json', './data/kanji/kanji-320.json', './manifest.webmanifest', './assets/images/backgrounds/bg_pixel_cinema.jpg', './assets/images/backgrounds/bg_cinema_wall.jpg', './assets/images/backgrounds/bg_grammar.jpg', './assets/images/backgrounds/bg_home.jpg', './assets/images/backgrounds/bg_kanji.jpg', './assets/images/backgrounds/bg_learn.jpg', './assets/images/backgrounds/bg_lesson_1.jpg', './assets/images/backgrounds/bg_lesson_2.jpg', './assets/images/backgrounds/bg_lesson_3.jpg', './assets/images/backgrounds/bg_lesson_4.jpg', './assets/images/backgrounds/bg_lesson_5.jpg', './assets/images/backgrounds/bg_lesson_6.jpg', './assets/images/backgrounds/bg_lesson_7.jpg', './assets/images/backgrounds/bg_lesson_8.jpg', './assets/images/backgrounds/bg_lesson_9.jpg', './assets/images/backgrounds/bg_lesson_10.jpg', './assets/images/backgrounds/bg_lesson_11.jpg', './assets/images/backgrounds/bg_lesson_12.jpg', './assets/images/backgrounds/bg_lesson_13.jpg', './assets/images/backgrounds/bg_lesson_14.jpg', './assets/images/backgrounds/bg_lesson_15.jpg', './assets/images/backgrounds/bg_lesson_16.jpg', './assets/images/backgrounds/bg_lesson_17.jpg', './assets/images/backgrounds/bg_lesson_18.jpg', './assets/images/backgrounds/bg_lesson_19.jpg', './assets/images/backgrounds/bg_lesson_20.jpg', './assets/images/backgrounds/bg_lesson_21.jpg', './assets/images/backgrounds/bg_lesson_22.jpg', './assets/images/backgrounds/bg_lesson_23.jpg', './assets/images/backgrounds/bg_lesson_24.jpg', './assets/images/backgrounds/bg_lesson_25.jpg', './assets/images/backgrounds/bg_more.jpg', './assets/images/backgrounds/bg_more_new.jpg', './assets/images/backgrounds/bg_review.jpg', './assets/images/backgrounds/bg_test_complete.jpg', './assets/images/backgrounds/bg_practice.jpg', './assets/images/backgrounds/bg_practice_new.jpg', './assets/images/backgrounds/fuji.jpg', './assets/images/backgrounds/fuji_wide.jpg', './assets/images/icons/icon_grammar.png', './assets/images/icons/icon_home.png', './assets/images/icons/icon_kanji.png', './assets/images/icons/icon_lessons.png', './assets/images/icons/icon_listening.png', './assets/images/icons/icon_mocktest.png', './assets/images/icons/nav_icon_home.png', './assets/images/icons/nav_icon_lessons.png', './assets/images/icons/nav_icon_vocabulary.png', './assets/images/icons/nav_icon_grammar.png', './assets/images/icons/nav_icon_kanji.png', './assets/images/icons/nav_icon_listening.png', './assets/images/icons/nav_icon_mocktest.png', './assets/images/icons/icon_vocabulary.png', './assets/pwa-icons/icon-180.png', './assets/pwa-icons/icon-192.png', './assets/pwa-icons/icon-512.png'
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

