var app = angular.module('MovieSearch', []);

app.controller('MainController', function($scope, $http) {
	// var fd = new FormData();
	$scope.movieName = null;
	$scope.scrapePic = function() {
		$http({
			method: 'POST',
 			url: '/data',
 			data: {
				movieName: $scope.movieName
			},
			dataType: 'json'
		}).then(function(data) {
			$scope.flag = true;
			$scope.movieData = data.data;
			console.log(data);
		});
	};
	$scope.flag = false;
	// $scope.uploadFile = function(files) {
  //   fd.append("file", files[0]);
	// };
});
