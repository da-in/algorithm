let a, b, v;
// [a, b, v] = require('fs').readFileSync('/dev/stdin').toString().split(' ').map(Number)
[a, b, v] = [100, 99, 1000000000];
console.log(Math.ceil((v - a) / (a - b)) + 1);
