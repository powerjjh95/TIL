function solution(input) {
  let [A, B, C] = input;
  let ABC = A * B * C;
  let numberCount = [];
  for (let i = 0; i < 10; i++) {
    numberCount.push(0);
  }
  for (let i = 0; i < ABC.toString().length; i++) {
    eachNumber = ABC.toString()[i];
    numberCount[eachNumber] += 1;
  }
  for (let i = 0; i < 10; i++) {
    console.log(numberCount[i]);
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
