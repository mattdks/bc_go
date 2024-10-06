var modal = document.getElementById("submission");

// Get all the box elements
var boxes = document.getElementsByClassName("task");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var pokeInput = document.getElementById("pokeInput");

// Get the hidden input where we'll store the source
var sourceInput = document.getElementById("sourceInput");

var dateInput = document.getElementById("dateInput");

// Attach click event to each box
for (var i = 0; i < boxes.length; i++) {
    boxes[i].onclick = function() {
        // Get the data-source attribute from the clicked box
        var source = this.getAttribute("data-source");
        var poke_value = this.getAttribute("pvalue");

        // Set the value of the hidden input to the source
        sourceInput.value = source; // value of buttons pushed
        pokeInput.value = poke_value;

        // Display the modal
        modal.style.display = "block";
    };
}

// Close the modal when the user clicks the close button (x)
span.onclick = function() {
    modal.style.display = "none";
}

document.getElementById("submission-form").addEventListener('submit', function(event) {
    event.preventDefault();

    var source = sourceInput.value; //value of button pushed
    var poke_value = pokeInput.value;
    var date = dateInput.value;

    if (source) {
        const overlayImage = document.getElementById("img"+source)
        overlayImage.style.display = "block";
    }

    if (poke_value) {
        const makeBright = (document.getElementById("p"+poke_value)).querySelector("img")
        makeBright.style.filter = "brightness(1)";
    }

    if (date) {
        document.getElementById("p"+poke_value).querySelector("h5").textContent = "Congratulations! You caught this Pokemon on " + date + "!";
    }

    this.reset();
    modal.style.display = "none";
})

// Close the modal if the user clicks outside the modal content
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}