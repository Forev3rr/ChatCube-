(function () {
  'use strict';

  angular
    .module('chatcube.authentication', [
      'chatcube.authentication.controllers',
      'chatcube.authentication.services'
    ]);

  angular
    .module('chatcube.authentication.controllers', []);

  angular
    .module('chatcube.authentication.services', ['ngCookies']);
})();