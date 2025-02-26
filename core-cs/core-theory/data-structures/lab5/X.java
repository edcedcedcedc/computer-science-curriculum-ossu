package lab5;

public class X {
	public static final int[] x = { 0, 1, 2 };

	/*
	 * public X(){
	 * this.x = new int[]{0,1,2};
	 * }
	 */

	public String toString() {
		String result = "[";
		for (int i = 0; i < this.x.length; i++) {
			result = result + " " + x[i] + " ";
		}
		return result + "]";
	}
}
