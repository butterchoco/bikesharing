function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== "") {
		var cookies = document.cookie.split(";");
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === name + "=") {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

var csrftoken = getCookie("csrftoken");

$.ajaxSetup({
	beforeSend: function(xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});

$("#login").on("click", function(e) {
	let ktpLogin = $("#id_ktp_login").val();
	let emailLogin = $("#id_email_login").val();
	$("#loading-screen").html(
		'<div class="sk-circle1 sk-child"></div><div class="sk-circle2 sk-child"></div><div class="sk-circle3 sk-child"></div><div class="sk-circle4 sk-child"></div><div class="sk-circle5 sk-child"></div><div class="sk-circle6 sk-child"></div><div class="sk-circle7 sk-child"></div><div class="sk-circle8 sk-child"></div><div class="sk-circle9 sk-child"></div><div class="sk-circle10 sk-child"></div><div class="sk-circle11 sk-child"></div><div class="sk-circle12 sk-child"></div>'
	);
	$.ajax({
		method: "POST",
		url: "/user/authenticating/",
		type: "json",
		data: {
			ktp: ktpLogin,
			email: emailLogin
		},
		success: function(data) {
			if (data.is_taken) {
				location.reload(true);
			} else {
				$("#loading-screen").html("");
				$(".alert").html(
					"<div class='alert-msg'>Salah memasukkan ktp atau email.</div>"
				);
			}
		}
	});
	event.preventDefault();
});
