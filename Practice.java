import java.util.Scanner;

public class Practice {
    public static void main(String[] args) {
         
int i = 1;
while (i < 6) {

    int j = 1;
    while (j < i){
        System.out.print(j);
        j ++;
    }
    System.out.println(i);
    i++;

   }

   String[] favfoods = {"spaghetti", "chicken", "beef stew"};
   System.out.println(favfoods[0]);
   
            
             //P5: Take a string from the user and print them the reverse!
             System.out.println("Problem 5");
             System.out.println("Type any word and the reverse will be output");
             //hint
             Scanner sc1 = new Scanner(System.in);
             String str= sc1.nextLine(), reverse="";
             char ch;
            
           System.out.print("Original word: ");
           System.out.println(str); 
            
           for (int p=0; p<str.length(); p++)
           {
             ch= str.charAt(p); //extracts each character
             reverse= ch+reverse; //adds each character in front of the existing string
           }
           System.out.println("Reversed word: "+ reverse);
         }
        }
            

  


      

   





