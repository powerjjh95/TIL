// TRY 1
/*
- Javascript에서 2차원 배열로 표현하는 것이 어려움
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
  for (let i = 1; i <= T; i++) {
    let [k, n] = [Number(input[2 * i - 1]), Number(input[2 * i])]; // k : 층, n : 호
    // 2차원 배열
    let apartment = new Array(k + 1); // apartment의 배열의 개수를 k+1 개 만큼 설정
    // c : 층, r : 호
    for (let c = 0; c <= k; c++) {
      // 배열의 개수만큼 순회하며 새로운 n개의 배열 생성
      apartment[c] = new Array(n);
    }
    for (let c = 1; c <= k; c++) {
      for (let r = 0; r < n; r++) {
        apartment[0][r] = r + 1; // 0층의 각 r호는 r만큼 배당
        apartment[c][r] = 0; // 1층 이상의 각 호는 0으로 설정
        for (let i = 0; i <= r; i++) {
          apartment[c][r] += apartment[c - 1][i]; // 각 층의 각 호수별 인원을 설정
        }
      }
    }
    let answer = apartment[k][n - 1];
    console.log(answer);
  }
}
