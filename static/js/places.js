function initMap() {
  
  var input = document.getElementById('search');
  


  var autocomplete = new google.maps.places.Autocomplete(input);

  // Bind the map's bounds (viewport) property to the autocomplete object,
  // so that the autocomplete requests use the current map bounds for the
  // bounds option in the request.

  // Set the data fields to return when the user selects a place.

  
      

  // Sets a listener on a radio button to change the filter type on Places
  // Autocomplete.
  

  
}

$(document).ready(function () {
   
   google.maps.event.addDomListener(window, 'load', initMap);

});