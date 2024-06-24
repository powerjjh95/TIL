// TRY 1
/*
- 다시 풀어보기
- 2차원 Array의 sort 함수 활용 방안
*/

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  if (!line) {
    rl.close();
  } else {
    input.push(line);
  }
}).on("close", () => {
  solution(input);
  process.exit();
});

function solution(input) {
  let N = Number(input[0]);
  let onlineJudge = [];
  for (let i = 1; i <= N; i++) {
    let member = input[i].split(" ").map((e) => e);
    onlineJudge.push(member);
  }
  onlineJudge.sort((a, b) => a[0] - b[0]);
  for (memberInformation of onlineJudge) {
    {
      console.log(Number(memberInformation[0]), memberInformation[1]);
    }
  }
}
