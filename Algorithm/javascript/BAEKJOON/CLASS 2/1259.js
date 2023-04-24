function solution(input) {
  for (let i = 0; i < input.length - 1; i++) {
    const number = input[i];
    const reverseNumberArray = input[i].split("").reverse();
    const reverseNumber = reverseNumberArray.join("");
    if (number === reverseNumber) {
      console.log("yes");
    } else {
      console.log("no");
    }
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
