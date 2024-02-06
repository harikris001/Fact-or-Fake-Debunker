import os
import streamlit as st
import requests
from dotenv import load_dotenv

def get_file_size(file):
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    return file_size

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))
filepath = os.environ.get("DROPBOX_LOCAL_FOLDER_PATH")


# Streamlit UI elements
st.title("You Have Been Warned 😮😮!!!")

with st.sidebar:
    st.markdown("## Fake or Fact Debunkathon...\n")
    st.markdown("**You Have Been Warned** is a MYTHBUSTER series that is famous for debunking science facts and Info. Ask any 'Outrageous Acts of Science.'  and we can tell you whether its *FAKE* or *FACT* with great explanation just like <br> *YOU HAVE BEEN WARNED*. 😎", unsafe_allow_html=True)
    st.markdown(
        """ Enter your weiredest science facts here.... \n"""
    )

    st.markdown( "Got any specific question upload your source document to [DropBox](https://www.dropbox.com/home/Documents) ")
    st.markdown(
        """[View the source code on GitHub](https://github.com/harikris001/) Liked the project consider giving a star. 🌟""")

st.markdown(" What's Your Question today mate.... ❓", unsafe_allow_html=True)

file_details = {}
file_path = ''

question = st.text_input("Tell me what to debunk today.🔑", placeholder="Ask mee..")

if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query":question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Gotcha...")
        st.markdown(response.json())
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")