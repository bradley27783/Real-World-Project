// Problem with the uni building locations: postcodes, coordinates (Only 6/23 markers)
// Previous problem could result into another problem with the directions being percise..
// All markers on the map show, hence the difference in transparency
    // Need to adjus the coordinates for all markers to appear on the map at more precise locations.
// Directions API and functions are incomplete and inconsistent...
// Info windows for each geographic location need to be implemented
// Initialize and add the map
var map, InfoWindow;
function initMap() {
    var directionsService = new google.maps.DirectionsService();
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
        // The location of Coventry University and center of map
    center: new google.maps.LatLng(52.405314, -1.500063),  
        });

    directionsDisplay.setMap(map);
    document.getElementById('submit').addEventListener('click', function() {
        calcRoute(directionsService, directionsDisplay);
  });
  
    infoWindow = new google.maps.InfoWindow;
     var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';
        var icons = {
          parking: {
            icon: iconBase + 'parking_lot_maps.png'
          },
          library: {
            icon: iconBase + 'library_maps.png'
          },
          info: {
            icon: iconBase + 'info-i_maps.png'
          }
        };
var features = [
          {
            position: new google.maps.LatLng(52.408989, -1.506330), //Alan Berry Building (CV1 5FB)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.409720, -1.500000), //Alma Building (CV1 5QA)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.406670, -1.501460), //Armstrong Siddeley Building (CV1 5DL)
            type: 'info'
          }, {
            position: new google.maps.LatLng(40.198450, 44.513150), //Bugatti Building (CV1 5PH)
            type: 'info'
          }, {
            position: new google.maps.LatLng(40.198450, 44.513150), //Charles Ward Building (CV1 5FD)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.405920, -1.495950), //Engineering & Computing Building (CV1 2JH)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.406818, -1.505230), //Ellen Terry Building (CV1 5RW)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.408989, -1.506330), //George Eliot Building (CV1 5FB)
            type: 'info'
          }, {
            position: new google.maps.LatLng(40.198448, 44.513149), //Graham Sutherland Building (CV1 5PH)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.406670, -1.501460), //Frederick Lanchester Library Building (CV1 5DD)
            type: 'library'
          }, {
            position: new google.maps.LatLng(52.406670, -1.501460), //Jaguar Building (CV1 5DL)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.408989, -1.506330), //TheHub Building (CV1 5FB)
            type: 'info'
          }, {
            position: new google.maps.LatLng(40.198448, 44.513149), //Maurice Foss Building (CV1 5PH)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.408989, -1.506330), //James Starley Building (CV1 5FB)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.407871, -1.495210), //Multi-Storey Car Park Building (CV1 5DE)
            type: 'parking'
          }, {
            position: new google.maps.LatLng(52.408989, -1.506330), //Priory Building (CV1 5FB)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.406818, -1.505230), // Richard Crossman Building (CV1 5RW)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.405980, -1.503890), //Alison Gingell Building (CV1 2DS)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.406080, -1.505810), //Sir John Laing Building (CV1 2LT)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.406670, -1.501460), //Sir William Lyons Building (CV1 5DL)
            type: 'info'  
          }, {
            position: new google.maps.LatLng(52.405918, -1.495950), //Student Centre Building (CV1 2JH)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.405979, -1.503890), //Whitefriars Building (CV1 2DS)
            type: 'info'  
          }, {
            position: new google.maps.LatLng(52.405979, -1.503890), //Sports Centre Building (CV1 2DS)
            type: 'info'  
          }
        ];
         
        // Create markers.
        features.forEach(function(feature) {
          var marker = new google.maps.Marker({
            position: feature.position,
            icon: icons[feature.type].icon,
            map: map
          });
        });
    if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };

            infoWindow.setPosition(pos);
            infoWindow.setContent('Location found. You are here:');
            infoWindow.open(map);
            map.setCenter(pos);
          }, 
            function() 
            {
            handleLocationError(true, infoWindow, map.getCenter());
          });
        }
     else 
     {
          // Browser doesn't support Geolocation
          handleLocationError(false, infoWindow, map.getCenter());
     }
}
      function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                                'Error: Enable Geolocation service through your browser to support map navigation.' :
                                'Error: Your browser does not support geolocation.');
        infoWindow.open(map);
          }
          
function calcRoute(directionsService, directionsDisplay) {
  var waypts = [];
  var checkboxArray = document.getElementById('waypoints');
  for (var i = 0; i < checkboxArray.length; i++) {
    if (checkboxArray.options[i].selected) {
      waypts.push({
        location: checkboxArray[i].value,
        stopover: true
      });
    }
  }

  directionsService.route({ 
    origin: document.getElementById('start').value,
    destination: document.getElementById('end').value,
    waypoints: waypts,
    optimizeWaypoints: true,
    selectedMode: document.getElementById('mode').value, 
    travelMode: google.maps.TravelMode[selectedMode]
  }, function(response, status) {
    if (status === 'OK') {
      directionsDisplay.setDirections(response);
      var route = response.routes[0];
      var summaryPanel = document.getElementById('directions-panel');
      summaryPanel.innerHTML = '';
      // For each route, display summary information.
      for (var i = 0; i < route.legs.length; i++) {
        var routeSegment = i + 1;
        summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment +
            '</b><br>';
        summaryPanel.innerHTML += route.legs[i].start_address + ' to ';
        summaryPanel.innerHTML += route.legs[i].end_address + '<br>';
        summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>';
      }
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
} 