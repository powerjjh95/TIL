function solution(input) {
  const [M, N] = input[0].split(" ").map((element) => parseInt(element));
  let board = [];
  for (let i = 1; i <= M; i++) {
    board.push(input[i]);
  }
  // 8 X 8 크기의 체스판 생성

  for (x = 0; x < N - 7; x++) {
    for (y = 0; y < M - 7; y++) {
      // blackStartCount = 0; // black 시작
      // whiteStartCount = 0; // white 시작
      for (i = x; i < x + 8; i++) {
        for (j = y; j < y + 8; j++) {
          if ((i + j) % 2 === 0) {
            if (board[i][j])
          }
        }
      }
    }
  }
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
