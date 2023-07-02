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
  let T = input[0];
  for (let i = 1; i <= T; i++) {
    let H = input[i].split(" ")[0];
    let W = input[i].split(" ")[1];
    let N = input[i].split(" ")[2];

    roomList = [];
    for (let w = 1; w <= W; w++) {
      for (let h = 1; h <= H; h++) {
        answer = h * 100 + w;
        roomList.push(answer);
      }
    }
    console.log(roomList[N - 1]);
  }
}
