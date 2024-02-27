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
  // console.log(input);
  let testCase = input[0];
  for (let i = 0; i < testCase; i++) {
    let N = Number(input[2 * i + 1].split(" ")[0]); // 문서의 개수
    let M = Number(input[2 * i + 1].split(" ")[1]); // 몇 번째로 인쇄되었는지 궁금한 문서의 순서
    let documentImportance = input[2 * i + 2].split(" ").map((i) => Number(i));
    // console.log(documentImportance);

    // 문서 중요도 인덱스 생성
    let documentImportanceIndex = [];
    for (let j = 0; j < N; j++) {
      documentImportanceIndex.push(j);
    }
    // console.log(documentImportanceIndex);
    let printOrder = 0;
    let tempDocumentImpotance = [];
    let tempDocumentImpotanceIndex = [];

    while (true) {
      if (documentImportance[0] != Math.max(...documentImportance)) {
        // let documentImportanceShift = documentImportance.shift();
        tempDocumentImpotance.push(documentImportance.shift());
        // console.log(tempDocumentImpotance);
        // let tempDocumentImpotanceShift = tempDocumentImpotance.shift();
        documentImportance.push(tempDocumentImpotance.shift());
        // console.log(documentImportance);
        // let documentImportanceIndexShift = documentImportanceIndex.shift();
        tempDocumentImpotanceIndex.push(documentImportanceIndex.shift());
        // console.log(tempDocumentImpotanceIndex);
        // let tempDocumentImpotanceIndexShift = tempDocumentImpotanceIndex.shift();
        documentImportanceIndex.push(tempDocumentImpotanceIndex.shift());
        // console.log(documentImportanceIndex);
      } else {
        printOrder++;
        if (documentImportanceIndex[0] == M) {
          break;
        } else {
          documentImportance.shift();
          documentImportanceIndex.shift();
        }
      }
    }
    console.log(printOrder);
  }
}

// `Math.max()`와 `Math.min()`은 주어진 값 중에서 최댓값과 최솟값을 구하기 때문에 Array의 최대, 최소 값을 구하기 위해서는 `...`문법을 사용해야 한다.
// `...` 관련 문법
// // var array = [1, 2, 3]
// // copy1
// // // var copy1 = array // 얕은 복사
// // // var [...copy2] = array // 깊은 복사
// // // var copy3 = [...arr]

// // // arr[0] = 'String';
// // // console.log(arr); // [ 'String', 2, 3 ]
// // // console.log(copy1); // [ 'String', 2, 3 ]
// // // console.log(copy2); // [ 1, 2, 3 ]
// // // console.log(copy3); // [ 1, 2, 3 ]
