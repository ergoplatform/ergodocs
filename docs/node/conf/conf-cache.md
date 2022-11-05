
# cache 

What to keep in memory

## history
### blockSectionsCacheSize
```
blockSectionsCacheSize = 12
```
The number of recently used block sections that will be kept in memory.

### headersCacheSize
```
headersCacheSize = 1000
```
The number of recently used headers that will be kept in memory.
### indexesCacheSize
```
indexesCacheSize = 10000
```
The number of recently used indexes that will be kept in memory.
## network
### invalidModifiersBloomFilterCapacity
```
invalidModifiersBloomFilterCapacity = 10000000
```
The maximum number of invalid modifiers to keep in DeliveryTracker.

### invalidModifiersBloomFilterExpirationRate
```
invalidModifiersBloomFilterExpirationRate = 0.1
```
Non-zero fraction of 1 as a rate of element expiration when capacity is full; the lower, the more gradual expiration.
Example: 0.1 is represented as 10 bloom filters expiring one by one.

### invalidModifiersCacheSize
```
invalidModifiersCacheSize = 10000
```
Maximum number of invalid modifiers to keep in the cache, following modifiers are kept in bloom filters.

### invalidModifiersCacheExpiration
```
invalidModifiersCacheExpiration = 6h
```

Determines how long we keep invalid modifiers in the cache.

## mempool
### invalidModifiersBloomFilterCapacity
```
invalidModifiersBloomFilterCapacity = 10000000
```
Maximum number of invalid modifiers to keep in DeliveryTracker

### invalidModifiersBloomFilterExpirationRate
```
invalidModifiersBloomFilterExpirationRate = 0.1
```
Non-zero fraction of 1 as a rate of element expiration when capacity is full; the lower, the more gradual expiration.
Example: 0.1 is represented as 10 bloom filters expiring one by one.

### invalidModifiersCacheSize
```
invalidModifiersCacheSize = 10000
```
Maximum number of invalid modifiers to keep in the cache, following modifiers are kept in bloom filters.

### invalidModifiersCacheExpiration
```
invalidModifiersCacheExpiration = 6h
```

Determines how long we keep invalid modifiers in the cache.
