// TRY 2
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

function solution(input) {
  let M = input.split(" ")[0];
  let N = input.split(" ")[1];

  const isPrimeNumber = (number) => {
    if (number === 1) {
      return false;
    }
    for (let divisor = 2; divisor < parseInt(number ** 0.5) + 1; divisor++) {
      if (number % divisor === 0) {
        return false;
      }
    }

    return true;
  };

  for (let number = Number(M); number <= Number(N); number++) {
    if (isPrimeNumber(number)) {
      console.log(number);
    }
  }
}

// // TRY 1
// const readline = require("readline");
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

// rl.on("line", (line) => {
//   input = line;
//   rl.close();
// }).on("close", () => {
//   solution(input);
//   process.exit();
// });

// function solution(input) {
//   let M = input.split(" ")[0];
//   let N = input.split(" ")[1];

//   for (let number = Number(M); number <= Number(N); number++) {
//     if (number === 1) {
//       continue;
//     } else {
//       for (let divisor = 2; divisor < parseInt(number ** 0.5) + 1; divisor++) {
//         if (number % divisor === 0) {
//           break;
//         } else {
//           console.log(number);
//         }
//       }
//     }
//   }
// }
