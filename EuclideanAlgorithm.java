public class EuclideanAlgorithm {
    /** Program finds the greatest common
     * divisor of two numbers via the 
     * Euclidean Algorithm
     */

    public static int gcd(int a, int b){
        int d = b;
        int mod = a % b;
        int[] gcdList = {d, mod};

        while (gcdList[1] != 0){
            gcdList[0] = mod;
            d = mod % d;
            gcdList[1] = d;

            gcdList[0] = d;
            mod = mod % d;
            gcdList[1] = mod;
        }

        return gcdList[0];
    }

    public static void main(String[] args){
        int a = 0;
        int b = 4;
        System.out.println(gcd(a, b));
    }
}