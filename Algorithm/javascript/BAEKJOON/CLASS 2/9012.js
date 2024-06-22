// TRY 1
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
  for (let i = 1; i <= N; i++) {
    parenthesisString = [];
    for (parenthesis of input[i]) {
      if (parenthesis == "(") {
        parenthesisString.push(parenthesis);
      } else if (parenthesis == ")") {
        if (
          parenthesisString.length != 0 &&
          parenthesisString[parenthesisString.length - 1] == "("
        ) {
          parenthesisString.pop();
        } else {
          parenthesisString.push(parenthesis);
        }
      }
    }
    if (parenthesisString.length == 0) {
      console.log("YES");
    } else {
      console.log("NO");
    }
  }
}
