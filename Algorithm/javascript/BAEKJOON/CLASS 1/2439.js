function solution(input) {
  let answer = "";
  let blank = "";
  for (let i = 1; i <= input; i++) {
    answer += "*";
    for (let j = 0; j < input - i; j++) {
      blank += " ";
    }
    console.log(blank + answer);
    blank = "";
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
