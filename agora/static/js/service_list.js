/**
 * Created by neuromatic on 23.2.16.
 */
var csrftoken = $("input[name='csrfmiddlewaretoken']").val();

var app = angular.module('service_list').config([
    '$httpProvider',
    '$interpolateProvider',
    function($httpProvider, $interpolateProvider) {
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $interpolateProvider.startSymbol('{');
        $interpolateProvider.endSymbol('}');
    }]).
    run([
    '$http',
    function($http) {
        $http.defaults.headers.post['X-CSRFToken'] = csrftoken;
}]);

app.controller('ListController', function($scope, $http, $httpParamSerializer, Upload) {





});