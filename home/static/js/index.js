
const animation = document.getElementById('animation');
const signup = document.getElementById('signup-home');
const description = document.getElementById('description');
const form = document.getElementById('signup-form');

signup.addEventListener('click', () => {
    animation.style.width = '100vw';
    animation.style.height = '100vh';
    animation.style.clipPath = 'circle(70.7% at 50% 50%)';
    description.style.marginTop = '10em';
    description.style.opacity = '0';
    description.style.visibility = 'hidden';
    form.style.opacity = '1';
    form.style.width = '40em';
    form.style. height = 'auto';
    form.style.visibility = 'visible';
})