package hw6;

import hw6.dict.HashTableChained;
import hw6.dict.Entry;
import hw5.list.InvalidNodeException;

public class Homework6TestExtended {

  // Generate a random 8x8 SimpleBoard with values in [0..2]
  private static SimpleBoard randomBoard() {
    SimpleBoard board = new SimpleBoard();
    for (int y = 0; y < 8; y++) {
      for (int x = 0; x < 8; x++) {
        int value = (int) (Math.random() * 12); // from your code, mod 3 applied internally
        board.setElementAt(x, y, value);
      }
    }
    return board;
  }

  // Insert numBoards random boards into the table with distinct values
  private static void initTable(HashTableChained table, int numBoards) throws InvalidNodeException {
    table.makeEmpty();
    for (int i = 0; i < numBoards; i++) {
      SimpleBoard b = randomBoard();
      table.insert(b, i);
    }
  }

  // Test insert and find functionality
  private static void testInsertFind() throws InvalidNodeException {
    System.out.println("Testing insert and find...");
    HashTableChained table = new HashTableChained(200);
    table.makeEmpty();

    SimpleBoard b1 = new SimpleBoard();
    b1.setElementAt(0, 0, 1);
    b1.setElementAt(7, 7, 2);

    table.insert(b1, "BoardOne");

    Entry found = table.find(b1);
    assert found != null : "find() failed to find inserted board";
    assert found.value().equals("BoardOne") : "Value mismatch";

    SimpleBoard b2 = new SimpleBoard();
    b2.setElementAt(0, 0, 2); // different board
    Entry notFound = table.find(b2);
    assert notFound == null : "find() should return null for non-existing key";

    System.out.println("Insert/find tests passed.");
  }

  // Test remove functionality
  private static void testRemove() throws InvalidNodeException {
    System.out.println("Testing remove...");
    HashTableChained table = new HashTableChained(100);
    table.makeEmpty();

    SimpleBoard b = new SimpleBoard();
    b.setElementAt(4, 4, 1);
    table.insert(b, "ToRemove");

    Entry found = table.find(b);
    assert found != null : "Entry should exist before removal";

    Entry removed = table.remove(b);
    assert removed != null : "Remove should return the removed entry";

    Entry foundAfter = table.find(b);
    assert foundAfter == null : "Entry should no longer be found after removal";

    System.out.println("Remove tests passed.");
  }

  // Test size and isEmpty methods
  private static void testSizeIsEmpty() throws InvalidNodeException {
    System.out.println("Testing size() and isEmpty()...");

    HashTableChained table = new HashTableChained(50);
    assert table.isEmpty() : "Table should be empty initially";
    assert table.size() == 0 : "Initial size should be 0";

    table.insert(new SimpleBoard(), 1);
    assert !table.isEmpty() : "Table should not be empty after insert";
    assert table.size() == 1 : "Size should be 1 after one insert";

    table.makeEmpty();
    assert table.isEmpty() : "Table should be empty after makeEmpty";
    assert table.size() == 0 : "Size should be 0 after makeEmpty";

    System.out.println("Size/isEmpty tests passed.");
  }

  // Optional: Test distribution of entries per bucket to detect collisions
  // This requires a method in HashTableChained to get bucket sizes, which
  // you should add for debugging purposes.
  private static void testDistribution() throws InvalidNodeException {
    System.out.println("Testing distribution of entries in buckets...");

    int numBoards = 1000;
    HashTableChained table = new HashTableChained(numBoards / 2);
    table.makeEmpty();

    initTable(table, numBoards);

    int[] bucketSizes = table.getBucketSizes(); // You need to implement this method
    int maxSize = 0;
    int sum = 0;
    for (int size : bucketSizes) {
      if (size > maxSize)
        maxSize = size;
      sum += size;
    }

    System.out.println("Number of buckets: " + bucketSizes.length);
    System.out.println("Total entries: " + sum);
    System.out.println("Max entries in any bucket: " + maxSize);

    // Could add histogram printing here if desired

    System.out.println("Distribution test complete.");
  }

  public static void main(String[] args) throws InvalidNodeException {
    testInsertFind();
    testRemove();
    testSizeIsEmpty();

    // Uncomment if you add the method getBucketSizes() in HashTableChained
    testDistribution();

    System.out.println("All tests completed.");
  }
}
