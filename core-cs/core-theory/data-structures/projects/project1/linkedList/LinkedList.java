package linkedList;

public class LinkedList {
    private Node head;
    private Node tail;
    private int size;

    LinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public int length() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void insertFront(Object item) {
        if (head == null && tail == null) {
            head = new Node(item);
            tail = head;
        } else {
            head = new Node(item, head);
        }
        size++;
    }

    /*
     * A->B->C
     */
    public void insertEnd(Object item) {
        if (head == null && tail == null) {
            tail = new Node(item);
            head = tail;
        } else {
            tail.next = new Node(item);
            tail = tail.next;
        }
        size++;
    }

    public Object nth(int position) {
        Node currentNode;
        if (position < 1 || head == null) {
            return null;
        } else {
            currentNode = head;
            while (position > 1) {
                currentNode = currentNode.next;
                if (currentNode == null) {
                    return null;
                }
                position--;
            }
            return currentNode.item;
        }

    }

    @Override
    public String toString() {
        String result = "";
        while (head != null) {
            result += " " + head.item.toString() + " ";
            head = head.next;
        }
        return "[" + " " + result + " " + "]";
    }

    public static void main(String[] param) {
        LinkedList a = new LinkedList();
        a.insertFront(1);
        a.insertFront(2);
        a.insertEnd(3);
        a.insertEnd(4);
        System.out.print(a.nth(1));
    }
}
