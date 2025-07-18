class TimeLimitedCache {
    cache = new Map()
    timeouts = new Map()
    
    constructor() {
    }
    
    set(key: number, value: number, duration: number): boolean {
        const existing = this.cache.get(key)
        const exists = existing !== undefined
        if(exists) {
          clearTimeout(this.timeouts.get(key))
        }
        this.cache.set(key, value)
        this.timeouts.set(key, setTimeout(() => this.cache.delete(key), duration))
        return exists
    }
    
    get(key: number): number {
        const existing = this.cache.get(key)
        if (existing == undefined) {
          return -1
        }
        return existing
    }
    
    count(): number {
        return this.cache.size
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */