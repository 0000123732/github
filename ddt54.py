import streamlit as st

st.title("카운터 앱")
if 'count' not in st.session_state:
    st.session state.counte = 0
if st.button("증가"):
   st.session_state.count += 1
st.markdown (f"## 현재 숫지: "{st.session_state.count}'")
