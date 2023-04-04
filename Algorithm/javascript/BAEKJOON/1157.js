function solution(input) {
  const alphabet = [];
  for (let i = 0; i < input.length; i++) {
    alphabet.push({ value: input[i] });
    console.log(alphabet);
  }
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
