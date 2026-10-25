---
title: Ergo Node API Interactive Schema
description: Browse request parameters, bodies, responses, and models from the versioned Ergo node OpenAPI snapshot.
owner: docs
---

<span id="swagger-api"></span>

# Node API Interactive Schema

This viewer uses the same checked-in specification as the [Node API Reference](openapi.md). Check its version against your node before implementing a client.

Use this page to browse request and response schemas. To **execute** requests, open `/swagger` on your own node, such as `http://127.0.0.1:9053/swagger`; see [API Access and Authentication](swagger.md#accessing-the-api). A relative server URL in this viewer points to the documentation host, not your node. Do not enter your node's API key into a public node's Swagger UI.

[Download the OpenAPI YAML](openapi.yaml) for client generation or local inspection.

!!swagger openapi.yaml!!
