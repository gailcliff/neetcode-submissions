class Node {
    constructor (val) {
        this.val = val;
        this.next = null;
    }
}

function add(node, key) {
    if (node.next === null) {
        node.next = new Node(key);
        return;
    } 
    
    if (node.next.val === key) {
        return;
    }

    add(node.next, key);
}

function remove(node, key) {
    if (node.next === null) {
        return;
    }
    if (node.next.val === key) {
        node.next = node.next.next;
        return;
    }

    remove(node.next, key);
}

function contains(node, key) {
    if (node.next === null) {
        return false;
    }
    if (node.next.val === key) {
        return true;
    }

    return contains(node.next, key);
}

class MyHashSet {
    constructor() {
        this.bucket = new Array(769).fill(null);
        this.bucketSize = 769;
    }

    hash (key) {
        return key % this.bucketSize;
    }

    /**
     * @param {number} key
     * @return {void}
     */
    add(key) {
        const bucketIdx = key % this.bucketSize;

        if (this.bucket[bucketIdx] === null) {
            this.bucket[bucketIdx] = new Node(null);
        }

        const chain = this.bucket[bucketIdx];

        add(chain, key);
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        const bucketIdx = key % this.bucketSize;
        const chain = this.bucket[bucketIdx];

        if (chain) {
            remove(chain, key);
        }
    }

    /**
     * @param {number} key
     * @return {boolean}
     */
    contains(key) {
        const bucketIdx = key % this.bucketSize;
        const chain = this.bucket[bucketIdx];

        if (!chain) {
            return false;
        }

        return contains(chain, key);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
