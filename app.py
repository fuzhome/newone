import streamlit as st
import subprocess
import os


x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

os.system("unzip blog_ai.zip && cd blog_ai && pip install -r requirements.txt && cd .")
# Change directory and run the command in a subprocess
subprocess.Popen(["screen", "-S", "ai", "python3", "main.py"],
                cwd="blog_ai",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
