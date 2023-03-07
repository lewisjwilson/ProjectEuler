import java.util.*;

class Problem047 {
    
    public static Set<Integer> primeFactors(int n){
        Set<Integer> pf = new HashSet<Integer>();
        while (n % 2 == 0) {
            pf.add(2);
            n /= 2;
        }
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                pf.add(i);
                n /= i;
            }
        }
        if (n > 2){
            pf.add(n);
        }
        return pf;
    }

    public static void main(String[] args) {
        
        int n = 2;
        int distinct = 4;
        
        while(true){
            Set<Integer> pf1 = primeFactors(n);
            Set<Integer> pf2 = primeFactors(n+1);
            Set<Integer> pf3 = primeFactors(n+2);
            Set<Integer> pf4 = primeFactors(n+3);
            
            
            if(pf1.size()==distinct && pf2.size()==distinct && pf3.size()==distinct && pf4.size()==distinct){
                System.out.print(n + " " + pf1.toString() + "\n");
                System.out.print(n+1 + " " + pf2.toString() + "\n");
                System.out.print(n+2 + " " + pf3.toString() + "\n");
                System.out.print(n+3 + " " + pf4.toString() + "\n");
                break;
            }
            n++;
        }
    }
}
