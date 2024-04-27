// TRY 1
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

function solution(input) {
  let N = input;
  let answer = 0;
  for (
    let constructor = Number(N) - 9 * N.length;
    constructor <= Number(N);
    constructor++
  ) {
    let digitSum = constructor;
    let number = constructor;
    while (number > 0) {
      digitSum += number % 10;
      number = parseInt(number / 10);
    }
    if (digitSum == N) {
      answer = constructor;
      break;
    }
  }
  console.log(answer);
}
