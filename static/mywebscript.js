let RunSentimentAnalysis = () => {
    console.log("Button clicked");

    let textToAnalyze = document.getElementById("textToAnalyze").value;
    console.log("Got the text: " + textToAnalyze);

    let xhttp = new XMLHttpRequest();
    console.log("Got http: " + xhttp);

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let response = xhttp.responseText;
            document.getElementById("system_response").innerHTML = response;
            console.log("Got system response: " + response);
        }
    };

    // Fixed API request - Now it correctly sends the text to backend
    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify({ text: textToAnalyze }));
};
