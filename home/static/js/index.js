
const animation = document.getElementById('animation');
const signup = document.getElementById('signup-home');
const description = document.getElementById('description');
const form = document.getElementById('signup-form');

signup.addEventListener('click', () => {
    animation.style.width = '100vw';
    animation.style.height = '100vh';
    animation.style.clipPath = 'circle(70.7% at 50% 50%)';
    description.style.opacity = '0';
    description.style.visibility = 'hidden';
    form.innerHTML = '<form role="form"><div class="form-group"><label for="exampleInputNoKTP1">No KTP</label><input type="text" class="form-control" id="exampleInputNoKTP1" /></div><div class="form-group"><label for="exampleInputname1">Nama Lengkap</label><input type="name" class="form-control" id="exampleInputname1" /></div><div class="form-group"><label for="exampleInputEmail1">Email address</label><input type="email" class="form-control" id="exampleInputEmail1" /></div><div class="form-group"><label for="exampleInputTanggalLahir1">Tanggal Lahir address</label><input type="date" class="form-control" id="exampleInputTanggalLahir1" /></div><div class="form-group"><label for="exampleInputNoTlp1">No. Telepon</label><input type="text" class="form-control" id="exampleInputNoTlp1" /></div><div class="form-group"><label for="exampleInputAlamat1">Alamat</label><input type="text" class="form-control" id="exampleInputAlamat1" /></div><div class="checkbox"><label><input type="checkbox" /> Setuju dengan ketentuan dan peraturan yang berlaku.</label></div> <button type="submit" class="btn btn-green m-3">Sign up</button></form>';
    form.style.marginTop = '0';
    form.style.opacity = '1';
    form.style. height = 'auto';
    form.style.visibility = 'visible';
})