/* HashTableChained.java */

package hw6.dict;

/**
 * HashTableChained implements a Dictionary as a hash table with chaining. All
 * objects used as keys must have a valid hashCode() method, which is used to
 * determine which bucket of the hash table an entry is stored in. Each object's
 * hashCode() is presumed to return an int between Integer.MIN_VALUE and
 * Integer.MAX_VALUE. The HashTableChained class implements only the compression
 * function, which maps the hash code to a bucket in the table's range.
 *
 * DO NOT CHANGE ANY PROTOTYPES IN THIS FILE.
 **/

import hw5.list.DList;
import hw5.list.DListNode;
import hw5.list.InvalidNodeException;

public class HashTableChained implements Dictionary {

  private int size;
  protected DList[] buckets;

  /**
   * Place any data fields here.
   **/

  /**
   * Construct a new empty hash table intended to hold roughly sizeEstimate
   * entries. (The precise number of buckets is up to you, but we recommend you
   * use a prime number, and shoot for a load factor between 0.5 and 1.)
   **/

  public HashTableChained(int sizeEstimate) {
    this.buckets = new DList[sizeEstimate];

    for (int i = 0; i <= this.buckets.length - 1; i++) {
      this.buckets[i] = new DList();
    }

    this.size = 0;
  }

  /**
   * Construct a new empty hash table with a default size. Say, a prime in the
   * neighborhood of 100.
   **/

  public HashTableChained() {
    // Your solution here.
  }

  /**
   * Converts a hash code in the range Integer.MIN_VALUE...Integer.MAX_VALUE to a
   * value in the range 0...(size of hash table) - 1.
   *
   * This function should have package protection (so we can test it), and should
   * be used by insert, find, and remove.
   **/

  int hash(Object key) {
    int index = compFunction(key.hashCode());
    return index;
  }

  int compFunction(int code) {
    return Math.abs(code) % buckets.length;
  }

  /**
   * Returns the number of entries stored in the dictionary. Entries with the same
   * key (or even the same key and value) each still count as a separate entry.
   * 
   * @return number of entries in the dictionary.
   **/

  public int size() {
    // Replace the following line with your solution.
    return this.size;
  }

  /**
   * Tests if the dictionary is empty.
   *
   * @return true if the dictionary has no entries; false otherwise.
   **/

  public boolean isEmpty() {
    // Replace the following line with your solution.
    return size == 0;
  }

  /**
   * Create a new Entry object referencing the input key and associated value, and
   * insert the entry into the dictionary. Return a reference to the new entry.
   * Multiple entries with the same key (or even the same key and value) can
   * coexist in the dictionary.
   *
   * This method should run in O(1) time if the number of collisions is small.
   *
   * @param key   the key by which the entry can be retrieved.
   * @param value an arbitrary object.
   * @return an entry containing the key and value.
   **/

  public Entry insert(Object key, Object value) {
    Entry entry = new Entry();
    entry.key = key;
    entry.value = value;
    int index = hash(key);
    buckets[index].insertBack(entry);
    size++;
    return entry;
  }

  /**
   * Searches for a node in the hash table's bucket list that contains the
   * specified key.
   *
   * @param the key to search for in the hash table.
   * @return the node containing the entry with the specified key, or null if not
   *         found.
   * @throws InvalidNodeException if an invalid node is encountered during
   *                              traversal.
   */
  public DListNode findNode(Object key) throws InvalidNodeException {
    int index = hash(key);
    DList bucket = buckets[index];
    DListNode node = (DListNode) bucket.front();
    while (node.isValidNode()) {
      Entry entry = (Entry) node.item();
      if (entry.key.equals(key)) {
        return node;
      }
      node = (DListNode) node.next();
    }
    return null;
  }

  /**
   * Search for an entry with the specified key. If such an entry is found, return
   * it; otherwise return null. If several entries have the specified key, choose
   * one arbitrarily and return it.
   *
   * This method should run in O(1) time if the number of collisions is small.
   *
   * @param key the search key.
   * @return an entry containing the key and an associated value, or null if no
   *         entry contains the specified key.
   * @throws InvalidNodeException
   **/

  public Entry find(Object key) throws InvalidNodeException {
    DListNode node = findNode(key);
    if (node != null) {
      Entry entry = (Entry) node.item();
      return entry;
    } else {
      return null;
    }
  }

  /**
   * Remove an entry with the specified key. If such an entry is found, remove it
   * from the table and return it; otherwise return null. If several entries have
   * the specified key, choose one arbitrarily, then remove and return it.
   *
   * This method should run in O(1) time if the number of collisions is small.
   *
   * @param key the search key.
   * @return an entry containing the key and an associated value, or null if no
   *         entry contains the specified key.
   */

  public Entry remove(Object key) throws InvalidNodeException {
    DListNode node = findNode(key);
    if (node != null) {
      Entry entry = (Entry) node.item();
      node.remove();
      size--;
      return entry;
    } else {
      return null;
    }
  }

  /**
   * Remove all entries from the dictionary.
   */
  public void makeEmpty() throws InvalidNodeException {
    for (int i = 0; i <= buckets.length - 1; i++) {
      DList bucket = buckets[i];
      DListNode node = (DListNode) bucket.front();
      while (node.isValidNode()) {
        DListNode current = node;
        current = (DListNode) current.next();
        node.remove();
        node = current;
        size--;
      }
    }
  }

  public static void main(String[] args) throws InvalidNodeException {
    HashTableChained table = new HashTableChained(7); // small prime for easy testing

    System.out.println("Is empty? " + table.isEmpty()); // true
    table.insert("foo", 42);
    table.insert("bar", 99);
    table.insert("baz", 123);

    System.out.println("Size: " + table.size()); // 3
    System.out.println("Find foo: " + table.find("foo") + " " + "Should be: Entry(foo, 42)"); // should print Entry with
                                                                                              // key "foo"
    System.out.println("Find bar: " + table.find("bar") + " " + "Should be: Entry(bar, 99)"); // should print Entry with
                                                                                              // key "bar"
    System.out.println("Find missing: " + table.find("missing") + " " + "Should be null"); // null

    System.out.println("Remove foo: " + table.remove("foo")); // should print Entry with key "foo"
    System.out.println("Size after remove: " + table.size()); // 2

    table.makeEmpty();
    System.out.println("Is empty after makeEmpty? " + table.isEmpty()); // true
  }

}
