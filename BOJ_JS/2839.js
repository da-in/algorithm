// let n = require('fs').readFileSync('/dev/stdin').toString();
// n = parseInt(n, 10);
let n = 5;
let answer = -1;

for (let i = 0; i < n / 5 + 1; i++) {
    if (n - i * 5 >= 0 && (n - i * 5) % 3 == 0) {
        answer = i + (n - i * 5) / 3;
    }
}

console.log(answer);
