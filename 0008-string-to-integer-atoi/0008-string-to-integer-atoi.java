class Solution {
    public int myAtoi(String s) {
        int min = Integer.MIN_VALUE;
        int max = Integer.MAX_VALUE;
        int sign = 1;
        long number = 0;
        boolean digitStarted = false;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == ' ' && number == 0)
                if (digitStarted)
                    break;
                else
                    continue;
            else if (ch == '+') {
                if (digitStarted)
                    break;

                digitStarted = true;
                continue;
            } else if (ch == '-') {
                if (digitStarted)
                    break;
                sign = -1;
                digitStarted = true;
                continue;
            } else if (!Character.isDigit(ch))
                break;

            digitStarted = true;
            number = number * 10 + Integer.parseInt(ch + "");
            if (number * sign > max)
                return max;
            else if (number * sign < min)
                return min;

        }
        return (int) (number * sign);
    }
}