import streamlit as st
import pandas as pd 
dic={"ages":[20,30,40,50]}
df=pd.DataFrame(dic)
st.title("Hello, Streamlit")
st.write("If you can read this, your app is live.")

code = '''
# to import streamlit use this command 
import streamlit as st
'''
st.code(code,language="python")
name = st.text_input("What's your name?")
if name:
    st.success(f"Nice to meet you, {name}!")

name   = st.text_input("Name")
age    = st.slider("Age", 0, 100, 25)
agree  = st.checkbox("I accept the terms")
flavor = st.selectbox("Pick one", ["Vanilla", "Mango", "Mint"])

if st.button("Submit"):
    st.write(f"{name} is {age} and likes {flavor}.")