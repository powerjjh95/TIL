function solution(input) {
  const [a, b] = input;
  console.log(a + b);
  console.log(a - b);
  console.log(a * b);
  console.log(parseInt(a / b));
  console.log(a % b);
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  input = line.split(" ").map((element) => parseInt(element));
  rl.close();
}).on("close", () => {
  solution(input);
  process.exit();
});
