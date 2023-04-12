function solution(input) {
  // 입력 받은 input을 할당
  let numbers = input;
  // remainder(for문에서 선언)를 담은 answerArray를 생성
  let answerArray = [];
  // remainder는 numbers의 숫자들을 42로 나눈 값
  // remainder를 구한 후 answerArray에 push
  for (let i = 0; i < numbers.length; i++) {
    let remainder = numbers[i] % 42;
    answerArray.push(remainder);
  }
  let answerSet = new Set(answerArray);
  console.log([...answerSet].length);
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
