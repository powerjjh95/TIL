// 1부터 숫자를 차례대로 입력하면서 push와 pop을 반복하여 문제에서 제시한 case에 적합하면 정답
//

function solution(input) {
  let n = input[0];
  let flag = 0;
  let stack = []; // 수열들이 들어갈
  let calculation = [];
  let current = 1;

  for (let i = 1; i < input.length; i++) {
    let number = Number(input[i]);
    while (current <= number) {
      stack.push(current);
      calculation.push("+");
      current++;
    }

    if (stack.slice(-1)[0] === number) {
      stack.pop();
      calculation.push("-");
    } else {
      console.log("NO");
      flag = 1;
      break;
    }
  }

  if (flag === 0) {
    for (let each of calculation) {
      console.log(each);
    }
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  outpus: process.stdout,
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
