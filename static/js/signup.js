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

$("#submit").on("click", function(e) {
	nama = $("#id_nama").val();
	ktp = $("#id_ktp").val();
	email = $("#id_email").val();
	tgl_lahir = $("#id_tgl_lahir").val();
	no_telp = $("#id_no_telp").val();
	alamat = $("#id_alamat").val();
	role = $("#id_role").val();
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

$("#login").on("click", function(e) {
	ktp = $("#id_ktp_login").val();
	email = $("#id_email_login").val();
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
			} else {
				alert("Salah memasukkan ktp atau email.");
			}
		}
	});
	event.preventDefault();
});

$("#id_ktp").on("focusin", function() {
	ktp = $("#id_ktp").val();
	email = $("#id_email").val();
	$("#loading-ktp").html(
		"<div class='loading'></div><div class='loading'></div>"
	);
});

$("#id_email").on("focusin", function() {
	ktp = $("#id_ktp").val();
	email = $("#id_email").val();
	$("#loading-email").html(
		"<div class='loading'></div><div class='loading'></div>"
	);
});

$("#id_ktp").on("focusout", function() {
	ktp = $("#id_ktp").val();
	email = $("#id_email").val();
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
				$("#alert").html("<div class='alert'>" + data.error + "</div>");
				$("#submit").prop("disabled", true);
			} else {
				$("#alert").html("");
			}
			$("#loading-ktp").html("");
		}
	});
	event.preventDefault();
});

$("#id_email").on("focusout", function() {
	ktp = $("#id_ktp").val();
	email = $("#id_email").val();
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
				$("#alert").html("<div class='alert'>" + data.error + "</div>");
				$("#submit").prop("disabled", true);
			} else {
				$("#alert").html("");
			}
			$("#loading-email").html("");
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
});

$("input").on("keyup", function() {
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
});
