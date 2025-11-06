public class ArrayOperations {
    static int arraySum(int[] arr) {
        int sum = 0;
        for (int x : arr) sum += x;
        return sum;
    }
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5};
        System.out.println("Sum: " + arraySum(nums));
    }
}
