---
tags:
  - Deploy
  - Operations
  - Reverse Proxy
  - API
owner: docs
last_reviewed: 2026-05-27
source_repos:
  - repo: ergoplatform/ergo
    branch: master
    paths:
      - src/main/resources/application.conf
source_of_truth:
  - https://github.com/ergoplatform/ergo/tree/master/src/main/resources/application.conf
---

# Reverse Proxy

Use a reverse proxy when remote services need node API access.

## Rules

- Bind node REST API to localhost when possible.
- Terminate TLS at proxy.
- Rate-limit public routes.
- Avoid proxying wallet routes publicly.
- Pass `api_key` only over HTTPS/private links.

## Nginx Skeleton

```nginx
server {
  listen 443 ssl;
  server_name node.example.com;

  location / {
    limit_req zone=node_api burst=20 nodelay;
    proxy_pass http://127.0.0.1:9052;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto https;
  }
}
```

For local admin, SSH tunnel is often simpler:

```shell
ssh -L 9053:127.0.0.1:9052 user@node-host
```

