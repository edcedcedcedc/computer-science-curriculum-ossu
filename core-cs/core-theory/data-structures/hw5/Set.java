package hw5;

/* Set.java */

import hw5.list.*;

/**
 * A Set is a collection of Comparable elements stored in sorted order.
 * Duplicate elements are not permitted in a Set.
 **/
public class Set {
  /* Fill in the data fields here. */

  /**
   * Set ADT invariants: 1) The Set's elements must be precisely the elements of
   * the List. 2) The List must always contain Comparable elements, and those
   * elements must always be sorted in ascending order. 3) No two elements in the
   * List may be equal according to compareTo().
   **/

  /**
   * Constructs an empty Set.
   *
   * Performance: runs in O(1) time.
   **/
  private DList elements;

  public Set() {
    // Your solution here.
    this.elements = new DList();
  }

  /**
   * cardinality() returns the number of elements in this Set.
   *
   * Performance: runs in O(1) time.
   **/
  public int cardinality() {
    // Replace the following line with your solution.
    return elements.length();
  }

  /**
   * insert() inserts a Comparable element into this Set.
   *
   * Sets are maintained in sorted order. The ordering is specified by the
   * compareTo() method of the java.lang.Comparable interface.
   *
   * Performance: runs in O(this.cardinality()) time.
   * 
   * @throws InvalidNodeException
   **/
  public void insert(Comparable c) throws InvalidNodeException {
    if (elements.isEmpty()) {
      elements.insertBack(c);
      return;
    }
    DListNode current = (DListNode) elements.front();
    while (current.isValidNode()) {
      int comparison = c.compareTo((Comparable) current.item());
      if (comparison == 0) {
        return;
      } else if (comparison < 0) {

        current.insertBefore(c);
        return;
      }
      current = (DListNode) current.next();
    }
    elements.insertBack(c);
  }

  /**
   * union() modifies this Set so that it contains all the elements it started
   * with, plus all the elements of s. The Set s is NOT modified. Make sure that
   * duplicate elements are not created.
   *
   * Performance: Must run in O(this.cardinality() + s.cardinality()) time.
   *
   * Your implementation should NOT copy elements of s or "this", though it will
   * copy _references_ to the elements of s. Your implementation will create new
   * _nodes_ for the elements of s that are added to "this", but you should reuse
   * the nodes that are already part of "this".
   *
   * DO NOT MODIFY THE SET s. DO NOT ATTEMPT TO COPY ELEMENTS; just copy
   * _references_ to them.
   **/
  public void union(Set s) throws InvalidNodeException {
    // Your solution here.
    DListNode thisCurrent = (DListNode) this.elements.front();
    DListNode sCurrent = (DListNode) s.elements.front();
    while (thisCurrent.isValidNode() && sCurrent.isValidNode()) {
      Comparable thisItem = (Comparable) thisCurrent.item();
      Comparable sItem = (Comparable) sCurrent.item();
      int comparison = thisItem.compareTo(sItem);
      if (comparison == 0) {
        sCurrent = (DListNode) sCurrent.next();
      } else if (comparison > 0) {
        thisCurrent.insertBefore(sItem);
        sCurrent = (DListNode) sCurrent.next();
      } else {
        thisCurrent = (DListNode) thisCurrent.next();
      }
    }
    while (sCurrent.isValidNode()) {
      this.elements.insertBack(sCurrent.item());
      sCurrent = (DListNode) sCurrent.next();
    }
  }

  /**
   * intersect() modifies this Set so that it contains the intersection of its own
   * elements and the elements of s. The Set s is NOT modified.
   *
   * Performance: Must run in O(this.cardinality() + s.cardinality()) time.
   *
   * Do not construct any new ListNodes during the execution of intersect. Reuse
   * the nodes of "this" that will be in the intersection.
   *
   * DO NOT MODIFY THE SET s. DO NOT CONSTRUCT ANY NEW NODES. DO NOT ATTEMPT TO
   * COPY ELEMENTS.
   **/
  public void intersect(Set s) throws InvalidNodeException {
    DListNode thisCurrent = (DListNode) this.elements.front();
    DListNode sCurrent = (DListNode) s.elements.front();

    while (thisCurrent.isValidNode() && sCurrent.isValidNode()) {
      Comparable thisItem = (Comparable) thisCurrent.item();
      Comparable sItem = (Comparable) sCurrent.item();

      int comparison = thisItem.compareTo(sItem);
      if (comparison == 0) {
        thisCurrent = (DListNode) thisCurrent.next();
        sCurrent = (DListNode) sCurrent.next();
      } else if (comparison < 0) {
        DListNode toRemove = thisCurrent;
        thisCurrent = (DListNode) thisCurrent.next();
        toRemove.remove();
      } else {
        sCurrent = (DListNode) sCurrent.next();
      }
    }
  }

  /**
   * toString() returns a String representation of this Set. The String must have
   * the following format: { } for an empty Set. No spaces before "{" or after
   * "}"; two spaces between them. { 1 2 3 } for a Set of three Integer elements.
   * No spaces before "{" or after "}"; two spaces before and after each element.
   * Elements are printed with their own toString method, whatever that may be.
   * The elements must appear in sorted order, from lowest to highest according to
   * the compareTo() method.
   *
   * WARNING: THE AUTOGRADER EXPECTS YOU TO PRINT SETS IN _EXACTLY_ THIS FORMAT,
   * RIGHT UP TO THE TWO SPACES BETWEEN ELEMENTS. ANY DEVIATIONS WILL LOSE POINTS.
   **/
  public String toString() {
    if (elements.isEmpty()) {
      return "{ }";
    }
    StringBuilder sb = new StringBuilder();
    sb.append("{");
    try {
      DListNode current = (DListNode) elements.front();
      while (current.isValidNode()) {
        sb.append(" ").append(current.item());
        current = (DListNode) current.next();
      }
    } catch (InvalidNodeException e) {
      System.out.println("Error traversing the list: " + e.getMessage());
    }

    sb.append(" }");
    return sb.toString();
  }

  public static void main(String[] argv) throws InvalidNodeException {
    Set s = new Set();
    s.insert(3);
    s.insert(4);
    s.insert(3);
    s.insert(6);
    System.out.println("Set s = " + s);
    s.elements.front().remove();
    System.out.println("Removing front from s " + s);
    s.elements.back().remove();
    System.out.println("Removing back from s " + s);
    System.out.print("Inserting again 3, 4, 3, 6" + '\n');
    s.insert(3);
    s.insert(4);
    s.insert(3);
    s.insert(6);
    System.out.println("Set s = " + s);
    Set s2 = new Set();
    s2.insert(4);
    s2.insert(5);
    s2.insert(5);
    System.out.println("Set s2 = " + s2);

    Set s3 = new Set();
    s3.insert(5);
    s3.insert(3);
    s3.insert(8);
    s3.insert(9);
    s3.insert(4);
    System.out.println("Set s3 = " + s3);

    s.union(s2);
    System.out.println("After s.union(s2), s = " + s);

    s.intersect(s3);
    System.out.println("After s.intersect(s3), s = " + s);

    System.out.println("s.cardinality() = " + s.cardinality());
    // You may want to add more (ungraded) test code here.
  }
}
