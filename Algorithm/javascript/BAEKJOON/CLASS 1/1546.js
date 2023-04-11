function solution(input) {
  let N = input[0];
  let scores = input[1].split(" ").map((element) => parseInt(element));
  let M = Math.max(...scores);
  let newScores = [];
  let scoreSum = 0;
  for (let i = 0; i < N; i++) {
    newScores.push((scores[i] / M) * 100);
    scoreSum += newScores[i];
  }
  console.log(scoreSum / N);
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
