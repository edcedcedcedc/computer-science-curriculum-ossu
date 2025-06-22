/* SibTreeNode.java */

package lab10.tree;

/**
 * A SibTreeNode object is a node in a SibTree (sibling-based general tree).
 * 
 * @author Jonathan Shewchuk
 */

class SibTreeNode extends TreeNode {

  /**
   * (inherited) item references the item stored in this node.
   * 
   * (inherited) valid is true if and only if this is a valid node in some Tree.
   * 
   * myTree references the Tree that contains this node. parent references this
   * node's parent node.
   * 
   * firstChild references this node's first (leftmost) child.
   * 
   * nextSibling references this node's next sibling.
   *
   * DO NOT CHANGE THE FOLLOWING FIELD DECLARATIONS.
   */

  /**
   * ADT implementation invariants:
   * 
   * 1) if valid == true, myTree != null.
   * 
   * 2) if valid == true, then this is a descendent of myTree.root.
   * 
   * 3) if valid == true, myTree satisfies all the invariants of a SibTree (listed
   * in SibTree.java).
   */

  protected SibTree myTree;
  protected SibTreeNode parent;
  protected SibTreeNode firstChild;
  protected SibTreeNode nextSibling;

  /**
   * Construct a valid SibTreeNode referring to a given item.
   */
  SibTreeNode(SibTree tree, Object item) {
    this.item = item;
    valid = true;
    myTree = tree;
    parent = null;
    firstChild = null;
    nextSibling = null;
  }

  /**
   * Construct an invalid SibTreeNode.
   */
  SibTreeNode() {
    valid = false;
  }

  /**
   * children() returns the number of children of the node at this position.
   * WARNING: Does not run in constant time. Actually counts the kids.
   */
  public int children() {
    if (isValidNode()) {
      int count = 0;
      SibTreeNode countNode = firstChild;
      while (countNode != null) {
        count++;
        countNode = countNode.nextSibling;
      }
      return count;
    } else {
      return 0;
    }
  }

  /**
   * parent() returns the parent TreeNode of this TreeNode.
   * 
   * Throws an exception if `this' is not a valid node.
   * 
   * Returns an invalid TreeNode if this node is the root.
   */
  public TreeNode parent() throws InvalidNodeException {
    if (!isValidNode())
      throw new InvalidNodeException();
    if (parent == null)
      return new SibTreeNode();
    return parent;
  }

  /**
   * child() returns the cth child of this TreeNode. Throws an exception if `this'
   * is not a valid node. Returns an invalid TreeNode if there is no cth child.
   */
  public TreeNode child(int c) throws InvalidNodeException {
    if (isValidNode()) {
      if (c < 1) {
        return new SibTreeNode();
      }
      SibTreeNode kid = firstChild;
      while ((kid != null) && (c > 1)) {
        kid = kid.nextSibling;
        c--;
      }
      if (kid == null) {
        return new SibTreeNode();
      } else {
        return kid;
      }
    } else {
      throw new InvalidNodeException();
    }
  }

  /**
   * nextSibling() returns the next sibling TreeNode to the right from this
   * TreeNode. Throws an exception if `this' is not a valid node. Returns an
   * invalid TreeNode if there is no sibling to the right of this node.
   */
  public TreeNode nextSibling() throws InvalidNodeException {
    if (isValidNode()) {
      if (nextSibling == null) {
        return new SibTreeNode();
      } else {
        return nextSibling;
      }
    } else {
      throw new InvalidNodeException();
    }
  }

  /**
   * insertChild() inserts an item as the cth child of this node.
   * 
   * Existing children numbered c or higher are shifted one place to the right to
   * accommodate.
   * 
   * If the current node has fewer than c children, the new item is inserted as
   * the last child.
   * 
   * If c < 1, act as if c is 1.
   *
   * Throws an InvalidNodeException if "this" node is invalid.
   * 
   * 
   * understanding:
   * 
   * this.firstChild -> B -> C -> D -> E -> F (the structure)
   * 
   * insert at c = 2 -> implies I have to insert at c - 1, so it will be 2 to
   * insert I need a previous pointer a current pointer and position (what does it
   * mean to insert)
   * 
   * edge cases: insert at 1 and insert at inf
   * 
   * 
   */
  public void insertChild(Object item, int c) throws InvalidNodeException {
    SibTreeNode prev = null;
    SibTreeNode current = this.firstChild;
    int position = 1;

    if (!isValidNode()) {
      throw new InvalidNodeException();
    }

    while (position < c && current != null) {
      prev = current;
      current = current.nextSibling;
      position++;
    }

    SibTreeNode newNode = new SibTreeNode(myTree, item);
    newNode.nextSibling = current;
    newNode.parent = this;

    if (prev == null) {
      this.firstChild = newNode;
    } else {
      prev.nextSibling = newNode;
    }

    myTree.size++;

  }

  /**
   * removeLeaf() removes the node at the current position from the tree if it is
   * a leaf.
   * 
   * Does nothing if `this' has one or more children.
   * 
   * Throws an exception if `this' is not a valid node.
   * 
   * If 'this' has siblings to its right, those siblings are all shifted left by
   * one.
   * 
   * understanding:
   * 
   * Find yourself in your parent’s list of children, and if you have no children
   * of your own, disconnect yourself from that list and mark yourself invalid.
   * 
   * 
   * a leaf node is a node that has no children
   * 
   * Parent |
   * 
   * -------v
   * 
   * -------Child1 -> Child2 (this node) -> Child3 -> null
   * 
   * 
   * 
   */
  public void removeLeaf() throws InvalidNodeException {
    if (!isValidNode())
      throw new InvalidNodeException();

    if (this.firstChild != null) // not a leaf node at start
      return;

    if (this.parent == null) {
      this.valid = false;
      this.myTree.size--;
      return;
    }

    SibTreeNode current = this.parent.firstChild;
    SibTreeNode prev = null;

    while (current != null) {
      if (current == this) {
        if (prev == null) {
          parent.firstChild = current.nextSibling;
        } else {
          prev.nextSibling = current.nextSibling;
        }
        current.valid = false;
        myTree.size--;
        break;
      } else {
        prev = current;
        current = current.nextSibling;
      }
    }
  }

}
