import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="공부 계획표 생성기",
    page_icon="📚"
)


st.title("📚 나만의 하루 공부 계획표")
st.write("과목과 공부 시간을 입력하면 자동으로 하루 계획을 만들어 줍니다.")


# -------------------------
# 기본 시간 입력
# -------------------------

wake_time = st.number_input(
    "⏰ 기상 시간",
    min_value=5,
    max_value=12,
    value=7
)

sleep_time = st.number_input(
    "🌙 취침 시간",
    min_value=21,
    max_value=24,
    value=23
)


st.divider()


# -------------------------
# 과목 입력
# -------------------------

st.subheader("📖 공부할 과목")


subject_count = st.number_input(
    "과목 개수",
    min_value=1,
    max_value=10,
    value=3
)


subjects = []


for i in range(subject_count):

    col1, col2 = st.columns(2)

    with col1:
        subject = st.text_input(
            f"{i+1}번째 과목 이름",
            key=f"subject_{i}"
        )

    with col2:
        hour = st.number_input(
            f"{i+1}번째 공부 시간(시간)",
            min_value=1,
            max_value=10,
            value=1,
            key=f"hour_{i}"
        )

    if subject:
        subjects.append(
            {
                "name": subject,
                "minutes": hour * 60
            }
        )



# -------------------------
# 계획 생성 함수
# -------------------------

def make_plan(wake, sleep, subjects):

    result = []

    current = wake * 60


    def add(start, end, text):

        start_h = start // 60
        start_m = start % 60

        end_h = end // 60
        end_m = end % 60


        result.append(
            {
                "시간":
                f"{start_h:02d}:{start_m:02d} ~ {end_h:02d}:{end_m:02d}",

                "내용": text
            }
        )



    # 기상

    add(
        current,
        current + 30,
        "🌞 기상 및 준비"
    )

    current += 30



    # 아침

    add(
        current,
        current + 30,
        "🍞 아침 식사"
    )

    current += 30



    for subject in subjects:

        remain = subject["minutes"]


        while remain > 0:


            # 점심 시간

            if 720 <= current < 780:

                add(
                    current,
                    780,
                    "🍚 점심 식사"
                )

                current = 780



            # 저녁 시간

            if 1080 <= current < 1140:

                add(
                    current,
                    1140,
                    "🍚 저녁 식사"
                )

                current = 1140



            # 공부 50분

            study_time = min(
                50,
                remain
            )


            add(
                current,
                current + study_time,
                f"📖 {subject['name']} 공부"
            )


            current += study_time
            remain -= study_time



            # 휴식 10분

            if remain > 0:

                add(
                    current,
                    current + 10,
                    "☕ 휴식"
                )

                current += 10



    # 취침

    add(
        sleep * 60,
        sleep * 60,
        "🌙 취침"
    )


    return result




# -------------------------
# 실행 버튼
# -------------------------

if st.button("✨ 하루 계획표 만들기"):


    if len(subjects) == 0:

        st.warning(
            "공부할 과목을 입력해주세요."
        )


    else:

        schedule = make_plan(
            wake_time,
            sleep_time,
            subjects
        )


        df = pd.DataFrame(schedule)


        st.success(
            "계획표 생성 완료!"
        )


        st.table(df)
