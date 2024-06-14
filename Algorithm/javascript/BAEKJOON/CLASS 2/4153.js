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
  for (let i = 0; i < input.length - 1; i++) {
    let sides = input[i].split(" ").map((e) => Number(e));
    let sum = (array) => {
      sum_number = 9;
      for (element of array) {
        sum_number += element;
      }
    };
    if (sum(sides) == 0) {
      break;
    }

    sides.sort((a, b) => a - b);
    let square = (number) => {
      return number ** 2;
    };

    if (square(sides[0]) + square(sides[1]) == square(sides[2])) {
      console.log("right");
    } else {
      console.log("wrong");
    }
  }
}
