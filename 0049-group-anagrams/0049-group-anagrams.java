class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        /*
         * Idea:
         * - Anagrams have the same frequency of each character.
         * - Create a frequency array of 26 characters for each word.
         * - Convert the frequency array into a String key.
         * - Words with the same key belong to the same group.
         *
         * Example:
         * "eat" -> [1,0,0,0,1,0,...,1]
         * "tea" -> [1,0,0,0,1,0,...,1]
         *
         * Same frequency pattern => same anagram group.
         *
         * Time Complexity: O(n * k)
         * n = number of strings
         * k = maximum length of a string
         *
         * Space Complexity: O(n * k)
         */

        for (String word : strs) {
            int[] count = new int[26];

            for (char c : word.toCharArray()) {
                count[c - 'a']++;
            }

            String key = Arrays.toString(count);

            groups.putIfAbsent(key, new ArrayList<>());
            groups.get(key).add(word);
        }

        return new ArrayList<>(groups.values());
    }
}