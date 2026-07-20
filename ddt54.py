import streamlit as st
import time

def reset_game():
    st.session_state.start_time = None
    st.session_state.result = 0
    st.session_state.running = False

if "start_time" not in st.session_state:
    reset_game()

st.title("10초 맞추기 게임")

col1, col2 = st.columns(2)

with col1:
    if st.button("시작"):
        st.session_state.start_time = time.perf_counter()
        st.session_state.running = True
        st.session_state.result = 0

with col2:
    if st.button("종료"):
        if st.session_state.running:
            st.session_state.result = (
                time.perf_counter() - st.session_state.start_time
            )
            st.session_state.running = False
        else:
            st.warning("시작 버튼을 먼저 눌러주세요!")

# 결과 출력
if not st.session_state.running and st.session_state.result > 0:
    diff = st.session_state.result
    st.header(f"결과: {diff:.2f}초")

    if 9.7 <= diff <= 10.3:
        st.success("대단해요! 정확합니다!")
    else:
        st.error(f"10초와 {abs(10-diff):.2f}초 차이가 납니다.")

st.button("다시 하기", on_click=reset_game)
