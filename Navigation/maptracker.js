// Style of the website (size)

//HTML
<!DOCTYPE html>
<html>
  <head>
    <title>Geolocation</title>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      map {
        height: 100%;
      }
      // Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>
        
/* Through the use of a Google geolocation API key this will
prompt a student to consent to providing their location through their browser
and have it displayed on google maps for them. */

var map, infoWindow;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 52.405314, lng: -1.500063},
    zoom: 14
  });
  infoWindow = new google.maps.InfoWindow;

  // Try HTML5(?) geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      infoWindow.setPosition(pos);
      infoWindow.setContent('Location found.');
      infoWindow.open(map);
      map.setCenter(pos);
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // In the case that the student's Browser doesn't support Geolocation:
    handleLocationError(false, infoWindow, map.getCenter());
  }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}

/*
</script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDHbYqwiDtGA8Zof2xXZVfGnnWrvEX09rw&callback=initMap">
    </script>
  </body>
</html>


// https://www.youtube.com/watch?v=Y5PtPYyrbYY - Reference
/* Allows students' to add any place within google map's database
 * and use a auto complete form to show relative possible results */


var autocomplete = new googlemaps.places.Autocomplete(DOM_MODE);

autocomplete.bindTo('bounds', map);
autocomplete.addEventListner('place_changed') 
 //   conat place = autocomplete.getPlace();    



/* Here the student can be given the fastest possible algorithms
/ within google's algorithms and herustics to determine the fastest possible route. */

/*
const calculateAndRenderDirections = {origin, destination} => {
    let directionsService = new google.maps.DirectionsService(), 
        // Calculates the directions needed to take to get there.
        directionDisplay = new google.maps.DirectionsRender(),
        // This renders a visual result of the directions to the map.
        request = {origin: origin
                  destination: destination,
                  travelMode: 'WALKING',
                  avoid: 'highways' 
                  }
    directionsDIsplay.netMap(map);
    directionsSerice.route{request, (result, status) => {
    if (status == 'OK') {
        directionsDisplay.netDirections(result);
    }
}
    
}

function directionMode ()
{
  origin: LatLng | String | google.maps.Place,
  destination: LatLng | String | google.maps.Place,
  travelMode: TravelMode,
  transitOptions: TransitOptions,
  drivingOptions: DrivingOptions,
  unitSystem: UnitSystem,
  waypoints[]: DirectionsWaypoint,
  optimizeWaypoints: Boolean,
  provideRouteAlternatives: Boolean,
  avoidFerries: Boolean,
  avoidHighways: Boolean,
  avoidTolls: Boolean,
  region: String
}

function usersCoordinates()
{
    
}


//Unfinished map call function.
let map = new google.maps.Map(document.getElementbyId('map')
{
    center: {lat:52.405314 lng: -1.500063}
    zoom: 14
}); 



// HTTPS > HTTP but both are possible.
 
/* Directions API requests example     
https://maps.googleapis.com/maps/api/directions/json?
origin=Covetry&destination=London
&avoid=highways
&mode=walking
&key=AIzaSyDHbYqwiDtGA8Zof2xXZVfGnnWrvEX09rw */  
    
/* Geolocation API Requests Example
 * https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDHbYqwiDtGA8Zof2xXZVfGnnWrvEX09rw */
    
/* Google Maps JS API Requests Example
 * https://www.googleapis.com/ */
    
/* Google Maps Gecoding API (?) Requests Example
 * https://www.googleapis.com/ */

// AIzaSyCkUOdZ5y7hMm0yrcCQoCvLwzdM6M8s5qk