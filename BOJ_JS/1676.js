// let input = require('fs').readFileSync('/dev/stdin').toString()
// input = parseInt(input, 10);
let input = 10;
let answer = 0;
while (input >= 5) {
    input = input / 5;
    answer += Math.floor(input);
}

console.log(answer);
