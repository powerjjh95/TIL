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
  let N = Number(input[0]);
  let integers = [];
  for (let i = 1; i <= N; i++) {
    integers.push(Number(input[i]));
  }

  // 산술평균
  let sumIntegers = 0;
  for (let integer of integers) {
    sumIntegers += integer;
  }
  let arithmeticMean = Math.round(sumIntegers / integers.length);
  console.log(arithmeticMean);

  // 중앙값
  let sortedIntegers = integers.sort();
  let median = 0;
  if (integers.length % 2 == 0) {
    median =
      (sortedIntegers[parseInt(N / 2) - 1] + sortedIntegers[parseInt(N / 2)]) /
      2;
  } else {
    median = sortedIntegers[parseInt(N / 2)];
  }
  console.log(median);

  // 최빈값
  let mode = 0;
  let integersObject = {};
  for (let integer of integers) {
    if (Object.keys(integersObject).includes(String(integer))) {
      integersObject[integer] += 1;
    } else {
      integersObject[integer] = 1;
    }
  }

  let integersObjectMaxValue = Math.max(...Object.values(integersObject));
  let integersObjectMaxValueArray = [];
  for (let [key, value] of Object.entries(integersObject)) {
    if (value == integersObjectMaxValue) {
      integersObjectMaxValueArray.push(Number(key));
    }
  }
  // console.log(integersObjectMaxValueArray);
  if (integersObjectMaxValueArray.length == 1) {
    mode = integersObjectMaxValueArray[0];
  } else {
    mode = integersObjectMaxValueArray[0];
  }
  console.log(mode);

  // 범위
  let range = Math.max(...integers) - Math.min(...integers);
  console.log(range);
}

// `for ... in ...`은 인덱스
// `for ... of ...`은 원소
// '몫' 표현시 `parseInt()` 또는 `Math.floor()` 사용
// Object의 Key 값을 Array 형태로 표현하기 위해 `Object.keys()` 사용
// Array에서 각 원소가 있는 지 판별하는 함수는
