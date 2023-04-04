function solution(input) {
  for (let i = 0; i < input.length - 1; i++) {
    let AB = input[i].split(" ").map((element) => parseInt(element));
    let A = AB[0];
    let B = AB[1];
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
  process.exit();
});
