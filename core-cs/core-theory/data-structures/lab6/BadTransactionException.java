package lab6;

public class BadTransactionException extends Exception {

	/**
	 * Creates an exception object for invalid amount.
	 **/
	public BadTransactionException(int amount) {
		super("Invalid amount: " + " " + amount);

	}
}
