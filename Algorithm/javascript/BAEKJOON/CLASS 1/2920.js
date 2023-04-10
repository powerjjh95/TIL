function solution(input) {
  let scale = input.split(" ");
  // console.log(scale);
  let ascending = [];
  for (let i = 1; i <= scale.length; i++) {
    ascending.push(i.toString());
  }
  // console.log(ascending);
  let descending = [];
  for (let i = scale.length; i >= 1; i--) {
    descending.push(i.toString());
  }
  // console.log(descending);

  if (JSON.stringify(scale) === JSON.stringify(ascending)) {
    console.log("ascending");
  } else if (JSON.stringify(descending) === JSON.stringify(scale)) {
    console.log("descending");
  } else {
    console.log("mixed");
  }

  //   let correctCount = 0;
  //   var answer = "";
  //   for (let i = 0; i < scale.length; i++) {
  //     if (scale[i] == ascending[i].toString()) {
  //       correctCount++;
  //       // console.log(correctCount);
  //       if (correctCount === 8) {
  //         var answer = "ascending";
  //       }
  //     } else if (scale[i] == descending[i].toString()) {
  //       correctCount++;
  //       // console.log(correctCount);
  //       if (correctCount === 8) {
  //         var answer = "descending";
  //       }
  //     } else {
  //       if (correctCount != 8) {
  //         var answer = "mixed";
  //       }
  //     }
  //   }
  //   console.log(answer);
}

const readline = require("readline");
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
