/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var copy=x,reverse=0;
    while(copy>0){
        var remainder=copy%10;
        reverse=reverse*10+remainder;
        copy=~~(copy/10);
    }
    if(reverse==x)return true;
    return false;
};