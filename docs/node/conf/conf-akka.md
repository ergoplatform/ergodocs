
## akka 

## actor.mailbox.requirements
## http
```conf
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
```conf
request-timeout = 1 minute
```conf
#### max-connections
```conf
max-connections = 128
```
### parsing
#### max-uri-length
```conf
max-uri-length = 8192
```


