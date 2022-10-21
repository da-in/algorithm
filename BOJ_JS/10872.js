// let n = require('fs').readFileSync('/dev/stdin').toString();
// n = parseInt(n, 10);
let n = 10;
answer = 1;

while (n > 0) {
    answer *= n;
    n -= 1;
}

console.log(answer);
