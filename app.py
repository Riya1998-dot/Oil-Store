import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Nexus LMS",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f5f7fb;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #101828;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.logo {
    font-size: 26px;
    font-weight: 800;
    padding: 15px 0 30px 0;
}

.nav-title {
    color: #98A2B3 !important;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 25px;
}

/* Header */
.hero {
    background: linear-gradient(135deg, #111827, #344054);
    padding: 35px;
    border-radius: 22px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 34px;
    margin-bottom: 8px;
}

.hero p {
    color: #D0D5DD;
}

/* Cards */
.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #EAECF0;
    box-shadow: 0 5px 20px rgba(16,24,40,0.05);
    margin-bottom: 20px;
}

.card h3 {
    margin-top: 0;
}

.course-card {
    background: white;
    border-radius: 18px;
    padding: 22px;
    border: 1px solid #EAECF0;
    min-height: 210px;
    box-shadow: 0 5px 20px rgba(16,24,40,0.04);
}

.course-icon {
    font-size: 35px;
}

.badge {
    display: inline-block;
    background: #ECFDF3;
    color: #027A48;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
}

.stat {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #EAECF0;
}

.stat-number {
    font-size: 30px;
    font-weight: 800;
}

.stat-label {
    color: #667085;
    font-size: 14px;
}

.lesson {
    background: white;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #EAECF0;
    margin-bottom: 10px;
}

.footer {
    text-align: center;
    color: #98A2B3;
    padding: 30px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "progress" not in st.session_state:
    st.session_state.progress = {
        "Python": 65,
        "Data Analytics": 40,
        "Web Development": 80
    }

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = None


# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.markdown('<div class="logo">🎓 NEXUS LMS</div>',
                unsafe_allow_html=True)

    st.markdown('<div class="nav-title">MAIN MENU</div>',
                unsafe_allow_html=True)

    if st.button("🏠  Dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"

    if st.button("📚  My Courses", use_container_width=True):
        st.session_state.page = "Courses"

    if st.button("📝  Quiz Center", use_container_width=True):
        st.session_state.page = "Quiz"

    if st.button("🏆  Certificates", use_container_width=True):
        st.session_state.page = "Certificates"

    st.markdown('<div class="nav-title">ACCOUNT</div>',
                unsafe_allow_html=True)

    if st.button("👤  Profile", use_container_width=True):
        st.session_state.page = "Profile"

    if st.button("⚙️  Settings", use_container_width=True):
        st.session_state.page = "Settings"

    st.markdown("---")
    st.caption("Nexus LMS v1.0")


# ---------------- DASHBOARD ----------------
if st.session_state.page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <h1>Good Morning, Suberiya 👋</h1>
        <p>Continue your learning journey and achieve your next milestone.</p>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="stat">
        <div class="stat-number">12</div>
        <div class="stat-label">Courses Enrolled</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="stat">
        <div class="stat-number">68%</div>
        <div class="stat-label">Overall Progress</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="stat">
        <div class="stat-number">24</div>
        <div class="stat-label">Lessons Completed</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="stat">
        <div class="stat-number">3</div>
        <div class="stat-label">Certificates</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Continue Learning")

    courses = [
        ("🐍", "Python Programming", "Learn Python from beginner to advanced.", 65),
        ("📊", "Data Analytics", "Excel, SQL, Python & Power BI.", 40),
        ("🌐", "Web Development", "HTML, CSS, JavaScript & React.", 80)
    ]

    cols = st.columns(3)

    for col, course in zip(cols, courses):

        icon, title, description, progress = course

        with col:

            st.markdown(f"""
            <div class="course-card">
                <div class="course-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{description}</p>
                <span class="badge">{progress}% Complete</span>
            </div>
            """, unsafe_allow_html=True)

            st.progress(progress / 100)

            if st.button("Continue →", key=title):
                st.session_state.page = "Courses"

    st.markdown("### Recent Activity")

    st.markdown("""
    <div class="card">
    <b>✓ Python Basics</b><br>
    Completed Variables & Data Types
    <hr>
    <b>✓ SQL Fundamentals</b><br>
    Completed SELECT and WHERE
    <hr>
    <b>🎯 Data Analytics</b><br>
    Next lesson: Introduction to Power BI
    </div>
    """, unsafe_allow_html=True)


# ---------------- COURSES ----------------
elif st.session_state.page == "Courses":

    st.title("📚 My Courses")
    st.write("Explore your enrolled learning programs.")

    courses = {
        "Python Programming": [
            "Introduction to Python",
            "Variables & Data Types",
            "Conditional Statements",
            "Loops",
            "Functions",
            "Object Oriented Programming"
        ],
        "Data Analytics": [
            "Introduction to Data Analytics",
            "Advanced Excel",
            "SQL for Analytics",
            "Python for Data Analysis",
            "Power BI",
            "Data Visualization"
        ],
        "Web Development": [
            "HTML Fundamentals",
            "CSS & Responsive Design",
            "JavaScript",
            "DOM Manipulation",
            "React Basics",
            "Building Projects"
        ]
    }

    for course_name, lessons in courses.items():

        progress = st.session_state.progress.get(course_name.split()[0], 50)

        st.markdown(f"""
        <div class="card">
            <h2>{course_name}</h2>
            <span class="badge">{progress}% Completed</span>
        </div>
        """, unsafe_allow_html=True)

        st.progress(progress / 100)

        for i, lesson in enumerate(lessons, 1):

            col1, col2 = st.columns([5, 1])

            with col1:
                st.markdown(
                    f'<div class="lesson">📖 Lesson {i} — <b>{lesson}</b></div>',
                    unsafe_allow_html=True
                )

            with col2:
                st.button(
                    "Open",
                    key=f"{course_name}_{i}"
                )


# ---------------- QUIZ ----------------
elif st.session_state.page == "Quiz":

    st.title("📝 Quiz Center")
    st.write("Test your knowledge.")

    questions = [
        {
            "question": "Which language is primarily used for Streamlit?",
            "options": ["Java", "Python", "PHP", "C++"],
            "answer": "Python"
        },
        {
            "question": "Which command is used to run a Streamlit application?",
            "options": [
                "python app.py",
                "streamlit run app.py",
                "run streamlit",
                "start app"
            ],
            "answer": "streamlit run app.py"
        },
        {
            "question": "Which language is used to style web pages?",
            "options": ["HTML", "CSS", "SQL", "Python"],
            "answer": "CSS"
        }
    ]

    answers = []

    for i, q in enumerate(questions):

        st.markdown(f"### {i+1}. {q['question']}")

        answer = st.radio(
            "Select your answer:",
            q["options"],
            key=f"question_{i}"
        )

        answers.append(answer)

    if st.button("🚀 Submit Quiz", type="primary"):

        score = 0

        for i, q in enumerate(questions):
            if answers[i] == q["answer"]:
                score += 1

        st.session_state.quiz_score = score

        st.success(
            f"Quiz completed! Your score: {score}/{len(questions)}"
        )

        if score == len(questions):
            st.balloons()


# ---------------- CERTIFICATES ----------------
elif st.session_state.page == "Certificates":

    st.title("🏆 My Certificates")

    certificates = [
        ("Python Programming", "NEXUS-PY-2026-001"),
        ("Web Development", "NEXUS-WEB-2026-002"),
        ("Data Analytics", "NEXUS-DA-2026-003")
    ]

    for title, certificate_id in certificates:

        st.markdown(f"""
        <div class="card">
            <h2>🏆 {title}</h2>
            <p>Certificate ID: <b>{certificate_id}</b></p>
            <span class="badge">Verified Certificate</span>
        </div>
        """, unsafe_allow_html=True)

        st.download_button(
            "Download Certificate",
            f"Certificate: {title}\nCertificate ID: {certificate_id}",
            file_name=f"{title.replace(' ', '_')}_Certificate.txt",
            key=certificate_id
        )


# ---------------- PROFILE ----------------
elif st.session_state.page == "Profile":

    st.title("👤 Student Profile")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.markdown("""
        <div class="card" style="text-align:center;">
            <div style="font-size:70px;">👩‍🎓</div>
            <h2>Suberiya S</h2>
            <span class="badge">Premium Student</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        name = st.text_input("Full Name", "Suberiya S")
        email = st.text_input("Email", "student@example.com")
        phone = st.text_input("Phone", "+91 XXXXX XXXXX")

        if st.button("Save Profile"):
            st.success("Profile updated successfully!")


# ---------------- SETTINGS ----------------
elif st.session_state.page == "Settings":

    st.title("⚙️ Settings")

    st.markdown("""
    <div class="card">
    <h3>Account Settings</h3>
    </div>
    """, unsafe_allow_html=True)

    st.toggle("Email Notifications", True)
    st.toggle("Course Reminders", True)
    st.toggle("Quiz Notifications", True)

    st.selectbox(
        "Language",
        ["English", "Tamil"]
    )

    st.success("Settings saved for this demo.")


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    🎓 Nexus LMS • Learn • Practice • Achieve
</div>
""", unsafe_allow_html=True)
