// let n = require('fs').readFileSync('/dev/stdin').toString().split(' ').map(Number);
let n = [3, 1, 2];

n.sort((a, b) => {
    return a - b;
});

console.log(n.join(' '));
