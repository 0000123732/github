import streamlit as st
import time

# 게임 상태를 초기화하는 함수
def reset_game():
    st.session_state.start_time = 0
    st.session_state.end_time = 0
    st.session_state.result = 0

# 세션 상태 초기화 (처음 앱이 실행될 때만 실행됨)
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

with col2:
    if st.button("종료"):
        if st.session_state.start_time != 0:
            # 원래는 여기에 시간 계산이 들어가지만, 
            # "종료 시 0으로 돌아가게" 하기 위해 세션을 초기화합니다.
            reset_game()
            st.success("타이머가 종료되고 초기화되었습니다!")
        else:
            st.warning("시작 버튼을 먼저 눌러주세요!")

# 현재 기록된 결과 출력 (종료를 누르면 0이 됩니다)
st.metric(label="현재 측정된 시간", value=f"{st.session_state.result:.2f}초")

# 다시 하기 버튼
st.button("다시 하기", on_click=reset_game)
