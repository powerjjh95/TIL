function solution(input) {
  const numbers = input;
  let eachNumberSquareSum = 0;
  for (let i = 0; i < numbers.length; i++) {
    eachNumberSquareSum += numbers[i] ** 2;
    answer = eachNumberSquareSum % 10;
  }
  console.log(answer);
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
  numbers = input.split(" ").map((element) => parseInt(element));
  solution(numbers);
  process.exit();
});
