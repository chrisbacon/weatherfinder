jQuery(window).ready(function(){
            $("#btnInit").click(initiate_geolocation);
            $('#search_button').click(search);
            $("div#data").hide();
        });

function initiate_geolocation() {
    navigator.geolocation.getCurrentPosition(handle_geolocation_query);
}

function handle_geolocation_query(position){
    get_weather_report(position.coords.longitude, position.coords.latitude);
}

function get_weather_report(lng, lat){
    $("div#data").hide()
    jQuery.post("/weather",
    {
        lng: lng,
        lat: lat
    },
    function(data){
        $.each(data, function(index, value) {
            $("span#" + index).text(value)
        });
        $("div#data").fadeIn()
    })
    .fail(function() {
        $("p#location").text("Something went wrong!!");
        $("div#data").fadeIn()
    });
}

function search() {
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode(
        {'address': $('#search_field').val()},
        function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                var loc = results[0].geometry.location;
                get_weather_report(loc.lng(), loc.lat());
            }
            else {
                alert("Not found: " + status);
            }
        }
    );
}