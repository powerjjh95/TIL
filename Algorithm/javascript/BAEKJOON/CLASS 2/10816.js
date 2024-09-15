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
  let NCards = input[1].split(" ").map((e) => Number(e));
  let M = input[2];
  let MCards = input[3].split(" ").map((e) => Number(e));

  let cardsCount = Object();
  for (let NCard of NCards) {
    if (Object.keys(cardsCount).includes(String(NCard))) {
      cardsCount[NCard] += 1;
    } else {
      cardsCount[NCard] = 1;
    }
  }

  let cardsCountArray = [];
  for (let MCard of MCards) {
    if (Object.keys(cardsCount).includes(String(MCard))) {
      cardsCountArray.push(cardsCount[String(MCard)]);
    } else {
      cardsCountArray.push(0);
    }
  }
  console.log(cardsCountArray.join(" "));
}
