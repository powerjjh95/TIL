function solution(input) {
  if (input % 4 === 0 && input % 100 != 0) {
    console.log(1);
  } else if (input % 4 === 0 && input % 400 === 0) {
    console.log(1);
  } else {
    console.log(0);
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
