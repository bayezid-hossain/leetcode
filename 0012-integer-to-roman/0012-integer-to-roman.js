/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
    
    let valueMap = { 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M" }
    
    let length=num.toString().length;
    let string=""
    while(num>0){
        let factorOfTen=Math.pow(10,length-1)
        let firstDigit=~~(num/factorOfTen)
        let wholeNumber=firstDigit*factorOfTen
        num-=wholeNumber;
        string+=getCharacters(wholeNumber,valueMap,factorOfTen,firstDigit)
        length--;
    }
    return string;
};

var getCharacters=function(num,map,factorCount,digit){
        let string="";
        while(num>0){
            if(digit==4 || digit==9){
                string+=map[num]
                num-=num;
            }
            else if( digit >3){
                num-=factorCount*5;
                if(num<0)break;
                string+=map[factorCount*5]
                string+=getCharacters(num,map,factorCount,num/factorCount)
            }
            
            else{
                string+=map[factorCount]
                num-=factorCount

            }
        }
        return string;

}