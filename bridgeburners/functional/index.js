

function sayHello(){ 
    return function(){
        return "Hello World";
    }
}


let numbers = [1,2,3];
let other = numbers.map(number => number * 2)

console.log(other)

let fn = sayHello();
let message = fn();
console.log("message ",message)