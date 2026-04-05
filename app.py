import streamlit as st
import difflib
import time

st.set_page_config(page_title="College Chatbot", page_icon="🎓")

st.title("🎓 College Assistant Chatbot")

# -------------------------
# Knowledge Base (Q&A)
# -------------------------

qa_pairs = {
"What is the college name?":
"Princeton Institute of Engineering and Technology for Women.",

"Where is the college located?":
"It is located in Chowdaryguda Village, Ghatkesar, Hyderabad, Telangana.",

"What are the college timings?":
"College timings are from 9:30 AM to 3:30 PM.",

"How can I apply for admission?":
"You can apply through the official website or through state counseling (EAMCET/ECET).",

"What is the admission process?":
"Admissions are based on entrance exams like TS EAMCET (B.Tech), TS ECET (lateral entry), and GATE/PGECET (M.Tech).",

"What are the eligibility criteria?":
"You must complete 10+2 with required marks and qualify in relevant entrance exams.",

"When do admissions start and end?":
"Admissions usually start after entrance exam results (around May–July).",

"What branches are available in the college?":
"CSE, ECE, EEE, Civil, Mechanical, and other engineering branches.",

"What courses are offered?":
"Diploma, B.Tech, and M.Tech programs are offered.",

"Does the college offer Computer Science or Data Science?":
"Yes, Computer Science and related specializations are available.",

"What documents are required for admission?":
"10th and 12th certificates, entrance exam rank card, Aadhaar card, photographs, and transfer certificate.",

"Is Aadhaar card mandatory for admission?":
"Yes, it is generally required for verification.",

"Do I need to submit previous academic certificates?":
"Yes, submission of previous academic records is mandatory.",

"Is hostel facility available?":
"Yes, hostel facilities are available for students.",

"What are the hostel fees?":
"Hostel fees vary, approximately ₹60,000–₹80,000 per year (may change).",

"Are separate hostels available for boys and girls?":
"Yes, hostel facilities are available (primarily for women students).",

"What is the fee structure for each branch?":
"Approximate tuition fee is around ₹70,000 per year (varies by course).",

"Are there any additional charges apart from tuition fees?":
"Yes, exam fees, hostel fees, and transport fees may apply.",

"Can the fees be paid in installments?":
"Yes, installment options may be available depending on management policy.",

"Is transport facility available?":
"Yes, transport (bus facility) is available for students.",

"What are the available bus routes?":
"Multiple routes across Hyderabad and nearby areas are available.",

"What is the transport fee?":
"Transport fee depends on distance (approx ₹10,000–₹25,000 per year).",

"Does the college provide placement opportunities?":
"Yes, the college has a dedicated placement cell.",

"Which companies visit the college for placements?":
"Various IT and core companies visit (exact list varies each year).",

"What is the placement percentage?":
"Placement support is provided; percentage varies yearly.",

"What is the average package offered?":
"Average package is around ₹3–4 LPA (approximate).",

"What is the highest package offered?":
"Highest package can go up to ₹6–8 LPA (varies by year).",

"Are scholarships available for students?":
"Yes, scholarships are provided as per government rules.",

"Who is eligible for scholarships?":
"Students eligible under government schemes (merit, caste, income-based).",

"How can I apply for a scholarship?":
"Apply through state scholarship portals or college administration.",

"What sports facilities are available in the college?":
"Sports grounds, indoor games, and gym facilities are available.",

"Are there any extracurricular activities?":
"Yes, technical events, cultural programs, and clubs are conducted.",

"What is the minimum attendance requirement?":
"Minimum 75% attendance is required.",

"What happens if attendance is below the required percentage?":
"You may not be allowed to appear for exams.",

"How are exams conducted in the college?":
"Semester-based exams with internal and external assessments.",

"What is the exam pattern?":
"Includes internal exams, assignments, and final semester exams.",

"Are there internal and external exams?":
"Yes, both internal assessments and external university exams are conducted.",

"What events are conducted in the college?":
"Technical fests, seminars, workshops, and cultural events are organized.",

"Are there technical fests or cultural programs held regularly?":
"Yes, technical symposiums and cultural fests are conducted regularly."
}

# -------------------------
# Smart Matching Function
# -------------------------

def get_bot_response(user_input):

    questions = list(qa_pairs.keys())

    match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.4)

    if match:
        return qa_pairs[match[0]]

    return "Sorry, I couldn't understand the question. Please ask about admissions, fees, placements, hostel, or courses."

# -------------------------
# Chat Memory
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# Chat Input
# -------------------------

user_prompt = st.chat_input("Ask something about the college...")

if user_prompt:

    st.session_state.messages.append({"role":"user","content":user_prompt})

    with st.chat_message("user"):
        st.markdown(user_prompt)

    response = get_bot_response(user_prompt)

    with st.chat_message("assistant"):

        placeholder = st.empty()
        text = ""

        for char in response:
            text += char
            placeholder.markdown(text + "▌")
            time.sleep(0.01)

        placeholder.markdown(text)

    st.session_state.messages.append({"role":"assistant","content":response})
