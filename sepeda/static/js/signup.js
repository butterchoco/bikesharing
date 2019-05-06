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

$("#submit_form").on('click', function(e) {
    nama = $('#id_nama').val()
    ktp = $('#id_ktp').val()
    email = $('#id_email').val()
    tgl_lahir = $('#id_tgl_lahir').val()
    no_telp = $('#id_no_telp').val()
    alamat = $('#id_alamat').val()
    $.ajax({
        method: "POST",
        url: "/registrasi/",
        data: {
            "nama": nama,
            "ktp": ktp,
            "email": email,
            "tgl_lahir": tgl_lahir,
            "no_telp": no_telp,
            "alamat": alamat,
        },
        success: function(data) {
            console.log("success")
        }
    })
    event.preventDefault();
})