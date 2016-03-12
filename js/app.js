var app = angular.module('MovieSearch', []);

app.controller('MainController', function($scope, $http) {
	var fd = new FormData();
	$scope.moviePic = null;
	$scope.movieData = null;

	$scope.scrapePic = function() {
		$http({
			method: 'POST',
 			url: 'py/data.py',
 			data: fd,
			headers: {'Content-Type': undefined},
	    transformRequest: angular.identity
		}).then(function(data) {
			console.log(data);
		});
	};

	$scope.uploadFile = function(files) {
    fd.append("file", files[0]);
	};
});
