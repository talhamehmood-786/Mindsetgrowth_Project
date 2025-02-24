import streamlit as st

def show_resume():  
    st.title("Professional Resume ✨")
    
   
    st.header("Personal Information")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    address = st.text_area("Address")
    
    
    st.header("Skills")
    skills = st.text_area("List your skills (comma separated)")

    
    st.header("Education")
    degree = st.text_input("Degree")
    university = st.text_input("University")
    grad_year = st.text_input("Graduation Year")
    
 
    with st.expander("Work Experience"):
        job_title = st.text_input("Job Title")
        company = st.text_input("Company Name")
        job_duration = st.text_input("Duration (e.g. 2020-2023)")
        job_desc = st.text_area("Job Description")
    
   
    if st.button("Generate Resume"):
        st.subheader("Your Resume")
        st.markdown(f"**Name:** {name}")
        st.markdown(f"**Email:** {email}")
        st.markdown(f"**Phone:** {phone}")
        st.markdown(f"**Address:** {address}")
        st.markdown("---")
        st.markdown(f"### Skills")
        st.markdown(skills)
        st.markdown("---")
        st.markdown(f"### Education")
        st.markdown(f"**{degree}** from {university}, {grad_year}")
        st.markdown(f"### Work Experience")
        st.markdown(f"**{job_title}** at {company} ({job_duration})")
        st.markdown(job_desc)
        st.markdown("---")
       
