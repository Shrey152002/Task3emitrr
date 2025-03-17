# SOAP Note Generator

## Overview
The SOAP Note Generator is a Flask-based web application that processes medical text and classifies sentences into SOAP (Subjective, Objective, Assessment, Plan) sections using NLP techniques. The system utilizes the SpaCy library for Named Entity Recognition (NER) and text processing to accurately categorize medical notes.

## Features
- Classifies medical text into SOAP sections:
  - **Subjective**: Patient-reported symptoms and history
  - **Objective**: Observations, test results, and physical examination details
  - **Assessment**: Diagnoses and clinical impressions
  - **Plan**: Treatment plans, prescriptions, and follow-ups
- Uses SpaCy for text processing and Named Entity Recognition (NER)
- Flask-based web application with API endpoint for SOAP note generation

![SOAP Interface](https://github.com/Shrey152002/Task3emitrr/blob/main/Screenshot%20(17).png)
## Installation
### Prerequisites
Ensure you have Python installed (version 3.7 or later). You also need `pip` for package management.

### Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd soap-note-generator
   ```
2. Create and activate a virtual environment (recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000/` to access the web interface.

## Usage
1. Enter or paste medical text into the input field.
2. Click the "Generate SOAP Note" button.
3. The application will classify the text into Subjective, Objective, Assessment, and Plan sections.
4. View the results on the web interface.

## API Endpoint
The application provides a `/generate` API endpoint for programmatic access.

### Request
- **URL**: `/generate`
- **Method**: POST
- **Content-Type**: `application/json`
- **Payload**:
  ```json
  {
    "text": "Patient reports mild headache and dizziness for two days. Blood pressure measured at 140/90. Diagnosis suggests mild hypertension. Prescribed low-dose medication and advised follow-up."
  }
  ```

### Response
- **Success (200 OK)**:
  ```json
  {
    "Subjective": ["Patient reports mild headache and dizziness for two days."],
    "Objective": ["Blood pressure measured at 140/90."],
    "Assessment": ["Diagnosis suggests mild hypertension."],
    "Plan": ["Prescribed low-dose medication and advised follow-up."]
  }
  ```
- **Error (400 Bad Request)**:
  ```json
  {
    "error": "No text provided"
  }
  ```

## Dependencies
- Flask
- SpaCy
- JSON
- Collections

## License
This project is licensed under the MIT License.



## Future Enhancements
- Improve NLP model for more accurate classifications.
- Integrate with external medical APIs for enhanced analysis.
- Deploy as a cloud-based service.

---
For any issues or suggestions, feel free to open an issue in the repository.

