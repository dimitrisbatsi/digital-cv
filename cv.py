import streamlit as st
import datetime

# --- Page Config ---
st.set_page_config(page_title="Dimitrios P. Batsilis - Digital CV", page_icon="💼", layout="wide")

# --- CSS Styling ---
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; font-weight: bold; color: #2e86c1;}
    .sidebar-name {font-size: 1.8rem; font-weight: bold; text-align: center; margin-bottom: 20px; color: #1b4f72;}
    .job-title {font-size: 1.2rem; font-weight: bold; color: #1b4f72; margin-bottom: 0px;}
    .date-text {color: #555555; font-style: italic;}
    .footer {
        text-align: center;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #eaeaea;
        color: #888888;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 1. Session State Initialization
# ==========================================
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = "About Me"

# ==========================================
# 2. Sidebar Navigation
# ==========================================
st.sidebar.image("images/personal_image_bw_small.jpg", width='stretch')
st.sidebar.markdown('<h1 class="sidebar-name" style="font-weight:700">Dimitrios P. Batsilis</h1>', unsafe_allow_html=True)

if st.sidebar.button("About Me ", icon=":material/arrow_right_alt:", icon_position="right", width='stretch', type="tertiary"):
    st.session_state['current_page'] = "About Me"

if st.sidebar.button("Experience", icon=":material/arrow_right_alt:", icon_position="right", width='stretch', type="tertiary"):
    st.session_state['current_page'] = "Experience"

if st.sidebar.button("Projects / Portfolio", icon=":material/arrow_right_alt:", icon_position="right", width='stretch', type="tertiary"):
    st.session_state['current_page'] = "Projects / Portfolio"

st.sidebar.markdown("---")
st.sidebar.write("**Tech Stack Highlights:**")
st.sidebar.write("♦️ ASP.NET Core / MVC / Blazor\n\n♦️ Python / Streamlit\n\n♦️ SQL & Data ETL\n\n♦️ Power BI")

# ==========================================
# Κουμπί Λήψης PDF Βιογραφικού
# ==========================================
# Διάβασμα του αρχείου PDF (βεβαιώσου ότι το αρχείο υπάρχει στον φάκελό σου)
try:
    with open("Batsilis_CV.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.sidebar.download_button(
        label="📄 Download CV (PDF)",
        data=PDFbyte,
        file_name="Dimitrios_Batsilis_CV.pdf",
        mime="application/octet-stream",
        width='stretch',
        type="primary" # Το primary το κάνει συνήθως να ξεχωρίζει χρωματικά
    )
except FileNotFoundError:
    st.sidebar.warning("Το αρχείο PDF του βιογραφικού δεν βρέθηκε τοπικά.")

# ==========================================
# 3. Content Display
# ==========================================
page = st.session_state['current_page']

# ==========================================
# PAGE 1: About Me
# ==========================================
if page == "About Me":
    # st.image("images/1598278843455.jpeg", width='stretch')
    st.image("images/cover2_small.jpg", width='content')
    st.markdown("---") 

    col1, col2 = st.columns([2.5, 1.2])
    
    with col1:
        st.markdown('<h3 class="main-header">Business Solutions Engineer | Senior ERP Consultant</h3>', unsafe_allow_html=True)
        st.write("""
        My expertise as a Solutions Engineer lies in my ability to bridge the gap between complex business needs and practical, scalable technical solutions. 
        I excel at analyzing intricate problems, identifying root causes, and developing innovative solutions that address both immediate challenges and long-term strategic goals.
        
        I possess a broad range of technical skills across Software Development (.NET, Python), Data Engineering (SQL, ETL, SSAS), and Business Intelligence (Power BI), enabling me to work with diverse technologies and platforms.
        """)
        
    with col2:
        st.error("""
        ##### Contact Info
        📍 Thessaloniki, Greece 
                  
        📞 +30 694 724 6710  
                                  
        🔗 [LinkedIn Profile](https://www.linkedin.com/in/dimitrios-batsilis-21033786/)  
                 
        🗣️ Greek (Native), English
        """)

    st.markdown("---")


    # --- SKILLS SECTION ---
    st.markdown("### Technical Skills & Expertise")
    skill_col1, skill_col2, skill_col3, skill_col4 = st.columns(4)
    
    with skill_col1:
        st.write("**Software Development**")
        st.write("✔️ ASP.NET Core / MVC\n\n✔️ Blazor\n\n✔️ Python\n\n✔️ C#\n\n✔️ JavaScript / HTML / CSS")
    with skill_col2:
        st.write("**Data Engineering & BI**")
        st.write("✔️ Microsoft Power BI\n\n✔️ SQL Server / SSAS\n\n✔️ ETL Pipelines\n\n✔️ Data Modeling\n\n✔️ Data Visualization")
    with skill_col3:
        st.write("**Systems & Integrations**")
        st.write("✔️ ERP Systems\n\n✔️ RESTful APIs / Webhooks\n\n✔️ Countersoft Gemini Admin\n\n✔️ Jira Administration")
    with skill_col4:
        st.write("**Core Competencies**")
        st.write("✔️ Requirements Analysis\n\n✔️ Technical Documentation\n\n✔️ IT Support & Training\n\n✔️ Workflow Optimization")

# ==========================================
# PAGE 2: Experience
# ==========================================
elif page == "Experience":
    st.markdown('<h3 class="main-header" style="font-weight:700">Work Experience</h3>', unsafe_allow_html=True)
    
    # Role 1
    st.markdown('<h4 class="job-title">Solutions Engineer - Services Operations | Epsilon SingularLogic</h4>', unsafe_allow_html=True)
    st.badge("Jan 2025 - Present", color="red")
    st.write("""
    * **Power BI Development & Reporting:** Designing, developing, and maintaining interactive dashboards and insightful reports using Power BI to visualize key performance indicators and business intelligence.
    * **ETL Processes & Data Integration:** Architecting, building, and managing ETL pipelines to integrate data from various internal systems into centralized data warehouses or data lakes.
    * **Data Transformation & Modeling:** Implementing data cleansing, transformation, and modeling techniques to ensure data accuracy, consistency, and usability for analysis and reporting.
    * **ASP.NET MVC Web Application Development:** Leading the design, development, and deployment of new ASP.NET MVC web applications to address specific internal business needs and improve workflow efficiency.
    * **Requirements Gathering & Analysis:** Collaborating with internal stakeholders to understand needs, gather requirements, and translate them into technical specifications.
    * **Testing, Deployment & Documentation:** Conducting thorough testing, overseeing deployments, providing ongoing support, and creating comprehensive technical documentation for data models, reports, and apps.
    """)
    st.markdown("---")
    
    # Role 2
    st.markdown('<h4 class="job-title">ERP Senior Consultant | Epsilon SingularLogic</h4>', unsafe_allow_html=True)
    st.badge("Apr 2022 - Feb 2025", color="red")
    st.write("""
    * **Customer Support:** Provided comprehensive customer support and communication, resolving technical issues to ensure client satisfaction.
    * **ERP Management:** Managed and maintained ERP platforms for system stability and optimal performance.
    * **System Enhancements:** Developed JavaScript code for custom integrations and enhancements, extending system functionality.
    * **TMS Administration:** Administered the TMS system (Countersoft Gemini) to ensure smooth operations and proper user access management.
    """)
    st.markdown("---")
    
    # Role 3
    st.markdown('<h4 class="job-title">Freelancer - Web Development & Systems Integration</h4>', unsafe_allow_html=True)
    st.badge("2021 - 2022", color="red")
    st.write("""
    * Handled end-to-end client communication, requirements gathering, and technical delivery as an independent freelancer.
    * Executed Custom Web Development, Landing Page Development, and Website Debugging across multiple platforms (Joomla, WordPress, Shopify, Wix).
    * Delivered API Integrations connecting web platforms with enterprise ERP and CRM systems.
    """)
    st.markdown("---")
    
    # Παλαιότερη Εμπειρία (Συμπτυγμένη)
    st.markdown('<h4 class="job-title">Early Career: Sales & Customer Support</h4>', unsafe_allow_html=True)
    st.badge("2017 - 2019", color="red")
    st.write("""
    * **Sales Promotions Specialist | MLS Innovation Inc.** (Jul 2018 - Sep 2019): Handled customer service, complaint management, and sales promotions.
    * **Internet Specialist & External Sales Representative | Vodafone** (Mar 2017 - Apr 2018): Focused on problem-solving, direct client communication, and external sales operations.
    """)

# ==========================================
# PAGE 3: Projects / Portfolio
# ==========================================
elif page == "Projects / Portfolio":
    st.markdown('<h3 class="main-header" style="font-weight:700">Featured Projects</h3>', unsafe_allow_html=True)
    st.write("Here are some selected projects that highlight my expertise across different technology domains.")
    
    tab1, tab2, tab3 = st.tabs(["💻 Software Development", "📊 Data Engineering & BI", "⚙️ Systems & Integrations"])
    
    with tab1:
        proj1_col1, proj1_col2 = st.columns([0.4, 1])
        with proj1_col1:
            st.image("images/stokk-b2b-app-preview.png", caption="SaaS App Preview")

        with proj1_col2:
            st.subheader("B2B SaaS Application (In Progress)")
            st.badge("**Tech Stack:** ASP.NET Core Full Stack", color="red")
            st.write("Designing and developing a scalable, full-stack B2B SaaS application aimed at optimizing business operations locally. Handling both backend architecture and frontend implementation.")
        
        st.markdown("---")
        st.subheader("Web Applications Development")
        st.badge("**Tech Stack:** ASP.NET MVC, Blazor", color="red")
        st.write("Development of responsive and highly functional web applications to cover specific business needs, ensuring clean code and scalable architecture.")

    with tab2:
        proj2_col1, proj2_col2 = st.columns([1, 2])
        with proj2_col1:
            st.subheader("Support Team Time Management Dashboard")
            st.badge("**Tech Stack:** Power BI, Python, SQL", color="red")
            st.write("Designed and developed a comprehensive BI tool to monitor and manage the time allocation of the support team. Handled the entire pipeline from data extraction (ETL) to visualization in Power BI.")
        with proj2_col2:
            st.image("images/power_bi_dashboard.jpg", caption="Power BI Dashboard")
        
        st.markdown("---")
        st.subheader("Enterprise Data Warehouse Setup")
        st.badge("**Tech Stack:** SQL Server, SSAS, ETL", color="red")
        st.write("Architecture and management of complex SQL Data Warehouses, establishing reliable Data ETL pipelines and configuring SQL Analysis Services for optimized reporting.")

    with tab3:
        st.subheader("Gemini to Jira Data Migration API")
        st.badge("**Tech Stack:** .NET Web API, RESTful Services", color="red")
        st.write("Engineered a custom .NET Web API application to facilitate the secure and automated migration of ticketing and operational data from Countersoft Gemini to Jira.")

        st.markdown("---")
        st.subheader("ERP & CRM Web Integrations")
        st.badge("**Tech Stack:** REST APIs, Webhooks, PHP/JS", color="red")
        st.write("Successfully integrated various CMS/E-commerce platforms (WordPress, Shopify, Joomla) with enterprise ERP and CRM systems to synchronize inventory, sales, and customer data.")

# ==========================================
# FOOTER (Copyright)
# ==========================================
current_year = datetime.datetime.now().year
st.markdown(f'<div class="footer">© {current_year} Dimitrios P. Batsilis. All Rights Reserved.</div>', unsafe_allow_html=True)