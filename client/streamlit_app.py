import streamlit as st


# Page Setup
about_page = st.Page(
    "./views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    url_path="/home",
    default=True
)

projects_page = st.Page(
    "./views/projects.py",
    title="Projects",
    url_path="/projects",
    icon=":material/play_arrow:"
)

resume_page = st.Page(
    "./views/resume.py",
    title="My Resume",
    url_path="/resume",
    icon=":material/info:"
)

# Navigation bar
pg = st.navigation(pages=[about_page, projects_page, resume_page])

st.sidebar.markdown(f"""
             <div style="display: flex; gap: 18px; align-items: center; justify-content: center;">       
        <a href="https://www.linkedin.com/in/nicholasjordanbe" target="_blank">
            <img src="https://img.icons8.com/?size=100&id=13930&format=png&color=000000"
                 alt="LinkedIn" width="48"/>
        </a>
                <a href="https://www.github.com/NickJordan-BE" target="_blank">
            <img src="https://img.icons8.com/?size=100&id=u9R54eMKS8fw&format=png&color=000000"
                 alt="GitHub" width="48"/>
        </a>
        <a href="NikJordan525@gmail.com" target="_blank">
            <img src="https://img.icons8.com/?size=100&id=P7UIlhbpWzZm&format=png&color=000000"
                 alt="Gmail" width="48" />
        </a>
                    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("</br> Made by Nicholas Jordan", unsafe_allow_html=True)
# Initialize navigation

pg.run()