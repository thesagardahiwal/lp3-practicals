public class Fibonachi {
    static int steps = 0;
    public static void main(String[] args) {
        int n = 10; // Change this value to compute more Fibonacci numbers
        System.out.println("Fibonacci Series up to " + n + " terms:");
        for (int i = 0; i < n; i++) {
            steps = 0;
            int fibNumber = fibonacci(i);
            System.out.println("Fibonacci(" + i + ") = " + fibNumber + ", Steps: " + steps);
        }
    }

    public static int fibonacci(int n) {
        steps++;
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}