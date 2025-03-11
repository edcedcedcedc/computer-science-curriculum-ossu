package projects.archive.LibraryManagementSystem.src.main.java.com.library;

import java.time.LocalDate;

public class Transaction {
    private Member member; // Member who performed the transaction
    private Book book; // Book that was borrowed or returned
    private LocalDate date; // Date of the transaction
    private String type; // Type of transaction: "borrow" or "return"

    public Transaction(Member member, Book book, String type) {
        this.member = member;
        this.book = book;
        this.date = LocalDate.now();
        this.type = type;
    }

    // Getters and Setters
    public Member getMember() {
        return member;
    }

    public Book getBook() {
        return book;
    }

    public LocalDate getDate() {
        return date;
    }

    public String getType() {
        return type;
    }

    // public String toString() {
    // return "Transaction[Member: " + member.getName() + ", Book: " +
    // book.getTitle() + ", Type: " + type + ", Date: "
    // + date + "]";
    // }

}
