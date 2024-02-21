// Listen for install event, set callback
self.addEventListener('install', function(event) {
  const CACHE_NAME = 'startup-v1';
  const urls = [
    '/',
    '/static/flask.png'
  ];
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(urls.map(url => new Request(url)));
      // use the following code if basic HTTP authentication is implemented
      // https://stackoverflow.com/questions/38193221/how-to-use-a-service-worker-with-basic-authentication-ntlm-negotiate
      // return cache.addAll(urls.map(url => new Request(url, {credentials: 'same-origin'})));
    })
  );
});
self.addEventListener('activate', function(event) {
  console.log('activate');
});
self.addEventListener('fetch', function(event) {
  console.log('fetch: ' + event.request.url);
  const ignoreUrls = [
    '/login',
    '/static/js/app.js'
  ];
  const url = new URL(event.request.url);
  if (ignoreUrls.indexOf(url.pathname) > -1) {
    console.log('ignore');
    return
  }
  // https://developers.google.com/web/ilt/pwa/caching-files-with-service-worker
  event.respondWith(
    // Cache falling back to the network
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});