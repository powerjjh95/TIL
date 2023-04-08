function solution(input) {
  let numbers = [];
  for (let i = 0; i < input.length; i++) {
    numbers.push(parseInt(input[i]));
  }

  let maxNumber = 0; // 주어지는 수는 자연수 이기 때문에 0을 최솟값으로 설정
  for (let i = 0; i < numbers.length; i++) {
    if (maxNumber < numbers[i]) {
      maxNumber = numbers[i];
    }
  }
  console.log(maxNumber);
  console.log(numbers.indexOf(maxNumber) + 1);
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
