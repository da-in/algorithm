// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n')
let input = ['3', '3 7', '15 7', '5 2'];
input.splice(0, 1);
let arr = Array.from({ length: 100 }, () => new Array(100).fill(0));
let x, y;
let answer = 0;

let temp = [];

for (row of input) {
    [x, y] = row.split(' ').map(Number);
    for (let i = x; i < x + 10; i++) {
        for (let j = y; j < y + 10; j++) {
            if (!arr[i][j]) {
                answer += 1;
            }
            arr[i][j] = 1;
        }
    }
}

console.log(answer);
