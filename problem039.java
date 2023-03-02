import java.lang.Math;
import java.util.*;


class Triangle {
    
    double a;
    double b;
    double c;
    
    public double getA() 
    {
        return a;
    }
    
    public double getB() 
    {
        return b;
    }
    
    public double getC() 
    {
        return c;
    }
    
    public double setA(double a) 
    {
        return this.a = a;
    }
    
    public double setB(double b) 
    {
        return this.b = b;
    }
    
    public double setC() 
    {
        return this.c = Math.sqrt(Math.pow(this.a, 2) + Math.pow(this.b, 2));
    }
     
    public static double getPerimeter(Triangle tri){
        return tri.getA() + tri.getB() + tri.getC();
    }
    
    
    public static void main(String[] args) {
        Triangle t = new Triangle();
        
        Hashtable<Double, Double> pVals = new Hashtable<Double, Double>();
        
        for(int p = 1; p<1001; p++){
            pVals.put((double)p, 0.0);
        }
        
        for(int a = 1; a<1000; a++){
            t.setA((double)a);
            for(int b = 1; b<1000; b++){
                t.setB((double)b);
                t.setC();
                double p = getPerimeter(t);
                
                if(p < 1000 && pVals.containsKey(p)){
                    // As a and b will appear twice in the same combination,
                    // We add 0.5 rather than 1.
                    pVals.put(p, pVals.get(p)+0.5);
                    //System.out.print("a: " + t.getA() + ", b:  " + t.getB() + ", c:  " + t.getC() + ", p: " + getPerimeter(t) + "\n");
                }
            }
        }
        
        //System.out.println("Number of solutions for p=120: " + pVals.get(1000.0));
        
        int maxP = 0;
        double maxVal = 0.0;
        
        for(int p = 1; p<1001; p++){
            double val = pVals.get((double)p);
            if(val>maxVal){
                maxP = p;
                maxVal = pVals.get((double)p);
            }
            //System.out.println("p: " + p + " " + pVals.get((double)p));
        }
        
        System.out.println("Solutions are maximised at p = " + maxP + ",\nwith the number of solutions equalling " + maxVal);
    }

}
