import streamlit as st



col1, col2 = st.columns(2, gap='small', vertical_alignment="center")

with col1:
    st.image("./static/Port.jpg", width=400)
with col2:
    st.title("Nicholas Jordan", anchor=False)
    st.write(
        "Software Developer and Research Scientist. Major interest in " \
        "Deep/Machine Learning Research, Cloud Computing and Hosting (Docker, Kubernetes, AWS), " \
        "Backend Development, and Data Science."
    )

    st.write("Contact Me @ NikJordan525@gmail.com")

st.subheader("-- About Me -- ")
st.write("My love for programming began in 4th grade when I was" \
" a programmer for my robotics team. Ever since I have fallen in " \
"love with problem solving and creating solutions with code. " \
"I am currently pursuing my Bachelors of Science in Computer Science"
" and Systems at The University Of Washington -- Tacoma with the intention" \
" to get my Master's Degree in Deep Learning/Machine Learning and eventually my PhD "
"with a similar thesis. I have a strong thirst for knowledge and a passion for learning." \
" I've worked full time since I was in high-school balancing multiple jobs, side-projects, " \
"extracurricular activities, research, and maintaining a GPA of 3.98.")

st.subheader("-- Hobbies and Interests -- ")
st.write("As mentioned before I love to learn! My two favorite hobbies of all time are" \
" learning languages and snowboarding. The love for languages comes from the connection that " \
"is formed when you speak to someone in their native language and the desire to attain knowledge." \
" Snowboarding is by far my favorite sport, the breathtaking scenery and feeling of speeding" \
" down the mountain is unmatched and every person on the mountain has a story to tell!")


col3, col4 = st.columns(2, gap="medium", vertical_alignment="center")
with col3:
    st.subheader("-- Projects -- ")
    st.link_button(label="Projects Page", url="http://localhost:8501/projects") 

with col4:
    st.subheader("-- Resume --")
    st.link_button(label="Resume", url="http://localhost:8501/resume")
