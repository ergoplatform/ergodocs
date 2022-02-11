
Some




## Run

```
java -jar -Xmx4G ergo.jar --mainnet -c ergo.conf

## Run with INFO logs suppressed
java -jar -Xmx8G -Dlogback.stdout.level=WARN -Dlogback.file.level=ERR ergo.jar --mainnet -c mainnet.conf

## Pipe output to a log file instead of the terminal
java -jar -Xmx4G ergo.jar --mainnet -c ergo.conf > new.log 2>&1 & 
```
The `-Xmx4G` flag specifies the amount of memory you want to allocate to the JVM Heap. 4 GB is recommended even if you can allocate more.  


## Troubleshooting


On OSX, this script will restart every `x` seconds - this seems to help with sync for those getting stuck at the end.
```
watch -n 6000  ./reset.sh
```

### Log

Some `grep` commands to search the logs. Pipe these into files by appending the `> output.log`

```
tail -Fn+0 ergo.log | grep 'height'
```

```
tail -Fn+0 ergo.log | grep 'ERROR\|WARN'
```

```
echo "$(tail -n 5000 server.log)" > server.log
```
echo "$(tail -Fn+0 ergo.log | grep 'ERROR')" > new.log


This will show the surrounding lines from the `Invalid z bytes` error.

```
cat ergo.log | grep -A 30 -B 30 "Invalid z bytes"
```


### Kill 

safe kill the process

```
curl -X POST "http://127.0.0.1:9053/node/shutdown" -H "api_key: hello"
```

```
kill -9 $(lsof -t -i:9053)
kill -9 $(lsof -t -i:9030)
```


