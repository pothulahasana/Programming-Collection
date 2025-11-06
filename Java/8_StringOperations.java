public class StringOperations {
    static int countVowels(String s) {
        int count = 0;
        for (char c : s.toLowerCase().toCharArray())
            if ("aeiou".indexOf(c) >= 0) count++;
        return count;
    }
    public static void main(String[] args) {
        System.out.println("Vowels in 'hello': " + countVowels("hello"));
    }
}
