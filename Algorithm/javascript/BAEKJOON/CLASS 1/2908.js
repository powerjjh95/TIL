function solution(input) {
  let [number1, number2] = input.split(" ").map((element) => element);
  let [reverseNumber1, reverseNumber2] = ["", ""];
  // console.log(reverseNumber1);
  for (let i = number1.length - 1; i >= 0; i--) {
    reverseNumber1 += number1[i];
    reverseNumber2 += number2[i];
  }
  if (parseInt(reverseNumber1) > parseInt(reverseNumber2)) {
    console.log(reverseNumber1);
  } else {
    console.log(reverseNumber2);
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
