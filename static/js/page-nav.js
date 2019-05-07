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
