import streamlit as st
import time

def reset_game():
    # 모든 상태를 0으로 초기화하는 함수
    st.session_state.start_time = 0
    st.session_state.end_time = 0
    st.session_state.result = 0

# 세션 상태 초기화 (처음 앱이 실행될 때만 실행)
if 'start_time' not in st.session_state:
    reset_game()

st.title("10초 맞추기 게임!")
st.write("시작 버튼을 누르고, 마음속으로 10초를 센 뒤 종료 버튼을 누르세요.")

col1, col2 = st.columns(2)
with col1:
    if st.button("시작"):
        st.session_state.start_time = time.time() # 현재 시각 기록
        st.session_state.end_time = 0             # 종료 시간 초기화
        st.session_state.result = 0
        st.success("타이머가 시작되었습니다! 마음속으로 10초를 세세요.")

with col2:
    if st.button("종료"):
        if st.session_state.start_time != 0:
            # 종료 버튼을 누르면 즉시 게임을 리셋하여 0초로 돌립니다.
            reset_game()
            st.info("종료 버튼을 눌러 타이머가 0초로 돌아갔습니다.")
        else:
            st.warning("시작 버튼을 먼저 눌러주세요!")

---

###  현재 타이머 상태
# 현재 결과 값을 화면에 보여줍니다. (종료를 누르면 0.00초가 됩니다)
st.header(f"측정된 시간: {st.session_state.result:.2f}초")

# 다시 하기 버튼
st.button("다시 하기", on_click=reset_game)
