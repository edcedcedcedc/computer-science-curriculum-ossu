package projects.archive.LibraryManagementSystem.src.main.java.com.library;

import java.util.Scanner;

public class LibraryManagementSystem {

    public static void main(String[] args) {
        // Initialize Library
        Library library = new Library();

        // Sample data: Adding some books and members
        // Book book1 = new Book("Effective Java", "Joshua Bloch", "12345");
        // Book book2 = new Book("Clean Code", "Robert C. Martin", "67890");
        // Member member1 = new Member("John Doe", "M001");
        // Member member2 = new Member("Jane Smith", "M002");

        // library.addBook(book1);
        // library.addBook(book2);
        // library.addMember(member1);
        // library.addMember(member2);

        // Simulating some transactions (borrows)
        // Transaction transaction1 = new Transaction(member1, book1, "borrow");
        // Transaction transaction2 = new Transaction(member2, book2, "borrow");

        // library.addTransaction(transaction1);
        // library.addTransaction(transaction2);

        // Simulate user input for library operations (e.g., borrowing, returning books)
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nWelcome to the Library Management System!");
            System.out.println("1. View Books");
            System.out.println("2. Borrow Book");
            System.out.println("3. Return Book");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();

            switch (choice) {
            case 1:
                // library.viewBooks();
                break;
            case 2:
                System.out.print("Enter book title to borrow: ");
                scanner.nextLine(); // consume newline
                String borrowTitle = scanner.nextLine();
                // library.borrowBook(member1, borrowTitle);
                break;
            case 3:
                System.out.print("Enter book title to return: ");
                scanner.nextLine(); // consume newline
                String returnTitle = scanner.nextLine();
                // library.returnBook(member1, returnTitle);
                break;
            case 4:
                System.out.println("Exiting...");
                scanner.close();
                return; // Exit the program
            default:
                System.out.println("Invalid option. Please try again.");
            }
        }
    }
}
