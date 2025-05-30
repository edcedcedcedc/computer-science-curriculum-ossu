/*  VirtualTeller.java */
package lab6;

import java.io.IOException;

import lab6.sortedlist.SortedList;

/**
 * An implementation of a virtual automated teller machine.
 **/
public class VirtualTeller {
  private static int nextAccountID = 100;
  private SortedList accounts;

  /**
   * Constructs a new virtual teller.
   **/
  public VirtualTeller() {
    accounts = new SortedList();
  }

  /**
   * openAccount() creates a new account for the customer "name".
   * 
   * @param name the customer's name.
   * @return the new account's ID number.
   **/
  public int openAccount(String name) {
    AccountData newData = new AccountData(name, nextAccountID);
    accounts.insert(newData);

    nextAccountID++;
    return newData.getNumber();
  }

  /**
   * withdraw() withdraws "amount" dollars from the account whose number is
   * "acct". Assumes that amount >= 0. If "acct" is invalid, no action is taken.
   * 
   * @param acct   is an account number.
   * @param amount an amount of money.
   */
  public void withdraw(int acct, int amount) throws IOException, BadAccountException, BadTransactionException {
    AccountData account = findAccount(acct);
    account.withdraw(amount);
  }

  /**
   * deposit() deposits "amount" dollars into the bank account whose number is
   * "acct". Assumes that amount >= 0. If "acct" is invalid, no action is taken.
   * 
   * @param acct   is an account number.
   * @param amount an amount of money.
   */
  public void deposit(int acct, int amount) throws BadAccountException, BadTransactionException {
    AccountData account = findAccount(acct);
    account.deposit(amount);
  }

  /**
   * balanceInquiry() finds the balance on the account whose number is "acct". If
   * "acct" is an invalid number, returns -1.
   * 
   * @param acct an account number.
   * @return the balance, or -1 if the account number is invalid.
   */
  public int balanceInquiry(int acct) throws IOException, BadAccountException {
    AccountData account = findAccount(acct);
    return account.getBalance();

  }

  /**
   * findAccount() gets the AccountData object associated with account number
   * "acct". If "acct" does not refer to a valid account, returns null.
   * 
   * @param acct is an account number.
   * @return the AccountData object associated with the account number.
   */
  public AccountData findAccount(int acct) throws BadAccountException {
    AccountData account = (AccountData) accounts.find(acct);
    if (account == null) {
      throw new BadAccountException(acct);
    }
    return account;
  }
}
