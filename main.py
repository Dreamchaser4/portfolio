import streamlit as st
import pandas

EMAIL = "johnsonstephen424@gmail.com"
PAGE_TITLE = "Digital CV | Stephen Johnson-Rokosu"
PAGE_ICON = ":wave:"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

col1, col2 = st.columns(2)

with col1:
    st.image("images/pic.png", )

with col2:
    st.title("Stephen Johnson-Rokosu")
    context = """
       Hello, my name is Stephen. I'm a Python coder and a big fan of the Django web framework. 
       I received a Bachelor of Technology in Computer Science from Olusegun Agagu University of 
       Science and Technology in 2020.
         """

    st.write(context)
    st.write("📫", EMAIL)



st.write("#")
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Django, Streamlit), SQL
- 🗄️ Databases: Postgres,MySQL
"""
)
st.write('\n')
st.write("#")
st.subheader(" The applications I have created in Python using Django and Streamlit are listed below.")






col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[3:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/johnsonstephen424@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/main.css")

