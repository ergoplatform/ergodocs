
## akka 

## actor.mailbox.requirements
## http
```
http {
    server {
      request-timeout = 1 minute
      max-connections = 128
    }
    parsing {
      max-uri-length = 8192
    }
  }
```
### server
#### request-timeout
```
request-timeout = 1 minute
```
#### max-connections
```
max-connections = 128
```
### parsing
#### max-uri-length
```
max-uri-length = 8192
```


