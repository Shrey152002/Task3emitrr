function generateSOAP() {
    const text = document.getElementById('inputText').value;
    if (!text) {
        alert('Please enter some text.');
        return;
    }

    fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    })
    .then(response => response.json())
    .then(data => {
        let outputHTML = '<h2>Generated SOAP Note</h2>';
        for (const section in data) {
            outputHTML += `<h3>${section}</h3><p>${data[section].join('<br>')}</p>`;
        }
        document.getElementById('output').innerHTML = outputHTML;
    })
    .catch(error => console.error('Error:', error));
}
