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
      III)
      Suppose subclass inherits a "public static final" constant from superclass
      and implements a java interface that contains a "public static final" constant 
      with the same name 
      a)No it wont it doesnt matter, in the interface you don't usually assign values 
      b)No it doesnt make a difference it will run the result 
      c) - am dropping this part.
      IV)
    */
    
    public static void main(String[] args) {
        X x = new X();
	Y y = new Y();
	System.out.println("x" + x + " " + "y" + y);

 
    }
}

