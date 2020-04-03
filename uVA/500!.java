import java.math.BigInteger;
import java.util.Scanner; 


class Main{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        while(input.hasNextInt()){
                
            int n = input.nextInt();
            BigInteger f = new BigInteger("1");
            for (int i=1; i<=n; i++){
                f = f.multiply(BigInteger.valueOf(i));
            }
            System.out.println(n + "!\n" + f.toString());
        }
    }
}