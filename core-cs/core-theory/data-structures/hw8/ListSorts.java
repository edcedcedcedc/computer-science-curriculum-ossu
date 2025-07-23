/* ListSorts.java */

package hw8;

import hw8.list.LinkedQueue;
import hw8.list.QueueEmptyException;

public class ListSorts {

  private final static int SORTSIZE = 1000;

  /**
   * makeQueueOfQueues() makes a queue of queues, each containing one item of q.
   * Upon completion of this method, q is empty.
   * 
   * @param q is a LinkedQueue of objects.
   * @return a LinkedQueue containing LinkedQueue objects, each of which contains
   *         one object from q.
   **/
  public static LinkedQueue makeQueueOfQueues(LinkedQueue q) {
    LinkedQueue result = new LinkedQueue();

    try {
      while (!q.isEmpty()) {
        Object item = q.dequeue(); // <-- remove an item from q

        // Step 2: Create a new queue that holds only this item
        LinkedQueue singleItemQueue = new LinkedQueue();
        singleItemQueue.enqueue(item); // <-- add item to the small queue

        // Step 3: Enqueue this single-item queue into the result queue
        result.enqueue(singleItemQueue); // <-- add the single queue to result
      }
    } catch (QueueEmptyException e) {
      System.err.println("Bug: tried to dequeue from an empty queue.");
    }

    return result;
  }

  /**
   * mergeSortedQueues() merges two sorted queues into a third. On completion of
   * this method, q1 and q2 are empty, and their items have been merged into the
   * returned queue.
   * 
   * @param q1 is LinkedQueue of Comparable objects, sorted from smallest to
   *           largest.
   * @param q2 is LinkedQueue of Comparable objects, sorted from smallest to
   *           largest.
   * @return a LinkedQueue containing all the Comparable objects from q1 and q2
   *         (and nothing else), sorted from smallest to largest.
   **/
  public static LinkedQueue mergeSortedQueues(LinkedQueue q1, LinkedQueue q2) {
    LinkedQueue result = new LinkedQueue();

    try {
      while (!q1.isEmpty() && !q2.isEmpty()) {
        Comparable item1 = (Comparable) q1.front();
        Comparable item2 = (Comparable) q2.front();

        if (item1.compareTo(item2) <= 0) {
          result.enqueue(q1.dequeue()); // <-- remove from q1 and add to result
        } else {
          result.enqueue(q2.dequeue()); // <-- remove from q2 and add to result
        }
      }

      // Now one of the queues is empty — empty the other
      while (!q1.isEmpty()) {
        result.enqueue(q1.dequeue()); // <-- what goes here?
      }

      while (!q2.isEmpty()) {
        result.enqueue(q2.dequeue()); // <-- and here?
      }
    } catch (QueueEmptyException e) {
      System.err.println("Bug: tried to dequeue from an empty queue.");
    }

    return result;
  }

  /**
   * partition() partitions qIn using the pivot item. On completion of this
   * method, qIn is empty, and its items have been moved to qSmall, qEquals, and
   * qLarge, according to their relationship to the pivot.
   * 
   * @param qIn     is a LinkedQueue of Comparable objects.
   * @param pivot   is a Comparable item used for partitioning.
   * @param qSmall  is a LinkedQueue, in which all items less than pivot will be
   *                enqueued.
   * @param qEquals is a LinkedQueue, in which all items equal to the pivot will
   *                be enqueued.
   * @param qLarge  is a LinkedQueue, in which all items greater than pivot will
   *                be enqueued.
   **/
  public static void partition(LinkedQueue qIn, Comparable pivot, LinkedQueue qSmall, LinkedQueue qEquals,
      LinkedQueue qLarge) {
    try {
      while (!qIn.isEmpty()) {
        Comparable item = (Comparable) qIn.dequeue();

        int cmp = item.compareTo(pivot);

        if (cmp < 0) {
          qSmall.enqueue(item);
        } else if (cmp == 0) {
          qEquals.enqueue(item);
        } else {
          qLarge.enqueue(item);
        }
      }
    } catch (QueueEmptyException e) {
      System.err.println("Bug: tried to dequeue from empty queue in partition().");
    }
  }

  /**
   * mergeSort() sorts q from smallest to largest using mergesort.
   * 
   * @param q is a LinkedQueue of Comparable objects.
   **/
  public static void mergeSort(LinkedQueue q) {
    if (q.size() <= 1) {
      return;
    }
    LinkedQueue queueOfQueues = makeQueueOfQueues(q);

    try {
      while (queueOfQueues.size() > 1) {
        LinkedQueue q1 = (LinkedQueue) queueOfQueues.dequeue();
        LinkedQueue q2 = (LinkedQueue) queueOfQueues.dequeue();

        LinkedQueue merged = mergeSortedQueues(q1, q2);

        queueOfQueues.enqueue(merged);
      }

      LinkedQueue sorted = (LinkedQueue) queueOfQueues.dequeue();
      q.append(sorted);

    } catch (QueueEmptyException e) {
      System.err.println("Unexpected empty queue during mergeSort.");
    }
  }

  /**
   * quickSort() sorts q from smallest to largest using quicksort.
   * 
   * @param q is a LinkedQueue of Comparable objects.
   **/
  public static void quickSort(LinkedQueue q) {
    if (q.size() <= 1) {
      return;
    }

    int pivotIndex = (int) (Math.random() * q.size()) + 1;
    Comparable pivot = (Comparable) q.nth(pivotIndex);

    LinkedQueue qSmall = new LinkedQueue();
    LinkedQueue qEquals = new LinkedQueue();
    LinkedQueue qLarge = new LinkedQueue();

    partition(q, pivot, qSmall, qEquals, qLarge);

    quickSort(qSmall);
    quickSort(qLarge);

    q.append(qSmall);
    q.append(qEquals);
    q.append(qLarge);
  }

  /**
   * makeRandom() builds a LinkedQueue of the indicated size containing Integer
   * items. The items are randomly chosen between 0 and size - 1.
   * 
   * @param size is the size of the resulting LinkedQueue.
   **/
  public static LinkedQueue makeRandom(int size) {
    LinkedQueue q = new LinkedQueue();
    for (int i = 0; i < size; i++) {
      q.enqueue((int) (size * Math.random()));
    }
    return q;
  }

  /**
   * main() performs some tests on mergesort and quicksort. Feel free to add more
   * tests of your own to make sure your algorithms works on boundary cases. Your
   * test code will not be graded.
   **/
  public static void main(String[] args) {

    LinkedQueue q = makeRandom(10);
    System.out.println(q.toString());
    mergeSort(q);
    System.out.println(q.toString());

    q = makeRandom(10);
    System.out.println(q.toString());
    quickSort(q);
    System.out.println(q.toString());

    // Remove these comments for Part III. Timer stopWatch = new Timer(); q =
    int SORTSIZE = 1;

    for (int i = 0; i <= 5; i++) {
      SORTSIZE *= 10;
      makeRandom(SORTSIZE);
      Timer stopWatch = new Timer();
      stopWatch.start();
      mergeSort(q);
      stopWatch.stop();
      System.out.println("\n");
      System.out.println("Mergesort time, " + SORTSIZE + " Integers:  " + stopWatch.elapsed() + " msec.");

      stopWatch.reset();
      q = makeRandom(SORTSIZE);
      stopWatch.start();
      quickSort(q);
      stopWatch.stop();
      System.out.println("Quicksort time, " + SORTSIZE + " Integers:  " + stopWatch.elapsed() + " msec.");

    }

  }

}
