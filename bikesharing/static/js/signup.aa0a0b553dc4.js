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

var successSignup = function() {
	ktp = $("#id_ktp").val();
	email = $("#id_email").val();
	$.ajax({
		method: "POST",
		url: "/user/authenticating/",
		type: "json",
		data: {
			ktp: ktp,
			email: email
		},
		success: function(data) {
			if (data.is_taken) {
				location.reload(true);
			}
		}
	});
};

var validate = function() {
	ktp = $("#id_ktp").val();
	email = $("#id_email").val();
	if ($("#id_ktp").is(":focus")) {
		$("#loading-ktp").html(
			'<div class="sk-circle1 sk-child"></div><div class="sk-circle2 sk-child"></div><div class="sk-circle3 sk-child"></div><div class="sk-circle4 sk-child"></div><div class="sk-circle5 sk-child"></div><div class="sk-circle6 sk-child"></div><div class="sk-circle7 sk-child"></div><div class="sk-circle8 sk-child"></div><div class="sk-circle9 sk-child"></div><div class="sk-circle10 sk-child"></div><div class="sk-circle11 sk-child"></div><div class="sk-circle12 sk-child"></div>'
		);
	} else if ($("#id_email").is(":focus")) {
		$("#loading-email").html(
			'<div class="sk-circle1 sk-child"></div><div class="sk-circle2 sk-child"></div><div class="sk-circle3 sk-child"></div><div class="sk-circle4 sk-child"></div><div class="sk-circle5 sk-child"></div><div class="sk-circle6 sk-child"></div><div class="sk-circle7 sk-child"></div><div class="sk-circle8 sk-child"></div><div class="sk-circle9 sk-child"></div><div class="sk-circle10 sk-child"></div><div class="sk-circle11 sk-child"></div><div class="sk-circle12 sk-child"></div>'
		);
	}
	$.ajax({
		method: "POST",
		url: "/user/validating/",
		type: "json",
		data: {
			ktp: ktp,
			email: email
		},
		success: function(data) {
			if (data.is_taken) {
				$(".alert").html("<div id='alert-msg'>" + data.error + "</div>");
				$("#submit").prop("disabled", true);
			} else {
				$(".alert").html("");
			}
			if (ktp != "" && email != "") {
				$("#loading-ktp").html("");
				$("#loading-email").html("");
			} else if (email != "") {
				$("#loading-email").html("");
			} else if (ktp != "") {
				$("#loading-ktp").html("");
			} else if (ktp == "" && email == "") {
				$("#loading-ktp").html("");
				$("#loading-email").html("");
			}
		}
	});
	event.preventDefault();
};

$("#signup-in-trans").on("click", function() {
	$(".alert").html("");
	$("#id_nama").val("");
	$("#id_ktp").val("");
	$("#id_email").val("");
	$("#id_tgl_lahir").val("");
	$("#id_no_telp").val("");
	$("#id_alamat").val("");
	$("#id_role").val("");
});

$("#submit").on("click", function(e) {
	let nama = $("#id_nama").val();
	let ktp = $("#id_ktp").val();
	let email = $("#id_email").val();
	let tgl_lahir = $("#id_tgl_lahir").val();
	let no_telp = $("#id_no_telp").val();
	let alamat = $("#id_alamat").val();
	let role = $("#id_role").val();
	$.ajax({
		method: "POST",
		url: "/user/signing+up/",
		type: "json",
		data: {
			nama: nama,
			ktp: ktp,
			email: email,
			tgl_lahir: tgl_lahir,
			no_telp: no_telp,
			alamat: alamat,
			role: role
		},
		success: function(data) {
			alert("success");
			successSignup();
		}
	});
	event.preventDefault();
});

$("select").on("change", function() {
	ktp = $("#id_ktp").val();
	email = $("#id_email").val();
	ktp = $("#id_ktp").val();
	email = $("#id_email").val();
	nama = $("#id_nama").val();
	alamat = $("#id_alamat").val();
	tgl_lahir = $("#id_tgl_lahir").val();
	role = $("#id_role").val();
	no_telp = $("#id_no_telp").val();

	if (
		ktp == "" ||
		email == "" ||
		nama == "" ||
		alamat == "" ||
		tgl_lahir == "" ||
		role == "" ||
		no_telp == ""
	) {
		$("#submit").prop("disabled", true);
	} else {
		$("#submit").prop("disabled", false);
	}
	validate();
});

$("input").on("keyup", function() {
	let ktpsignup = $("#id_ktp").val();
	let emailsignup = $("#id_email").val();
	let namasignup = $("#id_nama").val();
	let alamatsignup = $("#id_alamat").val();
	let tgl_lahirsignup = $("#id_tgl_lahir").val();
	let rolesignup = $("#id_role").val();
	let no_telpsignup = $("#id_no_telp").val();

	if (
		ktpsignup === "" ||
		emailsignup === "" ||
		namasignup === "" ||
		alamatsignup === "" ||
		tgl_lahirsignup === "" ||
		rolesignup === "" ||
		no_telpsignup === ""
	) {
		$("#submit").prop("disabled", true);
	} else {
		$("#submit").prop("disabled", false);
	}
	validate();
});
