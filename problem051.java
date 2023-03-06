import java.util.*;
import java.util.regex.*;

class HelloWorld {
    
    public static String perms = "";
    
    public static List<Integer> checkPrimes(String asteriskedNum){
        List<Integer> toCheck = new ArrayList<Integer>();
        if(!Pattern.matches("[\\*0-9]*", asteriskedNum)){
            System.out.println("Format incorrect. Should contain only digits 0-9 or *.");
            return toCheck;
        }
        
        for(int i = 0; i<10; i++){
            String iStr =  Integer.toString(i);
            String numStr = asteriskedNum.replaceAll("\\*", iStr);
            numStr = numStr.replaceFirst("^0*", "");
            int num = Integer.valueOf(numStr);
            if(numStr.length() != asteriskedNum.length()){
                continue;
            }
            if(isPrime(num)){
                toCheck.add(num);
            }
            
        }
        return toCheck;
    }
    
    public static boolean isPrime(int n){
        for (int i = 2; i <= n / 2; ++i) {
          // condition for nonprime number
          if (n % i == 0) {
            return false;
          }
        }
        return true;
    }
    
    public static void permute(String s, String answer){   
        if (s.length() == 0)
        {
            //System.out.print(answer + ", ");
            perms += answer + ", ";
            return;
        }
          
        for(int i = 0 ;i < s.length(); i++)
        {
            char ch = s.charAt(i);
            String left_substr = s.substring(0, i);
            String right_substr = s.substring(i + 1);
            String rest = left_substr + right_substr;
            permute(rest, answer + ch);
        }
    }
    
    public static void main(String[] args) {
        
        String numStr = "5000*";
        List<Integer> largestSet = new ArrayList<Integer>();
        
        for(int i = 1; i<numStr.length(); i++){
            
            permute(numStr, "");
            List<String> permutations = Arrays.asList(perms.split("\\s*,\\s*"));
            
            for(String n : permutations){
                //System.out.print(checkPrimes(n) + "\n");
                if(checkPrimes(n).size() > largestSet.size()){
                    largestSet = checkPrimes(n);
                }
            }
            
            numStr = numStr.substring(0, i-1) + numStr.substring(i-1, i) + numStr.substring(i);
        }
            
        System.out.print(largestSet + ", size: " + largestSet.size());
        
        
    }
}
