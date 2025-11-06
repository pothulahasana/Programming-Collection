public class Recursion {
    static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
    static int power(int x, int n) {
        return n == 0 ? 1 : x * power(x, n - 1);
    }
    public static void main(String[] args) {
        System.out.println("GCD(48, 18): " + gcd(48, 18));
        System.out.println("Power(2, 5): " + power(2, 5));
    }
}
