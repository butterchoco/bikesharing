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

$("#submit").on("click", function() {
	let voucher_id = $("#voucher_id").val();
	let voucher_nama = $("#voucher_nama").val();
	let voucher_kategori = $("#voucher_kategori").val();
	let voucher_nilai_poin = $("#voucher_poin").val();
	let voucher_deskripsi = $("#voucher_deskripsi").val();
	let voucher_no_kartu_anggota = null;
	if (voucher_nilai_poin > 0) {
		$("#modal-transaction").css("display", "none");
		$("#loading-screen").html(
			'<div class="sk-circle1 sk-child"></div><div class="sk-circle2 sk-child"></div><div class="sk-circle3 sk-child"></div><div class="sk-circle4 sk-child"></div><div class="sk-circle5 sk-child"></div><div class="sk-circle6 sk-child"></div><div class="sk-circle7 sk-child"></div><div class="sk-circle8 sk-child"></div><div class="sk-circle9 sk-child"></div><div class="sk-circle10 sk-child"></div><div class="sk-circle11 sk-child"></div><div class="sk-circle12 sk-child"></div>'
		);
		$.ajax({
			method: "POST",
			url: "/voucher/add/",
			data: {
				id_voucher: voucher_id,
				nama: voucher_nama,
				kategori: voucher_kategori,
				nilai_poin: voucher_nilai_poin,
				deskripsi: voucher_deskripsi,
				no_kartu_anggota: voucher_no_kartu_anggota
			},
			success: function(data) {
				location.reload(true);
			}
		});
		event.preventDefault();
	} else {
		alert("You must specified correct value. Minus value is not allowed!");
	}
});


var modalbtn = document.getElementsByClassName("modal-btn");
var modal = "";

Array.prototype.forEach.call(modalbtn, function (b) {
	b.addEventListener("click", function() {
		modal = document.getElementById(this.dataset.target);
		modal.style.display = "block";
	});
});

window.onclick = function(event) {
	if (event.target == modal) {
		modal.style.display = "none";
	}
};