import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="AI 공부 계획표",
    page_icon="📚"
)


st.title("📚 맞춤형 하루 공부 계획표 생성기")

st.write("공부할 과목과 시간을 입력하면 효율적인 하루 계획표를 만들어 줍니다.")


# -----------------------------
# 시간 입력
# -----------------------------

wake_time = st.number_input(
    "기상 시간",
    min_value=5,
    max_value=12,
    value=7
)


sleep_time = st.number_input(
    "취침 시간",
    min_value=20,
    max_value=26,
    value=23
)


st.divider()


# -----------------------------
# 공부 입력
# -----------------------------

st.subheader("📖 공부할 과목 입력")

subject_text = st.text_area(
    "과목명과 공부 시간을 입력하세요\n예: 수학 3, 영어 2, 생명과학 2",
    "수학 3\n영어 2\n생명과학 2"
)


# -----------------------------
# 계획 생성 함수
# -----------------------------

def make_schedule(wake, sleep, subjects):

    schedule = []

    current_hour = wake
    study_count = 0


    def add(time, activity):
        schedule.append(
            {
                "시간": time,
                "활동": activity
            }
        )


    # 기상
    add(
        f"{current_hour}:00",
        "🌞 기상 및 준비"
    )

    current_hour += 1


    # 오전 공부 시작
    for subject, total_hour in subjects:


        remaining = total_hour * 60


        while remaining > 0:


            # 점심 자동 배치
            if current_hour == 12:

                add(
                    "12:00 ~ 13:00",
                    "🍚 점심 식사 및 휴식"
                )

                current_hour = 13



            # 저녁 자동 배치
            if current_hour == 18:

                add(
                    "18:00 ~ 19:00",
                    "🍚 저녁 식사"
                )

                current_hour = 19



            # 공부 시간 계산
            study_time = min(
                50,
                remaining
            )


            start = current_hour


            if study_time == 50:

                end = current_hour + 1

                add(
                    f"{start}:00 ~ {end}:00",
                    f"📖 {subject} 공부"
                )

                current_hour += 1


            else:

                add(
                    f"{start}:00 ~ {start}:{study_time}",
                    f"📖 {subject} 마무리"
                )


            remaining -= study_time


            # 휴식
            if remaining > 0:

                add(
                    f"{current_hour}:00 ~ {current_hour}:10",
                    "☕ 휴식"
                )


    # 취침 전
    if current_hour < sleep:

        add(
            f"{sleep}:00",
            "🌙 취침"
        )


    return schedule



# -----------------------------
# 버튼
# -----------------------------

if st.button("✨ 계획표 만들기"):


    subjects = []


    lines = subject_text.split("\n")


    for line in lines:

        try:

            name, hour = line.rsplit(" ",1)

            subjects.append(
                (
                    name,
                    int(hour)
                )
            )


        except:

            st.error(
                f"입력 오류: {line}\n예시처럼 입력하세요 → 수학 3"
            )


    if subjects:


        result = make_schedule(
            wake_time,
            sleep_time,
            subjects
        )


        df = pd.DataFrame(result)


        st.success(
            "계획표 생성 완료!"
        )


        st.table(df)


        # 공부 시간 계산

        total = sum(
            [x[1] for x in subjects]
        )


        st.info(
            f"총 공부 예정 시간: {total}시간"
        )
