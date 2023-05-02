// Binary Search 사용
function solution(input) {
  let K = input[0].split(" ")[0];
  let N = input[0].split(" ")[1];
  let kLength = [];
  for (let i = 1; i <= Number(K); i++) {
    kLength.push(Number(input[i]));
  }

  // 최소길이와 최대길이를 설정
  // 두 길이의 중간값을 사용하여 kLength을 나누며 line을 Count

  let minLength = 1;
  let maxLength = Math.max(...kLength);

  let midLength = 0;
  while (minLength <= maxLength) {
    midLength = Math.floor((minLength + maxLength) / 2);
    lineCount = 0;

    for (let length of kLength) {
      lineCount += Math.floor(length / midLength);
    }

    if (lineCount >= Number(N)) {
      // lineCount가 문제에서 제시한 N보다 클 경우
      minLength = midLength + 1; // minLength를 다시 설정하여 line 자르기
    } else {
      // lineCount가 문제에서 제시한 N보다 작을 경우
      maxLength = midLength - 1; // maxLength를 다시 설정하여 line 자르기
    }
  }
  console.log(maxLength);
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
