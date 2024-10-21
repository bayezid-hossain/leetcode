class Solution {
    public int reverse(int x) {
        int sign=(x<0)?-1:1;
        if(x<0)x*=-1;
        int max = Integer.MAX_VALUE;
        long num = 0;
        while (x > 0) {
            num = num * 10 + (x % 10);
            x /= 10;
            if (num > max)
                return 0;
        }
        return (int)num*sign;
    }

}