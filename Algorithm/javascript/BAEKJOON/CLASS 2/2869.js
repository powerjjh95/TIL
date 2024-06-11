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
  let [A, B, V] = input.split(" ").map((e) => Number(e));
  let dayLength = A - B;
  let height = V - A;
  let day = 1 + Math.ceil(height / dayLength);
  console.log(day);
}
