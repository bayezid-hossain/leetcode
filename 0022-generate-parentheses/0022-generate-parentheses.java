class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res=new ArrayList<String>();
        recurseParenthesis(res,0,0,"",n);
        return res;
    }

    public void recurseParenthesis(List<String>res,int left,int right,String s,int length){
        if(s.length()==length*2){
            res.add(s);
            return;
        }
        if(left<length)recurseParenthesis(res,left+1,right,s+"(",length);
        if(right<left){
            recurseParenthesis(res,left,right+1,s+")",length);
        }
    }
}