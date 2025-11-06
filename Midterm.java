import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;
public class Midterm {
    public static void main(String args){
        Integer[] Cases = {1,5,10,20,25,50,75,100,200,250,500,750,1000,1500,2000,2500,5000,10000,20000,50000,100000,250000,500000,1000000,5000000,10000000};
        Scanner sc = new Scanner(System.in);  
    System.out.println("Enter your first case");

    String case1 = sc.nextLine();
    if (case1 == "yes");
    Random random = new Random();  
    Integer randomElement = Cases[random.nextInt(Cases.length)];  
  
System.out.println(randomElement);  
    }
}
    
