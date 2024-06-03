const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdput,
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
  let numberArray = input[0].split(" ").map((i) => Number(i));
  let minNumber = Math.min(...numberArray);

  let sum = (numberArray) => {
    let sumNumbers = 0;
    for (let number of numberArray) {
      sumNumbers += number;
    }
    return sumNumbers;
  };

  let divisor = (number) => {
    let divisorArray = [1];
    for (let i = 2; i < parseInt(number / 2) + 1; i++) {
      if (number % i == 0) {
        divisorArray.push(i);
      }
    }
    divisorArray.push(number);
    return divisorArray;
  };

  let gcd = (numberArray) => {
    let commonDivisorArray = [];
    let divisorArray = divisor(minNumber);
    for (let i of divisorArray) {
      let count = 0;
      for (let number of numberArray) {
        if (number % i == 0) {
          count++;
        }
        if (count == numberArray.length) {
          commonDivisorArray.push(i);
        }
      }
    }
    let theGreatestCommonDivisor = Math.max(...commonDivisorArray);
    return theGreatestCommonDivisor;
  };

  let lcm = (numberArray) => {
    let theGreatestCommonDivisor = gcd(numberArray);
    let theLeastCommonMultiple = gcd(numberArray);
    for (let i = 0; i < numberArray.length; i++) {
      numberArray[i] = parseInt(numberArray[i] / theGreatestCommonDivisor);
    }
    while (sum(numberArray) > numberArray.length) {
      for (let j = Math.max(...numberArray); j >= 1; j--) {
        for (let k = 0; k < numberArray.length; k++) {
          if (numberArray[k] % j == 0) {
            numberArray[k] = parseInt(numberArray[k] / j);
            theLeastCommonMultiple = theLeastCommonMultiple * j;
          }
        }
      }
    }
    console.log(theLeastCommonMultiple);
  };
  console.log(gcd(numberArray));
  lcm(numberArray);
}
