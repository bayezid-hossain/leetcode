/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let i=0,result=0;
    var numberMap={'I':1,'V':5,'X':10,"L":50,"C":100,"D":500,"M":1000};
    for(i=0;i<s.length;i++){
        const cur=numberMap[s[i]];
        const next=numberMap[s[i+1]];
        if(cur<next){
            result+=next-cur;
            i++;
        }else result+=cur
    }
    return result

};