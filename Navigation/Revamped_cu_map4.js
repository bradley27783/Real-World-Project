// Problem with the uni building locations: postcodes, coordinates (Only 6/23 markers)
// Previous problem could result into another problem with the directions being percise..
// All markers on the map show, hence the difference in transparency
    // Need to adjus the coordinates for all markers to appear on the map at more precise locations.
// Directions API and functions are incomplete and inconsistent...
// Info windows for each geographic location need to be implemented
// https://stackoverflow.com/questions/14976495/get-selected-option-text-with-javascript
// Initialize and add the map
// AIzaSyDHbYqwiDtGA8Zof2xXZVfGnnWrvEX09rw Custom API Key
var map, InfoWindow;
function initMap() {
    var directionsService = new google.maps.DirectionsService();
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var stepDisplay = new google.maps.InfoWindow;
    var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 16,
        // The location of Coventry University and center of map
    center: new google.maps.LatLng(52.407175, -1.504036),  
        });

    directionsDisplay.setMap(map);
    document.getElementById('submit').addEventListener('click', function() {
        calcRoute(directionsService, directionsDisplay);
   
   });     
   
   setMarkers(map);
   
    
  /*  directionsDisplay.addListener('directions_changed', function() {
    computeTotalDistance(directionsDisplay.getDirections());
   
  }); */
    infoWindow = new google.maps.InfoWindow;
    
    // var contentString = 
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
            position: new google.maps.LatLng(52.408070, -1.506023), //Alan Berry Building (CV1 5FB)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.4100173, -1.5026316), //Alma Building (CV1 5QA)
            type: 'info' 
          }, {
            position: new google.maps.LatLng(52.4075382, -1.5033031), //Armstrong Siddeley Building (CV1 5DL)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.407482, -1.502899), //Bugatti Building (CV1 5PH)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.408580, -1.504723), //Charles Ward Building (CV1 5FD)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.4052898, -1.501848), //Engineering & Computing Building (CV1 2JH)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.4066632, -1.506845), //Ellen Terry Building (CV1 5RW)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.408127,  -1.505058), //George Eliot Building (CV1 5FB)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.406976, -1.503427), //Graham Sutherland Building (CV1 5PH)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.405766, -1.500751), //Frederick Lanchester Library Building (CV1 5DD)
            type: 'library'
          }, {
            position: new google.maps.LatLng(52.406878, -1.500965), //Jaguar Building (CV1 5DL)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.4074963, -1.5069194), //TheHub Building (CV1 5FB)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.4078156, -1.5053153), //Maurice Foss Building (CV1 5PH)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.4077121, -1.5062505), //James Starley Building (CV1 5FB)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.4060105, -1.5016446), //Multi-Storey Car Park Building (CV1 5DE)
            type: 'parking'
          }, {
            position: new google.maps.LatLng(52.409127, -1.506061), //Priory Building (CV1 5FB)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.406743, -1.505417), // Richard Crossman Building (CV1 5RW)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.4054596, -1.5061344), //Alison Gingell Building (CV1 2DS)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.4058614, -1.5071858), //Sir John Laing Building (CV1 2LT)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.407411, -1.499745), //Sir William Lyons Building (CV1 5DL)
            type: 'info'  
          }, {
            position: new google.maps.LatLng(52.404934, -1.500546), //Student Centre Building (CV1 2JH)
            type: 'info'
          }, {
            position: new google.maps.LatLng(52.406156, -1.504071), //Whitefriars Building (CV1 2DS)
            type: 'info'  
          }, {
            position: new google.maps.LatLng(52.405602, -1.503907), //Sports Centre Building (CV1 2DS)
            type: 'info'  
          }
        ];
         
        // Create markers.
        features.forEach(function(feature, buildingNames) {
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
                  
          var buildingNames = [
  ['Alan Berry Building', 52.408070, -1.506023, 1],
  ['Alma Building', 52.4100173, -1.5026316, 2],
  ['Armstrong Siddeley Building', 52.4075382, -1.5033031, 3],
  ['Bugatti Building', 52.407482, -1.502899, 4],
  ['Charles Ward Building', 52.408580, -1.504723, 5],
  ['Engineering And Computing Building', 52.4052898, -1.501848, 6],
  ['Ellen Terry Building', 52.4066632, -1.506845, 7],
  ['George Eliot Building', 52.408127, -1.505058, 8],
  ['Graham Sutherland Building', 52.406976, -1.503427, 9],
  ['Frederick Lanchester Library Building', 52.405766, -1.500751, 10],
  ['Jaguar Building', 52.406878, -1.500965, 11],
  ['TheHub Building', 52.4074963, -1.5069194, 12],
  ['Maurice Foss Building', 52.4078156, -1.5053153, 13],
  ['James Starley Building', 52.4077121, -1.5062505, 14],
  ['Multi-Storey Car Park Building', 52.4060105, -1.5016446, 15],
  ['Priory Building', 52.409127, -1.506061, 16],
  ['Richard Crossman Building', 52.406743, -1.505417, 17],
  ['Alison Gingell Building', 52.4054596, -1.5061344, 18],
  ['Sir John Laing Building', 52.4058614, -1.5071858, 19],
  ['Sir William Lyons Building', 52.407411, -1.499745, 20],
  ['Student Centre Building', 52.404934, -1.500546, 21],
  ['Whitefriars Building', 52.406156, -1.504071, 22],
  ['Sports Centre Building 1', 52.405602, -1.503907, 23] 
  ];
  
  
function setMarkers(map){  
    var shape = {
          coords: [1, 1, 1, 20, 18, 20, 18, 1],
          type: 'poly'
        };
  for (var i = 0; i < buildingNames.length; i++) {
          var buildingName = buildingNames[i];
          var marker2 = new google.maps.Marker({
            position: {lat: buildingName[1], lng: buildingName[2]},
            map: map,
            icon: 'info' + 'parking' + 'library',
            shape: shape,
            title: buildingName[0],
            zIndex: buildingName[5]
          });
          
          }
          }
          
function calcRoute(directionsService, directionsDisplay) {
  travelMode: 'BICYCLING';
  travelMode: 'WALKING'
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
    travelMode: 'BICYCLING',
    travelMode: 'WALKING'
  }, function(response, status) {
    if (status === 'OK') {
    //  display.setDirections(response);  
      directionsDisplay.setDirections(response);
      var route = response.routes[0];
      var summaryPanel = document.getElementById('directions-panel');
      summaryPanel.innerHTML = '';
      // For each route, display summary information.
      for (var i = 0; i < route.legs.length; i++) {
        var routeSegment = i + 1;
        summaryPanel.innerHTML += '<b>Route Path: ' + routeSegment +
            '</b><br> Start Address: <br>';
        summaryPanel.innerHTML += route.legs[i].start_address + ' to <br> Finish Address: <br>';
        summaryPanel.innerHTML += route.legs[i].end_address + '<br> Total Time: <br>';
        summaryPanel.innerHTML += route.legs[i].duration.text + '<br> Distance (km): <br>';
        summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>';
      }
    } else {
      window.alert('Directions request failed due to... ' + status);
    }
  });
}

function showSteps(directionResult, markerArray, stepDisplay, map) {
  // For each step, place a marker, and add the text to the marker's infowindow.
  // Also attach the marker to an array so we can keep track of it and remove it
  // when calculating new routes.
  var myRoute = directionResult.routes[0].legs[0];
  for (var i = 0; i < myRoute.steps.length; i++) {
    var marker = markerArray[i] = markerArray[i] || new google.maps.Marker;
    marker.setMap(map);
    marker.setPosition(myRoute.steps[i].start_location);
    attachInstructionText(
        stepDisplay, marker, myRoute.steps[i].instructions, map);
  }
}

function attachInstructionText(stepDisplay, marker, text, map) {
  google.maps.event.addListener(marker, 'click', function() {
    // Open an info window when the marker is clicked on, containing the text
    // of the step.
    stepDisplay.setContent(text);
    stepDisplay.open(map, marker);
  });
}
        
function computeTotalDistance(result) {
  var total = 0;
  var myroute = result.routes[0];
  for (var i = 0; i < myroute.legs.length; i++) {
    total += myroute.legs[i].distance.value;
  }
  total = total / 1000;
  document.getElementById('total').innerHTML = total + ' km';
}
