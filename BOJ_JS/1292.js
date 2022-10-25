// let input = require('fs').readFileSync('/dev/stdin').toString().split(' ').map(Number);
input = [3, 7];
sum = [0];
let i = 1;
let check = true;
while (check) {
    for (let j = 0; j < i; j++) {
        sum.push(sum[sum.length - 1] + i);
        if (sum.length > input[1]) {
            check = false;
            break;
        }
    }
    i++;
}
console.log(sum);
console.log(sum[input[1]] - sum[input[0] - 1]);
