function solution(input) {
  const strings = input;
  console.log(strings);
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
