process.stdin.setEncoding('utf8');
process.stdin.on('data', (data) => {
    const n = data.split(' ');
    const a = Number(n[0]),
        b = Number(n[1]);
    let i = 0;
    const star = '*';
    while (i < b) {
        console.log(star.repeat(a));
        i++;
    }
});
