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
  for (let i = 1; i < input.length; i += 2) {
    let N = input[i].split(" ")[0]; // 문서의 개수
    let M = input[i].split(" ")[1]; // 몇 번째로 인쇄되었는지 궁금한 문서의 순서
    let documentImportance = input[i + 1].split("").map((i) => Number(i));
    // 문서 중요도 인덱스 생성
    let documentImportanceIndex = [];
    for (let j = 0; j <= N; j++) {
      documentImportanceIndex.push(j);
    }
    let tempDocumentImpotance = [];
    let tempDocumentImpotanceIndex = [];
    let printOrder = 0;
    while (true) {
      if (documentImportance[0] != Math.max(documentImportance)) {
        tempDocumentImpotance.push(documentImportance.shift());
        documentImportance.push(tempDocumentImpotance.shift());
        tempDocumentImpotanceIndex.push(documentImportanceIndex.shift());
        documentImportanceIndex.push(tempDocumentImpotanceIndex.shift());
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
