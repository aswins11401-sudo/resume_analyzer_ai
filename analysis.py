import os 
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai

from pdf import extract_pdf_text

key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=key)
model = genai.GenerativeModel('models/gemini-2.5-flash-lite')

def analyze_resume(pdf_doc,job_des):
    if pdf_doc is not None:
        pdf_text = extract_pdf_text(pdf_doc)
        st.write(f'Text Extracted Successfully ✅️')
        
    else:
        st.warning('Error !! Drop the file in PDF format ⟳')
    
    ats_score = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des}
                                       and provide ATS score on scale of 0 to 100''')
    probability = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des}
                                       Calculate the probability of the candidate
                                       getting a callback''')
    resume_rating = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des}
                                       Rate this resume as poor, moderate,
                                       good,very good''')
    skill_match = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des} and
                                       list all the skills that match and all the skills
                                       that does not match''')
    goodfit = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des}
                                       and check wheter the resume is suitable 
                                       for the JD if not then suggest any other 
                                       jobs''')
    swot = model.generate_content(f'''Compare the given pdf {pdf_text}
                                    and given job description {job_des}
                                    and create a SWOT analysis of the candidate''')
    return (st.write(ats_score.text),
            st.write(probability.text),
            st.write(skill_match.text),
            st.write(resume_rating.text),
            st.write(goodfit.text),
            st.write(swot.text))

