public class Palindrome {
    static boolean isPalin(String s) {
        return s.equals(new StringBuilder(s).reverse().toString());
    }
    public static void main(String[] args) {
        System.out.println("racecar is palindrome: " + isPalin("racecar"));
    }
}
