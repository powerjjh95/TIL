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
  let N = Number(input);
  let count = 0;
  while (N >= 0) {
    if (N % 5 == 0) {
      count += parseInt(N / 5);
      console.log(count);
      break;
    }
    N -= 3;
    count++;
  }
  if (N < 0) {
    console.log(-1);
  }
}
