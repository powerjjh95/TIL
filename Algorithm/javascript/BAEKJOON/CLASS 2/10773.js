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

function solution(input) {
  let [K, ...integers] = input;
  let integerArray = [];
  for (integer of integers) {
    if (Number(integer) == 0) {
      integerArray.pop();
    } else {
      integerArray.push(Number(integer));
    }
  }
  let answer = 0;
  for (number of integerArray) {
    answer += number;
  }
  console.log(answer);
}
