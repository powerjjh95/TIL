const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  input = line;
  rl.close();
}).on("close", () => {
  solution(input);
  process.exit();
});

// TRY 2
function solution(input) {
  let answer = 0;
  if (input === 0) answer;
  for (let i = 1; i <= input; i++) {
    if (i % 5 === 0) answer++;
    if (i % 25 === 0) answer++;
    if (i % 125 === 0) answer++;
  }
  return answer;
}

// TRY 1
// function solution(input) {
//   let N = Number(input);

//   let NFactorial = N;
//   for (let i = N - 1; i >= 1; i--) {
//     NFactorial *= i;
//   }

//   let NFactorialString = NFactorial.toString();
//   console.log(NFactorialString);
//   let count = 0;
//   for (let i = NFactorialString.length - 1; i >= 0; i--) {
//     console.log(NFactorialString[i]);
//     if (NFactorialString[i] == "0") {
//       count++;
//     } else {
//       break;
//     }
//   }
//   console.log(count);
// }
