function solution(input) {
  let T = input[0];
  for (let i = 1; i <= T; i++) {
    let numbers = input[i].split(" ").map((element) => parseInt(element));
    let A = numbers[0];
    let B = numbers[1];
    let answer = A + B;
    console.log(answer);
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  if (!line) {
    rl.close();
  } else {
    input.push(line);
  }
}).on("close", () => {
  solution(input);
  process.exit;
});
