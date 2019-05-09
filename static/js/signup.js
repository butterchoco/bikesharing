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
		}
	});
	event.preventDefault();
});

$("#login").on("click", function(e) {
	let ktpLogin = $("#id_ktp_login").val();
	let emailLogin = $("#id_email_login").val();
	$.ajax({
		method: "POST",
		url: "/user/authenticating/",
		type: "json",
		data: {
			ktp: ktpLogin,
			email: emailLogin
		},
		success: function(data) {
			console.log(data);
			if (data.is_taken) {
				window.location.href = "/report";
			} else {
				alert("Salah memasukkan ktp atau email.");
			}
		}
	});
	event.preventDefault();
});

$("#id_ktp").on("keyup", function() {
	$("#loading-ktp").html(
		"<div class='loading'></div><div class='loading'></div>"
	);
});

$("#id_email").on("keyup", function() {
	$("#loading-email").html(
		"<div class='loading'></div><div class='loading'></div>"
	);
});

$("input").on("keyup", function() {
	let ktpsignup = $("#id_ktp").val();
	let emailsignup = $("#id_email").val();
	let namasignup = $("#id_nama").val();
	let alamatsignup = $("#id_alamat").val();
	let tgl_lahirsignup = $("#id_tgl_lahir").val();
	let rolesignup = $("id_role").val();
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
	$.ajax({
		method: "POST",
		url: "/user/validating/",
		type: "json",
		data: {
			ktp: ktpsignup,
			email: emailsignup
		},
		success: function(data) {
			if (data.is_taken) {
				$("#alert").html(
					"<div class='alert'>Ktp atau email sudah terpakai.</div>"
				);
				$("#loading-ktp").html("");
				$("#loading-email").html("");
				$("#submit").prop("disabled", true);
			} else {
				$("#alert").html("");
				$("#loading-ktp").html("");
				$("#loading-email").html("");
			}
		}
	});
	event.preventDefault();
});
