document.getElementById("makePlan").addEventListener("click", function () {

    const wake = Number(document.getElementById("wake").value);
    const sleep = Number(document.getElementById("sleep").value);

    const subjects = document.getElementById("subjects").value.split(",");
    const hours = document.getElementById("hours").value.split(",");

    let result = "";

    let current = wake;

    result += `${current}:00 기상<br>`;
    result += `${current}:00 ~ ${current+0.5} 세면<br>`;
    current++;

    result += `${current-0.5}:30 ~ ${current}:00 아침식사<br><br>`;

    for(let i=0;i<subjects.length;i++){

        let h = Number(hours[i]);

        while(h>0){

            result += `${current}:00 ~ ${current+1}:00 <b>${subjects[i]}</b><br>`;
            current++;
            h--;

            if(current==12){
                result += `12:00 ~ 13:00 🍱 점심<br>`;
                current=13;
            }

            if(current==18){
                result += `18:00 ~ 19:00 🍚 저녁<br>`;
                current=19;
            }

            if(current%2==0){
                result += `${current}:00 ~ ${current}:10 ☕ 휴식<br>`;
            }

        }

    }

    result += `<br>${sleep}:00 취침`;

    document.getElementById("result").innerHTML=result;

});
<input id="wake" type="number" placeholder="기상시간(7)">

<input id="sleep" type="number" placeholder="취침시간(23)">

<input id="subjects"
placeholder="수학,영어,생명과학,한국사">

<input id="hours"
placeholder="2,1,2,1">

<button id="makePlan">
계획표 만들기
</button>

<div id="result"></div>
