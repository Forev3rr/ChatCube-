(function () {
  'use strict';

  angular
    .module('chatcube', [
      'chatcube.routes',
      'chatcube.config',
      'chatcube.authentication',
      'chatcube.layout'
    ]);

  angular
    .module('thinkster')
    .run(run);

   run.$inject = ['$http'];

/**
* @name run
* @desc Update xsrf $http headers to align with Django's defaults
*/
function run($http) {
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
}

   angular
    .module('chatcube.routes', ['ngRoute']);
    })();

