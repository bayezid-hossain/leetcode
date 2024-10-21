class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1 || s.length() <= 1)
            return s;
        StringBuilder[] sbs = new StringBuilder[numRows];
        for (int i = 0; i < sbs.length; i++) {
            sbs[i] = new StringBuilder();
        }
        char[] string = s.toCharArray();
        int col = 0;
        for (int i = 0; i < string.length; i++) {
            for (int j = 0; j < numRows && i < string.length; j++) {
                sbs[j].append(string[i] + "");
                i++;
            }
            col++;
            for (int j = numRows - 2; j > 0 && i < string.length; j--) {
                sbs[j].append(string[i] + "");
                i++;
                col++;

            }
            i--;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numRows; i++) {
            sb.append(sbs[i]);
        }
        return sb.toString();
    }
}