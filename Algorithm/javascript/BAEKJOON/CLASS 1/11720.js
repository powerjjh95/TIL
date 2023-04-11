function solution(input) {
  // console.log(input);
  let N = input[0];
  let numbers = input[1].split("");
  let answer = 0;
  for (let i = 0; i < numbers.length; i++) {
    answer += parseInt(numbers[i]);
  }
  // console.log(i);
  console.log(answer);
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
