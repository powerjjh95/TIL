function solution(input) {
  let N = parseInt(input);
  let count = 0;
  let number = 1;

  while (true) {
    if (number.toString().includes("666")) {
      count += 1;
    }
    if (count === N) {
      console.log(number);
      break;
    }
    number += 1;
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
