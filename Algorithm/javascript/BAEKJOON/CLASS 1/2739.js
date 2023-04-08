function solution(input) {
  for (let i = 1; i <= 9; i++) {
    // console.log(number);
    console.log(input + " * " + i + " = " + input * i);
  }
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
