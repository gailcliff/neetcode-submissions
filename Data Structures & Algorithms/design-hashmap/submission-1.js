class Node {
    constructor (key, value) {
        this.key = key;
        this.value = value;
        this.next = null;
    }
}
class MyHashMap {
    constructor() {
        this.bucket = new Array(769).fill(new Node(null, null));
        this.bucketSize = 769;
    }

    hash (key) {
        return key % this.bucketSize;
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        const bucketIdx = this.hash(key);
        let curr = this.bucket[bucketIdx];

        while (curr.next) {
            if (curr.next.key === key) {
                curr.next.value = value;
                return;
            }
            curr = curr.next;
        }
        curr.next = new Node(key, value);
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        const bucketIdx = this.hash(key);
        
        let curr = this.bucket[bucketIdx];

        while (curr.next) {
            if (curr.next.key === key) {
                return curr.next.value;
            }
            curr = curr.next;
        }
        
        return -1;
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        const bucketIdx = this.hash(key);

        let curr = this.bucket[bucketIdx];

        while (curr.next) {
            if (curr.next.key === key) {
                curr.next = curr.next.next;
                break;
            }
            curr = curr.next;
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
