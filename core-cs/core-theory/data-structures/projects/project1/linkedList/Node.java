package linkedList;

public class Node {

    Object item;
    Node next;

    Node(Object item) {
        this.item = item;
        this.next = null;
    }

    Node(Object item, Node next) {
        this.item = item;
        this.next = next;
    }

}
