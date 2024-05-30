// TRY1
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
  let roomAddress = 1;
  let number = 1;
  while (N > roomAddress) {
    roomAddress += 6 * number;
    number++;
  }
  console.log(number);
}
