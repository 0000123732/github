import streamlit as st
from datetime import datetime


st.set_page_config(
    page_title="Sleep Balance",
    page_icon="🌙",
    layout="centered"
)


# =========================
# 디자인 CSS
# =========================

st.markdown(
"""
<style>

.stApp {
    background:
    linear-gradient(
        180deg,
        #071426 0%,
        #10284d 60%,
        #1c3761 100%
    );
    color:white;
}


/* 구름 */

.cloud {
    position: fixed;
    opacity:0.15;
    font-size:80px;
    z-index:0;
}

.cloud1 {
    top:80px;
    left:40px;
}

.cloud2 {
    top:250px;
    right:50px;
}

.cloud3 {
    bottom:80px;
    left:100px;
}


.title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#ffffff;
}


.card {

    background:
    rgba(255,255,255,0.12);

    padding:25px;

    border-radius:25px;

    backdrop-filter: blur(10px);

}


.result {

    background:
    rgba(255,255,255,0.15);

    padding:20px;

    border-radius:20px;

    font-size:20px;

}


</style>


<div class="cloud cloud1">☁️</div>
<div class="cloud cloud2">☁️</div>
<div class="cloud cloud3">☁️</div>

""",
unsafe_allow_html=True
)



# =========================
# 제목
# =========================

st.markdown(
"""
<div class="title">
🌙 Sleep Balance
</div>

<p style="text-align:center;">
나의 생활 습관을 분석하고 건강한 수면을 추천해주는 앱
</p>

""",
unsafe_allow_html=True
)



st.write("")



# =========================
# 입력
# =========================


st.markdown(
"""
<div class="card">
<h3>🌌 오늘의 생활 기록</h3>
</div>
""",
unsafe_allow_html=True
)


sleep_time = st.time_input(
    "🌙 취침 시간",
    datetime.strptime(
        "23:00",
        "%H:%M"
    ).time()
)


wake_time = st.time_input(
    "🌞 기상 시간",
    datetime.strptime(
        "07:00",
        "%H:%M"
    ).time()
)



coffee = st.slider(
    "☕카페인 섭취 횟수",
    0,
    5,
    1
)


exercise = st.slider(
    "🏃 운동 시간(분)",
    0,
    120,
    20
)


study = st.slider(
    "📚 공부 시간(시간)",
    0,
    15,
    5
)



# =========================
# 분석
# =========================


def calculate_sleep(sleep, wake):

    sleep_hour = wake.hour - sleep.hour

    if sleep_hour < 0:
        sleep_hour += 24

    return sleep_hour



if st.button("✨ 수면 분석하기"):


    hours = calculate_sleep(
        sleep_time,
        wake_time
    )


    score = 100


    if hours < 6:
        score -= 30

    elif hours < 7:
        score -= 15


    if coffee >= 3:
        score -= 15


    if exercise < 10:
        score -= 10


    if study >= 10:
        score -= 10


    if score < 0:
        score = 0



    st.markdown(
    f"""
    <div class="result">

    🌙 예상 수면 시간:
    <b>{hours}시간</b>

    <br><br>

    ⭐ 수면 점수:
    <b>{score}점</b>

    </div>
    """,
    unsafe_allow_html=True
    )



    st.write("")


    if score >= 80:

        st.success(
            "✨ 좋은 수면 습관입니다! 현재 패턴을 유지해보세요."
        )


    elif score >= 50:

        st.warning(
            "🌙 조금 개선이 필요합니다. 취침 시간을 일정하게 유지해보세요."
        )


    else:

        st.error(
            "☁️ 수면 부족 상태입니다. 생활 패턴 조절이 필요합니다."
        )



    st.subheader("💡 추천")

    if hours < 7:
        st.write(
            "• 하루 최소 7시간 이상의 수면을 목표로 해보세요."
        )

    if coffee >= 3:
        st.write(
            "• 카페인은 잠들기 6시간 전부터 줄이는 것이 좋습니다."
        )

    if exercise < 10:
        st.write(
            "• 가벼운 운동을 추가하면 수면의 질 향상에 도움이 됩니다."
        )

    st.write(
        "• 매일 비슷한 시간에 자고 일어나는 습관을 만들어보세요."
    )
