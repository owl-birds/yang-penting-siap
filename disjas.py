import pandas as pd
import streamlit as st

import plotly.express as px
import altair as alt

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )
#######################################
# here is how to create containers
header_container = st.container()
stats_container = st.container()	
#######################################

with header_container:
	st.title("Visualisasi Penumpang Pelayaran dalam Negeri di Pelabuhan Utama (Orang) 2016-2021")
with stats_container:
    st.write(" #### source: https://www.bps.go.id/indicator/17/69/1/total-penumpang-pelayaran-dalam-negeri-di-pelabuhan-utama.html ")
    keberangkatan = pd.read_csv("penumpang-Keberangkatan3.csv")
    st.write(" ## Total Penumpang Keberangkatan menurut Pelabuhan utama 2016-2021")
    pelabuhan_keberangkatan = st.selectbox("Pelabuhan", ["Belawan","Tanjung Priok","Tanjung Perak", "Balikpapan", "Makassar"], key="keberangkatan")
    st.write(pelabuhan_keberangkatan)
    st.write(keberangkatan)
    # st.write(keberangkatan.iloc[:,1:-1].columns)
    # st.write(2 in [22,3,4])
    # st.write(keberangkatan["Makassar"].values)
    # edit dataset based on the user iniput 
    # fig = px.line(keberangkatan["Makassar"], y=keberangkatan["Makassar"])
    # st.write(fig)
    # st.line_chart(keberangkatan.iloc[:,1:-1].values)
    keberangkatan_dict = {
        "Belawan" : keberangkatan.iloc[:,1:2],
        "Tanjung Priok" : keberangkatan.iloc[:,2:3],
        "Tanjung Perak" : keberangkatan.iloc[:,3:4],
        "Balikpapan" : keberangkatan.iloc[:,4:5],
        "Makassar": keberangkatan.iloc[:, 5:6]
    }
    # st.write(keberangkatan.iloc[:,1:-1].values)
    # st.write(list(keberangkatan["Belawan"].values)[0] + "10000")
    # VISUALIZE
    st.line_chart(keberangkatan_dict[pelabuhan_keberangkatan])
    # fig = px.line(keberangkatan.iloc[:,1:-1], y=["Belawan"] x=list(range(1,len(keberangkatan)+1)) )
    # st.write(fig)
    # st.write(keberangkatan_dict)
    # st.line_chart(keberangkatan.iloc[:,1:-1])
    st.write(" ## Total Penumpang Kedatangan menurut Pelabuhan utama 2016-2021")
    kedatangan = pd.read_csv("penumpang-Kedatangan2.csv")
    pelabuhan_kedatangan = st.selectbox("Pelabuhan", ["Belawan","Tanjung Priok","Tanjung Perak", "Balikpapan", "Makassar"], key="kedatangan")
    st.write(pelabuhan_kedatangan)
    st.write(kedatangan)
    kedatangan_dict = {
        "Belawan" : kedatangan.iloc[:,1:2],
        "Tanjung Priok" : kedatangan.iloc[:,2:3],
        "Tanjung Perak" : kedatangan.iloc[:,3:4],
        "Balikpapan" : kedatangan.iloc[:,4:5],
        "Makassar": kedatangan.iloc[:, 5:6]
    }
    st.line_chart(kedatangan_dict[pelabuhan_kedatangan])
    # st.write(kedatangan.iloc[:,1:-1].columns)
    