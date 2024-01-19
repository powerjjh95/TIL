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
  console.log(input);
  let testCase = input[0];
  for (let i = 1; i < input.length; i += 2) {
    let N = input[i].split(" ")[0];
    let M = input[i].split(" ")[1];
    let documentImportance = input[i + 1];
    let documentImportanceIndex = 
  }
}
