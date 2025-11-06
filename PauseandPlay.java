
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;

public class PauseandPlay {

    public static void main(String[] args) {
       

       String[]FOODS = {"Sphaghetti", "Noodles", "Omelettes"};
       int[]even = {2,4,6,8,10};
       Boolean[]answer = {false, true, false};
       String[]Alphabet = {"a", "b", "c", "d",};
       System.out.println(FOODS[0]);
    
                
        for(int i = 0; i < (FOODS).length; i++){
            System.out.println((FOODS)[i]);
        }
        
        Integer[]random = {2,4,6,7,8,9,1,3,5,0};
        Arrays.sort(random);
        Arrays.sort(random, Collections.reverseOrder());
        System.out.println(Arrays.toString(random));

        int[]small = {3,8,10,6,2};
        Arrays.sort(small);
        System.out.println((small)[0]);



        List<String> Family = new ArrayList<>();
        Family.add("Tyler");
        Family.add("Mom");
        Family.add("Dad");
        Family.add("Sister");
        Family.add("Grandpa");
        System.out.println(Family);

        
        
        

    
}
}





        
   


