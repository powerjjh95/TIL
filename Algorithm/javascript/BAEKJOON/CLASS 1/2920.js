function solution(input) {}

const readline = reuqire("readline");
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
