function solution(input) {
  const strings = input;
  console.log(strings);
  let countOfWords = 0;
  for (let i = 0; i < strings.length; i++) {
    countOfWords++;
  }
  console.log(countOfWords);
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
  list = input.split(" ").map((element) => element);
  solution(list);
  process.exit();
});
