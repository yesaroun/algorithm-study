class Node {
  next = null;
  constructor(value) {
    this.value = value;
  }
}

class LinkedList {
  length = 0;
  head = null;

  add(value) {
    if (this.head) {
      let current = this.head;
      while (current.next) {
        current = current.next;
      }
      current.next = new Node(value);
    } else {
      this.head = new Node(value);
    }
    this.length++;
    return this.length;
  }

  search(index) {
    return this.#search(index)[1]?.value;
  }

  #search(index) {
    let count = 0;
    let prev;
    let current = this.head;
    while (count < index) {
      prev = current;
      current = current?.next;
      count++;
    }
    return [prev, current];
  }

  remove(index) {
    const [prev, current] = this.#search(index);

    if (current) {
      if (prev) {
        prev.next = current.next;
      } else {
        this.head = current.next;
      }
      this.length--;
      return this.length;
    }
  }
}

class Stack {
  linkedList = new LinkedList();

  push(value) {
    return this.linkedList.add(value);
  }

  top() {
    return this.linkedList.search(this.linkedList.length - 1);
  }

  pop() {
    return this.linkedList.remove(this.linkedList.length - 1);
  }
}

const stack = new Stack();
stack.push(100);
stack.top();
stack.pop();
