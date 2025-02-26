package lab5;

public class Y extends X implements MyTestInterface {
    int[] y;

    public Y() {
        this.y = new int[] { 1, 2, 3 };
    }

    @Override
    public String toString() {
        String result = "[";
        for (int i = 0; i < this.y.length; i++) {
            result = result + " " + y[i] + " ";
        }
        return result + "]";
    }

    public static void main(String[] args) {
        System.out.println(X.x[0]);
    }
}
