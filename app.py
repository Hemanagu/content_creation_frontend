import streamlit as st
import requests

be_url=st.secrets["be_url_server"]

st.set_page_config(
    page_title="AI Content Generator",
    layout="wide"
)

st.title("AI Content Generator")
st.write("Generate Blogs, LinkedIn Posts, Captions, Emails and more")

topic=st.text_input("Enter the topic")

technology= st.selectbox(
    "Select Technology",
    ['Python',
    'Java',
    'SQL',
    'React',
    'Node JS',
    'Mern',
    'C',
    'C++',
    'Machine Learning',
    'Deep Learning',
    'AI',
    'Gen AI'
]
    
)

content_type = st.selectbox(
    "Content Type",
    [
        "LinkedIn Post",
        "Blog",
        "Instagram Caption",
        "Twitter Post",
        "Email",
        "YouTube Description",
        "WhattsApp Message"
        
    ]
)

tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Technical",
        "Friendly",
        "Casual",
        "Marketing"
    ]
)

generate = st.button("Generate Content")

if generate:
    if topic=="":
        st.warning("Please Enter topic you want to create")
    
    else:
        with st.spinner("Please wait a moment....Generating Content"):
            response=requests.post(
                f"{be_url}/generate",
                params={
                    "topic":topic,
                    "technology":technology,
                    "content_type":content_type,
                    "tone":tone
                }
            )
        
        st.write("Status Code:", response.status_code)
        st.write("Response Text:", response.json()["content"])
        st.success("Content Generated Successfully")
        st.subheader("Generated Content")

