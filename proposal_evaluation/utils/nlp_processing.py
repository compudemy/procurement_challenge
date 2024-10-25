import spacy

# Loading the spaCy model
nlp = spacy.load("en_core_web_sm")

def parse_proposal_text(text):
    doc = nlp(text)
    key_entities = {"pricing": [], "tech_specs": [], "performance": [], "compliance": []}

    for ent in doc.ents:
        if ent.label_ in ["MONEY"]:  # Example entity types
            key_entities["pricing"].append(ent.text)
        elif ent.label_ == "ORG":
            key_entities["performance"].append(ent.text)
        # Continue adding conditions for technical specs and compliance as needed
    return key_entities
