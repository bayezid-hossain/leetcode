/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stackValue={'(':1,'{':10,'[':100,')':-1,'}':-10,']':-100};
    let oppositeValue={'(':')','{':'}','[':']'}
    let stack=[];
    for(let i=0;i<s.length;i++){
       if(stackValue[s[i]]<0) {
           let lastElement= stack.pop();
           if(s[i]!==oppositeValue[lastElement])return false;
       }
       else{
        stack.push(s[i])
       }
    }
    if(stack.length==0)return true;
    return false;
};
