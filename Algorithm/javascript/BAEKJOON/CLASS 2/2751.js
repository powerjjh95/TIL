// TRY 2
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdput,
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
  let [N, ...numbers] = input.map((e) => Number(e));
  let result = numbers.sort((a, b) => a - b);
  console.log(result.join("\n"));
}

// // TRY 1
// const readline = require("readline");
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdput,
// });

// let input = [];
// rl.on("line", (line) => {
//   if (!line) {
//     rl.close();
//   } else {
//     input.push(line);
//   }
// }).on("close", () => {
//   solution(input);
//   process.exit();
// });

// function solution(input) {
//   let N = Number(input[0]);
//   let numbers = [];
//   for (let i = 1; i <= N; i++) {
//     numbers.push(i);
//   }

//   let sortedNumbers = numbers.sort();

//   for (number of sortedNumbers) {
//     console.log(number);
//   }
// }
