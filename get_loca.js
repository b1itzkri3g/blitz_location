function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
        	div.innerHTML = "The Browser Does not Support Geolocation";
        }
      }
function loadDoc(lat,lon) {
  const xhttp = new XMLHttpRequest();
  xhttp.open("POST", "result.php");
  xhttp.onload = function() {
    document.getElementById("demo").innerHTML = this.responseText;
  }
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("lat="+lat+"&lon="+lon);
}

function showPosition(position) {
	var lat = position.coords.latitude;
	var lon = position.coords.longitude;
	loadDoc(lat,lon);
      }

function showError(error) {
	window.alert("Please reenter link and allow location access");
	getLocation();
	if(error.PERMISSION_DENIED){
		div.innerHTML = "The User have denied the request for Geolocation.";
        }
      }
      


getLocation();



