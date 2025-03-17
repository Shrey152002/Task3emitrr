import os
import pickle
import re
import json
import spacy
from flask import Flask, render_template, request, jsonify
from collections import defaultdict

class SOAPNoteGenerator:
    def __init__(self):
        """Initialize the SOAP Note Generator with necessary models and resources."""
        # Load SpaCy for NER and text processing
        try:
            self.nlp = spacy.load("en_core_web_lg")
        except:
            # Fallback if specific model not available
            self.nlp = spacy.load("en_core_web_sm")

        # Initialize medical terminology lists
        self.init_medical_terminology()

    def init_medical_terminology(self):
        """Initialize medical terminology lists for better classification."""
        # Symptoms commonly found in Subjective section
        self.subjective_terms = [
            "pain", "discomfort", "ache", "sore", "tender", "stiff", "difficulty",
            "trouble", "problem", "feel", "felt", "feeling", "worried", "concern",
            "complain", "report", "state", "mention", "describe", "experience",
            "history", "accident", "injury", "event", "sleep", "appetite"
        ]

        # Terms commonly found in Objective section
        self.objective_terms = [
            "exam", "examination", "observe", "observation", "vital", "sign",
            "test", "x-ray", "scan", "mri", "ct", "laboratory", "range", "movement",
            "motion", "tender", "tenderness", "mobility", "flexion", "extension",
            "inspection", "palpation", "auscultation", "percussion", "reflex",
            "strength", "muscle", "neurological", "sensation", "appearance",
            "measured", "found", "noted", "detected", "visible", "present"
        ]

        # Terms commonly found in Assessment section
        self.assessment_terms = [
            "assess", "assessment", "diagnose", "diagnosis", "condition", "impression",
            "evaluation", "conclude", "conclusion", "determine", "finding", "findings",
            "indicate", "indicates", "suggesting", "suspect", "consistent with",
            "likely", "probable", "possible", "rule out", "differential","differential", "working diagnosis", "clinical impression"
        ]

        # Terms commonly found in Plan section
        self.plan_terms = [
            "plan", "treatment", "therapy", "prescribe", "prescription", "medication", 
            "procedure", "surgery", "recommend", "advised", "counsel", "counseling", 
            "refer", "referral", "monitor", "follow-up", "re-evaluate", "schedule", 
            "therapy", "rehabilitation", "physical therapy", "occupational therapy", 
            "exercise", "lifestyle", "modification", "preventive", "precaution"
        ]

    def classify_sentence(self, sentence):
        """Classify a sentence into one of the SOAP sections based on keywords."""
        sentence_lower = sentence.lower()
        
        if any(term in sentence_lower for term in self.subjective_terms):
            return "Subjective"
        elif any(term in sentence_lower for term in self.objective_terms):
            return "Objective"
        elif any(term in sentence_lower for term in self.assessment_terms):
            return "Assessment"
        elif any(term in sentence_lower for term in self.plan_terms):
            return "Plan"
        else:
            return "Unclassified"

    def generate_soap_note(self, text):
        """Generate a SOAP note from input text by classifying sentences."""
        doc = self.nlp(text)
        soap_note = defaultdict(list)

        for sent in doc.sents:
            category = self.classify_sentence(sent.text)
            soap_note[category].append(sent.text)

        return soap_note

# Flask Application Setup
app = Flask(__name__)
soap_generator = SOAPNoteGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    soap_note = soap_generator.generate_soap_note(text)
    return jsonify(soap_note)

if __name__ == '__main__':
    app.run(debug=True)
