import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image
from googleapiclient.discovery import build

# --- Job Search Section ---
def job_search_section(job_query=None):
    st.subheader("\U0001F50D Government Job Search")

    if not job_query:
        job_query = st.text_input("Enter job keyword (e.g. 'police', 'railway', '12th pass')")

    if st.button("Search Job"):
        if not job_query:
            st.warning("Please enter a keyword to search.")
            return
        try:
            url = "https://www.sarkariresult.com/"
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            links = soup.find_all('a', href=True)
            results = [a for a in links if job_query.lower() in a.text.lower()]
            if results:
                for link in results:
                    link_text = link.text.strip()
                    link_url = link['href']
                    if not link_url.startswith('http'):
                        link_url = "https://www.sarkariresult.com/" + link_url
                    st.markdown(f"- [{link_text}]({link_url})")
            else:
                st.warning("No results found.")
        except Exception as e:
            st.error(f"Error: {e}")

# --- Dashboard Page ---
def dashboard():
    st.markdown(
        "<h3 style='color:#007ACC; font-weight:bold;'>🎓 Welcome to <span style='color:#FFD700;'>Prem Mohan</span>'s Learning Platform!</h3>",
        unsafe_allow_html=True
    )
    st.title(f"\U0001F389 Welcome! \U0001F44B!")

    st.subheader("\U0001F4DA 12th Complete? Now What to Do?")
    stream_choice = st.selectbox("🎓Dear Student Select Your Stream", [
                "Select",
                "🎨Arts Stream",
                "🧬Biology Stream",
                "🔢Mathematics Stream",
                "🏛️Government Jobs Opportunities",
                "🎓Government Jobs Opportunities After 12th",
                "🤖AI Skills: Future Jobs, High Demand, High Growth!"
            ])

    if stream_choice == "🎨Arts Stream":
        st.write("### Arts Stream (12th Arts) Options:")
        st.markdown("""
## 🎨 Career Options After 12th - Arts Stream

---

### 1. 📘 **BA (Bachelor of Arts)**
- **Specializations:** History, Political Science, Psychology, Sociology, Economics, etc.  
- **Duration:** 3 years  
- **Career:** Civil Services, Teaching, Research, NGOs, Content Writing

---

### 2. 🎨 **BFA (Bachelor of Fine Arts)**
- **Focus:** Visual and performing arts like painting, sculpture, animation  
- **Duration:** 3–4 years  
- **Career:** Artist, Illustrator, Animator, Art Director, Designer

---

### 3. 📰 **Journalism & Mass Communication**
- **Focus:** Media, reporting, content creation, public relations  
- **Duration:** 3 years  
- **Career:** Journalist, News Anchor, Editor, Media Planner, Content Creator

---

### 4. ⚖️ **Law (5-Year Integrated Course)**
- **Focus:** Legal studies, Indian constitution, criminal/civil law  
- **Duration:** 5 years  
- **Career:** Lawyer, Judge, Legal Advisor, Public Prosecutor

---

### 5. 🏨 **Hotel Management, Event Management, Travel & Tourism**
- **Focus:** Hospitality services, event planning, travel business  
- **Duration:** 3–4 years  
- **Career:** Hotel Manager, Event Planner, Travel Consultant, Tour Manager

---
""")
    elif stream_choice == "🧬Biology Stream":
        st.write("### Biology Stream (12th Biology) Options:")
        st.markdown("""
## 🧬 Career Options After 12th - Biology Stream

---

### 1. 🩺 **NEET (National Eligibility Entrance Test)**
- **Purpose:** Admission to MBBS, BDS, BAMS, BHMS, BPT, BSc Nursing  
- **Duration:** 
- MBBS: 5.5 years  
- BDS: 5 years  
- BAMS/BHMS: 5.5 years  
- BPT/Nursing: 4 years  
- **Focus:** Doctor, Dentist, Physiotherapist, Nurse, Ayurvedic/ Homeopathy Specialist

---

### 2. 🌿 **BAMS (Bachelor of Ayurvedic Medicine & Surgery)**
- **Focus:** Ayurvedic medicine and treatment  
- **Duration:** 5.5 years  
- **Career:** Ayurvedic doctor, practitioner, or researcher

---

### 3. 🧘 **BPT (Bachelor of Physiotherapy)**
- **Focus:** Physical therapy, rehabilitation, and fitness recovery  
- **Duration:** 4 years  
- **Career:** Physiotherapist, Sports Rehab Expert, Fitness Therapist

---

### 4. 🔬 **Biotechnology, Bioinformatics, Genetics**
- **Focus:** Research and development in life sciences  
- **Duration:** 3 years  
- **Career:** Lab Scientist, Geneticist, Biotech Engineer, R&D Specialist

---
""")
    elif stream_choice == "🔢Mathematics Stream":
        st.write("### Mathematics Stream (12th Mathematics) Options:")
        st.markdown("""
## 📐 Career Options After 12th - Mathematics Stream

---

### 1. � **JEE (Joint Entrance Examination)**
- **Purpose:** Admission to BTech/BE programs in top engineering institutes (IITs, NITs, IIITs)  
- **Duration:** 4 years  
- **Focus:** Engineering fields like Computer Science, Mechanical, Electrical, Civil, etc.

---

### 2. 💻 **BCA (Bachelor of Computer Applications)**
- **Focus:** Computer Science, software development, web & app programming  
- **Duration:** 3 years  
- **Career:** Software Developer, Web Developer, App Programmer, IT Consultant

---

### 3. 🔢 **BSc Mathematics**
- **Focus:** Advanced math concepts, theories, and real-world problem-solving  
- **Duration:** 3 years  
- **Career:** Mathematician, Statistician, Data Analyst, Educator

---

### 4. 📊 **Data Science & Analytics**
- **Focus:** Statistical analysis, big data, AI/ML models  
- **Duration:** 3 years (Bachelor's) or via specialized certifications  
- **Career:** Data Scientist, Analyst, Business Intelligence Expert

---

### 5. 🧾 **Actuarial Science**
- **Focus:** Risk analysis, finance, insurance mathematics  
- **Duration:** No fixed duration (depends on passing actuarial exams)  
- **Career:** Actuary, Financial Risk Manager, Insurance Analyst

---
""")
    elif stream_choice == "🏛️Government Jobs Opportunities":
        st.write("### Government Jobs Opportunities for you :")
        st.markdown("""
        ## 🔍 Top 10 Government Job Opportunities After 12th

        ---

        ### 1. 🏢 **SSC (Staff Selection Commission)**
        - **Role:** LDC, DEO, Junior Assistant, etc.  
        - **Eligibility:** 12th pass  
        - **Exam:** SSC CHSL  
        - **Salary:** ₹19,900 – ₹63,200  
        - **Age Limit:** 18–27 years  
        - **Type:** Central Government Jobs  

        ---

        ### 2. 🏦 **Bank Jobs**
        - **Role:** Clerk, Assistant, PO, Specialist Officer  
        - **Eligibility:** 12th pass (Clerk), Graduation (PO)  
        - **Exam:** SBI/IBPS Clerk & PO  
        - **Salary:** ₹20,000 – ₹45,000  
        - **Age Limit:** 20–30 years  
        - **Type:** Public Sector Banks  

        ---

        ### 3. 🚆 **Railway (RRB) Jobs**
        - **Role:** ASM, Ticket Collector, Group D, etc.  
        - **Eligibility:** 12th pass  
        - **Exam:** RRB NTPC, Group D, ALP  
        - **Salary:** ₹18,000 – ₹35,000  
        - **Age Limit:** 18–33 years  
        - **Type:** Indian Railways  

        ---

        ### 4. 🚓 **Police Jobs**
        - **Role:** Constable, Sub-Inspector (SI)  
        - **Eligibility:** 12th pass (Constable), Graduation (SI)  
        - **Exam:** SSC GD, State Police, UPSC CPO  
        - **Salary:** ₹21,700 – ₹1,12,400  
        - **Age Limit:** 18–25 (Constable), 20–25 (SI)  
        - **Type:** State & Central Police Forces  

        ---

        ### 5. 🪖 **Defence Jobs (Army/Navy/Air Force)**
        - **Role:** Soldier, Airmen, Sailor  
        - **Eligibility:** 12th pass (with specific subjects for technical roles)  
        - **Exam:** NDA, other recruitment exams  
        - **Salary:** ₹21,000 – ₹50,000+  
        - **Age Limit:** 16.5–23 years  
        - **Type:** Indian Armed Forces  

        ---

        ### 6. 👩‍🏫 **Teaching Jobs**
        - **Role:** Primary Teacher, TGT, PGT  
        - **Eligibility:** 12th + Diploma (Primary), Graduation for others  
        - **Exam:** CTET, State TET  
        - **Salary:** ₹25,000 – ₹60,000+  
        - **Age Limit:** 18–40 years  
        - **Type:** Government Schools  

        ---

        ### 7. 🎖️ **NDA (National Defence Academy)**
        - **Role:** Officer (Army/Navy/Air Force)  
        - **Eligibility:** 12th pass (PCM for tech roles)  
        - **Exam:** NDA  
        - **Salary:** ₹56,100 – ₹1,77,500+  
        - **Age Limit:** 16.5–19.5 years  
        - **Type:** Armed Forces Officer  

        ---

        ### 8. 📮 **Post Office Jobs**
        - **Role:** Postal Assistant, Sorting Assistant, MTS  
        - **Eligibility:** 12th pass  
        - **Exam:** India Post Exams  
        - **Salary:** ₹18,000 – ₹40,000+  
        - **Age Limit:** 18–27 years  
        - **Type:** India Post (Central Government)  

        ---

        ### 9. ✈️ **Air India Jobs**
        - **Role:** Cabin Crew, Ground Staff  
        - **Eligibility:** 12th pass  
        - **Exam:** Air India recruitment  
        - **Salary:** ₹25,000 – ₹50,000  
        - **Age Limit:** 18–27 years  
        - **Type:** Public Sector (Air India)  

        ---

        ### 10. 🏛️ **UPSC (Civil Services & Forest Services)**
        - **Role:** IAS, IPS, IFS  
        - **Eligibility:**  Graduation for others  
        - **Exam:** UPSC Civil Services, IFS  
        - **Salary:** ₹56,100 – ₹2,50,000  
        - **Age Limit:** 21–32 years  
        - **Type:** Central Government Services  

        ---
        """)
    elif stream_choice == "🤖AI Skills: Future Jobs, High Demand, High Growth!":
        st.write("### AI Skills: Future Jobs, High Demand, High Growth!")
        # Custom CSS for colorful design
        st.markdown("""
            <style>
            .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            }
            .stApp {
            background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
            }
            .header {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .section-header {
            font-size: 1.8rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 3px solid #667eea;
            }
            .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border-left: 5px solid #667eea;
            }
            .location-card {
            background: white;
            padding: 15px;
            border-radius: 10px;
            margin: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s;
            }
            .location-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            }
            .highlight {
            background: linear-gradient(90deg, #f6d365 0%, #fda085 100%);
            padding: 5px 10px;
            border-radius: 5px;
            font-weight: bold;
            color: white;
            }
            .apply-card {
            background: linear-gradient(90deg, #a8ff78 0%, #78ffd6 100%);
            padding: 25px;
            border-radius: 10px;
            margin-top: 30px;
            box-shadow: 0 6px 10px rgba(0,0,0,0.1);
            text-align: center;
            }
            .hour-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            padding: 8px;
            background-color: #f8f9fa;
            border-radius: 5px;
            }
            .footer {
            text-align: center;
            margin-top: 30px;
            padding: 15px;
            background: linear-gradient(90deg, #a1c4fd 0%, #c2e9fb 100%);
            border-radius: 10px;
            }
            </style>
            """, unsafe_allow_html=True)

        # Color palette
        colors = ["#FF9AA2", "#FFB7B2", "#FFDAC1", "#E2F0CB", "#B5EAD7", "#C7CEEA", "#F8B195", "#F67280", "#C06C84", "#6C5B7B"]

        # Header
        # Header
        st.markdown('<div class="header"><h1 style="color:white;text-align:center;">NSTI AI Programming Assistant Course</h1></div>', unsafe_allow_html=True)
        # Dictionary of NSTI locations and URLs
        locations = {
            "NSTI (W) Noida": "https://nstiwnoida.dgt.gov.in",
            "NSTI Kanpur": "https://nstikanpur.dgt.gov.in",
            "NSTI (W) Allahabad": "https://nstiwallahabad.dgt.gov.in",
            "NSTI (W) Hyderabad": "https://nstiw-hyderabad.dgt.gov.in",
            "NSTI Hyderabad (Ramanthapur)": "https://nstihyderabad.dgt.gov.in",
            "NSTI Mumbai": "https://nstimumbai.dgt.gov.in",
            "NSTI (W) Mumbai": "https://nstiwmumbai.dgt.gov.in",
            "NSTI (W) Vadodara": "https://nstiwvadodara.dgt.gov.in",
            "NSTI (W) Jaipur": "https://nstiwjaipur.dgt.gov.in",
            "NSTI Jodhpur": "https://nstijodhpur.dgt.gov.in",
            "NSTI (W) Kolkata": "https://nstiwkolkata.dgt.gov.in",
            "NSTI Howrah": "https://nstihowrah.dgt.gov.in",
            "NSTI Bengaluru": "https://nstibengaluru.dgt.gov.in",
            "NSTI (W) Bengaluru": "https://nstiwbengaluru.dgt.gov.in",
            "NSTI Ludhiana": "https://nstiludhiana.dgt.gov.in",
            "NSTI (W) Patna": "https://nstiwpatna.dgt.gov.in",
            "NSTI Chennai": "https://nstichennai.dgt.gov.in",
            "NSTI (W) Indore": "https://nstiwindore.dgt.gov.in",
            "NSTI Calicut": "https://nsticalicut.dgt.gov.in"
        }

        
        st.markdown('<div class="section-header">📍 Find Your NSTI Location</div>', unsafe_allow_html=True)
        st.markdown("🚀 *Now is the best time to learn AI skills!*<br>🧠 19 NSTIs across India have already started the **AI Programming Assistant** course.", unsafe_allow_html=True)

        selected_location = st.selectbox("Select NSTI Location: (NSTI (W)👉 National Skill Training Institute for Women)", ["Select"] + list(locations.keys()))

        if selected_location != "Select":
            url = locations[selected_location]
            st.success(f"Selected: {selected_location}")
            st.markdown(f'<a href="{url}" target="_blank"><button style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 10px 20px; border-radius: 5px; font-weight: bold; cursor: pointer;">Visit {selected_location} Website</button></a>', unsafe_allow_html=True)

        # 2. Eligibility Criteria
        st.markdown('<div class="section-header">✅ Eligibility Criteria</div>', unsafe_allow_html=True)

        eligibility_col1, eligibility_col2 = st.columns([1, 1])

        with eligibility_col1:
            st.markdown("""
            <div class="card">
            <h3>To apply for this course, you must:</h3>
            <ul>
                <li>Passed 10th class examination</li>
                <li>Have fundamental understanding of English</li>
                <li>Be willing to pursue a career in AI</li>
                <li>Open to migrate for job opportunities</li>
                <li>Dedicate 12 months to classroom learning</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        with eligibility_col2:
            st.markdown("""
            <div class="card" style="background-color: #f0f8ff;">
            <h3>📝 Additional Information</h3>
            <p><strong>Minimum Qualification:</strong> 10th Pass</p>
            <p><strong>Language Requirement:</strong> Basic English</p>
            <p><strong>Commitment:</strong> Full-time for 12 months</p>
            <p><strong>Admission:</strong> As per government norms</p>
            <p><strong>Career Focus:</strong> Artificial Intelligence</p>
            </div>
            """, unsafe_allow_html=True)

        # Course Overview
        st.markdown('''
            <div style="text-align: center; margin: 20px 0;">
            <h2>📚 Course Overview</h2>
            <p>The program is a <strong>structured and exhaustive engagement</strong> for eligible students with a strong focus on helping them develop relevant <span style="background: #f0c14b;">Artificial Intelligence skills</span> through an <strong>experiential learning methodology</strong>.</p>
            </div>

            <div style="display: flex; justify-content: space-around; text-align: center; margin: 20px 0;">
            <div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #667eea;">12</div>
            <div>Months</div>
            </div>
            <div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #667eea;">1,600</div>
            <div>Hours</div>
            </div>
            <div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #667eea;">2</div>
            <div>Levels</div>
            </div>
            <div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #667eea;">100%</div>
            <div>Practical Focus</div>
            </div>
            </div>

            <p>The program is delivered over <strong>12 months</strong> through <strong>Master Trainers</strong> with a combination of theoretical knowledge and hands-on practical experience.</p>
            ''', unsafe_allow_html=True)

        # Course Highlights
        st.markdown('<div style="font-size: 2rem; font-weight: bold; text-align: center; margin: 20px 0;">✨ Course Highlights</div>', unsafe_allow_html=True)

        highlights_col1, highlights_col2 = st.columns([1, 1])

        with highlights_col1:
            st.markdown("""
            <div class="benefits-card">
            <h3>🎯 Key Features</h3>
            <ul>
                <li><strong>Comprehensive AI training</strong> from fundamentals to advanced concepts</li>
                <li><strong>840+ hours</strong> of hands-on practical sessions</li>
                <li><strong>240 hours</strong> of virtual project-based learning</li>
                <li><strong>Industry-aligned</strong> curriculum designed with employer input</li>
                <li><strong>Employability focus</strong> with soft skills development</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        with highlights_col2:
            st.markdown("""
            <div class="benefits-card">
            <h3>🏆 What You'll Gain</h3>
            <ul>
                <li><strong>Strong foundation</strong> in core AI concepts and methodologies</li>
                <li><strong>Hands-on experience</strong> with real-world projects and case studies</li>
                <li><strong>Job-ready skillset</strong> tailored for AI industry demands</li>
                <li><strong>Official certification</strong> upon successful program completion</li>
                <li><strong>Career opportunities</strong> through our placement assistance program</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        # 5. Course Structure
        st.markdown('<div class="section-header">📚 Course Structure</div>', unsafe_allow_html=True)

        structure_col1, structure_col2 = st.columns([1, 1])

        with structure_col1:
            st.markdown("""
            <div class="card">
            <h3>⏳ Course Breakdown</h3>
            <div class="hour-item">
                <span>Trade Practical</span>
                <span class="highlight">840 hours</span>
            </div>
            <div class="hour-item">
                <span>Trade Theory</span>
                <span class="highlight">240 hours</span>
            </div>
            <div class="hour-item">
                <span>Employability Skills</span>
                <span class="highlight">120 hours</span>
            </div>
            <div class="hour-item">
                <span>Applied AI</span>
                <span class="highlight">240 hours</span>
            </div>
            <div class="hour-item">
                <span>Project-based Learning</span>
                <span class="highlight">160 hours</span>
            </div>
            </div>
            """, unsafe_allow_html=True)

        with structure_col2:
            st.markdown("""
            <div class="card">
            <h3>📊 Program Levels</h3>
            <div style="margin-bottom: 15px;">
                <h4>Foundational AI (1,200 hours)</h4>
                <p>Building core concepts and basic skills in Artificial Intelligence</p>
            </div>
            <div>
                <h4>Advanced AI (400 hours)</h4>
                <p>Specialized training in advanced AI techniques and applications</p>
            </div>
            <hr style="margin: 20px 0;">
            <div style="font-weight: bold; text-align: center;">
                <div style="font-size: 1.2rem;">Total Program Duration</div>
                <div style="font-size: 1.5rem; color: #667eea;">1,600 hours</div>
            </div>
            </div>
            """, unsafe_allow_html=True)

        # Apply Now Section
        st.markdown("""
        <div class="apply-card">
        <h2 style="color: #2c3e50; margin-bottom: 15px;">🚀 READY TO ACCELERATE YOUR AI CAREER?</h2>
        <p style="font-size: 1.2rem; margin-bottom: 10px;">Begin with the <strong>AI Programming Assistant</strong> course today!</p>
        <p style="font-size: 1.1rem; color: #444;"><strong>Prem Mohan</strong> has successfully completed the AI course at <strong>NSTI Kanpur</strong>. You can be next!</p>
        <a href="https://aimicrodegree.org/" target="_blank">
            <button style="background: linear-gradient(90deg, #ff416c 0%, #ff4b2b 100%);
                   color: white;
                   border: none;
                   padding: 12px 30px;
                   border-radius: 5px;
                   font-weight: bold;
                   cursor: pointer;
                   font-size: 1.1rem;
                   margin-top: 15px;">Apply Now</button>
        </a>
        </div>
        """, unsafe_allow_html=True)

        # Footer
        st.markdown("""
        <div class="footer">
        <p style="margin:0; font-weight:bold; font-size:1.1rem;">© 2025 NSTI AI Programming Assistant Course</p>
        <p style="margin:10px 0 0; font-size:0.9rem;">For more information, contact your nearest NSTI center</p>
        <p style="margin:5px 0 0; font-size:0.9rem;"><strong>Otherwise, contact: Mo. 8174083966 | Email: premmohan966@gmail.com</strong></p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        ## 🤖 AI & Future Skills - High Demand Careers

        ---
      

        ### 1. 💼 **Employability Skills**
        - **Skills Needed:** Communication, Teamwork, Problem Solving, Time Management  
        - **Courses:** Employability Skills by MSDE & NIMI, Soft Skills on Udemy  
        - **Jobs Impacted:** All job sectors including IT, marketing, customer service, and administration  
        - 📌 *These skills improve workplace performance and help in adapting to dynamic job roles.*
                    
        ---    

        ### 2. 🛠️ **Hardware Skills**
        - **Skills Needed:** Computer Assembly, Troubleshooting, Networking Basics, BIOS Setup  
        - **Courses:** Hardware & Networking by NIELIT, Basic IT Hardware from NSDC  
        - **Jobs:** Hardware Technician, Network Support Engineer, IT Maintenance Engineer  
        - 📌 *Hardware skills help you build, fix, and maintain computers and network systems – crucial for tech support and IT infrastructure roles.*                    

        ---
                    
        ### 3. 💻 **Software Skills**
        - **Skills Needed:** Operating Systems, MS Office, Code Editors (VS Code, Jupyter), Web Browsers  
        - **Courses:** MS Office by NIELIT, Computer Fundamentals by CSC Academy, Google Workspace Tutorials  
        - **Jobs:** Office Executive, Data Entry Operator, Software Tester  
        - 📌 *Software skills are essential for almost every job – from using MS Word and Excel to working with coding and productivity tools.*      

        ---            

        ### 4. 🐍 **Python for AI**
        - **Skills Needed:** Python Basics, Data Structures, Functions, Libraries (NumPy, Pandas, Matplotlib)  
        - **Courses:** Python for Everybody (Coursera), AICTE Python Course, W3Schools Python  
        - **Jobs:** AI Developer, Data Analyst, Machine Learning Engineer  
        - 📌 *Python is the foundation of AI. It is simple to learn and has powerful libraries used in AI and Data Science.*       
                    
        ---

        ### 5. 🧠 **Artificial Intelligence & Machine Learning**
        - **Skills Needed:** Python, TensorFlow, PyTorch, Data Analysis  
        - **Courses:** Google AI, IBM AI Engineering, Deep Learning Specialization  
        - **Jobs:** AI Engineer, ML Researcher, Data Scientist  

        ---

        ### 6. 📊 **Data Science & Analytics**
        - **Skills Needed:** Python/R, SQL, Statistics, Visualization  
        - **Courses:** IBM Data Science, Google Data Analytics  
        - **Jobs:** Data Analyst, Business Intelligence Expert  

        ---
                    
        ### 7. 🔒 **Cybersecurity**
        - **Skills Needed:** Ethical Hacking, Network Security, Cryptography  
        - **Certifications:** CEH, CompTIA Security+  
        - **Jobs:** Security Analyst, Penetration Tester  

        ---

        ### 8. 📊 **Power BI**
        - **Skills Needed:** Data Analysis, DAX (Data Analysis Expressions), Data Visualization, Excel Basics  
        - **Courses:** Microsoft Power BI (LinkedIn Learning), Power BI for Beginners (Udemy), Coursera - Data Visualization with Power BI  
        - **Jobs:** Business Intelligence Analyst, Data Analyst, Reporting Specialist  
        - 📌 *Power BI is a powerful tool used for creating interactive dashboards and reports. It helps organizations make data-driven decisions.*   

        ---

          ### 9. 🎯 **Placement Skills**
        - **Skills Needed:** Resume Writing, Interview Preparation, Aptitude, Group Discussions  
        - **Courses:** Naukri Learning - Interview Skills, TCS iON Career Edge  
        - **Jobs Impacted:** All tech/non-tech roles requiring interviews  
        - 📌 *Mastering placement skills helps you present your technical knowledge and personality effectively during interviews.*
                                         
                """)
    elif stream_choice == "🎓Government Jobs Opportunities After 12th":
        st.write("### 🔍Government Jobs Opportunities After 12th:")
        user_query = st.text_input('🎯 After 12th: Search Government Jobs & More Opportunities:')
        if user_query:
            job_search_section(user_query)
        else:   
            st.warning("Please enter a search query to find government jobs and opportunities.")
                

# --- YouTube Video Search ---
def search_youtube_videos(query, api_key):
    try:
        youtube = build("youtube", "v3", developerKey=api_key)
        request = youtube.search().list(
            q=query,
            part="snippet",
            maxResults=5,
            channelId="UCyvboRO_Z2rza0IOeJ85UxA"
        )
        response = request.execute()
        return response.get("items", [])
    except Exception as e:
        st.sidebar.error(f"Error fetching YouTube videos: {e}")
        return []

# --- Sidebar Learning Resources ---
def learn_more_sidebar():
    st.sidebar.title("Start Your Preparation with Prem Mohan NextGen \U0001F4DA")
    st.sidebar.title('\U0001F680 Boost Your Knowledge')

    st.sidebar.subheader("\U0001F4FA Prem Mohan's YouTube Channel")
    if st.sidebar.button("Go to YouTube Channel"):
        st.sidebar.markdown("[🎥 Hey Dear! Click Here to Visit My Channel 😊](https://www.youtube.com/@PremMohanofficial)")

    yt_search_query = st.sidebar.text_input("Search inside Channel:")
    if yt_search_query:
        videos = search_youtube_videos(
            yt_search_query,
            "AIzaSyA0rrzp3VznxIswQnmfzrIy9bb4PygmP38"
        )
        if videos:
            st.sidebar.success(f"🎉 Congratulations! Your video title was found. 👉 [Click Here] to watch. '{yt_search_query}':")
            for video in videos:
                if video['id'].get('kind') == 'youtube#video':
                    title = video['snippet']['title']
                    video_id = video['id'].get('videoId')
                    thumbnail = video['snippet']['thumbnails']['default']['url']
                    video_url = f"https://www.youtube.com/watch?v={video_id}"
                    st.sidebar.image(thumbnail, width=120)
                    st.sidebar.markdown(f"[{title}]({video_url})", unsafe_allow_html=True)
        else:
            st.sidebar.warning(f"😢 Sorry Dear! No videos found for your search query.'{yt_search_query}'")

    st.sidebar.subheader("Mock Test Options \U0001F4CB")
    search_test_query = st.sidebar.text_input("Search Mock Tests:", placeholder="Enter test name/subject")
    if search_test_query:
        search_url = f"https://testbook.com/online-test-series?q={search_test_query.replace(' ', '+')}"
        st.sidebar.markdown(f"\U0001F50D Searching for: **{search_test_query}**")
        st.sidebar.markdown(f"[\u2728 Congratulations! Your Searched Mock Test is Here!]({search_url})")

    if st.sidebar.button("Take Mock Test"):
        st.sidebar.markdown("[👉 Click here to take a Mock Test](https://testbook.com/online-test-series)")

    st.sidebar.subheader("\U0001F4CD Navigation")
    if st.sidebar.button("\U0001F3E0 Home"):
        st.session_state.page = "home"
        st.rerun()
    if st.sidebar.button("\u2139\uFE0F About"):
        st.session_state.page = "about"
        st.rerun()
    if st.sidebar.button("\U0001F4CA Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()


# --- Footer ---


def footer():
    st.markdown("""
    <style>
        .footer {
            padding: 20px;
            background-color: #f0f0f5;
            text-align: center;
            font-size: 14px;
            color: #333;
            border-top: 1px solid #ddd;
        }
        .footer h4 {
            font-size: 16px;
            margin-bottom: 10px;
        }
        .footer p {
            margin: 5px 0;
        }
        .success {
            font-size: 16px;
            color: #2E8B57;
            margin: 20px 0;
        }
    </style>

    <div class="footer">
        <div class="success">
            <h3>🎓 AI Programming Assistant Certified</h3>
            <p><strong>Congratulations!</strong> I've officially completed the <strong>Artificial Intelligence Programming Assistant (AIPA)</strong> course.</p>
            <p>You are now equipped to build intelligent applications using AI, Python, and data analysis techniques.</p>
            <p style="color: #4CAF50; font-weight: bold;">🔥 Future Innovator in the World of AI & Smart Tech!</p>
            <hr>
        </div>
        <h4>👨‍💼 Provider: Prem Mohan</h4>
        <p>📞 Contact: 8174083966</p>
        <p>🏠 Address: Gram & Post- Khaspur, Tanda, Dist- Ambedkar Nagar, Uttar Pradesh</p>
        <p>📧 Email: premmohan966@gmail.com</p>
        <p>🏡 Permanent Address: Gram & Post- Khaspur, Tanda, Dist- Ambedkar Nagar, Uttar Pradesh, 224190</p>
        <p>🔧 Hobbies: Explorer of New Technologies, Learning</p>
        <p>💻 Skills: Python, MySQL, HTML, Data Analysis, Machine Learning</p>
        <h4>🏅 Certifications:</h4>
        <p><strong>ADCA (12 Months)</strong><br>
        📅 November 2023 - November 2024<br>
        Skills: MS Office, Python, HTML, MySQL, Photoshop, Data Analysis, Communication</p>
        <p><strong>CCC (3 Months)</strong><br>
        📅 September 2024 - December 2024<br>
        Skills: Internet & Web Browsing, Basic Programming, Cloud Storage, Computer Operations</p>
    </div>
           <p><strong>AIPA (Artificial Intelligence Programming Assistant)</strong><br>
        📅 Completed<br>
        Skills: AI Programming, Python, Data Analysis, Machine Learning, Deep Learning, AI Application Development, Data Visualization, Neural Networks, NLP</p>
    </div>        
    """, unsafe_allow_html=True)

# --- Main Function ---
def main():
    st.set_page_config(page_title="Learning Platform", layout="wide")

    if "page" not in st.session_state:
        st.session_state.page = "home"

    learn_more_sidebar()
    if st.session_state.page == "dashboard":
        st.image("nextgen education.jpg.jpg", use_container_width=300)
        dashboard()
    elif st.session_state.page == "home":
        st.title("🏠 Home Page")
        st.image("nextgen education.jpg.jpg", use_container_width=300)
        st.markdown(
            "<h3 style='color:#009688; font-weight:bold;'>🎓 Welcome to <span style='color:#FF7043;'>Prem Mohan</span>'s Learning Platform!</h3>",
            unsafe_allow_html=True
        )

        st.markdown("""
        # 💼 Prem Mohan NextGen – Your Learning & Career Guide

        **Finished 12th and unsure what's next?**
        You're in the right place!

        **Prem Mohan NextGen** is a student-first platform built to guide your **career journey after 12th**.

        Whether you're from **Arts**, **Biology**, **Maths**, or aiming for **Government Jobs**, we provide the tools and knowledge to move ahead confidently.

        ---

        ### 🚀 What You Can Do Here

        ✅ **Explore Career Options**
        → Find courses, degrees, and career paths based on your stream.

        ✅ **Search Government Job Opportunities**
        → Stay updated with the latest **Sarkari Naukri** after 12th.

        ✅ **Learn from YouTube Videos**
        → Watch career tips, study tricks, and motivation from *Prem Mohan's Official Channel*.

        ✅ **Practice Mock Tests**
        → Get free test series to prep for exams.

        ✅ **Get Book Recommendations**
        → Access handpicked books and study materials for your goals.

        ---

        ### 👥 Who Is This For?

        * Students in or just completed **Class 12**
        * Aspirants preparing for **government or competitive exams**
        * Learners seeking **career advice and motivation**
        * Youth from **rural and small-town backgrounds** needing direction

        ---

        **Start today and shape a smarter, confident, and successful future with us!**
        """)
    elif st.session_state.page == "about":
        st.markdown(
            "<h3 style='color:#6A1B9A; font-weight:bold;'>🎓 Welcome to <span style='color:#00B8D4;'>Prem Mohan</span>'s Learning Platform!</h3>",
            unsafe_allow_html=True
        )
        st.header("👨‍💼About Prem Mohan NextGen")
        st.markdown("""
        *Prem Mohan NextGen* is a student-focused learning and career guidance platform dedicated to helping young minds shape their future after completing *12th grade*.

        We understand this stage of life can be \*confusing, \**overwhelming*, and full of questions like:

        * What should I do after 12th?
        * Which course or career is right for me?
        * How can I prepare for government jobs or competitive exams?
        * Where can I find the right study materials?

        🔍 Our platform is designed to answer \*all these questions in one place—with \**simplicity, clarity, and continuous support*.

        ---

        ### 🎯 Our Vision

        To \*empower students from every background—especially those in \**rural and semi-urban areas*—with accessible, reliable, and practical career guidance.

        We believe that \*talent is everywhere, but it needs the \**right direction and tools* to shine.

        ---

        ### 📚 What We Offer

        ✅ *Career Guidance Based on Your Stream*
        → Choose Arts, Biology, Mathematics, or Government Job stream and explore suitable career options, courses, and exams.

        ✅ *Latest Government Job Updates*
        → Stay updated with recent job notifications, eligibility criteria, and direct application links.

        ✅ *Free Mock Tests*
        → Test your knowledge with free online test series and exam simulations.

        ✅ *Video Learning from YouTube*
        → Watch career tips, study techniques, and motivational content from Prem Mohan's official YouTube channel.

        ✅ *Recommended Books*
        → Get handpicked books and materials tailored to your career goal and study needs.

        ✅ *Student-Friendly Interface*
        → Clean, simple, and mobile-friendly design to help you start learning anytime, anywhere.

        ---

        ### 👨‍🏫 Why Choose Us?

        * 🧑‍🎓 *Built by learners, for learners*
        * 🌐 *Completely online and easy to access*
        * 💡 *Focus on both academic and career development*
        * 🆓 *Most resources are free and community-driven*
        * 📞 *Personalized support and easy contact options*

        ---

        At \*Prem Mohan NextGen, we're not just building a platform—we're building a \**community of future leaders, dreamers, and achievers*.

        🚀 *Let's walk this journey together. Your future starts now!*
        """, unsafe_allow_html=True)
        footer()
    return

  

if __name__ == "__main__":
    main()
