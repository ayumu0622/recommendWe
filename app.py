import pandas as pd
import sys
import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import ast
from sklearn.decomposition import PCA
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("cosine_model.csv")
origin = pd.read_csv("originaldata.csv")
st.set_page_config(page_title="Explore Related Candidates Demo")
st.header("Explore Related Candidates Demo")

politician_name = st.sidebar.selectbox("Candidate", list(df["ballot_item_display_name"]))
similarity_matrix = pd.DataFrame(
    cosine_similarity(df[[i for i in df.columns if i not in ["we_vote_id",	"ballot_item_display_name"]]]))

def get_related_cand(dff, topk, similarity_matrix, loc):
  topkList = list(similarity_matrix[loc].sort_values(ascending=False).index)[0:topk]
  topkList.remove(loc)
  return topkList

if st.sidebar.button('Get Related Candidate', key='Get'):
    loc = list(df[df['ballot_item_display_name'] == politician_name].index)[0]

    st.write("candidate visited")
    st.write(origin.loc[[loc]])

    st.write("top 50 relate candidates")
    st.write(origin.loc[get_related_cand(df, 50, similarity_matrix, loc)])

# df = pd.read_csv("model_with_twitter.csv")

# st.set_page_config(page_title="Explore Related Candidates Demo")
# st.header("Explore Related Candidates Demo")

# politician_name = st.sidebar.selectbox("Candidate", list(df["ballot_item_display_name"]))
# if st.sidebar.button('Get Related Candidate', key='Get'):
#     cluster = df[df['ballot_item_display_name'] == politician_name]['Cluster'].item()
#     potCandidate = df[df["Cluster"] == cluster]
#     try:
#         potCandidate = potCandidate.sample(n=5)
#     except:
#         potCandidate = potCandidate.sample(n=1)

#     st.write(potCandidate)
