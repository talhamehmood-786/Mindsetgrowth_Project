import streamlit as st
import converter
import resume  
import quiz
import todolist  

st.set_page_config(page_title="✨Growth Mindset Challenge")
st.markdown("""
    <style>
        div[data-testid="stTabs"] button {
            font-size: 18px;
            font-weight: bold;
            color: white;
            background: #008CBA;
            border-radius: 10px;
            padding: 8px 20px;
            margin: 5px;
            border: none;
        }
        div[data-testid="stTabs"] button:hover {
            background: #005F73;
        }
        div[data-testid="stTabs"] button[aria-selected="true"] {
            background: #F39C12 !important;
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

tabs = st.tabs(["Home", "Resume Builder", "Quiz", "Converter", "To-Do List"])


with tabs[1]: 
    resume.show_resume() 

with tabs[2]: 
    st.title("❓ Quiz Section")
    quiz.show_quiz()  

with tabs[3]: 
    st.title("excel to csv")
    converter.show_converter()
  
with tabs[4]: 
    st.title("📝 To-Do List Section")
    todolist.show_todolist()

with tabs[0]: 
    st.title("🏠 Home Page")
    
    st.markdown("---") 
    
    st.subheader("✨ Growth Mindset Challenge ✨")
    st.write("💪 **Challenge yourself to grow every day!** Here are some habits to build a strong mindset:")

    st.write("✅ **Learn Something New Every Day:** Gain a new skill or knowledge daily, even if it's small.")  
    st.write("✅ **Learn from Mistakes:** See failures as lessons, not obstacles.")  
    st.write("✅ **Believe in Yourself:** Hard work and persistence lead to success.")  
    st.write("✅ **Embrace Challenges:** View difficulties as opportunities to grow.")  
    st.write("✅ **Keep Learning:** Read books, watch videos, and improve yourself daily.")  

   
    st.markdown("> *“Success is not final, failure is not fatal: it is the courage to continue that counts.”* – Winston Churchill")

    
    if st.button("🎯 Start Your Growth Challenge!"):
        st.success("Great! Start applying these habits today! 🚀")
