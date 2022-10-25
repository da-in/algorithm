// let receipt = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

let receipt = ['250000', '4', '20000 5', '30000 2', '10000 6', '5000 8'];
let total = parseInt(receipt[0], 10);
let p, c;
receipt = receipt.splice(2);

for (col of receipt) {
    [p, c] = col.split(' ').map(Number);
    total -= p * c;
}

if (total == 0) {
    console.log('Yes');
} else {
    console.log('No');
}
