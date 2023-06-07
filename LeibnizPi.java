import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;

/**
 *  Calculates Pi using the Leibniz formula for pi.
 *  https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
 *  The main method accepts the first input from stdin (has to be integer)
 *  and passes that to the calculatePi method which handles the calculation
 *  for the alternating series
 */

public class LeibnizPi {

    public static void main(String[] args){
        try {
            int precision = Integer.valueOf(args[0]);
            for (int i = 1; i < precision + 1; i++) {
                System.out.println(calculatePi(i).toPlainString());
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    private static BigDecimal calculatePi(int precision){
        MathContext mc = new MathContext(12, RoundingMode.HALF_DOWN);
        // numerator = -1
        BigDecimal numerator = new BigDecimal(-1);
        // sums = 0
        BigDecimal sums = new BigDecimal(0);

        for (int i = 0; i < precision; i++){
            // numerator += numerator.pow(i);
            numerator = numerator.pow(i);
            // denominator = 2*i + 1;
            BigDecimal denominator = new BigDecimal(2 * i + 1);
            // sums += numerator / denominator;
            sums = sums.add(numerator.divide(denominator, mc));
            numerator = new BigDecimal(-1);
        }

        // sums * 4
        sums = sums.multiply(new BigDecimal(4));
        return sums.round(mc);
    }
}
