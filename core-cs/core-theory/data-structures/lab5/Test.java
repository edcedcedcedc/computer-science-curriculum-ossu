public class Test {

    
    /*
      a, b straight proof)

      x is a superclass, y is a subclass, 
      x = y at compile time and run-time, 
      but y = x requires casting at compile-time but will fail at run-time,
      because of the class hierarchy
      QED
      you cannot be of type "you" but pointing to a "parent"
    */
    public static void main(String[] args) {
        X x = new X();
	Y y = new Y();
        y = (Y)x;
	System.out.println("x" + x + " " + "y" + y);

 
    }
}
