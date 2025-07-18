class TimeLimitedCache {
    cache = {}
    timeouts = {}
    
    constructor() {
        this.cache = {}
        this.timeouts = {}
    }
    
    set(key: number, value: number, duration: number): boolean {
        const existing = this.cache[key]
        const exists = this.cache[key] !== undefined
        if(exists) {
          clearTimeout(this.timeouts[key])
        }
        this.cache[key] = value
        this.timeouts[key] = setTimeout(() => delete this.cache[key], duration)
        return exists
    }
    
    get(key: number): number {
        const existing = this.cache[key]
        if (existing == undefined) {
          return -1
        }
        return existing
    }
    
    count(): number {
        return Object.keys(this.cache).length
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */