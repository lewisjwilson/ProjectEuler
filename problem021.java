// Question 21
// Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
// If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
// The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
// Evaluate the sum of all the amicable numbers under 10000.


// Solution - get divisors and compare, skip over numbers already checked (in checked array).


import java.util.Arrays;
import java.util.ArrayList;

class problem021 {
    
    public static ArrayList<Integer> checked = new ArrayList<>();
    public static ArrayList<Integer> amicable = new ArrayList<>();
    
    
    public static void main(String[] args) {
        
        ArrayList<Integer> div = new ArrayList<Integer>();
        int sum = 0;
        int sum2 = 0;
        
        for(int i=1 ; i<=10000 ; i++){
            if(checked.contains(i)){
                continue;
            }
            
            div = divisors(i);
            sum = div.stream().mapToInt(Integer::intValue).sum();
            div = divisors(sum);
            sum2 = div.stream().mapToInt(Integer::intValue).sum();
          
            if(i == sum2 && sum != sum2){
                System.out.println(sum + " and " + sum2);
                amicable.add(sum);
                amicable.add(sum2);
            }
            checked.add(sum);
            checked.add(sum2);
            
        }
        System.out.println(Arrays.toString(amicable.toArray()));
        System.out.println(amicable.stream().mapToInt(Integer::intValue).sum());
    }
    
    //non-inclusive of num itself
    public static ArrayList<Integer> divisors(int num){
        ArrayList<Integer> div = new ArrayList<>();;
        for (int i=1; i<num; i++){
            if (num%i==0){
                div.add(i);
            }
        }
        return div;
    }
  }
