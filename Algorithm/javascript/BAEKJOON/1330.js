function solution(input) {
  const [a, b] = input;
  if (a > b) {
    console.log(">");
  } else if (a == b) {
    console.log("==");
  } else {
    console.log("<");
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  input = line;
  rl.close();
}).on("close", function () {
  list = input.split(" ").map((element) => parseInt(element));
  solution(list);
  process.exit();
});
