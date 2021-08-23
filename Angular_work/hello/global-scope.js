var Name = 'James'

function changeName() {
    Name = 'Hames'
}
changeName()
console.log(Name)

let name = 'John';

function changeJina() {
    name = 'Johnte'
}
changeJina();
console.log(name);

const person = {};
person.name = 'Joe';
console.log(person);

const people = Object.freeze({});
people.name = 'Mary';
console.log(people);

let multiLine = `I am a multi-line
string and I use  Backticks all over 
my code`
console.log(multiLine);

const name1 = 'Macharia John';

const header = `hi, my name is ${name1}`;
console.log(header);