function solution(input) {
  let N = input[0];
  let numbers = input[1].split(" ").map((element) => parseInt(element));
  let answer = [];
  answer.push(Math.min(...numbers));
  answer.push(Math.max(...numbers));
  console.log(answer.join(" "));
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
