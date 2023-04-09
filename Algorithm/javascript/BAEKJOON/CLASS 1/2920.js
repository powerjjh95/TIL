function solution(input) {
  const ascending = [1, 2, 3, 4, 5, 6, 7, 8];
  let scale = input.split(" ");
  if (scale === ascending) {
    console.log("!!!!!!!!!!!!!!`");
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  (input = line), rl.close();
}).on("close", () => {
  solution(input);
  process.exit();
});
