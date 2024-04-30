import spacy

import pandas as pd


# Function to extract job descriptions from text
def extract_job_descriptions(text):
    doc = nlp(text)
    job_descriptions = ""
    
    for sent in doc.sents:
        # Identify sentences likely to contain job descriptions
        # Example: You can add more specific conditions based on your data
        if 'job description' in sent.text.lower() or 'responsibilities' in sent.text.lower() or 'requirements' in sent.text.lower() or 'qualifications:' in sent.text.lower() or 'eligibility' in sent.text.lower() or 'responsibility' in sent.text.lower() or 'Who can apply?' in sent.text.lower() or 'key skills' in sent.text.lower() :
            job_descriptions = job_descriptions +(sent.text.strip())
    
    return job_descriptions


df = pd.read_csv('OutFile.csv')

descriptions = df['job Description'].astype(str)

nlp = spacy.load('en_core_web_sm')

extracted_descriptions = descriptions.apply(extract_job_descriptions)
df["JD"] =  extracted_descriptions
df.to_csv('OutFile.csv', index=False)

