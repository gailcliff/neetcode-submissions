class MyHashSet {
    constructor() {
        this.bucket = new Array(769);
        this.bucketSize = 769;
    }

    /**
     * @param {number} key
     * @return {void}
     */
    add(key) {
        const bucketIdx = key % this.bucketSize;

        if (this.bucket[bucketIdx]) {
            const keyIdx = this.bucket[bucketIdx].indexOf(key);

            if (keyIdx === -1) {
                this.bucket[bucketIdx].push(key);
            }
        } else {
            this.bucket[bucketIdx] = [key];
        }
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        const bucketIdx = key % this.bucketSize;

        if (this.bucket[bucketIdx]) {
            const keyIdx = this.bucket[bucketIdx].indexOf(key);

            if (keyIdx !== -1) {
                this.bucket[bucketIdx].splice(keyIdx, 1);
            }
        }
    }

    /**
     * @param {number} key
     * @return {boolean}
     */
    contains(key) {
        const bucketIdx = key % this.bucketSize;

        if (this.bucket[bucketIdx]) {
            const keyIdx = this.bucket[bucketIdx].indexOf(key);

            return keyIdx !== -1;                
        } else {
            return false;
        }
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
