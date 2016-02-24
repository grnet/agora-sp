/**
 * Created by neuromatic on 23.2.16.
 */
var serviceListApp = angular.module('serviceListApp', ['ngRoute', 'ngSanitize']).config([
    '$httpProvider',
    '$interpolateProvider',
    '$routeProvider',
    '$locationProvider',

    function($httpProvider, $interpolateProvider, $routeProvider, $locationProvider) {
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $interpolateProvider.startSymbol('{');
        $interpolateProvider.endSymbol('}');

        $routeProvider.when('/catalogue/services/:uuid/:request_type', {
            controller: 'DetailsController'
        });

        $locationProvider.html5Mode({enabled: true, requireBase : false});


    }]);

serviceListApp.controller('ListController', function($scope, $http) {

    $scope.service_count = 0;
    $scope.services = [];

    $scope.portfolio_base = "/portfolio/services/";
    $scope.catalogue_base = "/catalogue/services/";

    $scope.getServiceList = function() {

        $http.get('/portfolio/services/').
        success(function (response, status, headers, config) {
            console.log(response);

            $scope.services = angular.fromJson(response['data']['services']);
            $scope.service_count = response['data']['count'];

        }).
        error(function (data, status, headers, config) {
        });
    };

    $scope.getServiceList();

});

serviceListApp.controller('DetailsController', function($scope, $http, $location, $sce) {


    $scope.uuid = $location.path().split("/")[3];
    $scope.detail_level = $location.path().split("/")[1];

    $scope.current_service = "";

    if ($location.search().view != null)
         $scope.view_param = $location.search().view.split("=")[0];
    else
        $scope.view_param = "";


    $scope.getServiceDetails = function() {

        $http.get('/'+$scope.detail_level+'/services/'+$scope.uuid+'?view='+$scope.view_param).
        success(function (response, status, headers, config) {
            console.log(response);
                $scope.current_service = response['data'][0];
                $scope.owner_link = $scope.current_service.id_service_owner;

                $scope.contact_info_link = $scope.current_service.id_contact_information;

                $scope.service_details_link =  "<a href='/service_details/"+ $scope.current_service.service_details['uuid']+"?view=short' target='_blank' >"+ $scope.current_service.service_details['uuid']+"</a>";

                debugger;

             if ($scope.detail_level == 'portfolio' && $scope.view_param=='complete')
                {

                    $scope.owner_link = "<a href='/owner/"+$scope.current_service.service_owner['uuid']+"' target='_blank' >"+$scope.current_service.service_owner['uuid']+"</a>";

                    $scope.contact_info_link = "<a href='/contact_info/"+ $scope.current_service.contact_information['uuid']+"' target='_blank' >"+ $scope.current_service.contact_information['uuid']+"</a>";

                    $scope.service_details_link =  "<a href='/service_details/"+ $scope.current_service.service_details['uuid']+"?view=complete' target='_blank' >"+ $scope.current_service.service_details['uuid']+"</a>";

                }
        }).
        error(function (data, status, headers, config) {
        });





    };

    $scope.getServiceDetails();






});