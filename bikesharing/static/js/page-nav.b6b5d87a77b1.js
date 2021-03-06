const toggleSidebar = document.getElementById("more");
const container = document.getElementById("page-nav");
const buttonTransition = document.getElementsByClassName("ripple");

var countSidebar = 1;
toggleSidebar.addEventListener("click", function() {
	if (countSidebar === 1) {
		container.style.marginLeft = "4em";
	} else container.style.marginLeft = "";
	countSidebar = countSidebar ^ 1;
});

Array.prototype.forEach.call(buttonTransition, function(b) {
	b.addEventListener("click", ripple);
});

function ripple(e) {
	const transitionEffect = document.createElement("div");
	transitionEffect.setAttribute("id", "ripple");
	transitionEffect.classList.add(this.dataset.color);
	this.appendChild(transitionEffect);

	var d = Math.max(this.clientWidth);
	transitionEffect.style.width = transitionEffect.style.height = d + "px";
	transitionEffect.style.left = e.clientX - this.offsetLeft - d / 2 + "px";
	transitionEffect.style.top = e.clientY - this.offsetTop - d / 2 + "px";
}

var toggleProfile = 0;
const avatar = document.getElementById("avatar");
const profileBar = document.getElementById("profileBar");
profileBar.style.opacity = "0";

avatar.onclick = function() {
	toggleProfile = toggleProfile ^ 1;
	if (toggleProfile == 1) {
		profileBar.style.opacity = "1";
	} else {
		profileBar.style.opacity = "0";
	}
};

tooltipIn = function(b) {
	b.children[0].children[0].style.display = 'block';
}

tooltipOut = function(b) {
	b.children[0].children[0].style.display = 'none';
}