// TRY 1
/*
- Javascript에서 2차원 리스트로 표현하는 것이 어려움
*/
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
  let T = Number(input[0]);
  console.log();
  for (let i = 1; i <= T; i++) {
    let [k, n] = [Number(input[2 * i - 1]), Number(input[2 * i])]; // k : 층, n : 호
    let apartment = new Array(k + 1);

    // c : 층, r : 호
    // for (let c = 0; c <= k; c++) {
    for (let r = 0; r < n; r++) {
      apartment[r] = new Array(k + 1);
    }
    // }
    console.log(apartment[0][0]);
  }
}
