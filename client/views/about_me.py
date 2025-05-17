import streamlit as st
from components.form import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


col1, col2 = st.columns(2, gap='small', vertical_alignment="center")

with col1:
    st.image("./assets/Port.jpg", width=400)
with col2:
    st.title("Nicholas Jordan", anchor=False)
    st.write(
        "Software Developer and Research Scientist. Major interest in " \
        "Deep/Machine Learning Research, Cloud Computing and Hosting (Docker, Kubernetes, AWS), " \
        "Backend Development, and Data Science."
    )

    if st.button("Contact Me"):
        show_contact_form()

st.subheader("-- About Me -- ")
st.write("My love for programming began in 4th grade when I was" \
" a programmer for my robotics team. Ever since I have fallen in " \
"love with problem solving and creating solutions with code." \
"I am currently pursuing my Bachelors of Science in Computer Science"
" and Systems and The University Of Washington -- Taocma with the intention" \
"to get my Master's Degree in Deep Learing/Machine Learning and eventually my PHD "
"with a similar thesis. I have a strong thirst for knowledge and a passion for learning." \
" I've worked full time since I was in high-school balancing multiple jobs, side-projects, " \
"extracurricular activies, and maintaining a GPA of 3.98.")

st.subheader("-- Hobbies and Interests -- ")
st.write()
