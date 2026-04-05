import streamlit as st
import difflib
import time

st.set_page_config(page_title="College Chatbot", page_icon="🎓")

st.title("🎓 College Assistant Chatbot")

# Knowledge base
qa_pairs = {
    "hi": "Hello! Welcome to our college chatbot 😊",
    "hello": "Hello! How can I help you today?",
    "hii": "Hello! Nice to meet you 😊",
    "college name": "Our college name is Princeton Institute of Engineering and Technology for Women.",
    "location": "The college is located at Vijayapuri Colony, Ghatkesar, Hyderabad.",
    "timings": """College timings:
9:30 AM – 3:30 PM
Classes: 9:30 – 12:30
Lunch: 12:30 – 1:15
Labs: 1:15 – 3:30""",
    "courses": "We offer B.Tech and M.Tech branches like CSE, CSD, CSM, ECE, and Civil.",
    "fee": "The fee for B.Tech is approximately ₹80,000 per year.",
    "placement": "Top companies include Infosys, Wipro, Microsoft, and Google.",
    "package": "Average package is around 4 LPA and highest is around 12 LPA.",
    "hostel": "Hostel facilities are available for girls with good security.",
    "transport": "College buses are available in most areas of Hyderabad.",
    "sports": "Sports facilities include cricket, football, volleyball, and indoor games.",
    "ragging": "Our college is a strict ragging-free campus with anti-ragging committees.",
    "faculty": "Yes, our college has experienced and supportive faculty members.",
    "labs": "Yes, the college provides well-equipped labs with computers and modern equipment.",
    "infrastructure": "The campus has good infrastructure including smart classrooms, labs, library, and playground.",
    "reviews": "Students generally give good reviews about teaching quality and campus environment."
}

# Bot response function with fuzzy matching
def get_bot_response(user_input):
    user_input = user_input.lower()

    matches = difflib.get_close_matches(user_input, qa_pairs.keys(), n=1, cutoff=0.4)

    if matches:
        return qa_pairs[matches[0]]
    else:
        return "Sorry, I didn't understand that. Please ask something about the college."

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_prompt = st.chat_input("Ask something about the college...")

if user_prompt:
    
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Bot response
    response = get_bot_response(user_prompt)

    # Typing animation
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for char in response:
            full_response += char
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.02)

        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": response})