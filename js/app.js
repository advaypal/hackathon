var app = angular.module('MovieSearch', []);

app.controller('MainController', ["$scope", "$http", function($scope, $http) {
	$scope.scrape = function($http) {
		return $http({
			method: 'POST', 
 			url: 'data.py',
 			data: { movieData: $scope.movieData }
		}).then(function(data) {
			console.log(data);
		});
	};
	$scope.movieData = null;
}]);