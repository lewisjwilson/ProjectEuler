// Question
// A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
// For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
// A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
// As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
// By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
// However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum 
// of two abundant numbers is less than this limit.
// Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


// Solution - find divisors of nums, add abundant nums to an arraylist, for nums 1 - 28123, do 2 nums in the abun array sum to i?


import java.util.*;

class problem023 {

    //proper divisors
    static ArrayList<Integer> getDivisors(int n)
    {
        ArrayList<Integer> divisors = new ArrayList<>();
        for (int i=1;i<n;i++){
            if (n%i==0){
                 divisors.add(i);
            }
        }
        return divisors;
    }
    
     private static boolean sumInArr(int n, int[] arr) {
        //create HashSet and store each element as key from array
        Set<Integer> set =  new HashSet<Integer>();
        for (int element : arr){
            set.add(element);
        }
    
        //Iterate through the array and find if (n - element) exists in set
        for (int element : arr) {
          if(set.contains(n - element)){
              return true;
          } 
        }
        return false;
    }
 
    
    public static void main(String[] args) {
        
        ArrayList<Integer> abun = new ArrayList<>();
        
        int nonAbundantSum = 0;
        
        for(int i=1 ; i <= 28123 ; i++){
            ArrayList<Integer> divs = getDivisors(i);
            int divSum = divs.stream().mapToInt(val -> val).sum();
            if(divSum > i){
                abun.add(i);
            }
        }
        
        int[] abunArr = abun.stream().mapToInt(i -> i).toArray();
        
        for(int i=1 ; i <= 28123 ; i++){
            if(!sumInArr(i, abunArr)){
                nonAbundantSum += i;
            }
        }
        
        System.out.println(nonAbundantSum);
        
    }
}
