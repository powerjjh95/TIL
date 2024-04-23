// TRY 2
/*
- LinkedList 사용
- 참고
  - https://sj0826.github.io/structure/structure-%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8/
- 추후 공부 방향
  - class 사용하는 방법 배우기
*/

// 데이터 입출력
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

// LinkedList
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }
  add(value) {
    const newNode = new Node(value);

    if (!this.head) {
      this.head = newNode;
    } else {
      this.tail.next = newNode;
      newNode.prev = this.tail;
    }

    this.tail = newNode;
    this.size++;

    return newNode;
  }
  getHead() {
    return this.head.value;
  }
  removeHead() {
    this.head = this.head.next;
    this.head.prev = null;
    this.size--;
  }
  getSize() {
    return this.size;
  }
}

function solution(input) {
  let N = Number(input);
  let cards = new LinkedList();
  for (let i = 1; i <= N; i++) {
    cards.add(i);
  }

  while (cards.getSize() != 1) {
    cards.removeHead();
    cards.add(cards.getHead());
    cards.removeHead();
  }

  // console.log(cards);
  console.log(cards.getHead());
}

// // TRY 1
// const readline = require("readline");
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

// input = [];
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

// function solution() {}
