// let input = require('fs').readFileSync('/dev/stdin').toString()
let input = '55+50-40+10';
input = input.split('-');
answer = input[0].split('+').reduce((a, b) => a + parseInt(b, 10), 0);

for (let i = 1; i < input.length; i++) {
    answer = input[i].split('+').reduce((a, b) => a - parseInt(b, 10), answer);
}

console.log(answer);
