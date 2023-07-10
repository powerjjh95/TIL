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
  let N = input[0];
  let A = input[1].split(" ");
  let M = input[2];
  let MNumbers = input[3].split(" ");

  let ASorted = A.sort();

  for (let i = 0; i < M; i++) {
    let start = 0;
    let end = N - 1;
    let isExist = false;

    while (start <= end) {
      let middle = parseInt((start + end) / 2);
      if (Number(MNumbers[i]) === Number(ASorted[middle])) {
        isExist = true;
        console.log(1);
        break;
      } else if (Number(MNumbers[i]) > Number(ASorted[middle])) {
        start = middle + 1;
      } else {
        end = middle - 1;
      }
    }
    if (!isExist) {
      console.log(0);
    }
  }
}
