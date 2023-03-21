function solution(input) {
  for (let i = 1; i <= input; i++) {
    console.log("*" * i);
  }
}

// readline module 불러오기
const readline = require("readline");

// Interface 생성하기
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (number) => {
  input = number;
  rl.close();
}).on("close", () => {
  solution(input);
  process.exit();
});
