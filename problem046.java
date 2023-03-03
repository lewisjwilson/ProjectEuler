import java.util.*;


class Goldbach {
    
    public static List<Integer> generatePrimesUpTo(int n){
        List<Integer> primes = new ArrayList<Integer>();
        for(int i = 2; i<=n; i++){
            if(!isComposite(i)){
                primes.add(i);
            }
        }
        return primes;
    }
    
    public static List<Integer> generateSquares(int n){
        List<Integer> squares = new ArrayList<Integer>();
        for(int i = 1; i<=n; i++){
            squares.add(i*i);
        }
        return squares;
    }
    
    public static boolean isComposite(int n){
        for (int i = 2; i <= n / 2; ++i) {
          // condition for nonprime number
          if (n % i == 0) {
            return true;
          }
        }
        return false;
    }
    
    
    public static void main(String[] args) {
        int n = 10000;
        List<Integer> primes = generatePrimesUpTo(n);
        List<Integer> squares = generateSquares(n);
        //System.out.println(squares.toString());
        
        for(int i=1; i<=1000000; i+=2){
            if(isComposite(i)){
                //System.out.print(i + "\n");
                
                List<Integer> subPrimes = new ArrayList<Integer>();
                List<Integer> subSquares = new ArrayList<Integer>();
                
                // For comparing only primes and squares lower than the current i value
                for(Integer p : primes){
                    if(p<i){
                        subPrimes.add(p);
                    } else {
                        break;
                    }
                }
                
                for(Integer s : squares){
                    if(s<i){
                        subSquares.add(s);
                    } else {
                        break;
                    }
                }
                
                boolean flag = false;
                
                for(Integer p : subPrimes){
                    for(Integer s : subSquares){
                        if(p + 2*s == i){
                            savedP = p;
                            savedS = s;
                            flag = true;
                            break;
                        }
                    }
                }
                
                if(!flag){
                    System.out.print(i + " is the smallest odd composite number that makes the Goldbach conjecture false!"");
                    break;
                }
            }
        }
    }
}
