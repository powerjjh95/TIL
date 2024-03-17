// TRY 2
const input = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);
const N = input.shift();
input.sort((a, b) => a - b);

console.log(Math.round(input.reduce((r, v) => r + v, 0) / N).toString());
console.log(input[Math.floor(N / 2)].toString());

const frequency = Object.entries(
  input.reduce((r, v) => {
    if (r[v]) r[v]++;
    else r[v] = 1;
    return r;
  }, {})
).sort((a, b) => {
  if (a[1] == b[1]) {
    return a[0] - b[0];
  } else {
    return b[1] - a[1];
  }
});
if (frequency.length > 1 && frequency[0][1] == frequency[1][1]) {
  console.log(frequency[1][0]);
} else {
  console.log(frequency[0][0]);
}

console.log((input[input.length - 1] - input[0]).toString());

// // TRY 1
// const readline = require("readline");
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

// let input = [];
// rl.on("line", (line) => {
//   if (!line) {
//     rl.close();
//   } else {
//     input.push(line);
//   }
// }).on("close", () => {
//   solution(input);
//   process.exit();
// });

// function solution(input) {
//   let N = Number(input[0]);
//   let integers = [];
//   for (let i = 1; i <= N; i++) {
//     integers.push(Number(input[i]));
//   }
//   // 오름차순을 위한 함수
//   function ascending(a, b) {
//     return a - b;
//   }

//   // 산술평균
//   let sumIntegers = 0;
//   for (let integer of integers) {
//     sumIntegers += integer;
//   }
//   let arithmeticMean = Math.round(sumIntegers / N);
//   console.log(arithmeticMean.toString());

//   // 중앙값
//   let sortedIntegers = integers.sort(ascending);
//   let median = 0;
//   if (integers.length % 2 == 1) {
//     median = sortedIntegers[Math.round(N / 2)];
//   } else {
//     median =
//       (sortedIntegers[Math.round(N / 2) - 1] +
//         sortedIntegers[Math.round(N / 2)]) /
//       2;
//   }
//   console.log(median.toString());

//   // 최빈값
//   let mode = 0;
//   let integersObject = {};
//   for (let integer of integers) {
//     if (Object.keys(integersObject).includes(String(integer))) {
//       integersObject[integer] += 1;
//     } else {
//       integersObject[integer] = 1;
//     }
//   }

//   let integersObjectMaxValue = Math.max(...Object.values(integersObject));
//   let integersObjectMaxValueArray = [];
//   for (let [key, value] of Object.entries(integersObject)) {
//     if (value == integersObjectMaxValue) {
//       integersObjectMaxValueArray.push(Number(key));
//     }
//   }
//   if (integersObjectMaxValueArray.length == 1) {
//     mode = integersObjectMaxValueArray[0];
//   } else {
//     mode = integersObjectMaxValueArray.sort(ascending)[1];
//   }
//   console.log(mode.toString());

//   // 범위
//   let range = Math.max(...integers) - Math.min(...integers);
//   console.log(range.toString());
// }

// // `for ... in ...`은 인덱스
// // `for ... of ...`은 원소
// // '몫' 표현시 `parseInt()` 또는 `Math.floor()` 사용
// // Object의 Key 값을 Array 형태로 표현하기 위해 `Object.keys()` 사용
// // Array에서 각 원소가 있는 지 판별하는 함수는
