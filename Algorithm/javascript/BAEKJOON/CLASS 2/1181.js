function solution(input) {
  let N = input[0];
  // Empty Array(wordArray)를 생성
  var wordArray = [];
  // wordArray에 단어를 추가
  for (let index = 1; index <= N; index++) {
    wordArray.push(input[index]);
  }

  // Set 사용하여 중복제거
  const wordSet = new Set(wordArray);

  // 중복제거된 WordSet을 다시 Array로 변경
  // 1. Array.from() : array-like object나 iterable object를 shallow copy하여 새로운 Array 생성
  // 2. [... Set]: Spread Operator / ES6 문법으로 Array나 String과 같이 반복가능한 객체를 하나씩 펼쳐 return
  // 3. forEach 이용
  var wordArray = [...wordSet];

  // 사전순으로 정렬
  wordArray.sort();

  // 길이순으로 정렬
  // Array.sort((a, b) => a.length - b.length)
  // a.length - b.length > 0 이면 a의 길이가 b의 길이보다 크다.
  // a.length - b.length > 0 이면 a의 길이가 b의 길이보다 작다.
  wordArray.sort((a, b) => a.length - b.length);

  // 조건에 맞게 정렬된 Array를 하나씩 출력
  // for (... of ...) {} 를 사용하여 출력
  for (let word of wordArray) {
    console.log(word);
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
