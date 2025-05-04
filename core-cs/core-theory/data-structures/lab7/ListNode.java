/* ListNode.java */
package lab7;

/**
 * ListNode is a very simple headless list class, akin to cons cells in Scheme.
 * Each ListNode contains an item and a reference to the next node.
 **/
class ListNode {

  public Object item;
  public ListNode next;

  /**
   * Constructs a ListNode with item i and next node n.
   * 
   * @param i the item to store in the ListNode.
   * @param n the next ListNode following this ListNode.
   **/
  ListNode(Object i, ListNode n) {
    item = i;
    next = n;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("[");
    ListNode current = this;
    while (current != null) {
      sb.append(current.item);
      if (current.next != null) {
        sb.append(", ");
      }
      current = current.next;
    }
    sb.append("]");
    return sb.toString();
  }

}
