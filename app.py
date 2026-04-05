import streamlit as st
import difflib
import time

st.set_page_config(page_title="College Chatbot", page_icon="🎓")

st.title("🎓 College Assistant Chatbot")

# ------------------------------
# Knowledge Base
# ------------------------------

knowledge_base = {
    "greeting": {
        "questions": ["hi","hello","hey","hii","good morning","good evening"],
        "answer": "Hello 👋 Welcome to the college chatbot. How can I help you?"
    },

    "college_name": {
        "questions": ["college name","name of college","what is your college"],
        "answer": "Our college name is Princeton Institute of Engineering and Technology for Women."
    },

    "location": {
        "questions": ["location","where is college","address","where located"],
        "answer": "The college is located at Vijayapuri Colony, Ghatkesar, Hyderabad."
    },

    "timings": {
        "questions": ["timings","college time","schedule","working hours"],
        "answer": """College timings:
9:30 AM – 3:30 PM
Classes: 9:30 – 12:30
Lunch: 12:30 – 1:15
Labs: 1:15 – 3:30"""
    },

    "admission": {
        "questions": ["admission","how to join","apply","entrance exam"],
        "answer": "Admissions are based on entrance exams and counselling."
    },

    "courses": {
        "questions": ["courses","branches","departments"],
        "answer": "We offer B.Tech branches like CSE, CSD, CSM, ECE, and CIVIL."
    },

    "faculty": {
        "questions": ["faculty","teachers","professors","staff"],
        "answer": "Yes, our college has experienced and highly qualified faculty members."
    },

    "labs": {
        "questions": ["labs","computers","laboratories"],
        "answer": "Yes, our college provides well-equipped labs with modern computer systems."
    },

    "infrastructure": {
        "questions": ["infrastructure","campus","buildings"],
        "answer": "The campus has good infrastructure including smart classrooms, labs, library, and playground."
    },

    "placement": {
        "questions": ["placement","companies","jobs"],
        "answer": "Top companies visiting our campus include Infosys, Wipro, TCS, and Microsoft."
    },

    "package": {
        "questions": ["package","salary","highest package"],
        "answer": "The average package is around 4 LPA and the highest package is around 12 LPA."
    },

    "hostel": {
        "questions": ["hostel","accommodation"],
        "answer": "Hostel facilities are available for girls with good security and food facilities."
    },

    "transport": {
        "questions": ["transport","bus","buses"],
        "answer": "College buses are available in most areas of Hyderabad."
    },

    "sports": {
        "questions": ["sports","games","playground"],
        "answer": "We have facilities for cricket, football, volleyball, and indoor games."
    },

    "ragging": {
        "questions": ["ragging","anti ragging","safe campus"],
        "answer": "Our college is a strict ragging-free campus with anti-ragging committees."
    },

    "library": {
        "questions": ["library","books"],
        "answer": "The college has a large library with academic books, journals, and digital resources."
    }
}

# ------------------------------
# Smart Matching Function
# ------------------------------

def get_bot_response(user_input):

    user_input = user_input.lower()

    for intent in knowledge_base:
        for question in knowledge_base[intent]["questions"]:
            if question in user_input:
                return knowledge_base[intent]["answer"]

    # Fuzzy backup matching
    all_questions = []
    intent_map = {}

    for intent in knowledge_base:
        for q in knowledge_base[intent]["questions"]:
            all_questions.append(q)
            intent_map[q] = intent

    match = difflib.get_close_matches(user_input, all_questions, n=1, cutoff=0.5)

    if match:
        return knowledge_base[intent_map[match[0]]]["answer"]

    return "Sorry, I didn't understand that. Please ask something about the college."

# ------------------------------
# Chat Memory
# ------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ------------------------------
# Chat Input
# ------------------------------

user_prompt = st.chat_input("Ask something about the college...")

if user_prompt:

    st.session_state.messages.append({"role":"user","content":user_prompt})

    with st.chat_message("user"):
        st.markdown(user_prompt)

    response = get_bot_response(user_prompt)

    with st.chat_message("assistant"):

        placeholder = st.empty()
        typed = ""

        for char in response:
            typed += char
            placeholder.markdown(typed + "▌")
            time.sleep(0.02)

        placeholder.markdown(typed)

    st.session_state.messages.append({"role":"assistant","content":response})
