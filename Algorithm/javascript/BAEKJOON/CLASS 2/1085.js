function solution(input) {
  let [x, y, w, h] = input.split(" ").map((element) => parseInt(element));

  let maxWidth = w;
  let maxHeight = h;

  console.log(Math.min(x, y, maxWidth - x, maxHeight - y));
}

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
