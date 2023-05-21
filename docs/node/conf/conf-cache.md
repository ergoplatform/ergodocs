# Cache Configuration

The `cache` configuration specifies what data to keep in memory to optimize the performance of the system.

## History

### Block Sections Cache Size
```conf
blockSectionsCacheSize = 12
```
The `blockSectionsCacheSize` setting determines the number of recently used block sections that will be kept in memory. In this configuration, the last 12 block sections are stored.

### Headers Cache Size
```conf
headersCacheSize = 1000
```
The `headersCacheSize` setting specifies the number of recently used headers that will be kept in memory. Here, the last 1000 headers are stored.

### Indexes Cache Size
```conf
indexesCacheSize = 10000
```
The `indexesCacheSize` setting determines the number of recently used indexes that will be kept in memory. In this configuration, the last 10000 indexes are stored.

## Network

### Invalid Modifiers Bloom Filter Capacity
```conf
invalidModifiersBloomFilterCapacity = 10000000
```
The `invalidModifiersBloomFilterCapacity` setting specifies the maximum number of invalid modifiers that the DeliveryTracker will keep.

### Invalid Modifiers Bloom Filter Expiration Rate
```conf
invalidModifiersBloomFilterExpirationRate = 0.1
```
The `invalidModifiersBloomFilterExpirationRate` setting defines the rate of element expiration when the capacity is full. It's represented as a non-zero fraction of 1. The lower the number, the more gradual the expiration. In this configuration, a rate of 0.1 is represented as 10 bloom filters expiring one by one.

### Invalid Modifiers Cache Size
```conf
invalidModifiersCacheSize = 10000
```
The `invalidModifiersCacheSize` setting determines the maximum number of invalid modifiers kept in the cache. Any modifiers beyond this number are kept in bloom filters.

### Invalid Modifiers Cache Expiration
```conf
invalidModifiersCacheExpiration = 6h
```
The `invalidModifiersCacheExpiration` setting defines how long invalid modifiers are kept in the cache. In this configuration, they are kept for 6 hours.

## Mempool

The mempool section has the same configuration options as the network section, with the same parameters, but they apply to the mempool rather than the network. In particular, these settings control how many invalid modifiers are kept in memory and how long they are kept before being removed. 

Overall, the cache configuration allows you to manage your memory usage and performance effectively, helping to keep your system running smoothly even under heavy load.