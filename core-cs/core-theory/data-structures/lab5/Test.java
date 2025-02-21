public class Test {

    
    /*
      I)
      a, b straight proof)

      x is a superclass, y is a subclass, 
      x = y at compile time and run-time, 
      but y = x requires casting at compile-time but will fail at run-time,
      because of the class hierarchy
      QED
      you cannot be of type "you" but pointing to a "parent"

      c)
      If X references an arrays of x can we assign it to y?
      answer:
      no we can't because x is a superclass of y
      Does it make a difference if the array of type X[] references objects that are all of class Y ?
      answer:
      Yes it does,you will be able to assign, becase Y is a subclass of X 
      
      II)
      a) yes
      b) generally no, depends on type compatibility
      c) ...
      d) no, it's just just a string, what's important, it's the position
    */
    public static void main(String[] args) {
        X x = new Y();
	Y y = new Y();
	System.out.println("x" + x + " " + "y" + y);

 
    }
}
