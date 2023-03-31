function solution(input) {
  let list1 = input[0].split(" ").map((element) => parseInt(element));
  let list2 = input[1].split(" ").map((element) => parseInt(element));
  const N = list1[0];
  const X = list1[1];
  const A = list2;
  let answerList = [];
  for (let i = 0; i < N; i++) {
    if (A[i] < X) {
      answerList.push(A[i]);
    }
  }
  console.log(answerList.join(" "));
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
