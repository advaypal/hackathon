var app = angular.module('MovieSearch', []);

app.controller('MainController', function($scope, $http) {
	$scope.scrape = function() {
		$http({
			method: 'POST',
 			url: 'py/data.py',
 			data: { movieData: $scope.movieData }
		}).then(function(data) {
			console.log(data);
		});
	};
	$scope.movieData = null;
});
