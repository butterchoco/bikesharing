const animation = document.getElementById('animation');
const signup = document.getElementById('signup-home');
const description = document.getElementById('description');
const formDesktop = document.getElementById('signup-form-desktop');
const formMobile = document.getElementById('signup-form-mobile');
const absolute = document.getElementsByClassName('absolute');

signup.addEventListener('click', () => {
    if (screen.width <= 800) {
        animation.style.width = '100vw';
        animation.style.height = '100vh';
        animation.style.clipPath = 'circle(70.7% at 50% 50%)';
        formMobile.innerHTML = '<form role="form"><div class="form-group"><label for="exampleInputNoKTP1">No KTP</label><input type="text" class="form-control" id="exampleInputNoKTP1" /></div><div class="form-group"><label for="exampleInputname1">Nama Lengkap</label><input type="name" class="form-control" id="exampleInputname1" /></div><div class="form-group"><label for="exampleInputEmail1">Email address</label><input type="email" class="form-control" id="exampleInputEmail1" /></div><div class="form-group"><label for="exampleInputTanggalLahir1">Tanggal Lahir address</label><input type="date" class="form-control" id="exampleInputTanggalLahir1" /></div><div class="form-group"><label for="exampleInputNoTlp1">No. Telepon</label><input type="text" class="form-control" id="exampleInputNoTlp1" /></div><div class="form-group"><label for="exampleInputAlamat1">Alamat</label><input type="text" class="form-control" id="exampleInputAlamat1" /></div><div class="checkbox"><label><input type="checkbox" /> Setuju dengan ketentuan dan peraturan yang berlaku.</label></div> <button type="submit" class="btn btn-green m-3">Sign up</button></form>';
        formMobile.style.marginTop = '';
        formMobile.style.opacity = '1';
        formMobile.style. height = 'auto';
        formMobile.style.visibility = 'visible';
        absolute[0].style.position = 'static';
        absolute[0].style.top = "0";
        absolute[0].style.height = "100vh";
        absolute[0].style.transform = "translate(0, 30%)";
    } else {
        animation.style.width = '130em';
        animation.style.height = '130em';
        animation.style.top = '50%';
        animation.style.left = '10%';
        animation.style.transform = 'translate(-20%,-50%)';
        formDesktop.innerHTML = '<form role="form"><div class="form-group"><label for="exampleInputNoKTP1">No KTP</label><input type="text" class="form-control" id="exampleInputNoKTP1" /></div><div class="form-group"><label for="exampleInputname1">Nama Lengkap</label><input type="name" class="form-control" id="exampleInputname1" /></div><div class="form-group"><label for="exampleInputEmail1">Email address</label><input type="email" class="form-control" id="exampleInputEmail1" /></div><div class="form-group"><label for="exampleInputTanggalLahir1">Tanggal Lahir address</label><input type="date" class="form-control" id="exampleInputTanggalLahir1" /></div><div class="form-group"><label for="exampleInputNoTlp1">No. Telepon</label><input type="text" class="form-control" id="exampleInputNoTlp1" /></div><div class="form-group"><label for="exampleInputAlamat1">Alamat</label><input type="text" class="form-control" id="exampleInputAlamat1" /></div><div class="checkbox"><label><input type="checkbox" /> Setuju dengan ketentuan dan peraturan yang berlaku.</label></div> <button type="submit" class="btn btn-green m-3">Sign up</button></form>';
        formDesktop.style.marginTop = '';
        formDesktop.style.opacity = '1';
        formDesktop.style. height = 'auto';
        formDesktop.style.visibility = 'visible';
    }
    description.style.opacity = '0';
    description.innerHTML = '';
})

window.addEventListener('scroll', () => {
    const target = document.querySelectorAll('.scroll-parallax');
    
    
    var index = 0, length = target.length;
    if (window.pageYOffset < window.innerHeight) {
        for (index; index < length; index++) {
            var pos = window.pageYOffset * target[index].dataset.rate;
            
            if(target[index].dataset.direction === 'vertical'){
                target[index].style.transform = 'translate3d(0px, '+pos+'px, 0px)';
            } else {
                var posX = windows.pageYOffset * target[index].dataset.ratex;
                var posY = windows.pageYOffset * target[index].dataset.ratey;

                target[index].style.transform = 'translate3d('+posX+'px, '+posY+'px, 0px)';
            }
        }
    }
})