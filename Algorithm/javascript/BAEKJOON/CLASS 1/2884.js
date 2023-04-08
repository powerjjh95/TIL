// H가 23시 이하, M이 45분 이상 => H : - 0 / M : - 45

// H가 0시, 45분 미만 => H : -1 + 24 / M : - 45 + 60

function solution(input) {
  var [H, M] = input.split(" ").map((element) => parseInt(element));

  // H가 23시 이하, M이 45분 이상 => H : - 0 / M : - 45
  if (H <= 23 && M >= 45) {
    var M = M - 45;
    console.log(H, M);
  } else if (
    // H가 1이상 23시 이하, M이 45분 미만 => H : - 1 / M : - 45 + 60
    H >= 1 &&
    H <= 23 &&
    M < 45
  ) {
    var H = H - 1;
    var M = M - 45 + 60;
    console.log(H, M);
  } else {
    //   // H가 0시, 45분 미만 => H : -1 + 24 / M : - 45 + 60
    var H = H - 1 + 24;
    var M = M - 45 + 60;
    console.log(H, M);
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  input = line;
  rl.close();
}).on("close", () => {
  solution(input);
  process.exit();
});
