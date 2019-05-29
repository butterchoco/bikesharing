function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$("#submit").on("click", function() {
    let brand = $("#id_brand").val();
    let type = $("#id_type").val();
    let status = $("#id_status").val();
    if (status == "Tersedia") status = true;
    else status = false;
    let station = $("#id_station").val();
    let pendonor = $("#id_pendonor").val();
		$("#modal-container").css("display", "none");
		$("#loading-screen").html(
			'<div class="sk-circle1 sk-child"></div><div class="sk-circle2 sk-child"></div><div class="sk-circle3 sk-child"></div><div class="sk-circle4 sk-child"></div><div class="sk-circle5 sk-child"></div><div class="sk-circle6 sk-child"></div><div class="sk-circle7 sk-child"></div><div class="sk-circle8 sk-child"></div><div class="sk-circle9 sk-child"></div><div class="sk-circle10 sk-child"></div><div class="sk-circle11 sk-child"></div><div class="sk-circle12 sk-child"></div>'
		);
		$.ajax({
			method: "POST",
			url: "/sepeda/add/",
			data: {
                brand: brand,
                type: type,
                status: status,
                station: station,
                pendonor: pendonor
			},
			success: function(data) {
				location.reload(true);
			}
		});
		event.preventDefault();
});

$(".delete").on("click", function (b) {
    let number = $(this).attr("id")
    $.ajax({
        method: "POST",
        url: "/sepeda/delete/",
        data: {
            number: number
        },
        success: function (data) {
            location.reload(true);
        }
    });
    event.preventDefault();
})

var numberData = "";
$("#update-form").on("click", function () {
    let brand = $("#id_brand_update").val();
    let type = $("#id_type_update").val();
    let status = $("#id_status_update").val();
    if (status == "Tersedia") status = true;
    else status = false;
    let station = $("#id_station_update").val();
    let pendonor = $("#id_pendonor_update").val();
    console.log(numberData)
		$("#modal-update").css("display", "none");
		$("#loading-screen").html(
			'<div class="sk-circle1 sk-child"></div><div class="sk-circle2 sk-child"></div><div class="sk-circle3 sk-child"></div><div class="sk-circle4 sk-child"></div><div class="sk-circle5 sk-child"></div><div class="sk-circle6 sk-child"></div><div class="sk-circle7 sk-child"></div><div class="sk-circle8 sk-child"></div><div class="sk-circle9 sk-child"></div><div class="sk-circle10 sk-child"></div><div class="sk-circle11 sk-child"></div><div class="sk-circle12 sk-child"></div>'
		);
		$.ajax({
			method: "POST",
			url: "/sepeda/update/",
            data: {
                number: numberData,
                brand: brand,
                type: type,
                status: status,
                station: station,
                pendonor: pendonor
			},
			success: function(data) {
				location.reload(true);
			}
		});
		event.preventDefault();
})

var modalbtn = document.getElementsByClassName("modal-update");
var modal = "";

Array.prototype.forEach.call(modalbtn, function (b) {
	b.addEventListener("click", function() {
		modal = document.getElementById(this.dataset.target);
        modal.style.display = "block";
        numberData = $(this).attr('id');
	});
});