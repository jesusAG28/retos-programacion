for (let i = 1; i <= 100; i++) {
    let m3 = i % 3 == 0 ? true : false;
    let m5 = i % 5 == 0 ? true : false;

    if (m3 && m5) console.log('fizzbuzz');
    else if (m3) console.log('fizz');
    else if (m5) console.log('buzz');
    else console.log(i);
}
