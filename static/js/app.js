var app = angular.module('MovieSearch', []);

app.controller('MainController', function($scope, $http) {
	var fd = new FormData();
	$scope.movieData = {};
	$scope.scrapePic = function() {
		// $http({
		// 	method: 'POST',
 	// 		url: '../data.py',
 	// 		data: fd,
		// 	headers: {'Content-Type': undefined},
	  //   transformRequest: angular.identity
		// }).then(function(data) {
		// 	$scope.flag = true;
		// 	$scope.movieData = data;
		// 	console.log(data);
		// });
		$http({
			method: 'POST',
 			url: '../data.py',
 			data: {
				hey: "bye"
			},
			dataType: "json"
		}).then(function(data) {
			$scope.flag = true;
			$scope.movieData = data;
			console.log(data);
		});
	};
	$scope.flag = false;
	$scope.uploadFile = function(files) {
    fd.append("file", files[0]);
	};
});
