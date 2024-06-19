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
    let string = input[i];
    let bracketArray = [];
    for (character of string) {
      if (character == "(" || character == "[") {
        bracketArray.push(character);
      } else if (character == ")") {
        if (
          bracketArray.length != 0 &&
          bracketArray[bracketArray.length - 1] == "("
        ) {
          bracketArray.pop();
        } else {
          bracketArray.push(character);
        }
      } else if (character == "]") {
        if (
          bracketArray.length != 0 &&
          bracketArray[bracketArray.length - 1] == "["
        ) {
          bracketArray.pop();
        } else {
          bracketArray.push(character);
        }
      }
    }
    if (bracketArray.length == 0) {
      console.log("yes");
    } else {
      console.log("no");
    }
  }
}
