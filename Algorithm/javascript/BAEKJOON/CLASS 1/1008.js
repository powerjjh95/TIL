function solution(input) {
  const [a, b] = input;
  const answer = a / b;
  console.log(answer);
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  input = line;
  rl.close();
}).on("close", function () {
  list = input.split(" ").map((el) => parseInt(el));
  solution(list);
  process.exit();
});
