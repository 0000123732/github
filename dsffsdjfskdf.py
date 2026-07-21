function makePlan(){

    const major=document.getElementById("major").value;
    const time=parseInt(document.getElementById("time").value);

    let subjects=[];

    if(major=="컴퓨터공학"){
        subjects=["수학","영어","Python","알고리즘","AI"];
    }

    if(major=="의학"){
        subjects=["생명과학","화학","영어","국어","수학"];
    }

    if(major=="경영학"){
        subjects=["수학","경제","영어","사회","독서"];
    }

    if(major=="디자인"){
        subjects=["드로잉","포토샵","색채학","영어","미술사"];
    }

    if(major=="교육학"){
        subjects=["국어","영어","교육학","독서","발표연습"];
    }

    let html="<h2>오늘의 계획표</h2>";

    let start=9;

    for(let i=0;i<time;i++){

        html+=`
        <p>
        ${start}:00 ~ ${start+1}:00
        ▶ ${subjects[i%subjects.length]}
        </p>
        `;

        start++;
    }

    document.getElementById("result").innerHTML=html;

}
body{
    font-family: Arial;
    background:#eef5ff;
}

.container{
    width:400px;
    margin:50px auto;
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0 0 15px gray;
}

button{
    margin-top:20px;
    width:100%;
    padding:10px;
    background:#4f7cff;
    color:white;
    border:none;
    border-radius:10px;
    cursor:pointer;
}

#result{
    margin-top:20px;
}
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>AI 공부 계획표</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
    <h1>📚 AI 공부 계획표</h1>

    <label>관심 분야</label>
    <select id="major">
        <option>컴퓨터공학</option>
        <option>의학</option>
        <option>경영학</option>
        <option>디자인</option>
        <option>교육학</option>
    </select>

    <label>하루 공부 가능 시간</label>
    <input type="number" id="time" placeholder="예: 6">

    <button onclick="makePlan()">계획표 만들기</button>

    <div id="result"></div>
</div>

<script src="script.js"></script>

</body>
</html>
