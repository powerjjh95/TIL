function solution(input) {
  let T = input[0];
  for (let i = 1; i <= T; i++) {
    let OX = input[i];
    // "O"가 나왔을 때 일시적으로 저장하는 score
    let score = 0;
    // 누적 점수 합계를 저장하는 accumulateScore
    let accumulateScore = 0;
    for (let j = 0; j < OX.length; j++) {
      if (OX[j] === "O") {
        score++;
        accumulateScore += score;
      } else if (OX[j] === "X") {
        score = 0;
      }
    }
    console.log(accumulateScore);
  }
}

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
