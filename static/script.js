var modal = document.getElementById("submission");

// Get all the box elements
var boxes = document.getElementsByClassName("task");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];


// Get the hidden input where we'll store the source
var sourceInput = document.getElementById("sourceInput");

// Attach click event to each box
for (var i = 0; i < boxes.length; i++) {
    boxes[i].onclick = function() {
        // Get the data-source attribute from the clicked box
        var source = this.getAttribute("data-source");

        // Set the value of the hidden input to the source
        sourceInput.value = source;

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
    console.log("Form submitted");

    var source = sourceInput.value;

    if (source) {
        console.log("Source:", source);
        const overlayImage = "#img" + document.getElementById(source)
        console.log("overlayImage", overlayImage);
        // overlayImage.style.display = "block";
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