$(document).ready(function() {
	let ripplePlaceholder = document.getElementById("ripplePlaceholder");
	let buttonTransition = document.getElementsByClassName("transition");
	let signup = document.getElementById("signup");
	let signin = document.getElementById("signin");
	let signupTitle = document.getElementById("signup-title");
	let signinTitle = document.getElementById("signin-title");

	let signupTrans = document.getElementById("signup-trans");
	let loginTrans = document.getElementById("login-trans");
	let description = document.getElementById("description");
	let formCard = document.getElementById("form-card");
	let page1 = document.getElementById("page1");

	signupTrans.addEventListener("click", function() {
		if (window.innerWidth < 800) {
			page1.style.height = "150%";
			page1.style.overflowY = "scroll";
		}
		formCard.classList.add("slide-up");
		description.classList.add("fade-out");
		description.hidden = true;
		formCard.hidden = false;
		signupTitle.hidden = false;
		signup.hidden = false;
	});

	loginTrans.addEventListener("click", function() {
		if (window.innerWidth < 800) {
			page1.style.height = "150%";
			page1.style.overflowY = "scroll";
		}
		formCard.classList.add("slide-up");
		description.classList.add("fade-out");
		description.hidden = true;
		formCard.hidden = false;
		signinTitle.hidden = false;
		signin.hidden = false;
	});

	// Dari SignIn form ke SignUp form
	let signupInTrans = document.getElementById("signup-in-trans");
	$("#signup-in-trans").on("click", function() {
		signin.classList.add("fade-out");
		signup.classList.add("fade-in");
		signupTitle.hidden = false;
		signinTitle.hidden = true;
		signup.hidden = false;
		signin.hidden = true;
	});

	// Dari SignUp form ke SignIn form
	let signinTrans = document.getElementById("signin-trans");
	$("#signin-trans").on("click", function() {
		signup.classList.add("fade-out");
		signin.classList.add("fade-in");
		signinTitle.hidden = false;
		signupTitle.hidden = true;
		signup.hidden = true;
		signin.hidden = false;
	});

	Array.prototype.forEach.call(buttonTransition, function(b) {
		b.addEventListener("click", ripple);
	});

	function ripple(e) {
		let transitionEffect = document.createElement("div");
		transitionEffect.setAttribute("id", "transition");
		transitionEffect.classList.add(this.dataset.color);
		ripplePlaceholder.appendChild(transitionEffect);

		var d = Math.max(document.body.clientWidth * 3);
		if (window.innerWidth < 800) d = Math.max(document.body.clientWidth * 5);
		transitionEffect.style.width = transitionEffect.style.height = d + "px";
		transitionEffect.style.left = e.clientX - d / 2 + "px";
		transitionEffect.style.top = e.clientY - d / 2 + "px";
	}
});
