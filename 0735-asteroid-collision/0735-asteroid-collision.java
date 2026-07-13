// import java.util.Stack;
import java.util.ArrayList;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {

        // Stack<Integer> st=new Stack<>();
        ArrayList<Integer> space=new ArrayList<>();

        for(int i=0; i<asteroids.length; i++){

            int current_asteroid=asteroids[i];

            if(current_asteroid>0){
                space.add(current_asteroid);
            }
            else{
                int len=space.size();
                while(len>0 && space.get(len-1)>0 && space.get(len-1)<-1*current_asteroid){
                    space.remove(len-1);
                    len=space.size();
                }
                if(len>0 && space.get(len-1).equals(-1*current_asteroid)){
                    space.remove(len-1);
                }
                else if(len==0 || space.get(len-1)<0){
                space.add(current_asteroid);
                }
            }

            }
            int[] result = new int[space.size()];

            for (int i = 0; i < space.size(); i++) {
                result[i] = space.get(i);
                }

            return result;
    }
}