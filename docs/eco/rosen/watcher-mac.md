# Setting up a Watcher on Mac


### Install Script

Download [this file](https://gist.github.com/glasgowm148/9b0aad9bed4684eb234832691a0a6af6) as rosen_install.sh

```bash
chmod +x rosen_install.sh
./rosen_install.sh
```

## Resources

See also the [General Watchers app Tutorials Playlist](https://youtube.com/playlist?list=PLyQeADPK2PWgztdc9lCvAyqjknPaN9woQ&si=SNYxoZMv2iID610o)

## Troubleshooting

### watcher-db-1 error 

ARM mac mini m1 Asahi linux Arch getting watcher-db-1 error upon docker compose up -d

Users are reporting that this issue can be fixed by pruning existing images and rebuilding 

```
docker system prune -a
``` 

as long as you don't have other docker images to worry about.