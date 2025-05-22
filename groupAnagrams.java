class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>(); //useful in grouping problems
        for(String s : strs){
            char[] a = s.toCharArray(); //converting string to char array
            Arrays.sort(a); //sort in alphabetical order
            String st = new String(a); //convert the char back to string format
            
            if(!map.containsKey(st)){ //we need to create new list if there is no match
            map.put(st, new ArrayList<>());
            }
            map.get(st).add(s);
        }
      return new ArrayList<>(map.values());
    }
}
