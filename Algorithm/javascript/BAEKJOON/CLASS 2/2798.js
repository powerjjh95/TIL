// TRY 1
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
  let [N, M] = input[0].split(" ").map((e) => Number(e));
  let cards = input[1].split(" ").map((e) => Number(e));
  let sumCards = 0;
  let answer = 0;
  for (let i = 0; i < N; i++) {
    for (let j = i + 1; j < N; j++) {
      for (let l = j + 1; l < N; l++) {
        sumCards += cards[i] + cards[j] + cards[l];
        if (sumCards <= M && sumCards > answer) {
          answer = sumCards;
          // console.log(i, j, l, answer);
        }
        sumCards = 0;
      }
    }
  }
  console.log(answer);
}
