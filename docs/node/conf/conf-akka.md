
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
```bash
request-timeout = 1 minute
```bash
#### max-connections
```bash
max-connections = 128
```
### parsing
#### max-uri-length
```bash
max-uri-length = 8192
```


