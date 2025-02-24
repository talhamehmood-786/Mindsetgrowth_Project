import streamlit as st

def show_quiz():
    questions = [
        "What is the smallest prime number?",
        "Which planet is known as the Red Planet?",
        "What is the largest mammal?",
        "Which country is known as the Land of the Rising Sun?",
        "What is the longest river in the world?",
        "Which gas do plants absorb from the atmosphere for photosynthesis?",
        "Who is known as the Father of Computers?",
        "Which element has the chemical symbol 'O'?",
        "What is the capital of Australia?",
        "Which of the following is a non-renewable resource?"
    ]

    options = [
        ["0", "1", "2", "3"],
        ["Venus", "Mars", "Earth", "Jupiter"],
        ["Elephant", "Blue Whale", "Giraffe", "Tiger"],
        ["China", "India", "Japan", "Thailand"],
        ["Nile", "Amazon", "Mississippi", "Yangtze"],
        ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        ["Isaac Newton", "Charles Babbage", "Albert Einstein", "Nikola Tesla"],
        ["Oxygen", "Osmium", "Ozone", "Opium"],
        ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        ["Wind", "Solar", "Coal", "Water"]
    ]

    correct_answers = [
        "2", "Mars", "Blue Whale", "Japan", "Nile", 
        "Carbon Dioxide", "Charles Babbage", "Oxygen", 
        "Canberra", "Coal"
    ]

   
    score = 0  

    user_answers = [st.radio(questions[i], options[i], key=f"question_{i}_{questions[i]}") for i in range(len(questions))]

    if st.button("Submit Quiz"):
        # Calculate score
        score = sum(1 for i in range(len(questions)) if user_answers[i] == correct_answers[i])
        
        # Display score
        st.write(f"✅ Your Score: {score} / {len(questions)}")

        # Highlight answers with color after submission
        for i in range(len(questions)):
            if user_answers[i] == correct_answers[i]:
                st.markdown(f"<p style='color:green;'>✔️ {questions[i]}</p>", unsafe_allow_html=True)  
            else:
                st.markdown(f"<p style='color:red;'>❌ {questions[i]}</p>", unsafe_allow_html=True)  

