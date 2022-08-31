// Question 
// n! means n × (n − 1) × ... × 3 × 2 × 1
// For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
// and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
// Find the sum of the digits in the number 100!


// Solution - Utilising BigInteger do to the size of the factorial

import java.math.BigInteger;

public class problem020 {

    public static void main(String[] args) {
        BigInteger fact = new BigInteger("1");
        for (int i = 100; i > 0; i--) {
            fact = fact.multiply(BigInteger.valueOf(i));
        }
        
        String factStr = fact.toString();
        int digitSum = 0;
        for(int i = 0 ; i < factStr.length(); i++){
            digitSum += Integer.parseInt(factStr.substring(i, i+1));
        }
        
        System.out.println(digitSum);
        
    }
}
