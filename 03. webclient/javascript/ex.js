// //var score = 100;
// function func() {
// score = 77;
// console.log("함수안 score = " + score);
// }
// func();
// console.log("함수밖 score = " + score);

// var veryBig = 1234/0;
// console.log("veryBig = " + veryBig);
// var noNumber = Math.sqrt(-2);
// console.log("noNumber = " + noNumber);

// var name = "김상형 : ";
// var score  = 98;
// console.log(name + score);

// var value1 = "8";
// var value2 = "6";
// var add = value1 + value2;

// console.log("add : "+ add);

// var sub = value1 -value2;
// console.log("substract : " +sub);


// var order = "";
// order += "date : 2014-06-29";
// order += "\n"
// order += "item : notebook";
// order += "\n"
// order += "price : 134";
// console.log(order);

// var a = 3;
// var b = (a % 2 == 0) ? "짝":"홀"
// console.log("a는 " + b +"수이다.");
// a = 2;
// b = "2";
// console.log("== 비교 : " + (a == b ? "같음":"다름"));

// var day = "월";

// switch (day) {
// case "월":
//     console.log("일주일의 시작입니다.");
//     break;
// case "화":
// case "수":
// case "목":
//     console.log("열심히 일해야할 때입니다.");
//     break;
// case "금":
//     console.log("불타는 금요일 보내세요.");
// break;
// case "토":
// case "일":
// console.log("편안핚 주말 보내세요.");
// break;
// }


var arScore = [88,78,96,54,23];
for(var st=0;st<5;st++){
    console.log(st + "번째 학생의 성적 : "+arScore[st]);
}

var sum = 0;

for(var i=1; i<=100; i++){
    sum = sum+i;
}
console.log("1~100까지의 합 = "+ sum);

var arScore = [88, 78, 96, 54, 23];
var sum = 0;
for (var st = 0; st < arScore.length; st++) {
sum += arScore[st];
}
console.log("총점 : " + sum + ", 평균 : " + sum/arScore.length);
console.log(`총점 : ${sum}, 평균 : ${sum/arScore.length}`);

var arScore = [88,78,96,54,23];
var sum = 0;


var ar =[[0,1,2,3],[4,5,6],[7,8]];
for(var i = 0; i<ar.length;i++){
    console.log("ar[|")
}

function func(){
    if(true)
    {
        throw "예외가 발생했습니다";
    }
}
try{
    func();
}catch(exeption){
    console.log(exeption);
}
console.log("실행을 완료하였습니다.");


fuction sum(n){
    if(n == undefined){
        n = 100;
        //n = n|| 100;
    }

    var s = 0;
    for( var i = 0; i<=n; i++){
        s += i;
    }
    return s;
}

console.log("1~10 = "+ sum(10));
console.log("1~100 = "+sum());
