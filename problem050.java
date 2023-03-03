import java.util.*;

class Problem050 {
    
    // Sieve of Eratosthenes
    public static List<Integer> generatePrimes(int to){
        List<Integer> primes = new ArrayList<Integer>();
        
        int from = 1, i;
        boolean[] a = new boolean[to + 1];
        Arrays.fill(a, true);
 
        // 0 and 1 are not prime
        a[0] = false;
        a[1] = false;
        for (i = 2; i <= Math.sqrt(to); i++){
            // Check if number is prime
            if (a[i]){
                for (int j = i * i; j <= to; j += i) {
                    a[j] = false;
                }
            }
        }
        for (i = from; i <= to; i++) {
            // Adding only prime numbers
            if (a[i]){
                primes.add(i);
            }
        }
        return primes;
    }
        
    public static void main(String[] args) {
        
        int n = 1000000;
        
        List<Integer> primes = generatePrimes(n);
        
        List<Integer> interesting = new ArrayList<Integer>();
        int poi = 0;
        int longest = 0;
        
        for(int l = 499; l<1000; l++){
            for(int i = 0; i<n-l ; i++){
                List<Integer> subPrimes = primes.subList(i, i+l);
                //System.out.print(subPrimes);
                int sum = subPrimes.stream().mapToInt(Integer::intValue).sum();
                if(sum>n){
                    break;
                }
                if(primes.contains(sum)){
                    if(subPrimes.size()>longest){
                        //System.out.print(sum + " " + subPrimes + "\n");
                        poi = sum;
                        interesting = subPrimes;
                        longest = interesting.size();
                    }
                    
                }
            }
        }
        
        System.out.print("interesting: " + interesting + "\n" + "poi: " + poi + "\n" + "longest: " + longest + "\n");
    }
}
