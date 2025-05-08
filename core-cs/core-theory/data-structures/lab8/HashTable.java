package lab8;

import java.util.LinkedList;

public class HashTable {
	private static class Entry {
		String key;
		String value;

		Entry(String key, String value) {
			this.key = key;
			this.value = value;
		}

		public String toString() {
			return key + " => " + value;
		}
	}

	private LinkedList<Entry>[] buckets;
	private int size;

	@SuppressWarnings("unchecked")
	public HashTable(int capacity) {
		buckets = new LinkedList[capacity];
		size = 0;
	}

	private int hash(String key) {
		int index = compress(key.hashCode());
		return index;
	}

	/* 0 ≤ remainder < N */
	private int compress(int hashCode) {
		return Math.abs(hashCode) % buckets.length;
	}

	public int length() {
		return size;
	}

	public void put(String key, String value) {
		int index = hash(key);
		if (buckets[index] == null) {
			buckets[index] = new LinkedList<>();
		}

		for (Entry e : buckets[index]) {
			if (e.key.equals(key)) {
				e.value = value;
				return;
			}
		}

		buckets[index].add(new Entry(key, value));
		size++;
	}

	public String remove(String key) {
		int index = hash(key);
		if (buckets[index] == null)
			return null;

		for (Entry e : buckets[index]) {
			if (e.key.equals(key)) {
				buckets[index].remove(e);
				size--;
				return e.value;
			}
		}

		return null;
	}

	public String toString() {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < buckets.length; i++) {
			sb.append(i).append(": ");
			if (buckets[i] != null) {
				for (Entry e : buckets[i]) {
					sb.append(e).append("  ");
				}
			}
			sb.append("\n");
		}
		return sb.toString();
	}

	/*
	 * Use linked list instead of arrays to handle collision because of the dynamic
	 * property
	 */

	public String get(String key) {
		int index = hash(key);
		LinkedList<Entry> bucket = buckets[index];
		if (bucket == null)
			return null;
		for (Entry e : bucket) {
			if (e.key.equals(key)) {
				return e.value;
			}
		}
		return null;
	}

	public static void main(String[] args) {
		HashTable table = new HashTable(10);
		System.out.print("Empty Table:");
		System.out.print('\n');
		System.out.println(table);
		System.out.print("Table with 5 items:");
		System.out.print('\n');
		table.put("hi", "hello");
		table.put("yo", "yo hi");
		table.put("ok", "okay");
		table.put("go", "lets go");
		table.put("hi", "hello 2");
		System.out.println(table);
		System.out.println("Get 'hi': ");
		System.out.print(table.get("hi") + '\n');
		System.out.print('\n');
		table.remove("yo");
		System.out.println("Remove 'yo': ");
		System.out.print(table);
		System.out.print('\n');
		System.out.print("Get Size");
		System.out.print('\n');
		System.out.print(table.length());
		System.out.print('\n');
		System.out.print('\n');
		System.out.print("Testing Collision");
		System.out.print('\n');
		table.put("apple", "green");
		table.put("elppa", "green");
		System.out.print(table);

	}
}
