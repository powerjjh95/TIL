function solution(input) {
  const strings = input;
  let wordCounts = 0;
  for (let i = 0; i < strings.length; i++) {
    if (strings[i] !== "") {
      wordCounts++;
    }
  }
  console.log(wordCounts);
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
