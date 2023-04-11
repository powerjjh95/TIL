function solution(input) {
  // 문자열 입력받기
  let S = input;

  // alphabetList 구현하기
  let alphabetPosition = [];
  for (let i = 0; i < 26; i++) {
    alphabetPosition.push(-1);
  }

  // 아스키 코드로 각 위치 만들기
  let SList = [];
  for (let i = 0; i < S.length; i++) {
    let eachS = S.charCodeAt(i) - 97;
    SList.push(eachS);
    alphabetPosition[eachS] = SList.indexOf(eachS);
  }
  console.log(alphabetPosition.join(" "));
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  input = line;
  rl.close();
}).on("close", () => {
  solution(input);
  process.exit();
});
