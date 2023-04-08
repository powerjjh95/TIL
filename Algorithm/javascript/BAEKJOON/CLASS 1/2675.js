function solution(input) {
  let T = input[0];

  for (let i = 1; i <= T; i++) {
    let answer = "";
    const [R, S] = input[i].split(" ");

    // console.log(S.length);
    for (let j = 0; j < S.length; j++) {
      for (let k = 0; k < R; k++) {
        answer += S[j];
      }
    }
    console.log(answer);
  }
  // console.log(answer);
}

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
