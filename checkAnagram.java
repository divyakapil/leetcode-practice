class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;  /* checking length to ensure count of characters is same */
        }
        char[] a = s.toCharArray();
        char[] b = t.toCharArray();

        Arrays.sort(a);
        Arrays.sort(b);
        return Arrays.equals(a,b);
    }
}
