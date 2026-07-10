import java.util.*;

class Solution {
    public List<List<Integer>> generate(int numRows) {

        List<List<Integer>> triangle = new ArrayList<>();

        // Generate each row
        for (int i = 0; i < numRows; i++) {

            List<Integer> row = new ArrayList<>();

            // First and last element are always 1
            for (int j = 0; j <= i; j++) {

                if (j == 0 || j == i) {
                    row.add(1);
                } else {
                    int value = triangle.get(i - 1).get(j - 1)
                              + triangle.get(i - 1).get(j);

                    row.add(value);
                }
            }

            triangle.add(row);
        }

        return triangle;
    }
}