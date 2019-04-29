const ripplePlaceholder = document.getElementById('ripplePlaceholder');
const buttonTransition = document.getElementsByClassName('transition');
const signup = document.getElementById('signup');
const signin = document.getElementById('signin');
const signupTitle = document.getElementById('signup-title');
const signinTitle = document.getElementById('signin-title');

const signupTrans = document.getElementById('signup-trans');
const description = document.getElementById('description');
const signupGroup = document.getElementById('signup-group');
const page1 = document.getElementById('page1')
signupTrans.addEventListener('click', function() {
    if(window.innerWidth < 800) {
        page1.style.height = '135vh';
        page1.style.overflowY = 'scroll';
    }
    signupGroup.classList.add('slide-up');
    description.classList.add('fade-out');
    signupTitle.hidden = false;
    signupGroup.hidden = false;
    description.hidden = true;
});

const signupInTrans = document.getElementById('signup-in-trans');
signupInTrans.addEventListener('click', function() {
    signin.classList.add('fade-out');
    signup.classList.add('fade-in');
    signupTitle.hidden = false;
    signinTitle.hidden = true;
    signup.hidden = false;
    signin.hidden = true;
});

const signinTrans = document.getElementById('signin-trans');
signinTrans.addEventListener('click', function() {
    signup.classList.add('fade-out');
    signin.classList.add('fade-in');
    signinTitle.hidden = false;
    signupTitle.hidden = true;
    signup.hidden = true;
    signin.hidden = false;
});

Array.prototype.forEach.call(buttonTransition, function(b) {
    b.addEventListener('click', ripple)
});


function ripple(e) {
    const transitionEffect = document.createElement('div');
    transitionEffect.setAttribute('id', 'ripple');
    transitionEffect.classList.add(this.dataset.color)
    ripplePlaceholder.appendChild(transitionEffect);

    var d = Math.max(document.body.clientWidth*3);
    if (window.innerWidth < 400) d = Math.max(document.body.clientWidth*5);
    transitionEffect.style.width = transitionEffect.style.height = d + 'px';
    transitionEffect.style.left = e.clientX - d/2 + 'px';
    transitionEffect.style.top = e.clientY - d/2 + 'px';

}