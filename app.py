import pandas as pd
import sys
import streamlit as st

df = pd.read_csv("/Users/ayumuueda/Desktop/wevote_reco/model_with_twitter.csv")

st.set_page_config(page_title="Explore Related Candidates Demo")
st.header("Explore Related Candidates Demo")

politician_name = st.sidebar.selectbox("Candidate", list(df["ballot_item_display_name"]))
if st.sidebar.button('Get Related Candidate', key='Get'):
    cluster = df[df['ballot_item_display_name'] == politician_name]['Cluster'].item()
    potCandidate = df[df["Cluster"] == cluster]
    try:
        potCandidate = potCandidate.sample(n=5)
    except:
        potCandidate = potCandidate.sample(n=1)

    st.write(potCandidate)
