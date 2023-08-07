
// Function to handle the Transcribe checkmark toggle
function handleTranscribeToggle() {
    let isChecked = document.getElementById("transcribeCheck").checked;
    console.log("Transcribe toggled", isChecked);
    // Todo: add logic to communicate with backend
}

// Function to handle changes in the Confidence Threshold selector
function handleConfidenceChange() {
    let thresholdValue = document.getElementById("confidenceThreshold").value;
    console.log("Confidence Threshold changed to: ", thresholdValue);
    // Todo: add logic to communicate with backend
}

function getReminder() {
    // Make a request to get proactive response
    //fetch('/agent')
    //.then(response => response.json())
    //.then(data => {
        // Insert reminder text into index.html
        //document.getElementById('reminder-text').innerText = data.reminder;
    //});

      // Todo: add logic to communicate with backend
}

function getLocation() {
     // Todo: add logic to communicate with backend
}

function getActivity() {
     // Todo: add logic to communicate with backend
}

