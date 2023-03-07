import java.util.*;

class LargestPandigitalPrime {
    
    public static boolean allDigits(int i){
    
        String iStr = Integer.toString(i);
        int l = iStr.length();
        
        ArrayList<Integer> iArrList = new ArrayList<Integer>();
        
        for(int x=0; x<l; x++){
            int digit = Integer.valueOf(iStr.substring(x, x+1));
            iArrList.add(digit);
        }
        
        ArrayList<Integer> digits = new ArrayList<Integer>();
        for(int d = 1; d<l+1; d++){
            digits.add(d);
        }
        
        return iArrList.containsAll(digits);
    }

    public static boolean isPrime(int num){
        boolean flag = false;
        for (int i = 2; i <= num / 2; ++i) {
          // condition for nonprime number
          if (num % i == 0) {
            flag = true;
            break;
          }
        }
        return !flag;
    }
  
    
    public static void main(String[] args) {
        
        int pandigitalPrimeMax = 0;
        
        for(int number = 100000000; number>2; number--){
            if(allDigits(number) && isPrime(number)){
                pandigitalPrimeMax = number;
                break;
            }
        }
        
        System.out.print(pandigitalPrimeMax + " is the largest pandigital prime.");
    }
}
