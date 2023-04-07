function solution(input) {
  number = parseInt(input);
  answer = "";
  for (let i = number; i > 0; i--) {
    answer += i + "\n";
  }
  console.log(answer);
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
