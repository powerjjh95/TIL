// TRY 1

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
  let N = Number(input[0]);
  let group = [];
  for (let i = 1; i <= N; i++) {
    let [weight, height] = input[i].split(" ").map((e) => Number(e));
    group.push([weight, height]);
  }
  let rankArray = [];
  for (compare1 of group) {
    let rank = 1;
    for (compare2 of group) {
      if (compare1[0] < compare2[0] && compare1[1] < compare2[1]) {
        rank++;
      }
    }
    rankArray.push(rank);
  }
  console.log(rankArray.join(" "));
}
