let result = /^[a-zA-Z ]+$/.test("John D#");
console.log(result);

let isNumber = /^\d+%?$/.test("111231331313");
console.log(isNumber);


// retorna os valores que são 'false' 
const testeObj = {
  dado1: true,
  dado2: true,
  dado3: true,
  dado4: false,  //4 = false
  dado5: true,
  dado6: true,
  dado7: false,  //7 = false
  dado8: true,
  dado9: true,
  frutas: false,
  losangos: false,
};

const valueFalseKeys = Object.keys(testeObj).filter((key) => testeObj[key] === false);
console.log(valueFalseKeys)
