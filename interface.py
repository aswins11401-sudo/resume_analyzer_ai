import streamlit as st
from analysis import analyze_resume

st.set_page_config('Resume Analyzer',page_icon='🛠️')
st.title('Resume Analyzer using 🤖🧠AI👾 ')
st.header(':blue[AI powered Resume Analyzer with given job description using AI ] 🤖')
st.subheader(''':red[This page helps you to compare the resume and the given job description and provide ATS, probability and SWOT analysis]''')
st.sidebar.subheader('Drop your resumer here 📋')
pdf_doc = st.sidebar.file_uploader('Click here',type=['pdf'])
st.sidebar.markdown('Designed by Aswin')
st.sidebar.markdown('GitHub : https://github.com/aswins11401-sudo/resume_analyzer_ai')

job_des = st.text_area('Copy and paste the JD here 📑',max_chars=10000)
submit = st.button('Get Results 🚀')
if submit:
    with st.spinner('Loading.... ⚔️'):
        analyze_resume(pdf_doc,job_des)
