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

function solution(input) {
  let N = Number(input[0]);
  let numbers = input[1].split(" ").map((i) => Number(i));
  // console.log(numbers);
  let count = 0;
  for (let number of numbers) {
    let compositeNumber = 0;
    if (number == 1) {
      compositeNumber--;
    } else if (number == 2) {
      compositeNumber = 0;
    } else if (number >= 3) {
      for (let divisor = 2; divisor < number ** (1 / 2) + 1; divisor++) {
        if (number % divisor == 0) {
          compositeNumber++;
        }
      }
    }
    // console.log(number, compositeNumber);
    if (compositeNumber == 0) {
      count++;
    }
  }
  console.log(count);
}
