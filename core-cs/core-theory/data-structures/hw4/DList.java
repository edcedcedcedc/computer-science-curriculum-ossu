/* DList.java */

package hw4;

/**
 * A DList is a mutable doubly-linked list ADT. Its implementation is
 * circularly-linked and employs a sentinel (dummy) node at the head of the
 * list.
 *
 * DO NOT CHANGE ANY METHOD PROTOTYPES IN THIS FILE.
 */

public class DList {

  /**
   * head references the sentinel node. size is the number of items in the list.
   * (The sentinel node does not store an item.)
   *
   * DO NOT CHANGE THE FOLLOWING FIELD DECLARATIONS.
   */

  protected DListNode head;
  protected int size;

  /*
   * DList invariants: 1) head != null. 2) For any DListNode x in a DList, x.next
   * != null. 3) For any DListNode x in a DList, x.prev != null. 4) For any
   * DListNode x in a DList, if x.next == y, then y.prev == x. 5) For any
   * DListNode x in a DList, if x.prev == y, then y.next == x. 6) size is the
   * number of DListNodes, NOT COUNTING the sentinel, that can be accessed from
   * the sentinel (head) by a sequence of "next" references.
   */

  /**
   * newNode() calls the DListNode constructor. Use this class to allocate new
   * DListNodes rather than calling the DListNode constructor directly. That way,
   * only this method needs to be overridden if a subclass of DList wants to use a
   * different kind of node.
   * 
   * @param item the item to store in the node.
   * @param prev the node previous to this node.
   * @param next the node following this node.
   */
  protected DListNode newNode(Object item, hw4.DListNode prev, hw4.DListNode next) {
    return new DListNode(item, prev, next);
  }

  /**
   * DList() constructor for an empty DList.
   */
  public DList() {
    head = newNode(null, null, null);
    head.next = head;
    head.prev = head;
    size = 0;
  }

  /**
   * isEmpty() returns true if this DList is empty, false otherwise.
   * 
   * @return true if this DList is empty, false otherwise. Performance: runs in
   *         O(1) time.
   */
  public boolean isEmpty() {
    return size == 0;
  }

  /**
   * length() returns the length of this DList.
   * 
   * @return the length of this DList. Performance: runs in O(1) time.
   */
  public int length() {
    return size;
  }

  /**
   * insertFront() inserts an item at the front of this DList.
   * 
   * @param item is the item to be inserted. Performance: runs in O(1) time.
   */
  public void insertFront(Object item) {
    DListNode newNode = newNode(item, head, head.next);
    head.next.prev = newNode;
    head.next = newNode;
    size++;
  }

  /**
   * insertBack() inserts an item at the back of this DList.
   * 
   * @param item is the item to be inserted. Performance: runs in O(1) time.
   */
  public void insertBack(Object item) {
    DListNode newNode = newNode(item, head.prev, head);
    head.prev.next = newNode;
    head.prev = newNode;
    size++;
  }

  /**
   * front() returns the node at the front of this DList. If the DList is empty,
   * return null.
   *
   * Do NOT return the sentinel under any circumstances!
   *
   * @return the node at the front of this DList. Performance: runs in O(1) time.
   */

  public DListNode front() {
    if (this.isEmpty()) {
      return null;
    }
    return head.next;
  }

  /**
   * back() returns the node at the back of this DList. If the DList is empty,
   * return null.
   *
   * Do NOT return the sentinel under any circumstances!
   *
   * @return the node at the back of this DList. Performance: runs in O(1) time.
   */

  public DListNode back() {
    if (this.isEmpty()) {
      return null;
    }
    return head.prev;
  }

  /**
   * next() returns the node following "node" in this DList. If "node" is null, or
   * "node" is the last node in this DList, return null.
   *
   * Do NOT return the sentinel under any circumstances!
   *
   * @param node the node whose successor is sought.
   * @return the node following "node". Performance: runs in O(1) time.
   */

  public DListNode next(DListNode node) {
    if (node == null || node.next == head) {
      return null;
    }
    return node.next;
  }

  /**
   * prev() returns the node prior to "node" in this DList. If "node" is null, or
   * "node" is the first node in this DList, return null.
   *
   * Do NOT return the sentinel under any circumstances!
   *
   * @param node the node whose predecessor is sought.
   * @return the node prior to "node". Performance: runs in O(1) time.
   */

  public DListNode prev(DListNode node) {
    if (node == null || node.prev != head) {
      return null;
    }
    return node.prev;
  }

  /**
   * insertAfter() inserts an item in this DList immediately following "node". If
   * "node" is null, do nothing.
   * 
   * @param item the item to be inserted.
   * @param node the node to insert the item after. Performance: runs in O(1)
   *             time.
   */
  public void insertAfter(Object item, DListNode node) {
    if (node != null && node.next != head) {
      node.next.item = item;
    }
  }

  /**
   * insertBefore() inserts an item in this DList immediately before "node". If
   * "node" is null, do nothing.
   * 
   * @param item the item to be inserted.
   * @param node the node to insert the item before. Performance: runs in O(1)
   *             time.
   */
  public void insertBefore(Object item, DListNode node) {
    if (node != null && node.prev != head) {
      node.prev.item = item;
    }
  }

  /**
   * remove() removes "node" from this DList. If "node" is null, do nothing.
   * Performance: runs in O(1) time.
   */

  /*
   * 
   * A -> B -> C -> D
   */
  public void remove(DListNode node) {
    if (node != head) {
      node.prev.next = node.next;
      node.next.prev = node.prev;
      size--;
    }
  }

  /**
   * toString() returns a String representation of this DList.
   *
   * DO NOT CHANGE THIS METHOD.
   *
   * @return a String representation of this DList. Performance: runs in O(n)
   *         time, where n is the length of the list.
   */
  @Override
  public String toString() {
    String result = "[  ";
    DListNode current = head.next;
    while (current != head) {
      result = result + current.item + "  ";
      current = current.next;
    }
    return result + "]";
  }

  public static void main(String[] args) {
    System.out.println("=== Testing DList Methods ===");

    // Create a new DList
    DList newList = new DList();
    System.out.println("1. Created a new empty DList.");
    System.out.println("Is the list empty? " + newList.isEmpty());
    System.out.println("List length: " + newList.length());
    System.out.println("List contents: " + newList.toString());
    System.out.println();

    // Test insertFront
    System.out.println("2. Testing insertFront() method:");
    newList.insertFront(1);
    newList.insertFront(0);
    System.out.println("Inserted 1 and 0 at the front.");
    System.out.println("List contents: " + newList.toString());
    System.out.println();

    // Test insertBack
    System.out.println("3. Testing insertBack() method:");
    newList.insertBack(2);
    newList.insertBack(3);
    System.out.println("Inserted 2 and 3 at the back.");
    System.out.println("List contents: " + newList.toString());
    System.out.println();

    // Test front and back
    System.out.println("4. Testing front() and back() methods:");
    System.out.println("Front item: " + (newList.front() != null ? newList.front().item : "null"));
    System.out.println("Back item: " + (newList.back() != null ? newList.back().item : "null"));
    System.out.println();

    // Test next
    System.out.println("5. Testing next() method:");
    DListNode frontNode = newList.front();
    System.out
        .println("Item after front: " + (newList.next(frontNode) != null ? newList.next(frontNode).item : "null"));
    System.out.println();

    // Test prev
    System.out.println("6. Testing prev() method:");
    DListNode backNode = newList.back();
    System.out.println("Item before back: " + (newList.prev(backNode) != null ? newList.prev(backNode).item : "null"));
    System.out.println();

    // Test insertAfter
    System.out.println("7. Testing insertAfter() method:");
    newList.insertAfter(5, newList.front());
    System.out.println("Inserted 5 after the front item.");
    System.out.println("List contents: " + newList.toString());
    System.out.println();

    // Test insertBefore
    System.out.println("8. Testing insertBefore() method:");
    newList.insertBefore(6, newList.back());
    System.out.println("Inserted 6 before the back item.");
    System.out.println("List contents: " + newList.toString());
    System.out.println();

    // Test remove
    System.out.println("9. Testing remove() method:");
    newList.remove(newList.front());
    System.out.println("Removed the front item.");
    System.out.println("List contents: " + newList.toString());
    newList.remove(newList.back());
    System.out.println("Removed the back item.");
    newList.remove(newList.back());
    System.out.println("Removed the back item.");
    System.out.println("List contents: " + newList.toString());
    System.out.println();

    // Test isEmpty and length after removals
    System.out.println("10. Testing isEmpty() and length() after removals:");
    System.out.println("Is the list empty? " + newList.isEmpty());
    System.out.println("List length: " + newList.length());
    System.out.println("List contents: " + newList.toString());
    System.out.println();

    // Test edge cases
    System.out.println("11. Testing edge cases:");
    System.out.println("Attempting to remove from an len(1) list...");
    newList.remove(newList.front());
    System.out.println("List contents: " + newList.toString());
    System.out.println("Attempting to insertAfter() on null node...");
    newList.insertAfter(7, null);
    System.out.println("List contents: " + newList.toString());
    System.out.println("Attempting to insertBefore() on null node...");
    newList.insertBefore(8, null);
    System.out.println("List contents: " + newList.toString());
    System.out.println();

    System.out.println("=== Finished Testing DList Methods ===");
  }
}
