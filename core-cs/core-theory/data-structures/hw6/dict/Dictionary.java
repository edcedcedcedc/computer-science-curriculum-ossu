/* Dictionary.java */

package hw6.dict;

import hw5.list.DListNode;
import hw5.list.InvalidNodeException;

/**
 * An interface for (unordered) dictionary ADTs.
 *
 * DO NOT CHANGE THIS FILE.
 **/

public interface Dictionary {

  /**
   * Returns the number of entries stored in the dictionary. Entries with the same
   * key (or even the same key and value) each still count as a separate entry.
   * 
   * @return number of entries in the dictionary.
   **/

  public int size();

  /**
   * Tests if the dictionary is empty.
   *
   * @return true if the dictionary has no entries; false otherwise.
   **/

  public boolean isEmpty();

  /**
   * Create a new Entry object referencing the input key and associated value, and
   * insert the entry into the dictionary. Return a reference to the new entry.
   * Multiple entries with the same key (or even the same key and value) can
   * coexist in the dictionary.
   *
   * @param key   the key by which the entry can be retrieved.
   * @param value an arbitrary object.
   * @return an entry containing the key and value.
   **/

  public Entry insert(Object key, Object value);

  /**
   * Search for an entry with the specified key. If such an entry is found, return
   * it; otherwise return null. If several entries have the specified key, choose
   * one arbitrarily and return it.
   *
   * @param key the search key.
   * @return an entry containing the key and an associated value, or null if no
   *         entry contains the specified key.
   * @throws InvalidNodeException
   **/

  /**
   * Searches for and returns the DListNode associated with the specified key.
   *
   * @param key the key whose associated node is to be found
   * @return the DListNode containing the specified key, or null if not found
   * @throws InvalidNodeException if the node is invalid or the operation cannot
   *                              be completed
   */
  public DListNode findNode(Object key) throws InvalidNodeException;

  public Entry find(Object key) throws InvalidNodeException;

  /**
   * Remove an entry with the specified key. If such an entry is found, remove it
   * from the table and return it; otherwise return null. If several entries have
   * the specified key, choose one arbitrarily, then remove and return it.
   *
   * @param key the search key.
   * @return an entry containing the key and an associated value, or null if no
   *         entry contains the specified key.
   */

  public Entry remove(Object key) throws InvalidNodeException;

  /**
   * Remove all entries from the dictionary.
   */

  public void makeEmpty() throws InvalidNodeException;

  public int[] getBucketSizes();
}
