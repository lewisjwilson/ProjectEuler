import java.util.*;

class Problem049 {
    
    public static boolean isPerm(int a, int b){
        Set<Integer> aCheck = new HashSet<Integer>();
        Set<Integer> bCheck = new HashSet<Integer>();
        Set<Integer> combined = new HashSet<Integer>();
        while(a>0){
            aCheck.add(a%10);
            combined.add(a%10);
            a /= 10;
        }
        while(b>0){
            bCheck.add(b%10);
            combined.add(b%10);
            b /= 10;
        }
        //System.out.print(aCheck.toString() + "\n");
        //System.out.print(bCheck.toString() + "\n");
        //System.out.print(combined.toString() + "\n");
        return aCheck.size() == combined.size() && bCheck.size() == combined.size();
    }
    
    public static List<Integer> generatePrimes(){
        List<Integer> primes = new ArrayList<Integer>();
        for(int i = 1000; i<=9999; i++){
            if(isPrime(i)){
                primes.add(i);
            }
        }
        return primes;
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
    
    public static void main(String[] args) {
        List<Integer> primes = generatePrimes();
        for(Integer a : primes){
            for(Integer b: primes){
                for(Integer c: primes){
                    if(a >= b || a >= c || b >= c){
                        continue;
                    }
                    int abDiff = b-a;
                    int bcDiff = c-b;
                    if(abDiff==bcDiff && isPerm(a, b) && isPerm(b, c)){
                        System.out.print(a + " " + b + " " + c + "\n");
                    }
                }
            }
        }
        
        System.out.println("All 4-digit numbers checked!");
    }
}
