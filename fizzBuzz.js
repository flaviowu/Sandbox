for (let i=0; i<101; i++){
    a = i%3 == 0 ? "Fizz":""
    b = i%5 == 0 ? "Buzz":""
    console.log(`${i}: ${a+b}`)
}