
// Get the sform
var sform = document.getElementById('f01');

// When the user clicks anywhere outside of the form, close it
window.onclick = function(event) {
    If (event.target == sform){
        sform.style.display = "none";
    }
}

