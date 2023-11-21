# Ergo Node API v5.0.15


/// admonition | Getting Started!
API docs for Ergo Node. Scroll down for code samples, example requests and responses
///



Base URLs:


* <a href="http://213.239.193.208:9053">http://213.239.193.208:9053</a>

## Authentication

* API Key (ApiKeyAuth)
    - Parameter Name: **api_key**, in: header. 

## UTXO

### getSnapshotsInfo

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X DEFAULT /utxo/getSnapshotsInfo
    ```

=== "http"

    ```http
    DEFAULT /utxo/getSnapshotsInfo HTTP/1.1
    ```

=== "javascript"

    ```javascript
    
    fetch('/utxo/getSnapshotsInfo',
    {
      method: 'DEFAULT'
    
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    result = RestClient.default '/utxo/getSnapshotsInfo',
      params: {
      }
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    
    r = requests.default('/utxo/getSnapshotsInfo')
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('DEFAULT','/utxo/getSnapshotsInfo', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utxo/getSnapshotsInfo");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("DEFAULT");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("DEFAULT", "/utxo/getSnapshotsInfo", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`DEFAULT /utxo/getSnapshotsInfo`

Error

<h3 id="default__utxo_getsnapshotsinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

## blocks

### getHeaderIds

<a id="opIdgetHeaderIds"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blocks \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blocks HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blocks',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blocks',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blocks', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blocks', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blocks");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blocks", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blocks`

*Get an array of header ids (hex encoded) for the given range of blockchain block heights. Returns a page of the whole list starting from `offset` and containing `limit` items.*

<h3 id="getheaderids-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer(int32)|false|The number of items in list to return|
|offset|query|integer(int32)|false|The first block height to include in the list|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      "8b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337"
    ]
    ```

<h3 id="getheaderids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Array of header ids|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getheaderids-responseschema">Response Schema</h3>

Status Code **200**

*Array of header ids*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

### sendMinedBlock

<a id="opIdsendMinedBlock"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /blocks \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /blocks HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "header": {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      },
      "blockTransactions": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactions": [
          {
            "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "inputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "spendingProof": {
                  "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "extension": {
                    "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                  }
                }
              }
            ],
            "dataInputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
              }
            ],
            "outputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "value": 147,
                "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
                "creationHeight": 9149,
                "assets": [
                  {
                    "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                    "amount": 1000
                  }
                ],
                "additionalRegisters": {
                  "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
                },
                "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "index": 0
              }
            ],
            "size": 0
          }
        ],
        "size": 0
      },
      "adProofs": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "proofBytes": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "size": 0
      },
      "extension": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "fields": [
          [
            "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          ]
        ]
      },
      "size": 0
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/blocks',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/blocks',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/blocks', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/blocks', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blocks");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/blocks", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /blocks`

*Send a mined block*

> Body parameter

=== "json"

    ```json
    {
      "header": {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      },
      "blockTransactions": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactions": [
          {
            "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "inputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "spendingProof": {
                  "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "extension": {
                    "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                  }
                }
              }
            ],
            "dataInputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
              }
            ],
            "outputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "value": 147,
                "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
                "creationHeight": 9149,
                "assets": [
                  {
                    "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                    "amount": 1000
                  }
                ],
                "additionalRegisters": {
                  "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
                },
                "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "index": 0
              }
            ],
            "size": 0
          }
        ],
        "size": 0
      },
      "adProofs": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "proofBytes": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "size": 0
      },
      "extension": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "fields": [
          [
            "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          ]
        ]
      },
      "size": 0
    }
    ```

<h3 id="sendminedblock-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[FullBlock](#schemafullblock)|true|none|

> Example responses

> default Response

=== "json"

    ```json
    {
      "error": 500,
      "reason": "Internal server error",
      "detail": "string"
    }
    ```

<h3 id="sendminedblock-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Block is valid|None|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getFullBlockAt

<a id="opIdgetFullBlockAt"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blocks/at/{blockHeight} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blocks/at/{blockHeight} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blocks/at/{blockHeight}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blocks/at/{blockHeight}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blocks/at/{blockHeight}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blocks/at/{blockHeight}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blocks/at/{blockHeight}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blocks/at/{blockHeight}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blocks/at/{blockHeight}`

*Get header ids at the given height*

<h3 id="getfullblockat-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|blockHeight|path|integer(int32)|true|Height of a block to retrieve header ids|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      "8b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337"
    ]
    ```

<h3 id="getfullblockat-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Array of header ids|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Blocks at this height doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getfullblockat-responseschema">Response Schema</h3>

Status Code **200**

*Array of header ids*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

### getChainSlice

<a id="opIdgetChainSlice"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blocks/chainSlice \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blocks/chainSlice HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blocks/chainSlice',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blocks/chainSlice',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blocks/chainSlice', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blocks/chainSlice', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blocks/chainSlice");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blocks/chainSlice", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blocks/chainSlice`

*Get headers in a specified range of heights*

<h3 id="getchainslice-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|fromHeight|query|integer(int32)|false|Min header height (start of the range)|
|toHeight|query|integer(int32)|false|Max header height of the range (last header height then omitted)|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ]
    ```

<h3 id="getchainslice-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Array of headers|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getchainslice-responseschema">Response Schema</h3>

Status Code **200**

*Array of headers*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[BlockHeader](#schemablockheader)]|false|none|Array of headers|
|» id|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» timestamp|[Timestamp](#schematimestamp)(int64)|true|none|Basic timestamp definition|
|» version|[Version](#schemaversion)(int8)|true|none|Ergo blockchain protocol version|
|» adProofsRoot|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|» stateRoot|[ADDigest](#schemaaddigest)(base16)|true|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|
|» transactionsRoot|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|» nBits|integer(int64)|true|none|Proof-of-work target (difficulty encoded)|
|» extensionHash|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|» powSolutions|[PowSolutions](#schemapowsolutions)|true|none|An object containing all components of pow solution|
|»» pk|string|true|none|Base16-encoded public key|
|»» w|string|true|none|none|
|»» n|string|true|none|none|
|»» d|number|true|none|none|
|» height|integer(int32)|true|none|Height of the block (genesis block height == 1)|
|» difficulty|string|true|none|none|
|» parentId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» votes|[Votes](#schemavotes)(base16)|true|none|Base16-encoded votes for a soft-fork and parameters|
|» size|integer(int32)|false|none|Size of the header in bytes|
|» extensionId|[ModifierId](#schemamodifierid)(base16)|false|none|Base16-encoded 32 byte modifier id|
|» transactionsId|[ModifierId](#schemamodifierid)(base16)|false|none|Base16-encoded 32 byte modifier id|
|» adProofsId|[ModifierId](#schemamodifierid)(base16)|false|none|Base16-encoded 32 byte modifier id|

<aside class="success">
This operation does not require authentication
</aside>

### getFullBlockById

<a id="opIdgetFullBlockById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blocks/{headerId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blocks/{headerId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blocks/{headerId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blocks/{headerId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blocks/{headerId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blocks/{headerId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blocks/{headerId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blocks/{headerId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blocks/{headerId}`

*Get the full block info by a given header id*

<h3 id="getfullblockbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|headerId|path|string|true|ID of the header the wanted block|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "header": {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      },
      "blockTransactions": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactions": [
          {
            "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "inputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "spendingProof": {
                  "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "extension": {
                    "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                  }
                }
              }
            ],
            "dataInputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
              }
            ],
            "outputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "value": 147,
                "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
                "creationHeight": 9149,
                "assets": [
                  {
                    "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                    "amount": 1000
                  }
                ],
                "additionalRegisters": {
                  "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
                },
                "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "index": 0
              }
            ],
            "size": 0
          }
        ],
        "size": 0
      },
      "adProofs": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "proofBytes": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "size": 0
      },
      "extension": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "fields": [
          [
            "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          ]
        ]
      },
      "size": 0
    }
    ```

<h3 id="getfullblockbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Block object representing the full block data|[FullBlock](#schemafullblock)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Block with this id doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getFullBlockByIds

<a id="opIdgetFullBlockByIds"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /blocks/headerIds \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /blocks/headerIds HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '[
      "string"
    ]';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/blocks/headerIds',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/blocks/headerIds',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/blocks/headerIds', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/blocks/headerIds', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blocks/headerIds");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/blocks/headerIds", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /blocks/headerIds`

*Get full blocks by given header ids*

> Body parameter

=== "json"

    ```json
    [
      "string"
    ]
    ```

<h3 id="getfullblockbyids-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|array[string]|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "header": {
          "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "timestamp": 1524143059077,
          "version": 2,
          "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "nBits": 19857408,
          "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "powSolutions": {
            "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
            "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
            "n": "0000000000000000",
            "d": 987654321
          },
          "height": 667,
          "difficulty": "9575989248",
          "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "votes": "000000",
          "size": 0,
          "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        },
        "blockTransactions": {
          "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactions": [
            {
              "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "inputs": [
                {
                  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "spendingProof": {
                    "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                    "extension": {
                      "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                    }
                  }
                }
              ],
              "dataInputs": [
                {
                  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
                }
              ],
              "outputs": [
                {
                  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "value": 147,
                  "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
                  "creationHeight": 9149,
                  "assets": [
                    {
                      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                      "amount": 1000
                    }
                  ],
                  "additionalRegisters": {
                    "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
                  },
                  "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "index": 0
                }
              ],
              "size": 0
            }
          ],
          "size": 0
        },
        "adProofs": {
          "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "proofBytes": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "size": 0
        },
        "extension": {
          "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "fields": [
            [
              "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
            ]
          ]
        },
        "size": 0
      }
    ]
    ```

<h3 id="getfullblockbyids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Full blocks corresponding to ids provided|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|No block exist for every id provided|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getfullblockbyids-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[FullBlock](#schemafullblock)]|false|none|[Block with header and transactions]|
|» header|[BlockHeader](#schemablockheader)|true|none|Header of a block. It authenticates link to a previous block, other block sections (transactions, UTXO set transformation proofs, extension), UTXO set, votes for blockchain parameters to be changed and proof-of-work related data.|
|»» id|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|»» timestamp|[Timestamp](#schematimestamp)(int64)|true|none|Basic timestamp definition|
|»» version|[Version](#schemaversion)(int8)|true|none|Ergo blockchain protocol version|
|»» adProofsRoot|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»» stateRoot|[ADDigest](#schemaaddigest)(base16)|true|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|
|»» transactionsRoot|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»» nBits|integer(int64)|true|none|Proof-of-work target (difficulty encoded)|
|»» extensionHash|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»» powSolutions|[PowSolutions](#schemapowsolutions)|true|none|An object containing all components of pow solution|
|»»» pk|string|true|none|Base16-encoded public key|
|»»» w|string|true|none|none|
|»»» n|string|true|none|none|
|»»» d|number|true|none|none|
|»» height|integer(int32)|true|none|Height of the block (genesis block height == 1)|
|»» difficulty|string|true|none|none|
|»» parentId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|»» votes|[Votes](#schemavotes)(base16)|true|none|Base16-encoded votes for a soft-fork and parameters|
|»» size|integer(int32)|false|none|Size of the header in bytes|
|»» extensionId|[ModifierId](#schemamodifierid)(base16)|false|none|Base16-encoded 32 byte modifier id|
|»» transactionsId|[ModifierId](#schemamodifierid)(base16)|false|none|Base16-encoded 32 byte modifier id|
|»» adProofsId|[ModifierId](#schemamodifierid)(base16)|false|none|Base16-encoded 32 byte modifier id|
|» blockTransactions|[BlockTransactions](#schemablocktransactions)|true|none|Section of a block which contains transactions.|
|»» headerId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|»» transactions|[[ErgoTransaction](#schemaergotransaction)]|true|none|List of ErgoTransaction objects|
|»»» id|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»»» inputs|[[ErgoTransactionInput](#schemaergotransactioninput)]|true|none|Inputs, that will be spent by this transaction|
|»»»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»»» spendingProof|[SpendingProof](#schemaspendingproof)|true|none|Spending proof for transaction input|
|»»»»» proofBytes|[SpendingProofBytes](#schemaspendingproofbytes)(base16)|true|none|Base16-encoded spending proofs|
|»»»»» extension|object|true|none|Variables to be put into context|
|»»»»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»» dataInputs|[[ErgoTransactionDataInput](#schemaergotransactiondatainput)]|true|none|Read-only inputs, that are not going to be spent by transaction.|
|»»»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» outputs|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|Outputs of the transaction, i.e. box candidates to be created by this transaction.|
|»»»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»»» value|integer(int64)|true|none|Amount of Ergo token|
|»»»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»»»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»»»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»»»» amount|integer(int64)|true|none|Amount of the token|
|»»»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»»»» index|integer(int32)|false|none|Index in the transaction outputs|
|»»» size|integer(int32)|false|none|Size of ErgoTransaction in bytes|
|»» size|integer(int32)|true|none|Size in bytes of all block transactions|
|» adProofs|[BlockADProofs](#schemablockadproofs)|true|none|none|
|»» headerId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|»» proofBytes|[SerializedAdProof](#schemaserializedadproof)(base16)|true|none|Base16-encoded ad proofs|
|»» digest|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»» size|integer(int32)|true|none|Size in bytes|
|» extension|[Extension](#schemaextension)|true|none|Section of a block which contains extension data.|
|»» headerId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|»» digest|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»» fields|[[KeyValueItem](#schemakeyvalueitem)]¦null|true|none|List of key-value records|
|» size|integer(int32)|true|none|Size in bytes|

<aside class="success">
This operation does not require authentication
</aside>

### getBlockHeaderById

<a id="opIdgetBlockHeaderById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blocks/{headerId}/header \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blocks/{headerId}/header HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blocks/{headerId}/header',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blocks/{headerId}/header',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blocks/{headerId}/header', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blocks/{headerId}/header', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blocks/{headerId}/header");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blocks/{headerId}/header", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blocks/{headerId}/header`

*Get the block header info by a given header id*

<h3 id="getblockheaderbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|headerId|path|string|true|ID of a wanted block header|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "version": 2,
      "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "nBits": 19857408,
      "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "powSolutions": {
        "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
        "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
        "n": "0000000000000000",
        "d": 987654321
      },
      "height": 667,
      "difficulty": "9575989248",
      "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "votes": "000000",
      "size": 0,
      "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

<h3 id="getblockheaderbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Block header object|[BlockHeader](#schemablockheader)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Block with this id doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getBlockTransactionsById

<a id="opIdgetBlockTransactionsById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blocks/{headerId}/transactions \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blocks/{headerId}/transactions HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blocks/{headerId}/transactions',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blocks/{headerId}/transactions',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blocks/{headerId}/transactions', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blocks/{headerId}/transactions', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blocks/{headerId}/transactions");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blocks/{headerId}/transactions", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blocks/{headerId}/transactions`

*Get the block transactions info by a given signature*

<h3 id="getblocktransactionsbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|headerId|path|string|true|ID of a wanted block transactions|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactions": [
        {
          "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "inputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "spendingProof": {
                "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "extension": {
                  "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                }
              }
            }
          ],
          "dataInputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
            }
          ],
          "outputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "value": 147,
              "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
              "creationHeight": 9149,
              "assets": [
                {
                  "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "amount": 1000
                }
              ],
              "additionalRegisters": {
                "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
              },
              "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "index": 0
            }
          ],
          "size": 0
        }
      ],
      "size": 0
    }
    ```

<h3 id="getblocktransactionsbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Block transaction object|[BlockTransactions](#schemablocktransactions)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Block with this id doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getProofForTx

<a id="opIdgetProofForTx"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blocks/{headerId}/proofFor/{txId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blocks/{headerId}/proofFor/{txId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blocks/{headerId}/proofFor/{txId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blocks/{headerId}/proofFor/{txId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blocks/{headerId}/proofFor/{txId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blocks/{headerId}/proofFor/{txId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blocks/{headerId}/proofFor/{txId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blocks/{headerId}/proofFor/{txId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blocks/{headerId}/proofFor/{txId}`

*Get Merkle proof for transaction*

<h3 id="getprooffortx-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|headerId|path|string|true|ID of a wanted block transactions|
|txId|path|string|true|ID of a wanted transaction|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "leaf": "cd665e49c834b0c25574fcb19a158d836f3f2aad8e91ac195f972534c25449b3",
      "levels": [
        [
          "018b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337",
          0
        ]
      ]
    }
    ```

<h3 id="getprooffortx-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Merkle proof object|[MerkleProof](#schemamerkleproof)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getLastHeaders

<a id="opIdgetLastHeaders"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blocks/lastHeaders/{count} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blocks/lastHeaders/{count} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blocks/lastHeaders/{count}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blocks/lastHeaders/{count}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blocks/lastHeaders/{count}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blocks/lastHeaders/{count}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blocks/lastHeaders/{count}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blocks/lastHeaders/{count}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blocks/lastHeaders/{count}`

*Get the last headers objects*

<h3 id="getlastheaders-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|count|path|number|true|a number of block headers to return|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ]
    ```

<h3 id="getlastheaders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Array of block headers|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getlastheaders-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[BlockHeader](#schemablockheader)]|false|none|[Header of a block. It authenticates link to a previous block, other block sections (transactions, UTXO set transformation proofs, extension), UTXO set, votes for blockchain parameters to be changed and proof-of-work related data.]|
|» id|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» timestamp|[Timestamp](#schematimestamp)(int64)|true|none|Basic timestamp definition|
|» version|[Version](#schemaversion)(int8)|true|none|Ergo blockchain protocol version|
|» adProofsRoot|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|» stateRoot|[ADDigest](#schemaaddigest)(base16)|true|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|
|» transactionsRoot|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|» nBits|integer(int64)|true|none|Proof-of-work target (difficulty encoded)|
|» extensionHash|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|» powSolutions|[PowSolutions](#schemapowsolutions)|true|none|An object containing all components of pow solution|
|»» pk|string|true|none|Base16-encoded public key|
|»» w|string|true|none|none|
|»» n|string|true|none|none|
|»» d|number|true|none|none|
|» height|integer(int32)|true|none|Height of the block (genesis block height == 1)|
|» difficulty|string|true|none|none|
|» parentId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» votes|[Votes](#schemavotes)(base16)|true|none|Base16-encoded votes for a soft-fork and parameters|
|» size|integer(int32)|false|none|Size of the header in bytes|
|» extensionId|[ModifierId](#schemamodifierid)(base16)|false|none|Base16-encoded 32 byte modifier id|
|» transactionsId|[ModifierId](#schemamodifierid)(base16)|false|none|Base16-encoded 32 byte modifier id|
|» adProofsId|[ModifierId](#schemamodifierid)(base16)|false|none|Base16-encoded 32 byte modifier id|

<aside class="success">
This operation does not require authentication
</aside>

### getModifierById

<a id="opIdgetModifierById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blocks/modifier/{modifierId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blocks/modifier/{modifierId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blocks/modifier/{modifierId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blocks/modifier/{modifierId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blocks/modifier/{modifierId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blocks/modifier/{modifierId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blocks/modifier/{modifierId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blocks/modifier/{modifierId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blocks/modifier/{modifierId}`

*Get the persistent modifier by its id*

<h3 id="getmodifierbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|modifierId|path|string|true|ID of a wanted modifier|

> Example responses

> 404 Response

=== "json"

    ```json
    {
      "error": 500,
      "reason": "Internal server error",
      "detail": "string"
    }
    ```

<h3 id="getmodifierbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Persistent modifier object|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Modifier with this id doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

## nipopow

### getPopowHeaderById

<a id="opIdgetPopowHeaderById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /nipopow/popowHeaderById/{headerId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /nipopow/popowHeaderById/{headerId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/nipopow/popowHeaderById/{headerId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/nipopow/popowHeaderById/{headerId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/nipopow/popowHeaderById/{headerId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/nipopow/popowHeaderById/{headerId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/nipopow/popowHeaderById/{headerId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/nipopow/popowHeaderById/{headerId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /nipopow/popowHeaderById/{headerId}`

*Construct PoPow header according to given header id*

<h3 id="getpopowheaderbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|headerId|path|string|true|ID of wanted header|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "header": {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      },
      "interlinks": [
        "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      ]
    }
    ```

<h3 id="getpopowheaderbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|PoPow header object|[PopowHeader](#schemapopowheader)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Header of extension of a corresponding block are not available|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getPopowHeaderByHeight

<a id="opIdgetPopowHeaderByHeight"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /nipopow/popowHeaderByHeight/{height} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /nipopow/popowHeaderByHeight/{height} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/nipopow/popowHeaderByHeight/{height}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/nipopow/popowHeaderByHeight/{height}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/nipopow/popowHeaderByHeight/{height}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/nipopow/popowHeaderByHeight/{height}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/nipopow/popowHeaderByHeight/{height}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/nipopow/popowHeaderByHeight/{height}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /nipopow/popowHeaderByHeight/{height}`

*Construct PoPow header for best header at given height*

<h3 id="getpopowheaderbyheight-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|height|path|integer(int32)|true|Height of a wanted header|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "header": {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      },
      "interlinks": [
        "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      ]
    }
    ```

<h3 id="getpopowheaderbyheight-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|PoPow header object|[PopowHeader](#schemapopowheader)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Header of extension of a corresponding block are not available|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getPopowProof

<a id="opIdgetPopowProof"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /nipopow/proof/{minChainLength}/{suffixLength} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /nipopow/proof/{minChainLength}/{suffixLength} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/nipopow/proof/{minChainLength}/{suffixLength}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/nipopow/proof/{minChainLength}/{suffixLength}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/nipopow/proof/{minChainLength}/{suffixLength}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/nipopow/proof/{minChainLength}/{suffixLength}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/nipopow/proof/{minChainLength}/{suffixLength}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/nipopow/proof/{minChainLength}/{suffixLength}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /nipopow/proof/{minChainLength}/{suffixLength}`

*Construct PoPoW proof for given min superchain length and suffix length*

<h3 id="getpopowproof-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|minChainLength|path|number|true|Minimal superchain length|
|suffixLength|path|number|true|Suffix length|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "m": 0,
      "k": 0,
      "prefix": [
        {
          "header": {
            "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "timestamp": 1524143059077,
            "version": 2,
            "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "nBits": 19857408,
            "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "powSolutions": {
              "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
              "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
              "n": "0000000000000000",
              "d": 987654321
            },
            "height": 667,
            "difficulty": "9575989248",
            "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "votes": "000000",
            "size": 0,
            "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          },
          "interlinks": [
            "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          ]
        }
      ],
      "suffixHead": {
        "header": {
          "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "timestamp": 1524143059077,
          "version": 2,
          "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "nBits": 19857408,
          "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "powSolutions": {
            "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
            "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
            "n": "0000000000000000",
            "d": 987654321
          },
          "height": 667,
          "difficulty": "9575989248",
          "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "votes": "000000",
          "size": 0,
          "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        },
        "interlinks": [
          "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        ]
      },
      "suffixTail": [
        {
          "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "timestamp": 1524143059077,
          "version": 2,
          "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "nBits": 19857408,
          "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "powSolutions": {
            "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
            "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
            "n": "0000000000000000",
            "d": 987654321
          },
          "height": 667,
          "difficulty": "9575989248",
          "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "votes": "000000",
          "size": 0,
          "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ]
    }
    ```

<h3 id="getpopowproof-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Nipopow proof object|[NipopowProof](#schemanipopowproof)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getPopowProofByHeaderId

<a id="opIdgetPopowProofByHeaderId"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /nipopow/proof/{minChainLength}/{suffixLength}/{headerId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /nipopow/proof/{minChainLength}/{suffixLength}/{headerId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/nipopow/proof/{minChainLength}/{suffixLength}/{headerId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/nipopow/proof/{minChainLength}/{suffixLength}/{headerId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/nipopow/proof/{minChainLength}/{suffixLength}/{headerId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/nipopow/proof/{minChainLength}/{suffixLength}/{headerId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/nipopow/proof/{minChainLength}/{suffixLength}/{headerId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/nipopow/proof/{minChainLength}/{suffixLength}/{headerId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /nipopow/proof/{minChainLength}/{suffixLength}/{headerId}`

*Construct PoPoW proof for given min superchain length, suffix length and header ID*

<h3 id="getpopowproofbyheaderid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|minChainLength|path|number|true|Minimal superchain length|
|suffixLength|path|number|true|Suffix length|
|headerId|path|string|true|ID of wanted header|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "m": 0,
      "k": 0,
      "prefix": [
        {
          "header": {
            "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "timestamp": 1524143059077,
            "version": 2,
            "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "nBits": 19857408,
            "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "powSolutions": {
              "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
              "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
              "n": "0000000000000000",
              "d": 987654321
            },
            "height": 667,
            "difficulty": "9575989248",
            "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "votes": "000000",
            "size": 0,
            "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          },
          "interlinks": [
            "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          ]
        }
      ],
      "suffixHead": {
        "header": {
          "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "timestamp": 1524143059077,
          "version": 2,
          "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "nBits": 19857408,
          "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "powSolutions": {
            "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
            "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
            "n": "0000000000000000",
            "d": 987654321
          },
          "height": 667,
          "difficulty": "9575989248",
          "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "votes": "000000",
          "size": 0,
          "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        },
        "interlinks": [
          "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        ]
      },
      "suffixTail": [
        {
          "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "timestamp": 1524143059077,
          "version": 2,
          "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "nBits": 19857408,
          "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "powSolutions": {
            "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
            "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
            "n": "0000000000000000",
            "d": 987654321
          },
          "height": 667,
          "difficulty": "9575989248",
          "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "votes": "000000",
          "size": 0,
          "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ]
    }
    ```

<h3 id="getpopowproofbyheaderid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Nipopow proof object|[NipopowProof](#schemanipopowproof)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

## info

### getNodeInfo

<a id="opIdgetNodeInfo"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /info \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /info HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/info',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/info',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/info', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/info', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/info");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/info", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /info`

*Get the information about the Node*

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "name": "my-node-1",
      "appVersion": "0.0.1",
      "fullHeight": 667,
      "headersHeight": 667,
      "maxPeerHeight": 706162,
      "bestFullHeaderId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "previousFullHeaderId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "bestHeaderId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateRoot": "dab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateType": "digest",
      "stateVersion": "fab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "isMining": true,
      "peersCount": 327,
      "unconfirmedCount": 327,
      "difficulty": 667,
      "currentTime": 1524143059077,
      "launchTime": 1524143059077,
      "headersScore": 0,
      "fullBlocksScore": 0,
      "genesisBlockId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "parameters": {
        "height": 667,
        "storageFeeFactor": 100000,
        "minValuePerByte": 360,
        "maxBlockSize": 1048576,
        "maxBlockCost": 104876,
        "blockVersion": 2,
        "tokenAccessCost": 100,
        "inputCost": 100,
        "dataInputCost": 100,
        "outputCost": 100
      },
      "eip27Supported": true,
      "restApiUrl": "https://example.com"
    }
    ```

<h3 id="getnodeinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Node info object|[NodeInfo](#schemanodeinfo)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

## transactions

### sendTransaction

<a id="opIdsendTransaction"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /transactions \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /transactions HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "size": 0
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/transactions',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/transactions',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/transactions', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/transactions', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/transactions", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /transactions`

*Submit an Ergo transaction to unconfirmed pool to send it over the network*

> Body parameter

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "size": 0
    }
    ```

<h3 id="sendtransaction-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ErgoTransaction](#schemaergotransaction)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

<h3 id="sendtransaction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|JSON with ID of the new transaction|[TransactionId](#schematransactionid)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### sendTransactionAsBytes

<a id="opIdsendTransactionAsBytes"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /transactions/bytes \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /transactions/bytes HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"02c9e71790399816b3e40b2207e9ade19a9b7fe0600186cfb8e2b115bfdb34b57f38cd3c9f2890d11720eb3bb993993f00ededf812a590d2993df094a7ca4f0213e4820e1ab831eed5dc5c72665396d3a01d2a12900f1c3ab77700b284ae24fa8e8f7754f86f2282c795db6b0b17df1c29cc0552e59d01f7d777c638a813333277271c2f8b4d99d01ff0e6ee8695697bdd5b568089395620d7198c6093ce8bc59b928611b1b12452c05addaa42f4beff6a0a6fe90000000380d0dbc3f40210090402040005c801040205c8010500040004000e2003faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04d807d601e4c6a70408d602b2a5730000d603e4c6a70601d604e4c6a7080ed605e4c6a70505d606e4c6a70705d60795720399c1a7c1720299c17202c1a7eb027201d1ededededededededed93c27202c2a793e4c672020408720193e4c6720205059572039d9c72057eb272047301000573029d9c72057eb2720473030005730494e4c672020601720393e4c672020705720693e4c67202080e720493e4c67202090ec5a79572039072079c720672059272079c72067205917207730595ef720393b1db630872027306d801d608b2db63087202730700ed938c7208017308938c7208027206c8df35000508cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba0405c8a8c105010105dc8b020e0266608cdea8baf0380008cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba04c8df350000c0843d1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304c8df350000"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/transactions/bytes',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/transactions/bytes',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/transactions/bytes', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/transactions/bytes', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/bytes");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/transactions/bytes", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /transactions/bytes`

*Submit an Ergo transaction given as hex-encoded transaction bytes to unconfirmed pool to send it over the network*

> Body parameter

=== "json"

    ```json
    "\"02c9e71790399816b3e40b2207e9ade19a9b7fe0600186cfb8e2b115bfdb34b57f38cd3c9f2890d11720eb3bb993993f00ededf812a590d2993df094a7ca4f0213e4820e1ab831eed5dc5c72665396d3a01d2a12900f1c3ab77700b284ae24fa8e8f7754f86f2282c795db6b0b17df1c29cc0552e59d01f7d777c638a813333277271c2f8b4d99d01ff0e6ee8695697bdd5b568089395620d7198c6093ce8bc59b928611b1b12452c05addaa42f4beff6a0a6fe90000000380d0dbc3f40210090402040005c801040205c8010500040004000e2003faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04d807d601e4c6a70408d602b2a5730000d603e4c6a70601d604e4c6a7080ed605e4c6a70505d606e4c6a70705d60795720399c1a7c1720299c17202c1a7eb027201d1ededededededededed93c27202c2a793e4c672020408720193e4c6720205059572039d9c72057eb272047301000573029d9c72057eb2720473030005730494e4c672020601720393e4c672020705720693e4c67202080e720493e4c67202090ec5a79572039072079c720672059272079c72067205917207730595ef720393b1db630872027306d801d608b2db63087202730700ed938c7208017308938c7208027206c8df35000508cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba0405c8a8c105010105dc8b020e0266608cdea8baf0380008cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba04c8df350000c0843d1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304c8df350000\""
    ```

<h3 id="sendtransactionasbytes-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

<h3 id="sendtransactionasbytes-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|JSON with ID of the new transaction|[TransactionId](#schematransactionid)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### checkTransaction

<a id="opIdcheckTransaction"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /transactions/check \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /transactions/check HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "size": 0
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/transactions/check',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/transactions/check',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/transactions/check', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/transactions/check', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/check");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/transactions/check", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /transactions/check`

*Checks an Ergo transaction without sending it over the network. Checks that transaction is valid and its inputs are in the UTXO set. Returns transaction identifier if the transaction is passing the checks.*

> Body parameter

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "size": 0
    }
    ```

<h3 id="checktransaction-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ErgoTransaction](#schemaergotransaction)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

<h3 id="checktransaction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|JSON with ID of the new transaction|[TransactionId](#schematransactionid)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### checkTransactionAsBytes

<a id="opIdcheckTransactionAsBytes"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /transactions/checkBytes \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /transactions/checkBytes HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"02c9e71790399816b3e40b2207e9ade19a9b7fe0600186cfb8e2b115bfdb34b57f38cd3c9f2890d11720eb3bb993993f00ededf812a590d2993df094a7ca4f0213e4820e1ab831eed5dc5c72665396d3a01d2a12900f1c3ab77700b284ae24fa8e8f7754f86f2282c795db6b0b17df1c29cc0552e59d01f7d777c638a813333277271c2f8b4d99d01ff0e6ee8695697bdd5b568089395620d7198c6093ce8bc59b928611b1b12452c05addaa42f4beff6a0a6fe90000000380d0dbc3f40210090402040005c801040205c8010500040004000e2003faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04d807d601e4c6a70408d602b2a5730000d603e4c6a70601d604e4c6a7080ed605e4c6a70505d606e4c6a70705d60795720399c1a7c1720299c17202c1a7eb027201d1ededededededededed93c27202c2a793e4c672020408720193e4c6720205059572039d9c72057eb272047301000573029d9c72057eb2720473030005730494e4c672020601720393e4c672020705720693e4c67202080e720493e4c67202090ec5a79572039072079c720672059272079c72067205917207730595ef720393b1db630872027306d801d608b2db63087202730700ed938c7208017308938c7208027206c8df35000508cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba0405c8a8c105010105dc8b020e0266608cdea8baf0380008cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba04c8df350000c0843d1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304c8df350000"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/transactions/checkBytes',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/transactions/checkBytes',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/transactions/checkBytes', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/transactions/checkBytes', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/checkBytes");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/transactions/checkBytes", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /transactions/checkBytes`

*Checks an Ergo transaction without sending it over the network given in form of hex-encoded transaction bytes. Checks that transaction is valid and its inputs are in the UTXO set. Returns transaction identifier if the transaction is passing the checks.*

> Body parameter

=== "json"

    ```json
    "\"02c9e71790399816b3e40b2207e9ade19a9b7fe0600186cfb8e2b115bfdb34b57f38cd3c9f2890d11720eb3bb993993f00ededf812a590d2993df094a7ca4f0213e4820e1ab831eed5dc5c72665396d3a01d2a12900f1c3ab77700b284ae24fa8e8f7754f86f2282c795db6b0b17df1c29cc0552e59d01f7d777c638a813333277271c2f8b4d99d01ff0e6ee8695697bdd5b568089395620d7198c6093ce8bc59b928611b1b12452c05addaa42f4beff6a0a6fe90000000380d0dbc3f40210090402040005c801040205c8010500040004000e2003faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04d807d601e4c6a70408d602b2a5730000d603e4c6a70601d604e4c6a7080ed605e4c6a70505d606e4c6a70705d60795720399c1a7c1720299c17202c1a7eb027201d1ededededededededed93c27202c2a793e4c672020408720193e4c6720205059572039d9c72057eb272047301000573029d9c72057eb2720473030005730494e4c672020601720393e4c672020705720693e4c67202080e720493e4c67202090ec5a79572039072079c720672059272079c72067205917207730595ef720393b1db630872027306d801d608b2db63087202730700ed938c7208017308938c7208027206c8df35000508cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba0405c8a8c105010105dc8b020e0266608cdea8baf0380008cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba04c8df350000c0843d1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304c8df350000\""
    ```

<h3 id="checktransactionasbytes-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

<h3 id="checktransactionasbytes-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|JSON with ID of the new transaction|[TransactionId](#schematransactionid)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getUnconfirmedTransactions

<a id="opIdgetUnconfirmedTransactions"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /transactions/unconfirmed \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /transactions/unconfirmed HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/transactions/unconfirmed',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/transactions/unconfirmed',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/transactions/unconfirmed', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/transactions/unconfirmed', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/unconfirmed");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/transactions/unconfirmed", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /transactions/unconfirmed`

*Get current pool of the unconfirmed transactions pool*

<h3 id="getunconfirmedtransactions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer(int32)|false|The number of items in list to return|
|offset|query|integer(int32)|false|The number of items in list to skip|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "size": 0
      }
    ]
    ```

<h3 id="getunconfirmedtransactions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Array with Ergo transactions|[Transactions](#schematransactions)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### checkUnconfirmedTransaction

<a id="opIdcheckUnconfirmedTransaction"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X HEAD /transactions/unconfirmed/{txId}
    ```

=== "http"

    ```http
    HEAD /transactions/unconfirmed/{txId} HTTP/1.1
    ```

=== "javascript"

    ```javascript
    
    fetch('/transactions/unconfirmed/{txId}',
    {
      method: 'HEAD'
    
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    result = RestClient.head '/transactions/unconfirmed/{txId}',
      params: {
      }
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    
    r = requests.head('/transactions/unconfirmed/{txId}')
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('HEAD','/transactions/unconfirmed/{txId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/unconfirmed/{txId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("HEAD");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("HEAD", "/transactions/unconfirmed/{txId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`HEAD /transactions/unconfirmed/{txId}`

*Check if given transaction is unconfirmed in pool*

<h3 id="checkunconfirmedtransaction-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|txId|path|string|true|ID of a transaction in question|

<h3 id="checkunconfirmedtransaction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Transaction is in pool|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Transaction is not in pool|None|

<aside class="success">
This operation does not require authentication
</aside>

### getUnconfirmedTransactionById

<a id="opIdgetUnconfirmedTransactionById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /transactions/unconfirmed/byTransactionId/{txId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /transactions/unconfirmed/byTransactionId/{txId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/transactions/unconfirmed/byTransactionId/{txId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/transactions/unconfirmed/byTransactionId/{txId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/transactions/unconfirmed/byTransactionId/{txId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/transactions/unconfirmed/byTransactionId/{txId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/unconfirmed/byTransactionId/{txId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/transactions/unconfirmed/byTransactionId/{txId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /transactions/unconfirmed/byTransactionId/{txId}`

*Get unconfirmed transaction from pool*

<h3 id="getunconfirmedtransactionbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|txId|path|string|true|ID of a transaction in question|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "size": 0
    }
    ```

<h3 id="getunconfirmedtransactionbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ergo transaction|[ErgoTransaction](#schemaergotransaction)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getUnconfirmedTransactionsByErgoTree

<a id="opIdgetUnconfirmedTransactionsByErgoTree"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /transactions/unconfirmed/byErgoTree \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /transactions/unconfirmed/byErgoTree HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/transactions/unconfirmed/byErgoTree',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/transactions/unconfirmed/byErgoTree',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/transactions/unconfirmed/byErgoTree', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/transactions/unconfirmed/byErgoTree', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/unconfirmed/byErgoTree");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/transactions/unconfirmed/byErgoTree", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /transactions/unconfirmed/byErgoTree`

*Finds unconfirmed transactions by ErgoTree hex of one of its output or input boxes (if present in UtxoState)*

> Body parameter

=== "json"

    ```json
    "\"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301\""
    ```

<h3 id="getunconfirmedtransactionsbyergotree-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|
|limit|query|integer(int32)|false|The number of items in list to return|
|offset|query|integer(int32)|false|The number of items in list to skip|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "size": 0
      }
    ]
    ```

<h3 id="getunconfirmedtransactionsbyergotree-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ergo transaction|[Transactions](#schematransactions)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getFeeHistogram

<a id="opIdgetFeeHistogram"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /transactions/poolHistogram \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /transactions/poolHistogram HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/transactions/poolHistogram',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/transactions/poolHistogram',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/transactions/poolHistogram', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/transactions/poolHistogram', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/poolHistogram");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/transactions/poolHistogram", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /transactions/poolHistogram`

*Get histogram (waittime, (n_trans, sum(fee)) for transactions in mempool. It contains "bins"+1 bins, where i-th elements corresponds to transaction with wait time [i*maxtime/bins, (i+1)*maxtime/bins), and last bin corresponds to the transactions with wait time >= maxtime.*

<h3 id="getfeehistogram-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|bins|query|integer(int32)|false|The number of bins in histogram|
|maxtime|query|integer(int64)|false|Maximal wait time in milliseconds|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "nTxns": 0,
        "totalFee": 0
      }
    ]
    ```

<h3 id="getfeehistogram-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Array with fee histogram|[FeeHistogram](#schemafeehistogram)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getRecommendedFee

<a id="opIdgetRecommendedFee"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /transactions/getFee?waitTime=1&txSize=100 \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /transactions/getFee?waitTime=1&txSize=100 HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/transactions/getFee?waitTime=1&txSize=100',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/transactions/getFee',
      params: {
      'waitTime' => 'integer(int32)',
    'txSize' => 'integer(int32)'
    }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/transactions/getFee', params={
      'waitTime': '1',  'txSize': '100'
    }, headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/transactions/getFee', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/getFee?waitTime=1&txSize=100");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/transactions/getFee", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /transactions/getFee`

*Get recommended fee (in nanoErgs) for a transaction with specified size (in bytes) to be proceeded in specified time (in minutes)*

<h3 id="getrecommendedfee-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|waitTime|query|integer(int32)|true|Maximum transaction wait time in minutes|
|txSize|query|integer(int32)|true|Transaction size|

> Example responses

> 200 Response

=== "json"

    ```json
    0
    ```

<h3 id="getrecommendedfee-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Recommended fee for the transaction (in nanoErgs)|integer|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getExpectedWaitTime

<a id="opIdgetExpectedWaitTime"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /transactions/waitTime?fee=1&txSize=100 \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /transactions/waitTime?fee=1&txSize=100 HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/transactions/waitTime?fee=1&txSize=100',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/transactions/waitTime',
      params: {
      'fee' => 'integer(int32)',
    'txSize' => 'integer(int32)'
    }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/transactions/waitTime', params={
      'fee': '1',  'txSize': '100'
    }, headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/transactions/waitTime', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/waitTime?fee=1&txSize=100");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/transactions/waitTime", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /transactions/waitTime`

*Get expected wait time for the transaction with specified fee and size*

<h3 id="getexpectedwaittime-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|fee|query|integer(int32)|true|Transaction fee (in nanoErgs)|
|txSize|query|integer(int32)|true|Transaction size|

> Example responses

> 200 Response

=== "json"

    ```json
    0
    ```

<h3 id="getexpectedwaittime-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Expected wait time in milliseconds|integer|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

## inputs

### getUnconfirmedTransactionInputBoxById

<a id="opIdgetUnconfirmedTransactionInputBoxById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /transactions/unconfirmed/inputs/byBoxId/{boxId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /transactions/unconfirmed/inputs/byBoxId/{boxId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/transactions/unconfirmed/inputs/byBoxId/{boxId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/transactions/unconfirmed/inputs/byBoxId/{boxId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/transactions/unconfirmed/inputs/byBoxId/{boxId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/transactions/unconfirmed/inputs/byBoxId/{boxId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/unconfirmed/inputs/byBoxId/{boxId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/transactions/unconfirmed/inputs/byBoxId/{boxId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /transactions/unconfirmed/inputs/byBoxId/{boxId}`

*Get input box from unconfirmed transactions in pool*

<h3 id="getunconfirmedtransactioninputboxbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of an input box in question|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
    ```

<h3 id="getunconfirmedtransactioninputboxbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Unspent Ergo Box that is to be used as Input in unconfirmed tx|[ErgoTransactionOutput](#schemaergotransactionoutput)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

## outputs

### getUnconfirmedTransactionOutputBoxById

<a id="opIdgetUnconfirmedTransactionOutputBoxById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /transactions/unconfirmed/outputs/byBoxId/{boxId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /transactions/unconfirmed/outputs/byBoxId/{boxId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/transactions/unconfirmed/outputs/byBoxId/{boxId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/transactions/unconfirmed/outputs/byBoxId/{boxId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/transactions/unconfirmed/outputs/byBoxId/{boxId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/transactions/unconfirmed/outputs/byBoxId/{boxId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/unconfirmed/outputs/byBoxId/{boxId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/transactions/unconfirmed/outputs/byBoxId/{boxId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /transactions/unconfirmed/outputs/byBoxId/{boxId}`

*Get output box from unconfirmed transactions in pool*

<h3 id="getunconfirmedtransactionoutputboxbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of an output box in question|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
    ```

<h3 id="getunconfirmedtransactionoutputboxbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Unspent Ergo Box that is to be created by unconfirmed tx|[ErgoTransactionOutput](#schemaergotransactionoutput)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getUnconfirmedTransactionOutputBoxesByErgoTree

<a id="opIdgetUnconfirmedTransactionOutputBoxesByErgoTree"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /transactions/unconfirmed/outputs/byErgoTree \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /transactions/unconfirmed/outputs/byErgoTree HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/transactions/unconfirmed/outputs/byErgoTree',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/transactions/unconfirmed/outputs/byErgoTree',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/transactions/unconfirmed/outputs/byErgoTree', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/transactions/unconfirmed/outputs/byErgoTree', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/unconfirmed/outputs/byErgoTree");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/transactions/unconfirmed/outputs/byErgoTree", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /transactions/unconfirmed/outputs/byErgoTree`

*Finds all output boxes by ErgoTree hex among unconfirmed transactions*

> Body parameter

=== "json"

    ```json
    "\"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301\""
    ```

<h3 id="getunconfirmedtransactionoutputboxesbyergotree-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|
|limit|query|integer(int32)|false|The number of items in list to return|
|offset|query|integer(int32)|false|The number of items in list to skip|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ]
    ```

<h3 id="getunconfirmedtransactionoutputboxesbyergotree-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Unconfirmed transaction output boxes that correspond to given ErgoTree hex|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getunconfirmedtransactionoutputboxesbyergotree-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|false|none|none|
|» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» value|integer(int64)|true|none|Amount of Ergo token|
|» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|» creationHeight|integer(int32)|true|none|Height the output was created at|
|» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»» amount|integer(int64)|true|none|Amount of the token|
|» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|» index|integer(int32)|false|none|Index in the transaction outputs|

<aside class="success">
This operation does not require authentication
</aside>

### getUnconfirmedTransactionOutputBoxesByTokenId

<a id="opIdgetUnconfirmedTransactionOutputBoxesByTokenId"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /transactions/unconfirmed/outputs/byTokenId/{tokenId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /transactions/unconfirmed/outputs/byTokenId/{tokenId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/transactions/unconfirmed/outputs/byTokenId/{tokenId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/transactions/unconfirmed/outputs/byTokenId/{tokenId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/transactions/unconfirmed/outputs/byTokenId/{tokenId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/transactions/unconfirmed/outputs/byTokenId/{tokenId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/unconfirmed/outputs/byTokenId/{tokenId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/transactions/unconfirmed/outputs/byTokenId/{tokenId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /transactions/unconfirmed/outputs/byTokenId/{tokenId}`

*Get output box from unconfirmed transactions in pool by tokenId*

<h3 id="getunconfirmedtransactionoutputboxesbytokenid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tokenId|path|string|true|ID of a token in question|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ]
    ```

<h3 id="getunconfirmedtransactionoutputboxesbytokenid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Unspent Ergo Boxes that are to be created by unconfirmed tx and contain given token|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getunconfirmedtransactionoutputboxesbytokenid-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|false|none|none|
|» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» value|integer(int64)|true|none|Amount of Ergo token|
|» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|» creationHeight|integer(int32)|true|none|Height the output was created at|
|» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»» amount|integer(int64)|true|none|Amount of the token|
|» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|» index|integer(int32)|false|none|Index in the transaction outputs|

<aside class="success">
This operation does not require authentication
</aside>

### getUnconfirmedTransactionOutputBoxesByRegisters

<a id="opIdgetUnconfirmedTransactionOutputBoxesByRegisters"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /transactions/unconfirmed/outputs/byRegisters \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /transactions/unconfirmed/outputs/byRegisters HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/transactions/unconfirmed/outputs/byRegisters',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/transactions/unconfirmed/outputs/byRegisters',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/transactions/unconfirmed/outputs/byRegisters', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/transactions/unconfirmed/outputs/byRegisters', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/transactions/unconfirmed/outputs/byRegisters");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/transactions/unconfirmed/outputs/byRegisters", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /transactions/unconfirmed/outputs/byRegisters`

*Finds all output boxes among unconfirmed transactions that contain given registers*

> Body parameter

=== "json"

    ```json
    {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    }
    ```

<h3 id="getunconfirmedtransactionoutputboxesbyregisters-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Registers](#schemaregisters)|true|none|
|limit|query|integer(int32)|false|The number of items in list to return|
|offset|query|integer(int32)|false|The number of items in list to skip|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ]
    ```

<h3 id="getunconfirmedtransactionoutputboxesbyregisters-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Unconfirmed transaction output boxes that contain given registers|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getunconfirmedtransactionoutputboxesbyregisters-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|false|none|none|
|» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» value|integer(int64)|true|none|Amount of Ergo token|
|» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|» creationHeight|integer(int32)|true|none|Height the output was created at|
|» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»» amount|integer(int64)|true|none|Amount of the token|
|» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|» index|integer(int32)|false|none|Index in the transaction outputs|

<aside class="success">
This operation does not require authentication
</aside>

## peers

### getAllPeers

<a id="opIdgetAllPeers"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /peers/all \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /peers/all HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/peers/all',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/peers/all',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/peers/all', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/peers/all', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/peers/all");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/peers/all", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /peers/all`

*Get all known peers*

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "address": "127.0.0.1:5673",
        "restApiUrl": "https://example.com",
        "name": "mynode",
        "lastSeen": 1524143059077,
        "connectionType": "Incoming"
      }
    ]
    ```

<h3 id="getallpeers-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Array of peer objects|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getallpeers-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Peer](#schemapeer)]|false|none|none|
|» address|string|true|none|none|
|» restApiUrl|string¦null|false|none|none|
|» name|string¦null|false|none|none|
|» lastSeen|[Timestamp](#schematimestamp)(int64)|false|none|Basic timestamp definition|
|» connectionType|string¦null|false|none|none|

##### Enumerated Values

|Property|Value|
|---|---|
|connectionType|Incoming|
|connectionType|Outgoing|

<aside class="success">
This operation does not require authentication
</aside>

### getConnectedPeers

<a id="opIdgetConnectedPeers"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /peers/connected \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /peers/connected HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/peers/connected',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/peers/connected',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/peers/connected', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/peers/connected', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/peers/connected");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/peers/connected", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /peers/connected`

*Get current connected peers*

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "address": "127.0.0.1:5673",
        "restApiUrl": "https://example.com",
        "name": "mynode",
        "lastSeen": 1524143059077,
        "connectionType": "Incoming"
      }
    ]
    ```

<h3 id="getconnectedpeers-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Array of peer objects|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getconnectedpeers-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Peer](#schemapeer)]|false|none|none|
|» address|string|true|none|none|
|» restApiUrl|string¦null|false|none|none|
|» name|string¦null|false|none|none|
|» lastSeen|[Timestamp](#schematimestamp)(int64)|false|none|Basic timestamp definition|
|» connectionType|string¦null|false|none|none|

##### Enumerated Values

|Property|Value|
|---|---|
|connectionType|Incoming|
|connectionType|Outgoing|

<aside class="success">
This operation does not require authentication
</aside>

### connectToPeer

<a id="opIdconnectToPeer"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /peers/connect \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /peers/connect HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"127.0.0.1:5673"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/peers/connect',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/peers/connect',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/peers/connect', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/peers/connect', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/peers/connect");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/peers/connect", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /peers/connect`

*Add address to peers list*

> Body parameter

=== "json"

    ```json
    "\"127.0.0.1:5673\""
    ```

<h3 id="connecttopeer-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|

> Example responses

> default Response

=== "json"

    ```json
    {
      "error": 500,
      "reason": "Internal server error",
      "detail": "string"
    }
    ```

<h3 id="connecttopeer-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Attempt to connect to the peer|None|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### getBlacklistedPeers

<a id="opIdgetBlacklistedPeers"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /peers/blacklisted \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /peers/blacklisted HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/peers/blacklisted',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/peers/blacklisted',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/peers/blacklisted', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/peers/blacklisted', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/peers/blacklisted");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/peers/blacklisted", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /peers/blacklisted`

*Get blacklisted peers*

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "addresses": [
        "string"
      ]
    }
    ```

<h3 id="getblacklistedpeers-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Array of the addresses|[BlacklistedPeers](#schemablacklistedpeers)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getPeersStatus

<a id="opIdgetPeersStatus"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /peers/status \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /peers/status HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/peers/status',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/peers/status',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/peers/status', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/peers/status', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/peers/status");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/peers/status", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /peers/status`

*Get last incoming message timestamp and current network time*

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "lastIncomingMessage": 1524143059077,
        "currentNetworkTime": 1524143059077
      }
    ]
    ```

<h3 id="getpeersstatus-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Network status|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getpeersstatus-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[PeersStatus](#schemapeersstatus)]|false|none|none|
|» lastIncomingMessage|[Timestamp](#schematimestamp)(int64)|true|none|Basic timestamp definition|
|» currentNetworkTime|[Timestamp](#schematimestamp)(int64)|true|none|Basic timestamp definition|

<aside class="success">
This operation does not require authentication
</aside>

### getPeersSyncInfo

<a id="opIdgetPeersSyncInfo"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /peers/syncInfo \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /peers/syncInfo HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/peers/syncInfo',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/peers/syncInfo',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/peers/syncInfo', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/peers/syncInfo', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/peers/syncInfo");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/peers/syncInfo", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /peers/syncInfo`

*Get sync info reported by peers, including versions, current status and height (if available)*

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "address": "127.0.0.1:5673",
        "mode": {
          "state": "utxo",
          "verifyingTransactions": true,
          "fullBlocksSuffix": 2880
        },
        "version": "4.0.16",
        "status": "Older",
        "height": 65780
      }
    ]
    ```

<h3 id="getpeerssyncinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Network status|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getpeerssyncinfo-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[SyncInfo](#schemasyncinfo)]|false|none|none|
|» address|string|true|none|none|
|» mode|[PeerMode](#schemapeermode)|true|none|none|
|»» state|string|true|none|none|
|»» verifyingTransactions|boolean|true|none|none|
|»» fullBlocksSuffix|integer|true|none|none|
|» version|string|true|none|none|
|» status|string|true|none|none|
|» height|integer|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

### getPeersTrackInfo

<a id="opIdgetPeersTrackInfo"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /peers/trackInfo \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /peers/trackInfo HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/peers/trackInfo',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/peers/trackInfo',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/peers/trackInfo', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/peers/trackInfo', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/peers/trackInfo");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/peers/trackInfo", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /peers/trackInfo`

*Get track info reported by peers, including count of invalid modifiers and details of requested and received modifiers*

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "invalidModifierApproxSize": 65780,
        "requested": {
          "property1": {
            "property1": {
              "address": "127.0.0.1:5673",
              "version": "4.0.26",
              "checks": 4
            },
            "property2": {
              "address": "127.0.0.1:5673",
              "version": "4.0.26",
              "checks": 4
            }
          },
          "property2": {
            "property1": {
              "address": "127.0.0.1:5673",
              "version": "4.0.26",
              "checks": 4
            },
            "property2": {
              "address": "127.0.0.1:5673",
              "version": "4.0.26",
              "checks": 4
            }
          }
        },
        "received": {
          "property1": {
            "property1": {
              "address": "127.0.0.1:5673",
              "version": "4.0.26",
              "lastMessage": 1524143059077
            },
            "property2": {
              "address": "127.0.0.1:5673",
              "version": "4.0.26",
              "lastMessage": 1524143059077
            }
          },
          "property2": {
            "property1": {
              "address": "127.0.0.1:5673",
              "version": "4.0.26",
              "lastMessage": 1524143059077
            },
            "property2": {
              "address": "127.0.0.1:5673",
              "version": "4.0.26",
              "lastMessage": 1524143059077
            }
          }
        }
      }
    ]
    ```

<h3 id="getpeerstrackinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Network status|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getpeerstrackinfo-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[TrackInfo](#schematrackinfo)]|false|none|none|
|» invalidModifierApproxSize|integer|true|none|none|
|» requested|object|true|none|Currently requested modifiers|
|»» **additionalProperties**|[RequestedInfoByModifierId](#schemarequestedinfobymodifierid)|false|none|none|
|»»» **additionalProperties**|[RequestedInfo](#schemarequestedinfo)|false|none|none|
|»»»» address|string|false|none|none|
|»»»» version|string|false|none|none|
|»»»» checks|integer|true|none|How many times we checked for modifier delivery status|
|» received|object|true|none|Received modifiers|
|»» **additionalProperties**|[ConnectedPeerByModifierId](#schemaconnectedpeerbymodifierid)|false|none|none|
|»»» **additionalProperties**|[ConnectedPeer](#schemaconnectedpeer)|false|none|none|
|»»»» address|string|true|none|none|
|»»»» version|string|false|none|none|
|»»»» lastMessage|[Timestamp](#schematimestamp)(int64)|false|none|Basic timestamp definition|

<aside class="success">
This operation does not require authentication
</aside>

## utils

### getRandomSeed

<a id="opIdgetRandomSeed"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utils/seed \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /utils/seed HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/utils/seed',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/utils/seed',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/utils/seed', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utils/seed', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utils/seed");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utils/seed", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utils/seed`

*Get random seed of 32 bytes*

> Example responses

> 200 Response

=== "json"

    ```json
    "\"7e1e79dd4936bdc7d09f4ba9212849136b589fba4bcf4263a0961a95b65d08cb16\""
    ```

<h3 id="getrandomseed-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Base16-encoded 32 byte seed|string|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### CheckAddressValidityWithGet

<a id="opIdCheckAddressValidityWithGet"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utils/address/{address} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /utils/address/{address} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/utils/address/{address}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/utils/address/{address}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/utils/address/{address}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utils/address/{address}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utils/address/{address}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utils/address/{address}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utils/address/{address}`

*Check address validity (prefer POST request as addresses can be too big)*

<h3 id="checkaddressvaliditywithget-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|[ErgoAddress](#schemaergoaddress)|true|address to check|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "isValid": true,
      "error": "string"
    }
    ```

<h3 id="checkaddressvaliditywithget-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Address validity with validation error|[AddressValidity](#schemaaddressvalidity)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### CheckAddressValidity

<a id="opIdCheckAddressValidity"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /utils/address \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /utils/address HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/utils/address',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/utils/address',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/utils/address', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/utils/address', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utils/address");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/utils/address", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /utils/address`

*Checks address validity*

> Body parameter

=== "json"

    ```json
    "\"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt\""
    ```

<h3 id="checkaddressvalidity-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|address to check|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "isValid": true,
      "error": "string"
    }
    ```

<h3 id="checkaddressvalidity-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Address validity with validation error|[AddressValidity](#schemaaddressvalidity)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### AddressToRaw

<a id="opIdAddressToRaw"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utils/addressToRaw/{address} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /utils/addressToRaw/{address} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/utils/addressToRaw/{address}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/utils/addressToRaw/{address}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/utils/addressToRaw/{address}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utils/addressToRaw/{address}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utils/addressToRaw/{address}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utils/addressToRaw/{address}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utils/addressToRaw/{address}`

*Convert Pay-To-Public-Key Address to raw representation (hex-encoded serialized curve point)*

<h3 id="addresstoraw-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|[ErgoAddress](#schemaergoaddress)|true|address to extract public key from|

> Example responses

> 200 Response

=== "json"

    ```json
    "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
    ```

<h3 id="addresstoraw-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|hex-encoded public key (serialized secp256k1 element)|string|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### RawToAddress

<a id="opIdRawToAddress"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utils/rawToAddress/{pubkeyHex} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /utils/rawToAddress/{pubkeyHex} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/utils/rawToAddress/{pubkeyHex}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/utils/rawToAddress/{pubkeyHex}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/utils/rawToAddress/{pubkeyHex}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utils/rawToAddress/{pubkeyHex}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utils/rawToAddress/{pubkeyHex}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utils/rawToAddress/{pubkeyHex}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utils/rawToAddress/{pubkeyHex}`

*Generate Pay-To-Public-Key address from hex-encoded raw pubkey (secp256k1 serialized point)*

<h3 id="rawtoaddress-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pubkeyHex|path|string|true|public key to get address from|

> Example responses

> 200 Response

=== "json"

    ```json
    "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    ```

<h3 id="rawtoaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Pay-to-public-key (P2PK) address|[ErgoAddress](#schemaergoaddress)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### ErgoTreeToAddressWithGet

<a id="opIdErgoTreeToAddressWithGet"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utils/ergoTreeToAddress/{ergoTreeHex} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /utils/ergoTreeToAddress/{ergoTreeHex} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/utils/ergoTreeToAddress/{ergoTreeHex}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/utils/ergoTreeToAddress/{ergoTreeHex}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/utils/ergoTreeToAddress/{ergoTreeHex}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utils/ergoTreeToAddress/{ergoTreeHex}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utils/ergoTreeToAddress/{ergoTreeHex}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utils/ergoTreeToAddress/{ergoTreeHex}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utils/ergoTreeToAddress/{ergoTreeHex}`

*Generate Ergo address from hex-encoded ErgoTree (prefer POST request as ErgoTree can be too big)*

<h3 id="ergotreetoaddresswithget-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|ergoTreeHex|path|string|true|ErgoTree to derive an address from|

> Example responses

> 200 Response

=== "json"

    ```json
    "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    ```

<h3 id="ergotreetoaddresswithget-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ergo address|[ErgoAddress](#schemaergoaddress)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### ErgoTreeToAddress

<a id="opIdErgoTreeToAddress"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /utils/ergoTreeToAddress \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /utils/ergoTreeToAddress HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/utils/ergoTreeToAddress',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/utils/ergoTreeToAddress',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/utils/ergoTreeToAddress', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/utils/ergoTreeToAddress', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utils/ergoTreeToAddress");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/utils/ergoTreeToAddress", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /utils/ergoTreeToAddress`

*Generate Ergo address from hex-encoded ErgoTree*

> Body parameter

=== "json"

    ```json
    "\"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301\""
    ```

<h3 id="ergotreetoaddress-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|ErgoTree hex to derive an address from|

> Example responses

> 200 Response

=== "json"

    ```json
    "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    ```

<h3 id="ergotreetoaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ergo address|[ErgoAddress](#schemaergoaddress)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getRandomSeedWithLength

<a id="opIdgetRandomSeedWithLength"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utils/seed/{length} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /utils/seed/{length} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/utils/seed/{length}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/utils/seed/{length}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/utils/seed/{length}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utils/seed/{length}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utils/seed/{length}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utils/seed/{length}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utils/seed/{length}`

*Generate random seed of specified length in bytes*

<h3 id="getrandomseedwithlength-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|length|path|string|true|seed length in bytes|

> Example responses

> 200 Response

=== "json"

    ```json
    "\"83375fd213cfd7dfd984ce1901d62c302a1db53160b416674c8da1a393a6bbc316\""
    ```

<h3 id="getrandomseedwithlength-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Base16-encoded N byte seed|string|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### hashBlake2b

<a id="opIdhashBlake2b"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /utils/hash/blake2b \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /utils/hash/blake2b HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"7yaASMijGEGTbttYHg1MrXnWB8EbzjJnFLSWvmNoHrXV"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/utils/hash/blake2b',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/utils/hash/blake2b',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/utils/hash/blake2b', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/utils/hash/blake2b', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utils/hash/blake2b");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/utils/hash/blake2b", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /utils/hash/blake2b`

*Return Blake2b hash of specified message*

> Body parameter

=== "json"

    ```json
    "\"7yaASMijGEGTbttYHg1MrXnWB8EbzjJnFLSWvmNoHrXV\""
    ```

<h3 id="hashblake2b-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    "\"6ed54addddaf10fe8fcda330bd443a57914fbce38a9fa27248b07e361cc76a41\""
    ```

<h3 id="hashblake2b-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Base16-encoded 32 byte hash|string|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

## wallet

### walletInit

<a id="opIdwalletInit"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/init \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/init HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "pass": "string",
      "mnemonicPass": "string"
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/init',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/init',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/init', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/init', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/init");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/init", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/init`

*Initialize new wallet with randomly generated seed*

> Body parameter

=== "json"

    ```json
    {
      "pass": "string",
      "mnemonicPass": "string"
    }
    ```

<h3 id="walletinit-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[InitWallet](#schemainitwallet)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "mnemonic": "string"
    }
    ```

<h3 id="walletinit-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|New wallet with randomly generated seed created successfully|[InitWalletResult](#schemainitwalletresult)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletRestore

<a id="opIdwalletRestore"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/restore \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/restore HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "pass": "string",
      "mnemonic": "string",
      "mnemonicPass": "string",
      "usePre1627KeyDerivation": true
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/restore',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/restore',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/restore', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/restore', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/restore");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/restore", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/restore`

*Create new wallet from existing mnemonic seed*

> Body parameter

=== "json"

    ```json
    {
      "pass": "string",
      "mnemonic": "string",
      "mnemonicPass": "string",
      "usePre1627KeyDerivation": true
    }
    ```

<h3 id="walletrestore-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RestoreWallet](#schemarestorewallet)|true|none|

> Example responses

> default Response

=== "json"

    ```json
    {
      "error": 500,
      "reason": "Internal server error",
      "detail": "string"
    }
    ```

<h3 id="walletrestore-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Wallet restored successfully|None|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### checkSeed

<a id="opIdcheckSeed"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/check \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/check HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "mnemonic": "string",
      "mnemonicPass": "string"
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/check',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/check',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/check', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/check', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/check");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/check", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/check`

*Check whether mnemonic phrase is corresponding to the wallet seed*

> Body parameter

=== "json"

    ```json
    {
      "mnemonic": "string",
      "mnemonicPass": "string"
    }
    ```

<h3 id="checkseed-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CheckWallet](#schemacheckwallet)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "matched": true
    }
    ```

<h3 id="checkseed-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Whether passphrase match wallet|[PassphraseMatch](#schemapassphrasematch)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletUnlock

<a id="opIdwalletUnlock"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/unlock \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/unlock HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "pass": "string"
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/unlock',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/unlock',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/unlock', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/unlock', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/unlock");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/unlock", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/unlock`

*Unlock wallet*

> Body parameter

=== "json"

    ```json
    {
      "pass": "string"
    }
    ```

<h3 id="walletunlock-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UnlockWallet](#schemaunlockwallet)|true|none|

> Example responses

> default Response

=== "json"

    ```json
    {
      "error": 500,
      "reason": "Internal server error",
      "detail": "string"
    }
    ```

<h3 id="walletunlock-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Wallet unlocked successfully|None|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletLock

<a id="opIdwalletLock"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /wallet/lock \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /wallet/lock HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/lock',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/wallet/lock',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/wallet/lock', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/wallet/lock', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/lock");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/wallet/lock", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /wallet/lock`

*Lock wallet*

> Example responses

> default Response

=== "json"

    ```json
    {
      "error": 500,
      "reason": "Internal server error",
      "detail": "string"
    }
    ```

<h3 id="walletlock-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Wallet locked successfully|None|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletRescan

<a id="opIdwalletRescan"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/rescan \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/rescan HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "fromHeight": 0
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/rescan',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/rescan',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/rescan', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/rescan', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/rescan");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/rescan", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/rescan`

*Rescan wallet (all the available full blocks). When fromHeight is set wallet would not see any boxes below it.*

> Body parameter

=== "json"

    ```json
    {
      "fromHeight": 0
    }
    ```

<h3 id="walletrescan-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» fromHeight|body|integer(int32)|true|none|

> Example responses

> default Response

=== "json"

    ```json
    {
      "error": 500,
      "reason": "Internal server error",
      "detail": "string"
    }
    ```

<h3 id="walletrescan-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Wallet rescanned|None|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### getWalletStatus

<a id="opIdgetWalletStatus"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /wallet/status \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /wallet/status HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/status',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/wallet/status',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/wallet/status', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/wallet/status', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/status");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/wallet/status", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /wallet/status`

*Get wallet status*

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "isInitialized": true,
      "isUnlocked": true,
      "changeAddress": "3WzCFq7mkykKqi4Ykdk8BK814tkh6EsPmA42pQZxU2NRwSDgd6yB",
      "walletHeight": 0,
      "error": "string"
    }
    ```

<h3 id="getwalletstatus-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Wallet status|[WalletStatus](#schemawalletstatus)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletUpdateChangeAddress

<a id="opIdwalletUpdateChangeAddress"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/updateChangeAddress \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/updateChangeAddress HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/updateChangeAddress',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/updateChangeAddress',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/updateChangeAddress', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/updateChangeAddress', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/updateChangeAddress");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/updateChangeAddress", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/updateChangeAddress`

*Update address to be used to send change to*

> Body parameter

=== "json"

    ```json
    "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    ```

<h3 id="walletupdatechangeaddress-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ErgoAddress](#schemaergoaddress)|true|none|

> Example responses

> default Response

=== "json"

    ```json
    {
      "error": 500,
      "reason": "Internal server error",
      "detail": "string"
    }
    ```

<h3 id="walletupdatechangeaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Change address updated successfully|None|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletDeriveKey

<a id="opIdwalletDeriveKey"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/deriveKey \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/deriveKey HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "derivationPath": "m/1/2"
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/deriveKey',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/deriveKey',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/deriveKey', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/deriveKey', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/deriveKey");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/deriveKey", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/deriveKey`

*Derive new key according to a provided path*

> Body parameter

=== "json"

    ```json
    {
      "derivationPath": "m/1/2"
    }
    ```

<h3 id="walletderivekey-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DeriveKey](#schemaderivekey)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    }
    ```

<h3 id="walletderivekey-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Resulted address|[DeriveKeyResult](#schemaderivekeyresult)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletDeriveNextKey

<a id="opIdwalletDeriveNextKey"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /wallet/deriveNextKey \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /wallet/deriveNextKey HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/deriveNextKey',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/wallet/deriveNextKey',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/wallet/deriveNextKey', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/wallet/deriveNextKey', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/deriveNextKey");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/wallet/deriveNextKey", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /wallet/deriveNextKey`

*Derive next key*

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "derivationPath": "m/1/2",
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    }
    ```

<h3 id="walletderivenextkey-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Resulted secret path and address|[DeriveNextKeyResult](#schemaderivenextkeyresult)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletBalances

<a id="opIdwalletBalances"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /wallet/balances \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /wallet/balances HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/balances',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/wallet/balances',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/wallet/balances', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/wallet/balances', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/balances");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/wallet/balances", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /wallet/balances`

*Get total amount of confirmed Ergo tokens and assets*

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "height": 0,
      "balance": 0,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ]
    }
    ```

<h3 id="walletbalances-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Get total amount of confirmed Ergo tokens and assets|[BalancesSnapshot](#schemabalancessnapshot)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletTransactions

<a id="opIdwalletTransactions"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /wallet/transactions \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /wallet/transactions HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/transactions',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/wallet/transactions',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/wallet/transactions', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/wallet/transactions', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/transactions");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/wallet/transactions", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /wallet/transactions`

*Get a list of all wallet-related transactions*

<h3 id="wallettransactions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|minInclusionHeight|query|integer(int32)|false|Minimal tx inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximal tx inclusion height|
|minConfirmations|query|integer(int32)|false|Minimal confirmations number|
|maxConfirmations|query|integer(int32)|false|Maximal confirmations number|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "inclusionHeight": 20998,
        "numConfirmations": 20998,
        "scans": [
          1
        ],
        "size": 0
      }
    ]
    ```

<h3 id="wallettransactions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all wallet-related transactions|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="wallettransactions-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WalletTransaction](#schemawallettransaction)]|false|none|[Transaction augmented with some useful information]|
|» id|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|» inputs|[[ErgoTransactionInput](#schemaergotransactioninput)]|true|none|Transaction inputs|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» spendingProof|[SpendingProof](#schemaspendingproof)|true|none|Spending proof for transaction input|
|»»» proofBytes|[SpendingProofBytes](#schemaspendingproofbytes)(base16)|true|none|Base16-encoded spending proofs|
|»»» extension|object|true|none|Variables to be put into context|
|»»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» dataInputs|[[ErgoTransactionDataInput](#schemaergotransactiondatainput)]|true|none|Transaction data inputs|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» outputs|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|Transaction outputs|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|» numConfirmations|integer(int32)|true|none|Number of transaction confirmations|
|» scans|[integer]|true|none|Scan identifiers the transaction relates to|
|» size|integer(int32)|false|none|Size in bytes|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletGetTransaction

<a id="opIdwalletGetTransaction"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /wallet/transactionById?id=string \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /wallet/transactionById?id=string HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/transactionById?id=string',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/wallet/transactionById',
      params: {
      'id' => 'string'
    }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/wallet/transactionById', params={
      'id': 'string'
    }, headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/wallet/transactionById', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/transactionById?id=string");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/wallet/transactionById", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /wallet/transactionById`

*Get wallet-related transaction by id*

<h3 id="walletgettransaction-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|query|string|true|Transaction id|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "inclusionHeight": 20998,
        "numConfirmations": 20998,
        "scans": [
          1
        ],
        "size": 0
      }
    ]
    ```

<h3 id="walletgettransaction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Wallet-related transaction|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Transaction with specified id not found in wallet|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="walletgettransaction-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WalletTransaction](#schemawallettransaction)]|false|none|[Transaction augmented with some useful information]|
|» id|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|» inputs|[[ErgoTransactionInput](#schemaergotransactioninput)]|true|none|Transaction inputs|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» spendingProof|[SpendingProof](#schemaspendingproof)|true|none|Spending proof for transaction input|
|»»» proofBytes|[SpendingProofBytes](#schemaspendingproofbytes)(base16)|true|none|Base16-encoded spending proofs|
|»»» extension|object|true|none|Variables to be put into context|
|»»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» dataInputs|[[ErgoTransactionDataInput](#schemaergotransactiondatainput)]|true|none|Transaction data inputs|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» outputs|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|Transaction outputs|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|» numConfirmations|integer(int32)|true|none|Number of transaction confirmations|
|» scans|[integer]|true|none|Scan identifiers the transaction relates to|
|» size|integer(int32)|false|none|Size in bytes|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletTransactionsByScanId

<a id="opIdwalletTransactionsByScanId"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /wallet/transactionsByScanId/{scanId} \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /wallet/transactionsByScanId/{scanId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/transactionsByScanId/{scanId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/wallet/transactionsByScanId/{scanId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/wallet/transactionsByScanId/{scanId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/wallet/transactionsByScanId/{scanId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/transactionsByScanId/{scanId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/wallet/transactionsByScanId/{scanId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /wallet/transactionsByScanId/{scanId}`

*Get scan-related transactions by scan id*

<h3 id="wallettransactionsbyscanid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scanId|path|integer(int32)|true|identifier of a scan|
|minInclusionHeight|query|integer(int32)|false|Minimal tx inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximal tx inclusion height|
|minConfirmations|query|integer(int32)|false|Minimal confirmations number|
|maxConfirmations|query|integer(int32)|false|Maximal confirmations number|
|includeUnconfirmed|query|boolean|false|Include transactions from mempool|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "inclusionHeight": 20998,
        "numConfirmations": 20998,
        "scans": [
          1
        ],
        "size": 0
      }
    ]
    ```

<h3 id="wallettransactionsbyscanid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Scan-related transactions|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Transactions with related scan id not found in wallet|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="wallettransactionsbyscanid-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WalletTransaction](#schemawallettransaction)]|false|none|[Transaction augmented with some useful information]|
|» id|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|» inputs|[[ErgoTransactionInput](#schemaergotransactioninput)]|true|none|Transaction inputs|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» spendingProof|[SpendingProof](#schemaspendingproof)|true|none|Spending proof for transaction input|
|»»» proofBytes|[SpendingProofBytes](#schemaspendingproofbytes)(base16)|true|none|Base16-encoded spending proofs|
|»»» extension|object|true|none|Variables to be put into context|
|»»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» dataInputs|[[ErgoTransactionDataInput](#schemaergotransactiondatainput)]|true|none|Transaction data inputs|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» outputs|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|Transaction outputs|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|» numConfirmations|integer(int32)|true|none|Number of transaction confirmations|
|» scans|[integer]|true|none|Scan identifiers the transaction relates to|
|» size|integer(int32)|false|none|Size in bytes|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletBoxes

<a id="opIdwalletBoxes"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /wallet/boxes \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /wallet/boxes HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/boxes',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/wallet/boxes',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/wallet/boxes', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/wallet/boxes', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/boxes");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/wallet/boxes", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /wallet/boxes`

*Get a list of all wallet-related boxes, both spent and unspent. Set minConfirmations to -1 to get mempool boxes included.*

<h3 id="walletboxes-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|minConfirmations|query|integer(int32)|false|Minimal number of confirmations, -1 means we consider unconfirmed|
|maxConfirmations|query|integer(int32)|false|Maximum number of confirmations, -1 means unlimited|
|minInclusionHeight|query|integer(int32)|false|Minimal box inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximum box inclusion height, -1 means unlimited|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "box": {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        },
        "confirmationsNum": 147,
        "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
        "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingHeight": 147,
        "inclusionHeight": 147,
        "onchain": true,
        "spent": false,
        "creationOutIndex": 2,
        "scans": [
          1
        ]
      }
    ]
    ```

<h3 id="walletboxes-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all wallet-related boxes|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="walletboxes-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WalletBox](#schemawalletbox)]|false|none|none|
|» box|[ErgoTransactionOutput](#schemaergotransactionoutput)|true|none|none|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|» creationTransaction|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingTransaction|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|» spent|boolean|true|none|A flag signalling whether the box was spent|
|» creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|» scans|[integer]|true|none|Scan identifiers the box relates to|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletBoxesCollect

<a id="opIdwalletBoxesCollect"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/boxes/collect \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/boxes/collect HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "targetAssets": [
        [
          "string",
          "string"
        ]
      ],
      "targetBalance": 0
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/boxes/collect',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/boxes/collect',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/boxes/collect', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/boxes/collect', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/boxes/collect");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/boxes/collect", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/boxes/collect`

*Get a list of collected boxes.*

> Body parameter

=== "json"

    ```json
    {
      "targetAssets": [
        [
          "string",
          "string"
        ]
      ],
      "targetBalance": 0
    }
    ```

<h3 id="walletboxescollect-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BoxesRequestHolder](#schemaboxesrequestholder)|true|This API method recieves balance and assets, according to which, it's collecting result|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "box": {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        },
        "confirmationsNum": 147,
        "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
        "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingHeight": 147,
        "inclusionHeight": 147,
        "onchain": true,
        "spent": false,
        "creationOutIndex": 2,
        "scans": [
          1
        ]
      }
    ]
    ```

<h3 id="walletboxescollect-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all collected boxes|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="walletboxescollect-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WalletBox](#schemawalletbox)]|false|none|none|
|» box|[ErgoTransactionOutput](#schemaergotransactionoutput)|true|none|none|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|» creationTransaction|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingTransaction|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|» spent|boolean|true|none|A flag signalling whether the box was spent|
|» creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|» scans|[integer]|true|none|Scan identifiers the box relates to|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletUnspentBoxes

<a id="opIdwalletUnspentBoxes"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /wallet/boxes/unspent \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /wallet/boxes/unspent HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/boxes/unspent',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/wallet/boxes/unspent',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/wallet/boxes/unspent', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/wallet/boxes/unspent', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/boxes/unspent");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/wallet/boxes/unspent", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /wallet/boxes/unspent`

*Get a list of unspent boxes. Set minConfirmations to -1 to have mempool boxes considered.*

<h3 id="walletunspentboxes-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|minConfirmations|query|integer(int32)|false|Minimal number of confirmations, -1 means we consider unconfirmed|
|maxConfirmations|query|integer(int32)|false|Maximum number of confirmations, -1 means unlimited|
|minInclusionHeight|query|integer(int32)|false|Minimal box inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximum box inclusion height, -1 means unlimited|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "box": {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        },
        "confirmationsNum": 147,
        "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
        "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingHeight": 147,
        "inclusionHeight": 147,
        "onchain": true,
        "spent": false,
        "creationOutIndex": 2,
        "scans": [
          1
        ]
      }
    ]
    ```

<h3 id="walletunspentboxes-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of unspent boxes|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="walletunspentboxes-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WalletBox](#schemawalletbox)]|false|none|none|
|» box|[ErgoTransactionOutput](#schemaergotransactionoutput)|true|none|none|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|» creationTransaction|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingTransaction|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|» spent|boolean|true|none|A flag signalling whether the box was spent|
|» creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|» scans|[integer]|true|none|Scan identifiers the box relates to|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletBalancesUnconfirmed

<a id="opIdwalletBalancesUnconfirmed"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /wallet/balances/withUnconfirmed \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /wallet/balances/withUnconfirmed HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/balances/withUnconfirmed',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/wallet/balances/withUnconfirmed',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/wallet/balances/withUnconfirmed', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/wallet/balances/withUnconfirmed', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/balances/withUnconfirmed");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/wallet/balances/withUnconfirmed", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /wallet/balances/withUnconfirmed`

*Get summary amount of confirmed plus unconfirmed Ergo tokens and assets*

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "height": 0,
      "balance": 0,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ]
    }
    ```

<h3 id="walletbalancesunconfirmed-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Get summary amount of confirmed plus unconfirmed Ergo tokens and assets|[BalancesSnapshot](#schemabalancessnapshot)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletAddresses

<a id="opIdwalletAddresses"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /wallet/addresses \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /wallet/addresses HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/addresses',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/wallet/addresses',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/wallet/addresses', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/wallet/addresses', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/addresses");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/wallet/addresses", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /wallet/addresses`

*Get wallet addresses*

> Example responses

> 200 Response

=== "json"

    ```json
    [
      "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    ]
    ```

<h3 id="walletaddresses-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|String with encoded wallet addresses|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="walletaddresses-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ErgoAddress](#schemaergoaddress)]|false|none|[Encoded Ergo Address]|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletTransactionGenerate

<a id="opIdwalletTransactionGenerate"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/transaction/generate \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/transaction/generate HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "requests": [
        {
          "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
          "value": 1,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "registers": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          }
        }
      ],
      "fee": 1000000,
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/transaction/generate',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/transaction/generate',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/transaction/generate', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/transaction/generate', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/transaction/generate");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/transaction/generate", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/transaction/generate`

*Generate arbitrary transaction from array of requests.*

> Body parameter

=== "json"

    ```json
    {
      "requests": [
        {
          "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
          "value": 1,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "registers": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          }
        }
      ],
      "fee": 1000000,
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }
    ```

<h3 id="wallettransactiongenerate-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RequestsHolder](#schemarequestsholder)|true|This API method receives a sequence of requests as an input. Each request will produce an output of the resulting transaction (with fee output created automatically). Currently supported types of requests are payment and asset issuance requests. An example for a transaction with requests of both kinds is provided below. Please note that for the payment request "assets" and "registers" fields are not needed. For asset issuance request, "registers" field is not needed.|

##### Detailed descriptions

**body**: This API method receives a sequence of requests as an input. Each request will produce an output of the resulting transaction (with fee output created automatically). Currently supported types of requests are payment and asset issuance requests. An example for a transaction with requests of both kinds is provided below. Please note that for the payment request "assets" and "registers" fields are not needed. For asset issuance request, "registers" field is not needed.
You may specify boxes to spend by providing them in "inputsRaw". Please note you need to have strict equality between input and output total amounts of Ergs in this case. If you want wallet to pick up the boxes, leave "inputsRaw" empty.

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "size": 0
    }
    ```

<h3 id="wallettransactiongenerate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Generated Ergo transaction|[ErgoTransaction](#schemaergotransaction)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad transaction request|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletUnsignedTransactionGenerate

<a id="opIdwalletUnsignedTransactionGenerate"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/transaction/generateUnsigned \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/transaction/generateUnsigned HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "requests": [
        {
          "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
          "value": 1,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "registers": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          }
        }
      ],
      "fee": 1000000,
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/transaction/generateUnsigned',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/transaction/generateUnsigned',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/transaction/generateUnsigned', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/transaction/generateUnsigned', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/transaction/generateUnsigned");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/transaction/generateUnsigned", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/transaction/generateUnsigned`

*Generate unsigned transaction from array of requests.*

> Body parameter

=== "json"

    ```json
    {
      "requests": [
        {
          "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
          "value": 1,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "registers": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          }
        }
      ],
      "fee": 1000000,
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }
    ```

<h3 id="walletunsignedtransactiongenerate-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RequestsHolder](#schemarequestsholder)|true|The same as /wallet/transaction/generate but generates unsigned transaction.|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extension": {
            "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ]
    }
    ```

<h3 id="walletunsignedtransactiongenerate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Generated unsigned Ergo transaction|[UnsignedErgoTransaction](#schemaunsignedergotransaction)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad transaction request|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletTransactionSign

<a id="opIdwalletTransactionSign"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/transaction/sign \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/transaction/sign HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "tx": {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ]
      },
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ],
      "hints": {
        "secretHints": [
          {
            "01": [
              {
                "hint": "cmtWithSecret",
                "pubkey": {
                  "op": -51,
                  "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
                },
                "position": "0-1",
                "type": "dlog",
                "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
                "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
              }
            ]
          }
        ],
        "publicHints": [
          {
            "01": [
              {
                "hint": "cmtWithSecret",
                "pubkey": {
                  "op": -51,
                  "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
                },
                "position": "0-1",
                "type": "dlog",
                "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
                "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
              }
            ]
          }
        ]
      },
      "secrets": {
        "dlog": [
          "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
        ],
        "dht": [
          {
            "secret": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
            "g": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "h": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "u": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "v": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
          }
        ]
      }
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/transaction/sign',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/transaction/sign',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/transaction/sign', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/transaction/sign', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/transaction/sign");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/transaction/sign", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/transaction/sign`

*Sign arbitrary unsigned transaction with wallet secrets and also secrets provided.*

> Body parameter

=== "json"

    ```json
    {
      "tx": {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ]
      },
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ],
      "hints": {
        "secretHints": [
          {
            "01": [
              {
                "hint": "cmtWithSecret",
                "pubkey": {
                  "op": -51,
                  "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
                },
                "position": "0-1",
                "type": "dlog",
                "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
                "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
              }
            ]
          }
        ],
        "publicHints": [
          {
            "01": [
              {
                "hint": "cmtWithSecret",
                "pubkey": {
                  "op": -51,
                  "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
                },
                "position": "0-1",
                "type": "dlog",
                "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
                "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
              }
            ]
          }
        ]
      },
      "secrets": {
        "dlog": [
          "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
        ],
        "dht": [
          {
            "secret": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
            "g": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "h": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "u": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "v": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
          }
        ]
      }
    }
    ```

<h3 id="wallettransactionsign-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TransactionSigningRequest](#schematransactionsigningrequest)|true|With this API method an arbitrary unsigned transaction can be signed with secrets provided or stored in the wallet. Both DLOG and Diffie-Hellman tuple secrets are supported.|

##### Detailed descriptions

**body**: With this API method an arbitrary unsigned transaction can be signed with secrets provided or stored in the wallet. Both DLOG and Diffie-Hellman tuple secrets are supported.
Please note that the unsigned transaction contains only identifiers of inputs and data inputs. If the node holds UTXO set, it is able to extract boxes needed. Otherwise, input (and data-input) boxes can be provided in "inputsRaw" and "dataInputsRaw" fields.

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "size": 0
    }
    ```

<h3 id="wallettransactionsign-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Generated Ergo transaction|[ErgoTransaction](#schemaergotransaction)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad transaction request|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletTransactionGenerateAndSend

<a id="opIdwalletTransactionGenerateAndSend"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/transaction/send \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/transaction/send HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "requests": [
        {
          "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
          "value": 1,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "registers": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          }
        }
      ],
      "fee": 1000000,
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/transaction/send',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/transaction/send',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/transaction/send', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/transaction/send', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/transaction/send");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/transaction/send", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/transaction/send`

*Generate and send arbitrary transaction*

> Body parameter

=== "json"

    ```json
    {
      "requests": [
        {
          "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
          "value": 1,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "registers": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          }
        }
      ],
      "fee": 1000000,
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }
    ```

<h3 id="wallettransactiongenerateandsend-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RequestsHolder](#schemarequestsholder)|true|See description of /wallet/transaction/generate|

> Example responses

> 200 Response

=== "json"

    ```json
    "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

<h3 id="wallettransactiongenerateandsend-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Identifier of an Ergo transaction generated|[TransactionId](#schematransactionid)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad transaction request|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletPaymentTransactionGenerateAndSend

<a id="opIdwalletPaymentTransactionGenerateAndSend"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/payment/send \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/payment/send HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '[
      {
        "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
        "value": 1,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "registers": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        }
      }
    ]';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/payment/send',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/payment/send',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/payment/send', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/payment/send', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/payment/send");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/payment/send", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/payment/send`

*Generate and send payment transaction (default fee of 0.001 Erg is used)*

> Body parameter

=== "json"

    ```json
    [
      {
        "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
        "value": 1,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "registers": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        }
      }
    ]
    ```

<h3 id="walletpaymenttransactiongenerateandsend-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PaymentRequest](#schemapaymentrequest)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

<h3 id="walletpaymenttransactiongenerateandsend-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Identifier of an Ergo transaction generated|[TransactionId](#schematransactionid)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad payment request|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### walletGetPrivateKey

<a id="opIdwalletGetPrivateKey"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/getPrivateKey \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/getPrivateKey HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/getPrivateKey',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/getPrivateKey',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/getPrivateKey', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/getPrivateKey', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/getPrivateKey");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/getPrivateKey", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/getPrivateKey`

*Get the private key corresponding to a known address*

> Body parameter

=== "json"

    ```json
    "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    ```

<h3 id="walletgetprivatekey-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ErgoAddress](#schemaergoaddress)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
    ```

<h3 id="walletgetprivatekey-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully retrieved secret key|[DlogSecret](#schemadlogsecret)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Address not found in wallet database|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### generateCommitments

<a id="opIdgenerateCommitments"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/generateCommitments \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/generateCommitments HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "tx": {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ]
      },
      "secrets": {
        "dlog": [
          "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
        ],
        "dht": [
          {
            "secret": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
            "g": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "h": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "u": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "v": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
          }
        ]
      },
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/generateCommitments',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/generateCommitments',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/generateCommitments', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/generateCommitments', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/generateCommitments");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/generateCommitments", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/generateCommitments`

*Generate signature commitments for inputs of an unsigned transaction*

> Body parameter

=== "json"

    ```json
    {
      "tx": {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ]
      },
      "secrets": {
        "dlog": [
          "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
        ],
        "dht": [
          {
            "secret": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
            "g": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "h": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "u": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "v": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
          }
        ]
      },
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }
    ```

<h3 id="generatecommitments-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[GenerateCommitmentsRequest](#schemageneratecommitmentsrequest)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "secretHints": [
        {
          "01": [
            {
              "hint": "cmtWithSecret",
              "pubkey": {
                "op": -51,
                "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
              },
              "position": "0-1",
              "type": "dlog",
              "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
              "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
            }
          ]
        }
      ],
      "publicHints": [
        {
          "01": [
            {
              "hint": "cmtWithSecret",
              "pubkey": {
                "op": -51,
                "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
              },
              "position": "0-1",
              "type": "dlog",
              "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
              "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
            }
          ]
        }
      ]
    }
    ```

<h3 id="generatecommitments-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Transaction-related hints|[TransactionHintsBag](#schematransactionhintsbag)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Error|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### extractHints

<a id="opIdextractHints"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /wallet/extractHints \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /wallet/extractHints HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "tx": {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "size": 0
      },
      "real": [
        {
          "op": 0,
          "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "condition": true
        }
      ],
      "simulated": [
        {
          "op": 0,
          "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "condition": true
        }
      ],
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/wallet/extractHints',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/wallet/extractHints',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/wallet/extractHints', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/wallet/extractHints', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/wallet/extractHints");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/wallet/extractHints", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /wallet/extractHints`

*Extract hints from a transaction*

> Body parameter

=== "json"

    ```json
    {
      "tx": {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "size": 0
      },
      "real": [
        {
          "op": 0,
          "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "condition": true
        }
      ],
      "simulated": [
        {
          "op": 0,
          "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "condition": true
        }
      ],
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }
    ```

<h3 id="extracthints-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[HintExtractionRequest](#schemahintextractionrequest)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "secretHints": [
        {
          "01": [
            {
              "hint": "cmtWithSecret",
              "pubkey": {
                "op": -51,
                "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
              },
              "position": "0-1",
              "type": "dlog",
              "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
              "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
            }
          ]
        }
      ],
      "publicHints": [
        {
          "01": [
            {
              "hint": "cmtWithSecret",
              "pubkey": {
                "op": -51,
                "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
              },
              "position": "0-1",
              "type": "dlog",
              "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
              "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
            }
          ]
        }
      ]
    }
    ```

<h3 id="extracthints-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Hints for the transaction|[TransactionHintsBag](#schematransactionhintsbag)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Error|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

## mining

### miningRequestBlockCandidate

<a id="opIdminingRequestBlockCandidate"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /mining/candidate \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /mining/candidate HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/mining/candidate',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/mining/candidate',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/mining/candidate', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/mining/candidate', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/mining/candidate");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/mining/candidate", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /mining/candidate`

*Request block candidate*

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "msg": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "b": 987654321,
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "proof": {
        "msgPreimage": "0112e03c6d39d32509855be7cee9b62ff921f7a0cf6883e232474bd5b54d816dd056f846980d34c3b23098bdcf41222f8cdee5219224aa67750055926c3a2310a483accc4f9153e7a760615ea972ac67911cff111f8c17f563d6147205f58f85133ae695d1d4157e4aecdbbb29952cfa42b75129db55bddfce3bc53b8fd5b5465f10d8be8ddda62ed3b86afb0497ff2d381ed884bdae5287d20667def224a28d2b6e3ebfc78709780702c70bd8df0e000000",
        "txProofs": [
          {
            "leaf": "cd665e49c834b0c25574fcb19a158d836f3f2aad8e91ac195f972534c25449b3",
            "levels": [
              [
                "018b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337",
                0
              ]
            ]
          }
        ]
      }
    }
    ```

<h3 id="miningrequestblockcandidate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|External candidate|[WorkMessage](#schemaworkmessage)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### miningRequestBlockCandidateWithMandatoryTransactions

<a id="opIdminingRequestBlockCandidateWithMandatoryTransactions"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /mining/candidateWithTxs \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /mining/candidateWithTxs HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '[
      {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "size": 0
      }
    ]';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/mining/candidateWithTxs',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/mining/candidateWithTxs',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/mining/candidateWithTxs', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/mining/candidateWithTxs', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/mining/candidateWithTxs");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/mining/candidateWithTxs", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /mining/candidateWithTxs`

*Request block candidate*

> Body parameter

=== "json"

    ```json
    [
      {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "size": 0
      }
    ]
    ```

<h3 id="miningrequestblockcandidatewithmandatorytransactions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Transactions](#schematransactions)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "msg": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "b": 987654321,
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "proof": {
        "msgPreimage": "0112e03c6d39d32509855be7cee9b62ff921f7a0cf6883e232474bd5b54d816dd056f846980d34c3b23098bdcf41222f8cdee5219224aa67750055926c3a2310a483accc4f9153e7a760615ea972ac67911cff111f8c17f563d6147205f58f85133ae695d1d4157e4aecdbbb29952cfa42b75129db55bddfce3bc53b8fd5b5465f10d8be8ddda62ed3b86afb0497ff2d381ed884bdae5287d20667def224a28d2b6e3ebfc78709780702c70bd8df0e000000",
        "txProofs": [
          {
            "leaf": "cd665e49c834b0c25574fcb19a158d836f3f2aad8e91ac195f972534c25449b3",
            "levels": [
              [
                "018b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337",
                0
              ]
            ]
          }
        ]
      }
    }
    ```

<h3 id="miningrequestblockcandidatewithmandatorytransactions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|External candidate|[WorkMessage](#schemaworkmessage)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### miningReadMinerRewardAddress

<a id="opIdminingReadMinerRewardAddress"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /mining/rewardAddress \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /mining/rewardAddress HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/mining/rewardAddress',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/mining/rewardAddress',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/mining/rewardAddress', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/mining/rewardAddress', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/mining/rewardAddress");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/mining/rewardAddress", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /mining/rewardAddress`

*Read miner reward address*

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "rewardAddress": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    }
    ```

<h3 id="miningreadminerrewardaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Miner Reward Script (in P2S format)|[RewardAddress](#schemarewardaddress)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### miningReadMinerRewardPubkey

<a id="opIdminingReadMinerRewardPubkey"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /mining/rewardPublicKey \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /mining/rewardPublicKey HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/mining/rewardPublicKey',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/mining/rewardPublicKey',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/mining/rewardPublicKey', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/mining/rewardPublicKey', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/mining/rewardPublicKey");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/mining/rewardPublicKey", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /mining/rewardPublicKey`

*Read public key associated with miner rewards*

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "rewardPubkey": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
    }
    ```

<h3 id="miningreadminerrewardpubkey-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Public key for miner rewards (as hex-encoded secp256k1 point)|[RewardPubKey](#schemarewardpubkey)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### miningSubmitSolution

<a id="opIdminingSubmitSolution"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /mining/solution \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /mining/solution HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
      "n": "0000000000000000",
      "d": 987654321
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/mining/solution',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/mining/solution',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/mining/solution', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/mining/solution', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/mining/solution");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/mining/solution", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /mining/solution`

*Submit solution for current candidate*

> Body parameter

=== "json"

    ```json
    {
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
      "n": "0000000000000000",
      "d": 987654321
    }
    ```

<h3 id="miningsubmitsolution-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PowSolutions](#schemapowsolutions)|true|none|

> Example responses

> 400 Response

=== "json"

    ```json
    {
      "error": 500,
      "reason": "Internal server error",
      "detail": "string"
    }
    ```

<h3 id="miningsubmitsolution-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Solution is valid|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Solution is invalid|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

## utxo

### getBoxesBinaryProof

<a id="opIdgetBoxesBinaryProof"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /utxo/getBoxesBinaryProof \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /utxo/getBoxesBinaryProof HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '[
      "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ]';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/utxo/getBoxesBinaryProof',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/utxo/getBoxesBinaryProof',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/utxo/getBoxesBinaryProof', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/utxo/getBoxesBinaryProof', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utxo/getBoxesBinaryProof");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/utxo/getBoxesBinaryProof", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /utxo/getBoxesBinaryProof`

*Get serialized batch proof for given set of boxes*

> Body parameter

=== "json"

    ```json
    [
      "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ]
    ```

<h3 id="getboxesbinaryproof-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TransactionBoxId](#schematransactionboxid)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

<h3 id="getboxesbinaryproof-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Serialized batch proof|[SerializedAdProof](#schemaserializedadproof)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Prove error|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### getBoxById

<a id="opIdgetBoxById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utxo/byId/{boxId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /utxo/byId/{boxId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/utxo/byId/{boxId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/utxo/byId/{boxId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/utxo/byId/{boxId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utxo/byId/{boxId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utxo/byId/{boxId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utxo/byId/{boxId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utxo/byId/{boxId}`

*Get box contents for a box by a unique identifier.*

<h3 id="getboxbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of a wanted box|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
    ```

<h3 id="getboxbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Box object|[ErgoTransactionOutput](#schemaergotransactionoutput)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Box with this id doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxByIdBinary

<a id="opIdgetBoxByIdBinary"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utxo/byIdBinary/{boxId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /utxo/byIdBinary/{boxId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/utxo/byIdBinary/{boxId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/utxo/byIdBinary/{boxId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/utxo/byIdBinary/{boxId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utxo/byIdBinary/{boxId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utxo/byIdBinary/{boxId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utxo/byIdBinary/{boxId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utxo/byIdBinary/{boxId}`

*Get serialized box from UTXO pool in Base16 encoding by an identifier.*

<h3 id="getboxbyidbinary-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of a wanted box|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "bytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

<h3 id="getboxbyidbinary-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Json containing box identifier and hex-encoded box bytes|[SerializedBox](#schemaserializedbox)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Box with this id doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxWithPoolById

<a id="opIdgetBoxWithPoolById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utxo/withPool/byId/{boxId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /utxo/withPool/byId/{boxId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/utxo/withPool/byId/{boxId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/utxo/withPool/byId/{boxId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/utxo/withPool/byId/{boxId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utxo/withPool/byId/{boxId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utxo/withPool/byId/{boxId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utxo/withPool/byId/{boxId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utxo/withPool/byId/{boxId}`

*Get box contents for a box by a unique identifier, from UTXO set and also the mempool.*

<h3 id="getboxwithpoolbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of a box to obtain|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
    ```

<h3 id="getboxwithpoolbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Box object|[ErgoTransactionOutput](#schemaergotransactionoutput)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Box with this id doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxWithPoolByIds

<a id="opIdgetBoxWithPoolByIds"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /utxo/withPool/byIds \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /utxo/withPool/byIds HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '[
      "string"
    ]';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/utxo/withPool/byIds',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/utxo/withPool/byIds',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/utxo/withPool/byIds', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/utxo/withPool/byIds', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utxo/withPool/byIds");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/utxo/withPool/byIds", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /utxo/withPool/byIds`

*Get boxes for ids provided, from UTXO or the mempool.*

> Body parameter

=== "json"

    ```json
    [
      "string"
    ]
    ```

<h3 id="getboxwithpoolbyids-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|array[string]|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ]
    ```

<h3 id="getboxwithpoolbyids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Box object|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|No any box exists for every id provided|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getboxwithpoolbyids-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|false|none|none|
|» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» value|integer(int64)|true|none|Amount of Ergo token|
|» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|» creationHeight|integer(int32)|true|none|Height the output was created at|
|» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»» amount|integer(int64)|true|none|Amount of the token|
|» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|» index|integer(int32)|false|none|Index in the transaction outputs|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxWithPoolByIdBinary

<a id="opIdgetBoxWithPoolByIdBinary"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utxo/withPool/byIdBinary/{boxId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /utxo/withPool/byIdBinary/{boxId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/utxo/withPool/byIdBinary/{boxId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/utxo/withPool/byIdBinary/{boxId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/utxo/withPool/byIdBinary/{boxId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utxo/withPool/byIdBinary/{boxId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utxo/withPool/byIdBinary/{boxId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utxo/withPool/byIdBinary/{boxId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utxo/withPool/byIdBinary/{boxId}`

*Get serialized box in Base16 encoding by an identifier, considering also the mempool.*

<h3 id="getboxwithpoolbyidbinary-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of a wanted box|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "bytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

<h3 id="getboxwithpoolbyidbinary-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Json containing box identifier and hex-encoded box bytes|[SerializedBox](#schemaserializedbox)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Box with this id doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getSnapshotsInfo

<a id="opIdgetSnapshotsInfo"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utxo/getSnapshotsInfo
    ```

=== "http"

    ```http
    GET /utxo/getSnapshotsInfo HTTP/1.1
    ```

=== "javascript"

    ```javascript
    
    fetch('/utxo/getSnapshotsInfo',
    {
      method: 'GET'
    
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    result = RestClient.get '/utxo/getSnapshotsInfo',
      params: {
      }
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    
    r = requests.get('/utxo/getSnapshotsInfo')
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utxo/getSnapshotsInfo', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utxo/getSnapshotsInfo");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utxo/getSnapshotsInfo", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utxo/getSnapshotsInfo`

*Get information about locally stored UTXO snapshots*

<h3 id="getsnapshotsinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of saved snapshots|None|

<aside class="success">
This operation does not require authentication
</aside>

### genesisBoxes

<a id="opIdgenesisBoxes"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /utxo/genesis \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /utxo/genesis HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/utxo/genesis',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/utxo/genesis',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/utxo/genesis', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/utxo/genesis', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/utxo/genesis");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/utxo/genesis", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /utxo/genesis`

*Get genesis boxes (boxes existed before the very first block)*

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ]
    ```

<h3 id="genesisboxes-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A list of all the genesis boxes|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Box with this id doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="genesisboxes-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|false|none|none|
|» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» value|integer(int64)|true|none|Amount of Ergo token|
|» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|» creationHeight|integer(int32)|true|none|Height the output was created at|
|» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»» amount|integer(int64)|true|none|Amount of the token|
|» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|» index|integer(int32)|false|none|Index in the transaction outputs|

<aside class="success">
This operation does not require authentication
</aside>

## script

### scriptP2SAddress

<a id="opIdscriptP2SAddress"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /script/p2sAddress \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /script/p2sAddress HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "source": "string"
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/script/p2sAddress',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/script/p2sAddress',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/script/p2sAddress', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/script/p2sAddress', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/script/p2sAddress");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/script/p2sAddress", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /script/p2sAddress`

*Create P2SAddress from Sigma source*

> Body parameter

=== "json"

    ```json
    {
      "source": "string"
    }
    ```

<h3 id="scriptp2saddress-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SourceHolder](#schemasourceholder)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    }
    ```

<h3 id="scriptp2saddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ergo address derived from source|[AddressHolder](#schemaaddressholder)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad source|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### scriptP2SHAddress

<a id="opIdscriptP2SHAddress"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /script/p2shAddress \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /script/p2shAddress HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "source": "string"
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/script/p2shAddress',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/script/p2shAddress',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/script/p2shAddress', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/script/p2shAddress', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/script/p2shAddress");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/script/p2shAddress", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /script/p2shAddress`

*Create P2SHAddress from Sigma source*

> Body parameter

=== "json"

    ```json
    {
      "source": "string"
    }
    ```

<h3 id="scriptp2shaddress-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SourceHolder](#schemasourceholder)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    }
    ```

<h3 id="scriptp2shaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|P2SH address derived from source|[AddressHolder](#schemaaddressholder)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad source|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### addressToTree

<a id="opIdaddressToTree"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /script/addressToTree/{address} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /script/addressToTree/{address} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/script/addressToTree/{address}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/script/addressToTree/{address}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/script/addressToTree/{address}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/script/addressToTree/{address}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/script/addressToTree/{address}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/script/addressToTree/{address}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /script/addressToTree/{address}`

*Convert an address to hex-encoded serialized ErgoTree (script)*

<h3 id="addresstotree-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|[ErgoAddress](#schemaergoaddress)|true|address to get a script from|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "tree": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
    }
    ```

<h3 id="addresstotree-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Base16-encoded ErgoTree (script)|[ErgoTreeObject](#schemaergotreeobject)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### addressToBytes

<a id="opIdaddressToBytes"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /script/addressToBytes/{address} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /script/addressToBytes/{address} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/script/addressToBytes/{address}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/script/addressToBytes/{address}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/script/addressToBytes/{address}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/script/addressToBytes/{address}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/script/addressToBytes/{address}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/script/addressToBytes/{address}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /script/addressToBytes/{address}`

*Convert an address to hex-encoded Sigma byte array constant which contains script bytes*

<h3 id="addresstobytes-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|[ErgoAddress](#schemaergoaddress)|true|address to get a script from|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "bytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

<h3 id="addresstobytes-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Base16-encoded Sigma byte array constant which contains script bytes|[ScriptBytes](#schemascriptbytes)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### executeWithContext

<a id="opIdexecuteWithContext"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /script/executeWithContext \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /script/executeWithContext HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "script": "string",
      "namedConstants": {},
      "context": {
        "lastBlockUtxoRoot": {
          "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "treeFlags": 0,
          "keyLength": 0,
          "valueLength": 0
        },
        "headers": [
          {
            "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "timestamp": 1524143059077,
            "version": 2,
            "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "stateRoot": {
              "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "treeFlags": 0,
              "keyLength": 0,
              "valueLength": 0
            },
            "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "nBits": 19857408,
            "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extensionRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "height": 667,
            "size": 667,
            "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "powSolutions": {
              "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
              "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
              "n": "0000000000000000",
              "d": 987654321
            },
            "votes": "000000",
            "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
            "powOnetimePk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
            "powNonce": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "powDistance": 123456789
          }
        ],
        "preHeader": {
          "timestamp": 1524143059077,
          "version": 2,
          "nBits": 19857408,
          "height": 667,
          "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "votes": "000000",
          "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
        },
        "dataBoxes": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "boxesToSpend": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "spendingTransaction": {
          "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "inputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "spendingProof": {
                "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "extension": {
                  "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                }
              }
            }
          ],
          "dataInputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
            }
          ],
          "outputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "value": 147,
              "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
              "creationHeight": 9149,
              "assets": [
                {
                  "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "amount": 1000
                }
              ],
              "additionalRegisters": {
                "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
              },
              "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "index": 0
            }
          ]
        },
        "selfIndex": 0,
        "extension": {},
        "validationSettings": "10e8070001e9070001ea070001eb070001ec070001ed070001ee070001ef070001f0070001f1070001f2070001f3070001f4070001f5070001f6070001f7070001",
        "costLimit": 0,
        "initCost": 0
      }
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/script/executeWithContext',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/script/executeWithContext',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/script/executeWithContext', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/script/executeWithContext', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/script/executeWithContext");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/script/executeWithContext", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /script/executeWithContext`

*Execute script with context*

> Body parameter

=== "json"

    ```json
    {
      "script": "string",
      "namedConstants": {},
      "context": {
        "lastBlockUtxoRoot": {
          "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "treeFlags": 0,
          "keyLength": 0,
          "valueLength": 0
        },
        "headers": [
          {
            "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "timestamp": 1524143059077,
            "version": 2,
            "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "stateRoot": {
              "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "treeFlags": 0,
              "keyLength": 0,
              "valueLength": 0
            },
            "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "nBits": 19857408,
            "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extensionRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "height": 667,
            "size": 667,
            "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "powSolutions": {
              "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
              "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
              "n": "0000000000000000",
              "d": 987654321
            },
            "votes": "000000",
            "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
            "powOnetimePk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
            "powNonce": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "powDistance": 123456789
          }
        ],
        "preHeader": {
          "timestamp": 1524143059077,
          "version": 2,
          "nBits": 19857408,
          "height": 667,
          "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "votes": "000000",
          "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
        },
        "dataBoxes": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "boxesToSpend": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "spendingTransaction": {
          "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "inputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "spendingProof": {
                "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "extension": {
                  "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                }
              }
            }
          ],
          "dataInputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
            }
          ],
          "outputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "value": 147,
              "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
              "creationHeight": 9149,
              "assets": [
                {
                  "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "amount": 1000
                }
              ],
              "additionalRegisters": {
                "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
              },
              "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "index": 0
            }
          ]
        },
        "selfIndex": 0,
        "extension": {},
        "validationSettings": "10e8070001e9070001ea070001eb070001ec070001ed070001ee070001ef070001f0070001f1070001f2070001f3070001f4070001f5070001f6070001f7070001",
        "costLimit": 0,
        "initCost": 0
      }
    }
    ```

<h3 id="executewithcontext-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ExecuteScript](#schemaexecutescript)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "value": {
        "op": -45,
        "condition": true
      },
      "cost": 10
    }
    ```

<h3 id="executewithcontext-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Result of reduceToCrypto|[CryptoResult](#schemacryptoresult)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Compiler error|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

## scan

### registerScan

<a id="opIdregisterScan"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /scan/register \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /scan/register HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "scanName": "Assets Tracker",
      "walletInteraction": "off",
      "removeOffchain": true,
      "trackingRule": {
        "predicate": "containsAsset",
        "assetId": "02dada811a888cd0dc7a0a41739a3ad9b0f427741fe6ca19700cf1a51200c96bf7"
      }
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/scan/register',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/scan/register',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/scan/register', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/scan/register', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/scan/register");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/scan/register", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /scan/register`

*Register a scan*

> Body parameter

=== "json"

    ```json
    {
      "scanName": "Assets Tracker",
      "walletInteraction": "off",
      "removeOffchain": true,
      "trackingRule": {
        "predicate": "containsAsset",
        "assetId": "02dada811a888cd0dc7a0a41739a3ad9b0f427741fe6ca19700cf1a51200c96bf7"
      }
    }
    ```

<h3 id="registerscan-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ScanRequest](#schemascanrequest)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "scanId": 0
    }
    ```

<h3 id="registerscan-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Identifier of a scan generated|[ScanId](#schemascanid)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### deregisterScan

<a id="opIdderegisterScan"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /scan/deregister \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /scan/deregister HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "scanId": 0
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/scan/deregister',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/scan/deregister',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/scan/deregister', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/scan/deregister', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/scan/deregister");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/scan/deregister", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /scan/deregister`

*Stop tracking and deregister scan*

> Body parameter

=== "json"

    ```json
    {
      "scanId": 0
    }
    ```

<h3 id="deregisterscan-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ScanId](#schemascanid)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "scanId": 0
    }
    ```

<h3 id="deregisterscan-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Identifier of a scan removed|[ScanId](#schemascanid)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|No scan found|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### listAllScans

<a id="opIdlistAllScans"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /scan/listAll \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /scan/listAll HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/scan/listAll',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/scan/listAll',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/scan/listAll', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/scan/listAll', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/scan/listAll");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/scan/listAll", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /scan/listAll`

*List all the registered scans*

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "scanId": 2,
        "scanName": "Assets Tracker",
        "walletInteraction": "off",
        "removeOffchain": true,
        "trackingRule": {
          "predicate": "containsAsset",
          "assetId": "02dada811a888cd0dc7a0a41739a3ad9b0f427741fe6ca19700cf1a51200c96bf7"
        }
      }
    ]
    ```

<h3 id="listallscans-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of scans registered|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="listallscans-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Scan](#schemascan)]|false|none|none|
|» scanName|string|false|none|none|
|» scanId|integer|false|none|none|
|» walletInteraction|string|false|none|none|
|» removeOffchain|boolean|false|none|none|
|» trackingRule|[ScanningPredicate](#schemascanningpredicate)|false|none|none|
|»» predicate|string|true|none|none|

##### Enumerated Values

|Property|Value|
|---|---|
|walletInteraction|off|
|walletInteraction|shared|
|walletInteraction|forced|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### listUnspentScans

<a id="opIdlistUnspentScans"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /scan/unspentBoxes/{scanId} \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /scan/unspentBoxes/{scanId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/scan/unspentBoxes/{scanId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/scan/unspentBoxes/{scanId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/scan/unspentBoxes/{scanId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/scan/unspentBoxes/{scanId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/scan/unspentBoxes/{scanId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/scan/unspentBoxes/{scanId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /scan/unspentBoxes/{scanId}`

*List boxes which are not spent.*

<h3 id="listunspentscans-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scanId|path|integer(int32)|true|identifier of a scan|
|minConfirmations|query|integer(int32)|false|Minimal number of confirmations, -1 means we consider unconfirmed|
|maxConfirmations|query|integer(int32)|false|Maximum number of confirmations, -1 means unlimited|
|minInclusionHeight|query|integer(int32)|false|Minimal box inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximum box inclusion height, -1 means unlimited|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "box": {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        },
        "confirmationsNum": 147,
        "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
        "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingHeight": 147,
        "inclusionHeight": 147,
        "onchain": true,
        "spent": false,
        "creationOutIndex": 2,
        "scans": [
          1
        ]
      }
    ]
    ```

<h3 id="listunspentscans-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of unspent boxes|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="listunspentscans-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WalletBox](#schemawalletbox)]|false|none|none|
|» box|[ErgoTransactionOutput](#schemaergotransactionoutput)|true|none|none|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|» creationTransaction|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingTransaction|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|» spent|boolean|true|none|A flag signalling whether the box was spent|
|» creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|» scans|[integer]|true|none|Scan identifiers the box relates to|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### listSpentScans

<a id="opIdlistSpentScans"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /scan/spentBoxes/{scanId} \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    GET /scan/spentBoxes/{scanId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/scan/spentBoxes/{scanId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.get '/scan/spentBoxes/{scanId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.get('/scan/spentBoxes/{scanId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/scan/spentBoxes/{scanId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/scan/spentBoxes/{scanId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/scan/spentBoxes/{scanId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /scan/spentBoxes/{scanId}`

*List boxes which are spent.*

<h3 id="listspentscans-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scanId|path|integer(int32)|true|identifier of a scan|
|minConfirmations|query|integer(int32)|false|Minimal number of confirmations, -1 means we consider unconfirmed|
|maxConfirmations|query|integer(int32)|false|Maximum number of confirmations, -1 means unlimited|
|minInclusionHeight|query|integer(int32)|false|Minimal box inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximum box inclusion height, -1 means unlimited|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "box": {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        },
        "confirmationsNum": 147,
        "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
        "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingHeight": 147,
        "inclusionHeight": 147,
        "onchain": true,
        "spent": false,
        "creationOutIndex": 2,
        "scans": [
          1
        ]
      }
    ]
    ```

<h3 id="listspentscans-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of spent boxes|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="listspentscans-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WalletBox](#schemawalletbox)]|false|none|none|
|» box|[ErgoTransactionOutput](#schemaergotransactionoutput)|true|none|none|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|» creationTransaction|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingTransaction|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|» spent|boolean|true|none|A flag signalling whether the box was spent|
|» creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|» scans|[integer]|true|none|Scan identifiers the box relates to|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### scanStopTracking

<a id="opIdscanStopTracking"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /scan/stopTracking \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /scan/stopTracking HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "scanId": 0,
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/scan/stopTracking',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/scan/stopTracking',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/scan/stopTracking', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/scan/stopTracking', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/scan/stopTracking");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/scan/stopTracking", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /scan/stopTracking`

*Stop scan-related box tracking*

> Body parameter

=== "json"

    ```json
    {
      "scanId": 0,
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

<h3 id="scanstoptracking-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ScanIdBoxId](#schemascanidboxid)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "scanId": 0,
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

<h3 id="scanstoptracking-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The box is not tracked anymore|[ScanIdBoxId](#schemascanidboxid)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### scriptP2SRule

<a id="opIdscriptP2SRule"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /scan/p2sRule \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /scan/p2sRule HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '4MQyML64GnzMxZgm';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/scan/p2sRule',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/scan/p2sRule',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/scan/p2sRule', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/scan/p2sRule', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/scan/p2sRule");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/scan/p2sRule", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /scan/p2sRule`

*Create and register a scan to track P2S address provided*

> Body parameter

=== "json"

    ```json
    "4MQyML64GnzMxZgm"
    ```

<h3 id="scriptp2srule-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "scanId": 0
    }
    ```

<h3 id="scriptp2srule-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Id of custom scan generated and registered|[ScanId](#schemascanid)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad source|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

### addBox

<a id="opIdaddBox"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /scan/addBox \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /scan/addBox HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '{
      "scanIds": [
        0
      ],
      "box": {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    }';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/scan/addBox',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/scan/addBox',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/scan/addBox', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/scan/addBox', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/scan/addBox");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/scan/addBox", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /scan/addBox`

*Adds a box to scans, writes box to database if it is not there. You can use scan number 10 to add a box to the wallet.*

> Body parameter

=== "json"

    ```json
    {
      "scanIds": [
        0
      ],
      "box": {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    }
    ```

<h3 id="addbox-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ScanIdsBox](#schemascanidsbox)|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

<h3 id="addbox-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|It the box is added successfully, then its id is returned|[TransactionId](#schematransactionid)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

## node

### nodeShutdown

<a id="opIdnodeShutdown"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /node/shutdown \
      -H 'Accept: application/json' \
      -H 'api_key: API_KEY'
    ```

=== "http"

    ```http
    POST /node/shutdown HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json',
      'api_key':'API_KEY'
    };
    
    fetch('/node/shutdown',
    {
      method: 'POST',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json',
      'api_key' => 'API_KEY'
    }
    
    result = RestClient.post '/node/shutdown',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json',
      'api_key': 'API_KEY'
    }
    
    r = requests.post('/node/shutdown', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
        'api_key' => 'API_KEY',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/node/shutdown', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/node/shutdown");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
            "api_key": []string{"API_KEY"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/node/shutdown", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /node/shutdown`

*Shuts down the node*

> Example responses

> default Response

=== "json"

    ```json
    {
      "error": 500,
      "reason": "Internal server error",
      "detail": "string"
    }
    ```

<h3 id="nodeshutdown-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The node will be shut down in 5 seconds|None|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )
</aside>

## emission

### emissionAt

<a id="opIdemissionAt"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /emission/at/{blockHeight} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /emission/at/{blockHeight} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/emission/at/{blockHeight}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/emission/at/{blockHeight}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/emission/at/{blockHeight}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/emission/at/{blockHeight}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/emission/at/{blockHeight}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/emission/at/{blockHeight}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /emission/at/{blockHeight}`

*Get emission data for a given height*

<h3 id="emissionat-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|blockHeight|path|integer(int32)|true|Height to get emission data for|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "minerReward": 0,
      "totalCoinsIssued": 0,
      "totalRemainCoins": 0,
      "reemitted": 0
    }
    ```

<h3 id="emissionat-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Emission data|[EmissionInfo](#schemaemissioninfo)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### emissionScripts

<a id="opIdemissionScripts"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /emission/scripts \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /emission/scripts HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/emission/scripts',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/emission/scripts',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/emission/scripts', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/emission/scripts', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/emission/scripts");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/emission/scripts", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /emission/scripts`

*Print emission-related scripts*

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "emission": "string",
      "reemission": "string",
      "pay2Reemission": "string"
    }
    ```

<h3 id="emissionscripts-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Emission-related scripts|[EmissionScripts](#schemaemissionscripts)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

## blockchain

### getIndexedHeight

<a id="opIdgetIndexedHeight"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blockchain/indexedHeight \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blockchain/indexedHeight HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blockchain/indexedHeight',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blockchain/indexedHeight',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blockchain/indexedHeight', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blockchain/indexedHeight', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/indexedHeight");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blockchain/indexedHeight", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blockchain/indexedHeight`

*Get current indexed block height. (The indexer has processed all blocks up to this height.)*

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "indexedHeight": 0,
      "fullHeight": 0
    }
    ```

<h3 id="getindexedheight-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|height of the indexer and full height|Inline|

<h3 id="getindexedheight-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» indexedHeight|integer|false|none|number of blocks indexed|
|» fullHeight|integer|false|none|number of all known blocks|

<aside class="success">
This operation does not require authentication
</aside>

### getTxById

<a id="opIdgetTxById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blockchain/transaction/byId/{txId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blockchain/transaction/byId/{txId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blockchain/transaction/byId/{txId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blockchain/transaction/byId/{txId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blockchain/transaction/byId/{txId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blockchain/transaction/byId/{txId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/transaction/byId/{txId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blockchain/transaction/byId/{txId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blockchain/transaction/byId/{txId}`

*Retrieve a transaction by its id*

<h3 id="gettxbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|txId|path|string|true|id of the wanted transaction|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "inclusionHeight": 20998,
      "numConfirmations": 20998,
      "blockId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "index": 3,
      "globalIndex": 3565445,
      "size": 0
    }
    ```

<h3 id="gettxbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|transaction with wanted id|[IndexedErgoTransaction](#schemaindexedergotransaction)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Transaction with this id doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getTxByIndex

<a id="opIdgetTxByIndex"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blockchain/transaction/byIndex/{txIndex} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blockchain/transaction/byIndex/{txIndex} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blockchain/transaction/byIndex/{txIndex}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blockchain/transaction/byIndex/{txIndex}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blockchain/transaction/byIndex/{txIndex}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blockchain/transaction/byIndex/{txIndex}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/transaction/byIndex/{txIndex}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blockchain/transaction/byIndex/{txIndex}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blockchain/transaction/byIndex/{txIndex}`

*Retrieve a transaction by global index number*

<h3 id="gettxbyindex-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|txIndex|path|number|true|index of the wanted transaction|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "inclusionHeight": 20998,
      "numConfirmations": 20998,
      "blockId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "index": 3,
      "globalIndex": 3565445,
      "size": 0
    }
    ```

<h3 id="gettxbyindex-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|transaction with wanted index|[IndexedErgoTransaction](#schemaindexedergotransaction)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Transaction with this index doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getTxsByAddress

<a id="opIdgetTxsByAddress"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /blockchain/transaction/byAddress \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /blockchain/transaction/byAddress HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/blockchain/transaction/byAddress',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/blockchain/transaction/byAddress',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/blockchain/transaction/byAddress', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/blockchain/transaction/byAddress', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/transaction/byAddress");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/blockchain/transaction/byAddress", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /blockchain/transaction/byAddress`

*Retrieve transactions by their associated address*

> Body parameter

=== "json"

    ```json
    "\"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt\""
    ```

<h3 id="gettxsbyaddress-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|body|body|string|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "items": [
        {
          "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "inputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "spendingProof": {
                "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "extension": {
                  "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                }
              }
            }
          ],
          "dataInputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
            }
          ],
          "outputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "value": 147,
              "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
              "creationHeight": 9149,
              "assets": [
                {
                  "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "amount": 1000
                }
              ],
              "additionalRegisters": {
                "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
              },
              "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "index": 0
            }
          ],
          "inclusionHeight": 20998,
          "numConfirmations": 20998,
          "blockId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "timestamp": 1524143059077,
          "index": 3,
          "globalIndex": 3565445,
          "size": 0
        }
      ],
      "total": 0
    }
    ```

<h3 id="gettxsbyaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|transactions associated with wanted address|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|No transactions found for wanted address|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="gettxsbyaddress-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|[[IndexedErgoTransaction](#schemaindexedergotransaction)]|false|none|Array of transactions|
|»» id|[TransactionId](#schematransactionid)(base16)|true|none|Base16-encoded transaction id bytes|
|»» inputs|[[ErgoTransactionInput](#schemaergotransactioninput)]|true|none|Transaction inputs|
|»»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» spendingProof|[SpendingProof](#schemaspendingproof)|true|none|Spending proof for transaction input|
|»»»» proofBytes|[SpendingProofBytes](#schemaspendingproofbytes)(base16)|true|none|Base16-encoded spending proofs|
|»»»» extension|object|true|none|Variables to be put into context|
|»»»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» dataInputs|[[ErgoTransactionDataInput](#schemaergotransactiondatainput)]|true|none|Transaction data inputs|
|»»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» outputs|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|Transaction outputs|
|»»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» value|integer(int64)|true|none|Amount of Ergo token|
|»»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»»» amount|integer(int64)|true|none|Amount of the token|
|»»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»»» index|integer(int32)|false|none|Index in the transaction outputs|
|»» inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|»» numConfirmations|integer(int32)|true|none|Number of transaction confirmations|
|»» blockId|[ModifierId](#schemamodifierid)(base16)|true|none|Id of the block the transaction was included in|
|»» timestamp|[Timestamp](#schematimestamp)(int64)|true|none|Basic timestamp definition|
|»» index|integer(int32)|true|none|index of the transaction in the block it was included in|
|»» globalIndex|integer(int64)|true|none|Global index of the transaction in the blockchain|
|»» size|integer(int32)|true|none|Size in bytes|
|» total|integer|false|none|Total count of retreived transactions|

<aside class="success">
This operation does not require authentication
</aside>

### getTxRange

<a id="opIdgetTxRange"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blockchain/transaction/range \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blockchain/transaction/range HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blockchain/transaction/range',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blockchain/transaction/range',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blockchain/transaction/range', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blockchain/transaction/range', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/transaction/range");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blockchain/transaction/range", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blockchain/transaction/range`

*Get a range of transaction ids*

<h3 id="gettxrange-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ]
    ```

<h3 id="gettxrange-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|transactions ids in wanted range|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="gettxrange-responseschema">Response Schema</h3>

Status Code **200**

*Array of transaction ids*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ModifierId](#schemamodifierid)]|false|none|Array of transaction ids|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxById

<a id="opIdgetBoxById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blockchain/box/byId/{boxId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blockchain/box/byId/{boxId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blockchain/box/byId/{boxId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blockchain/box/byId/{boxId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blockchain/box/byId/{boxId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blockchain/box/byId/{boxId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/box/byId/{boxId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blockchain/box/byId/{boxId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blockchain/box/byId/{boxId}`

*Retrieve a box by its id*

<h3 id="getboxbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|id of the wanted box|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0,
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingHeight": 147,
      "inclusionHeight": 147,
      "globalIndex": 83927
    }
    ```

<h3 id="getboxbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|box with wanted id|[IndexedErgoBox](#schemaindexedergobox)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|No box found with wanted id|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxByIndex

<a id="opIdgetBoxByIndex"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blockchain/box/byIndex/{boxIndex} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blockchain/box/byIndex/{boxIndex} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blockchain/box/byIndex/{boxIndex}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blockchain/box/byIndex/{boxIndex}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blockchain/box/byIndex/{boxIndex}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blockchain/box/byIndex/{boxIndex}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/box/byIndex/{boxIndex}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blockchain/box/byIndex/{boxIndex}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blockchain/box/byIndex/{boxIndex}`

*Retrieve a box by global index number*

<h3 id="getboxbyindex-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxIndex|path|number|true|index of the wanted box|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0,
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingHeight": 147,
      "inclusionHeight": 147,
      "globalIndex": 83927
    }
    ```

<h3 id="getboxbyindex-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|box with wanted index|[IndexedErgoBox](#schemaindexedergobox)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Box with this index doesn't exist|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxesByTokenId

<a id="opIdgetBoxesByTokenId"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blockchain/box/byTokenId/{tokenId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blockchain/box/byTokenId/{tokenId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blockchain/box/byTokenId/{tokenId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blockchain/box/byTokenId/{tokenId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blockchain/box/byTokenId/{tokenId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blockchain/box/byTokenId/{tokenId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/box/byTokenId/{tokenId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blockchain/box/byTokenId/{tokenId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blockchain/box/byTokenId/{tokenId}`

*Retrieve boxes by an associated token id*

<h3 id="getboxesbytokenid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tokenId|path|[ModifierId](#schemamodifierid)|true|id of the token|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "items": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0,
          "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
          "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingHeight": 147,
          "inclusionHeight": 147,
          "globalIndex": 83927
        }
      ],
      "total": 0
    }
    ```

<h3 id="getboxesbytokenid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|boxes associated with wanted token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|No boxes found for wanted token|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getboxesbytokenid-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|[allOf]|false|none|Array of boxes|

*allOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|[ErgoTransactionOutput](#schemaergotransactionoutput)|false|none|none|
|»»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» value|integer(int64)|true|none|Amount of Ergo token|
|»»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»»» amount|integer(int64)|true|none|Amount of the token|
|»»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»»» index|integer(int32)|false|none|Index in the transaction outputs|

*and*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Box indexed with extra information|
|»»» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|»»» spentTransactionId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|»»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» total|integer|false|none|Total number of retreived boxes|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxesByTokenIdUnspent

<a id="opIdgetBoxesByTokenIdUnspent"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blockchain/box/unspent/byTokenId/{tokenId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blockchain/box/unspent/byTokenId/{tokenId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blockchain/box/unspent/byTokenId/{tokenId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blockchain/box/unspent/byTokenId/{tokenId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blockchain/box/unspent/byTokenId/{tokenId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blockchain/box/unspent/byTokenId/{tokenId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/box/unspent/byTokenId/{tokenId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blockchain/box/unspent/byTokenId/{tokenId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blockchain/box/unspent/byTokenId/{tokenId}`

*Retrieve unspent boxes by an associated token id*

<h3 id="getboxesbytokenidunspent-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tokenId|path|[ModifierId](#schemamodifierid)|true|id of the token|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|sortDirection|query|string|false|desc = new boxes first ; asc = old boxes first|
|includeUnconfirmed|query|boolean|false|if true include unconfirmed transactions from mempool|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0,
        "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
        "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingHeight": 147,
        "inclusionHeight": 147,
        "globalIndex": 83927
      }
    ]
    ```

<h3 id="getboxesbytokenidunspent-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|unspent boxes associated with wanted token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|No unspent boxes found for wanted token|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getboxesbytokenidunspent-responseschema">Response Schema</h3>

Status Code **200**

*Array of boxes*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[allOf]|false|none|Array of boxes|

*allOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErgoTransactionOutput](#schemaergotransactionoutput)|false|none|none|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|

*and*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|Box indexed with extra information|
|»» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|»» spentTransactionId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxesByAddress

<a id="opIdgetBoxesByAddress"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /blockchain/box/byAddress \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /blockchain/box/byAddress HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/blockchain/box/byAddress',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/blockchain/box/byAddress',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/blockchain/box/byAddress', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/blockchain/box/byAddress', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/box/byAddress");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/blockchain/box/byAddress", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /blockchain/box/byAddress`

*Retrieve boxes by their associated address*

> Body parameter

=== "json"

    ```json
    "\"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt\""
    ```

<h3 id="getboxesbyaddress-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|body|body|string|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "items": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0,
          "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
          "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingHeight": 147,
          "inclusionHeight": 147,
          "globalIndex": 83927
        }
      ],
      "total": 0
    }
    ```

<h3 id="getboxesbyaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|boxes associated with wanted address|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|No boxes found for wanted address|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getboxesbyaddress-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|[allOf]|false|none|Array of boxes|

*allOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|[ErgoTransactionOutput](#schemaergotransactionoutput)|false|none|none|
|»»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» value|integer(int64)|true|none|Amount of Ergo token|
|»»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»»» amount|integer(int64)|true|none|Amount of the token|
|»»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»»» index|integer(int32)|false|none|Index in the transaction outputs|

*and*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Box indexed with extra information|
|»»» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|»»» spentTransactionId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|»»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» total|integer|false|none|Total number of retreived boxes|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxesByAddressUnspent

<a id="opIdgetBoxesByAddressUnspent"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /blockchain/box/unspent/byAddress \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /blockchain/box/unspent/byAddress HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/blockchain/box/unspent/byAddress',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/blockchain/box/unspent/byAddress',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/blockchain/box/unspent/byAddress', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/blockchain/box/unspent/byAddress', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/box/unspent/byAddress");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/blockchain/box/unspent/byAddress", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /blockchain/box/unspent/byAddress`

*Retrieve unspent boxes by their associated address*

> Body parameter

=== "json"

    ```json
    "\"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt\""
    ```

<h3 id="getboxesbyaddressunspent-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|sortDirection|query|string|false|desc = new boxes first ; asc = old boxes first|
|includeUnconfirmed|query|boolean|false|if true include unconfirmed transactions from mempool|
|body|body|string|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0,
        "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
        "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingHeight": 147,
        "inclusionHeight": 147,
        "globalIndex": 83927
      }
    ]
    ```

<h3 id="getboxesbyaddressunspent-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|unspent boxes associated with wanted address|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|No unspent boxes found for wanted address|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getboxesbyaddressunspent-responseschema">Response Schema</h3>

Status Code **200**

*Array of boxes*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[allOf]|false|none|Array of boxes|

*allOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ErgoTransactionOutput](#schemaergotransactionoutput)|false|none|none|
|»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|

*and*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|Box indexed with extra information|
|»» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|»» spentTransactionId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxRange

<a id="opIdgetBoxRange"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blockchain/box/range \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blockchain/box/range HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blockchain/box/range',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blockchain/box/range',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blockchain/box/range', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blockchain/box/range', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/box/range");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blockchain/box/range", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blockchain/box/range`

*Get a range of box ids*

<h3 id="getboxrange-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|

> Example responses

> 200 Response

=== "json"

    ```json
    [
      "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ]
    ```

<h3 id="getboxrange-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|box ids in wanted range|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getboxrange-responseschema">Response Schema</h3>

Status Code **200**

*Array of box ids*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ModifierId](#schemamodifierid)]|false|none|Array of box ids|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxesByErgoTree

<a id="opIdgetBoxesByErgoTree"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /blockchain/box/byErgoTree \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /blockchain/box/byErgoTree HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/blockchain/box/byErgoTree',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/blockchain/box/byErgoTree',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/blockchain/box/byErgoTree', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/blockchain/box/byErgoTree', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/box/byErgoTree");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/blockchain/box/byErgoTree", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /blockchain/box/byErgoTree`

*Retrieve boxes by their associated ergotree*

> Body parameter

=== "json"

    ```json
    "\"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301\""
    ```

<h3 id="getboxesbyergotree-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|body|body|string|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "items": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0,
          "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
          "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingHeight": 147,
          "inclusionHeight": 147,
          "globalIndex": 83927
        }
      ],
      "total": 0
    }
    ```

<h3 id="getboxesbyergotree-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|boxes with wanted ergotree|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getboxesbyergotree-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|[allOf]|false|none|Array of boxes|

*allOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|[ErgoTransactionOutput](#schemaergotransactionoutput)|false|none|none|
|»»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» value|integer(int64)|true|none|Amount of Ergo token|
|»»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»»» amount|integer(int64)|true|none|Amount of the token|
|»»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»»» index|integer(int32)|false|none|Index in the transaction outputs|

*and*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Box indexed with extra information|
|»»» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|»»» spentTransactionId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|»»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» total|integer|false|none|Total number of retreived boxes|

<aside class="success">
This operation does not require authentication
</aside>

### getBoxesByErgoTreeUnspent

<a id="opIdgetBoxesByErgoTreeUnspent"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /blockchain/box/unspent/byErgoTree \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /blockchain/box/unspent/byErgoTree HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/blockchain/box/unspent/byErgoTree',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/blockchain/box/unspent/byErgoTree',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/blockchain/box/unspent/byErgoTree', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/blockchain/box/unspent/byErgoTree', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/box/unspent/byErgoTree");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/blockchain/box/unspent/byErgoTree", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /blockchain/box/unspent/byErgoTree`

*Retrieve unspent boxes by their associated ergotree*

> Body parameter

=== "json"

    ```json
    "\"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301\""
    ```

<h3 id="getboxesbyergotreeunspent-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|sortDirection|query|string|false|desc = new boxes first ; asc = old boxes first|
|includeUnconfirmed|query|boolean|false|if true include unconfirmed transactions from mempool|
|body|body|string|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "items": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0,
          "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
          "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingHeight": 147,
          "inclusionHeight": 147,
          "globalIndex": 83927
        }
      ],
      "total": 0
    }
    ```

<h3 id="getboxesbyergotreeunspent-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|unspent boxes with wanted ergotree|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|No unspent box found with wanted ergotree|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getboxesbyergotreeunspent-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|[allOf]|false|none|Array of boxes|

*allOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|[ErgoTransactionOutput](#schemaergotransactionoutput)|false|none|none|
|»»» boxId|[TransactionBoxId](#schematransactionboxid)(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» value|integer(int64)|true|none|Amount of Ergo token|
|»»» ergoTree|[ErgoTree](#schemaergotree)(base16)|true|none|Base16-encoded ergo tree bytes|
|»»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»»» assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|»»»» tokenId|[Digest32](#schemadigest32)(base16)|true|none|Base16-encoded 32 byte digest|
|»»»» amount|integer(int64)|true|none|Amount of the token|
|»»» additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|»»»» **additionalProperties**|[SValue](#schemasvalue)(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»» transactionId|[TransactionId](#schematransactionid)(base16)|false|none|Base16-encoded transaction id bytes|
|»»» index|integer(int32)|false|none|Index in the transaction outputs|

*and*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Box indexed with extra information|
|»»» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|»»» spentTransactionId|[ModifierId](#schemamodifierid)(base16)|true|none|Base16-encoded 32 byte modifier id|
|»»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» total|integer|false|none|Total number of retreived boxes|

<aside class="success">
This operation does not require authentication
</aside>

### getTokenById

<a id="opIdgetTokenById"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X GET /blockchain/token/byId/{tokenId} \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    GET /blockchain/token/byId/{tokenId} HTTP/1.1
    
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    
    const headers = {
      'Accept':'application/json'
    };
    
    fetch('/blockchain/token/byId/{tokenId}',
    {
      method: 'GET',
    
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Accept' => 'application/json'
    }
    
    result = RestClient.get '/blockchain/token/byId/{tokenId}',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Accept': 'application/json'
    }
    
    r = requests.get('/blockchain/token/byId/{tokenId}', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('GET','/blockchain/token/byId/{tokenId}', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/token/byId/{tokenId}");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("GET");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("GET", "/blockchain/token/byId/{tokenId}", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`GET /blockchain/token/byId/{tokenId}`

*Retrieve minting information about a token*

<h3 id="gettokenbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tokenId|path|string|true|id of the wanted token|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "boxId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "emissionAmount": 3500000,
      "name": "string",
      "description": "string",
      "decimals": 8
    }
    ```

<h3 id="gettokenbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|token with wanted id|[IndexedToken](#schemaindexedtoken)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|No token found with wanted id|[ApiError](#schemaapierror)|
|default|Default|Error|[ApiError](#schemaapierror)|

<aside class="success">
This operation does not require authentication
</aside>

### getAddressBalanceTotal

<a id="opIdgetAddressBalanceTotal"></a>

> Code samples

=== "shell"

    ```shell
    ## You can also use wget
    curl -X POST /blockchain/balance \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json'
    ```

=== "http"

    ```http
    POST /blockchain/balance HTTP/1.1
    
    Content-Type: application/json
    Accept: application/json
    ```

=== "javascript"

    ```javascript
    const inputBody = '"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"';
    const headers = {
      'Content-Type':'application/json',
      'Accept':'application/json'
    };
    
    fetch('/blockchain/balance',
    {
      method: 'POST',
      body: inputBody,
      headers: headers
    })
    .then(function(res) {
        return res.json();
    }).then(function(body) {
        console.log(body);
    });
    ```

=== "ruby"

    ```ruby
    require 'rest-client'
    require 'json'
    
    headers = {
      'Content-Type' => 'application/json',
      'Accept' => 'application/json'
    }
    
    result = RestClient.post '/blockchain/balance',
      params: {
      }, headers: headers
    
    p JSON.parse(result)
    ```

=== "python"

    ```python
    import requests
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    
    r = requests.post('/blockchain/balance', headers = headers)
    
    print(r.json())
    ```

=== "php"

    ```php
    <?php
    
    require 'vendor/autoload.php';
    
    $headers = array(
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    );
    
    $client = new \GuzzleHttp\Client();
    
    // Define array of request body.
    $request_body = array();
    
    try {
        $response = $client->request('POST','/blockchain/balance', array(
            'headers' => $headers,
            'json' => $request_body,
           )
        );
        print_r($response->getBody()->getContents());
     }
     catch (\GuzzleHttp\Exception\BadResponseException $e) {
        // handle exception or api errors.
        print_r($e->getMessage());
     }
    
     // ...
    ```

=== "java"

    ```java
    URL obj = new URL("/blockchain/balance");
    HttpURLConnection con = (HttpURLConnection) obj.openConnection();
    con.setRequestMethod("POST");
    int responseCode = con.getResponseCode();
    BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
    String inputLine;
    StringBuffer response = new StringBuffer();
    while ((inputLine = in.readLine()) != null) {
        response.append(inputLine);
    }
    in.close();
    System.out.println(response.toString());
    ```

=== "go"

    ```go
    package main
    
    import (
           "bytes"
           "net/http"
    )
    
    func main() {
    
        headers := map[string][]string{
            "Content-Type": []string{"application/json"},
            "Accept": []string{"application/json"},
        }
    
        data := bytes.NewBuffer([]byte{jsonReq})
        req, err := http.NewRequest("POST", "/blockchain/balance", data)
        req.Header = headers
    
        client := &http.Client{}
        resp, err := client.Do(req)
        // ...
    }
    ```

`POST /blockchain/balance`

*Retrieve confirmed and unconfirmed balance of an address*

> Body parameter

=== "json"

    ```json
    "\"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt\""
    ```

<h3 id="getaddressbalancetotal-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|

> Example responses

> 200 Response

=== "json"

    ```json
    {
      "confirmed": {
        "nanoErgs": 0,
        "tokens": [
          {
            "tokenId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 0,
            "decimals": 0,
            "name": "string"
          }
        ]
      },
      "unconfirmed": {
        "nanoErgs": 0,
        "tokens": [
          {
            "tokenId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 0,
            "decimals": 0,
            "name": "string"
          }
        ]
      }
    }
    ```

<h3 id="getaddressbalancetotal-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|balance information|Inline|
|default|Default|Error|[ApiError](#schemaapierror)|

<h3 id="getaddressbalancetotal-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» confirmed|[BalanceInfo](#schemabalanceinfo)|false|none|Balance information|
|»» nanoErgs|integer(int64)|true|none|Balance of nanoERGs|
|»» tokens|[object]|true|none|Balance of tokens|
|»»» tokenId|[ModifierId](#schemamodifierid)(base16)|false|none|Base16-encoded 32 byte modifier id|
|»»» amount|integer(int64)|false|none|Amount of the token|
|»»» decimals|integer|false|none|Number of decimals of the token|
|»»» name|string|false|none|Name of the token, if any|
|» unconfirmed|[BalanceInfo](#schemabalanceinfo)|false|none|Balance information|

<aside class="success">
This operation does not require authentication
</aside>

## Schemas

### ErgoTransactionInput
<!-- backwards compatibility -->
<a id="schemaergotransactioninput"></a>
<a id="schema_ErgoTransactionInput"></a>
<a id="tocSergotransactioninput"></a>
<a id="tocsergotransactioninput"></a>

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|boxId|[TransactionBoxId](#schematransactionboxid)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|spendingProof|[SpendingProof](#schemaspendingproof)|true|none|Spending proof for transaction input|

### ErgoTransactionDataInput
<!-- backwards compatibility -->
<a id="schemaergotransactiondatainput"></a>
<a id="schema_ErgoTransactionDataInput"></a>
<a id="tocSergotransactiondatainput"></a>
<a id="tocsergotransactiondatainput"></a>

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|boxId|[TransactionBoxId](#schematransactionboxid)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|

### ErgoTransactionUnsignedInput
<!-- backwards compatibility -->
<a id="schemaergotransactionunsignedinput"></a>
<a id="schema_ErgoTransactionUnsignedInput"></a>
<a id="tocSergotransactionunsignedinput"></a>
<a id="tocsergotransactionunsignedinput"></a>

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "extension": {
        "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
      }
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|boxId|[TransactionBoxId](#schematransactionboxid)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|extension|object|false|none|none|
|» **additionalProperties**|[SValue](#schemasvalue)|false|none|Base-16 encoded serialized Sigma-state value|

### SpendingProof
<!-- backwards compatibility -->
<a id="schemaspendingproof"></a>
<a id="schema_SpendingProof"></a>
<a id="tocSspendingproof"></a>
<a id="tocsspendingproof"></a>

=== "json"

    ```json
    {
      "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "extension": {
        "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
      }
    }
    ```

Spending proof for transaction input

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|proofBytes|[SpendingProofBytes](#schemaspendingproofbytes)|true|none|Base16-encoded spending proofs|
|extension|object|true|none|Variables to be put into context|
|» **additionalProperties**|[SValue](#schemasvalue)|false|none|Base-16 encoded serialized Sigma-state value|

### SerializedBox
<!-- backwards compatibility -->
<a id="schemaserializedbox"></a>
<a id="schema_SerializedBox"></a>
<a id="tocSserializedbox"></a>
<a id="tocsserializedbox"></a>

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "bytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|boxId|[TransactionBoxId](#schematransactionboxid)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|bytes|[HexString](#schemahexstring)|true|none|Base16-encoded bytes|

### ScriptBytes
<!-- backwards compatibility -->
<a id="schemascriptbytes"></a>
<a id="schema_ScriptBytes"></a>
<a id="tocSscriptbytes"></a>
<a id="tocsscriptbytes"></a>

=== "json"

    ```json
    {
      "bytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bytes|[HexString](#schemahexstring)|true|none|Base16-encoded bytes|

### SnapshotsInfo
<!-- backwards compatibility -->
<a id="schemasnapshotsinfo"></a>
<a id="schema_SnapshotsInfo"></a>
<a id="tocSsnapshotsinfo"></a>
<a id="tocssnapshotsinfo"></a>

=== "json"

    ```json
    {
      "availableManifests": [
        {}
      ]
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|availableManifests|[object]|true|none|Map of available manifests height -> manifestId|

### ErgoTransactionOutput
<!-- backwards compatibility -->
<a id="schemaergotransactionoutput"></a>
<a id="schema_ErgoTransactionOutput"></a>
<a id="tocSergotransactionoutput"></a>
<a id="tocsergotransactionoutput"></a>

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|boxId|[TransactionBoxId](#schematransactionboxid)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|value|integer(int64)|true|none|Amount of Ergo token|
|ergoTree|[ErgoTree](#schemaergotree)|true|none|Base16-encoded ergo tree bytes|
|creationHeight|integer(int32)|true|none|Height the output was created at|
|assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|additionalRegisters|[Registers](#schemaregisters)|true|none|Ergo box registers|
|transactionId|[TransactionId](#schematransactionid)|false|none|Base16-encoded transaction id bytes|
|index|integer(int32)|false|none|Index in the transaction outputs|

### WalletBox
<!-- backwards compatibility -->
<a id="schemawalletbox"></a>
<a id="schema_WalletBox"></a>
<a id="tocSwalletbox"></a>
<a id="tocswalletbox"></a>

=== "json"

    ```json
    {
      "box": {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      },
      "confirmationsNum": 147,
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingHeight": 147,
      "inclusionHeight": 147,
      "onchain": true,
      "spent": false,
      "creationOutIndex": 2,
      "scans": [
        1
      ]
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|box|[ErgoTransactionOutput](#schemaergotransactionoutput)|true|none|none|
|confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|creationTransaction|[ModifierId](#schemamodifierid)|true|none|Transaction which created the box|
|spendingTransaction|[ModifierId](#schemamodifierid)|true|none|Transaction which created the box|
|spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|spent|boolean|true|none|A flag signalling whether the box was spent|
|creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|scans|[integer]|true|none|Scan identifiers the box relates to|

### BalanceInfo
<!-- backwards compatibility -->
<a id="schemabalanceinfo"></a>
<a id="schema_BalanceInfo"></a>
<a id="tocSbalanceinfo"></a>
<a id="tocsbalanceinfo"></a>

=== "json"

    ```json
    {
      "nanoErgs": 0,
      "tokens": [
        {
          "tokenId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 0,
          "decimals": 0,
          "name": "string"
        }
      ]
    }
    ```

Balance information

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nanoErgs|integer(int64)|true|none|Balance of nanoERGs|
|tokens|[object]|true|none|Balance of tokens|
|» tokenId|[ModifierId](#schemamodifierid)|false|none|Identifier of the token|
|» amount|integer(int64)|false|none|Amount of the token|
|» decimals|integer|false|none|Number of decimals of the token|
|» name|string|false|none|Name of the token, if any|

### IndexedErgoBox
<!-- backwards compatibility -->
<a id="schemaindexedergobox"></a>
<a id="schema_IndexedErgoBox"></a>
<a id="tocSindexedergobox"></a>
<a id="tocsindexedergobox"></a>

=== "json"

    ```json
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0,
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingHeight": 147,
      "inclusionHeight": 147,
      "globalIndex": 83927
    }
    ```

#### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ErgoTransactionOutput](#schemaergotransactionoutput)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|Box indexed with extra information|
|» address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|» spentTransactionId|[ModifierId](#schemamodifierid)|true|none|Transaction which spent the box|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|

### IndexedToken
<!-- backwards compatibility -->
<a id="schemaindexedtoken"></a>
<a id="schema_IndexedToken"></a>
<a id="tocSindexedtoken"></a>
<a id="tocsindexedtoken"></a>

=== "json"

    ```json
    {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "boxId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "emissionAmount": 3500000,
      "name": "string",
      "description": "string",
      "decimals": 8
    }
    ```

Token indexed with extra information

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|[ModifierId](#schemamodifierid)|true|none|Id of the token|
|boxId|[ModifierId](#schemamodifierid)|true|none|Id of the box that created the token|
|emissionAmount|integer(int64)|true|none|The total supply of the token|
|name|string|true|none|The name of the token|
|description|string|true|none|The description of the token|
|decimals|integer(int32)|true|none|The number of decimals the token supports|

### UnsignedErgoTransaction
<!-- backwards compatibility -->
<a id="schemaunsignedergotransaction"></a>
<a id="schema_UnsignedErgoTransaction"></a>
<a id="tocSunsignedergotransaction"></a>
<a id="tocsunsignedergotransaction"></a>

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extension": {
            "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ]
    }
    ```

Unsigned Ergo transaction

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|[TransactionId](#schematransactionid)|false|none|Base16-encoded transaction id bytes|
|inputs|[[ErgoTransactionUnsignedInput](#schemaergotransactionunsignedinput)]|true|none|Unsigned inputs of the transaction|
|dataInputs|[[ErgoTransactionDataInput](#schemaergotransactiondatainput)]|true|none|Data inputs of the transaction|
|outputs|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|Outputs of the transaction|

### ErgoTransaction
<!-- backwards compatibility -->
<a id="schemaergotransaction"></a>
<a id="schema_ErgoTransaction"></a>
<a id="tocSergotransaction"></a>
<a id="tocsergotransaction"></a>

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "size": 0
    }
    ```

ErgoTransaction is an atomic operation which changes UTXO state.

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|[TransactionId](#schematransactionid)|false|none|Id of the transaction|
|inputs|[[ErgoTransactionInput](#schemaergotransactioninput)]|true|none|Inputs, that will be spent by this transaction|
|dataInputs|[[ErgoTransactionDataInput](#schemaergotransactiondatainput)]|true|none|Read-only inputs, that are not going to be spent by transaction.|
|outputs|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|Outputs of the transaction, i.e. box candidates to be created by this transaction.|
|size|integer(int32)|false|none|Size of ErgoTransaction in bytes|

### WalletTransaction
<!-- backwards compatibility -->
<a id="schemawallettransaction"></a>
<a id="schema_WalletTransaction"></a>
<a id="tocSwallettransaction"></a>
<a id="tocswallettransaction"></a>

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "inclusionHeight": 20998,
      "numConfirmations": 20998,
      "scans": [
        1
      ],
      "size": 0
    }
    ```

Transaction augmented with some useful information

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|[TransactionId](#schematransactionid)|false|none|Base16-encoded transaction id bytes|
|inputs|[[ErgoTransactionInput](#schemaergotransactioninput)]|true|none|Transaction inputs|
|dataInputs|[[ErgoTransactionDataInput](#schemaergotransactiondatainput)]|true|none|Transaction data inputs|
|outputs|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|Transaction outputs|
|inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|numConfirmations|integer(int32)|true|none|Number of transaction confirmations|
|scans|[integer]|true|none|Scan identifiers the transaction relates to|
|size|integer(int32)|false|none|Size in bytes|

### IndexedErgoTransaction
<!-- backwards compatibility -->
<a id="schemaindexedergotransaction"></a>
<a id="schema_IndexedErgoTransaction"></a>
<a id="tocSindexedergotransaction"></a>
<a id="tocsindexedergotransaction"></a>

=== "json"

    ```json
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "inclusionHeight": 20998,
      "numConfirmations": 20998,
      "blockId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "index": 3,
      "globalIndex": 3565445,
      "size": 0
    }
    ```

Transaction indexed with extra information

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|[TransactionId](#schematransactionid)|true|none|Base16-encoded transaction id bytes|
|inputs|[[ErgoTransactionInput](#schemaergotransactioninput)]|true|none|Transaction inputs|
|dataInputs|[[ErgoTransactionDataInput](#schemaergotransactiondatainput)]|true|none|Transaction data inputs|
|outputs|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|Transaction outputs|
|inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|numConfirmations|integer(int32)|true|none|Number of transaction confirmations|
|blockId|[ModifierId](#schemamodifierid)|true|none|Id of the block the transaction was included in|
|timestamp|[Timestamp](#schematimestamp)|true|none|Basic timestamp definition|
|index|integer(int32)|true|none|index of the transaction in the block it was included in|
|globalIndex|integer(int64)|true|none|Global index of the transaction in the blockchain|
|size|integer(int32)|true|none|Size in bytes|

### ErgoAddress
<!-- backwards compatibility -->
<a id="schemaergoaddress"></a>
<a id="schema_ErgoAddress"></a>
<a id="tocSergoaddress"></a>
<a id="tocsergoaddress"></a>

=== "json"

    ```json
    "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    ```

Encoded Ergo Address

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|Encoded Ergo Address|

### RewardAddress
<!-- backwards compatibility -->
<a id="schemarewardaddress"></a>
<a id="schema_RewardAddress"></a>
<a id="tocSrewardaddress"></a>
<a id="tocsrewardaddress"></a>

=== "json"

    ```json
    {
      "rewardAddress": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|rewardAddress|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|

### RewardPubKey
<!-- backwards compatibility -->
<a id="schemarewardpubkey"></a>
<a id="schema_RewardPubKey"></a>
<a id="tocSrewardpubkey"></a>
<a id="tocsrewardpubkey"></a>

=== "json"

    ```json
    {
      "rewardPubkey": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|rewardPubkey|string|true|none|none|

### DlogSecret
<!-- backwards compatibility -->
<a id="schemadlogsecret"></a>
<a id="schema_DlogSecret"></a>
<a id="tocSdlogsecret"></a>
<a id="tocsdlogsecret"></a>

=== "json"

    ```json
    "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
    ```

Hex-encoded big-endian 256-bits secret exponent

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|Hex-encoded big-endian 256-bits secret exponent|

### DhtSecret
<!-- backwards compatibility -->
<a id="schemadhtsecret"></a>
<a id="schema_DhtSecret"></a>
<a id="tocSdhtsecret"></a>
<a id="tocsdhtsecret"></a>

=== "json"

    ```json
    {
      "secret": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
      "g": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
      "h": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
      "u": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
      "v": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
    }
    ```

Hex-encoded big-endian 256-bits secret exponent "w" along with generators "g", "h", and group elements "u", "v", such as g^w = u, h^w = v

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|secret|string|true|none|Hex-encoded big-endian 256-bits secret exponent|
|g|string|true|none|Hex-encoded "g" generator for the Diffie-Hellman tuple (secp256k1 curve point)|
|h|string|true|none|Hex-encoded "h" generator for the Diffie-Hellman tuple (secp256k1 curve point)|
|u|string|true|none|Hex-encoded "u" group element of the Diffie-Hellman tuple (secp256k1 curve point)|
|v|string|true|none|Hex-encoded "v" group element of the Diffie-Hellman tuple (secp256k1 curve point)|

### TransactionSigningRequest
<!-- backwards compatibility -->
<a id="schematransactionsigningrequest"></a>
<a id="schema_TransactionSigningRequest"></a>
<a id="tocStransactionsigningrequest"></a>
<a id="tocstransactionsigningrequest"></a>

=== "json"

    ```json
    {
      "tx": {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ]
      },
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ],
      "hints": {
        "secretHints": [
          {
            "01": [
              {
                "hint": "cmtWithSecret",
                "pubkey": {
                  "op": -51,
                  "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
                },
                "position": "0-1",
                "type": "dlog",
                "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
                "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
              }
            ]
          }
        ],
        "publicHints": [
          {
            "01": [
              {
                "hint": "cmtWithSecret",
                "pubkey": {
                  "op": -51,
                  "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
                },
                "position": "0-1",
                "type": "dlog",
                "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
                "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
              }
            ]
          }
        ]
      },
      "secrets": {
        "dlog": [
          "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
        ],
        "dht": [
          {
            "secret": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
            "g": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "h": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "u": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "v": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
          }
        ]
      }
    }
    ```

A request to sign a transaction with secrets provided

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tx|[UnsignedErgoTransaction](#schemaunsignedergotransaction)|true|none|Unsigned transaction to sign|
|inputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|
|dataInputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|
|hints|[TransactionHintsBag](#schematransactionhintsbag)|false|none|Optional list of hints used for signing|
|secrets|object|true|none|Secrets used for signing|
|» dlog|[[DlogSecret](#schemadlogsecret)]|false|none|Sequence of secret exponents (DLOG secrets)|
|» dht|[[DhtSecret](#schemadhtsecret)]|false|none|Sequence of secret Diffie-Hellman tuple exponents (DHT secrets)|

### AddressHolder
<!-- backwards compatibility -->
<a id="schemaaddressholder"></a>
<a id="schema_AddressHolder"></a>
<a id="tocSaddressholder"></a>
<a id="tocsaddressholder"></a>

=== "json"

    ```json
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    }
    ```

Holds encoded ErgoAddress

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|

### BoxesRequestHolder
<!-- backwards compatibility -->
<a id="schemaboxesrequestholder"></a>
<a id="schema_BoxesRequestHolder"></a>
<a id="tocSboxesrequestholder"></a>
<a id="tocsboxesrequestholder"></a>

=== "json"

    ```json
    {
      "targetAssets": [
        [
          "string",
          "string"
        ]
      ],
      "targetBalance": 0
    }
    ```

Holds request for wallet boxes

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|targetAssets|[array]|true|none|Target assets|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|TokenId|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|Long|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|targetBalance|integer(int64)|true|none|Target balance|

### RequestsHolder
<!-- backwards compatibility -->
<a id="schemarequestsholder"></a>
<a id="schema_RequestsHolder"></a>
<a id="tocSrequestsholder"></a>
<a id="tocsrequestsholder"></a>

=== "json"

    ```json
    {
      "requests": [
        {
          "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
          "value": 1,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "registers": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          }
        }
      ],
      "fee": 1000000,
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }
    ```

Holds many transaction requests and transaction fee

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|requests|[anyOf]|true|none|Sequence of transaction requests|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[PaymentRequest](#schemapaymentrequest)|false|none|Request for generation of payment transaction to a given address|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[BurnTokensRequest](#schemaburntokensrequest)|false|none|Request for burning tokens in wallet|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[AssetIssueRequest](#schemaassetissuerequest)|false|none|Request for generation of asset issue transaction|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|fee|integer(int64)|false|none|Transaction fee|
|inputsRaw|[string]|false|none|List of inputs to be used in serialized form|
|dataInputsRaw|[string]|false|none|List of data inputs to be used in serialized form|

### SourceHolder
<!-- backwards compatibility -->
<a id="schemasourceholder"></a>
<a id="schema_SourceHolder"></a>
<a id="tocSsourceholder"></a>
<a id="tocssourceholder"></a>

=== "json"

    ```json
    {
      "source": "string"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|source|string|true|none|Sigma source to be compiled|

### ErgoLikeTransaction
<!-- backwards compatibility -->
<a id="schemaergoliketransaction"></a>
<a id="schema_ErgoLikeTransaction"></a>
<a id="tocSergoliketransaction"></a>
<a id="tocsergoliketransaction"></a>

=== "json"

    ```json
    {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ]
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|[ModifierId](#schemamodifierid)|true|none|Base16-encoded 32 byte modifier id|
|inputs|[[ErgoTransactionInput](#schemaergotransactioninput)]|true|none|none|
|dataInputs|[[ErgoTransactionDataInput](#schemaergotransactiondatainput)]|true|none|none|
|outputs|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|none|

### SigmaHeader
<!-- backwards compatibility -->
<a id="schemasigmaheader"></a>
<a id="schema_SigmaHeader"></a>
<a id="tocSsigmaheader"></a>
<a id="tocssigmaheader"></a>

=== "json"

    ```json
    {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "version": 2,
      "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateRoot": {
        "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "treeFlags": 0,
        "keyLength": 0,
        "valueLength": 0
      },
      "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "nBits": 19857408,
      "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "extensionRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "height": 667,
      "size": 667,
      "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "powSolutions": {
        "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
        "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
        "n": "0000000000000000",
        "d": 987654321
      },
      "votes": "000000",
      "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
      "powOnetimePk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
      "powNonce": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "powDistance": 123456789
    }
    ```

Block header format used for sigma ErgoLikeContext

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|[ModifierId](#schemamodifierid)|false|none|Base16-encoded 32 byte modifier id|
|timestamp|[Timestamp](#schematimestamp)|true|none|Basic timestamp definition|
|version|[Version](#schemaversion)|true|none|Ergo blockchain protocol version|
|adProofsRoot|[Digest32](#schemadigest32)|true|none|Base16-encoded 32 byte digest|
|adProofsId|[ModifierId](#schemamodifierid)|false|none|Base16-encoded 32 byte modifier id|
|stateRoot|[AvlTreeData](#schemaavltreedata)|true|none|none|
|transactionsRoot|[Digest32](#schemadigest32)|true|none|Base16-encoded 32 byte digest|
|transactionsId|[ModifierId](#schemamodifierid)|false|none|Base16-encoded 32 byte modifier id|
|nBits|integer(int64)|true|none|none|
|extensionHash|[Digest32](#schemadigest32)|true|none|Base16-encoded 32 byte digest|
|extensionRoot|[Digest32](#schemadigest32)|false|none|Base16-encoded 32 byte digest|
|extensionId|[ModifierId](#schemamodifierid)|false|none|Base16-encoded 32 byte modifier id|
|height|integer(int32)|true|none|none|
|size|integer(int32)|false|none|none|
|parentId|[ModifierId](#schemamodifierid)|true|none|Base16-encoded 32 byte modifier id|
|powSolutions|[PowSolutions](#schemapowsolutions)|false|none|An object containing all components of pow solution|
|votes|[Votes](#schemavotes)|true|none|Base16-encoded votes for a soft-fork and parameters|
|minerPk|string|false|none|none|
|powOnetimePk|string|false|none|none|
|powNonce|[Digest32](#schemadigest32)|false|none|Base16-encoded 32 byte digest|
|powDistance|number|false|none|sigma.BigInt|

### PreHeader
<!-- backwards compatibility -->
<a id="schemapreheader"></a>
<a id="schema_PreHeader"></a>
<a id="tocSpreheader"></a>
<a id="tocspreheader"></a>

=== "json"

    ```json
    {
      "timestamp": 1524143059077,
      "version": 2,
      "nBits": 19857408,
      "height": 667,
      "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "votes": "000000",
      "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|timestamp|[Timestamp](#schematimestamp)|true|none|Basic timestamp definition|
|version|[Version](#schemaversion)|true|none|Ergo blockchain protocol version|
|nBits|integer(int64)|true|none|none|
|height|integer(int32)|true|none|none|
|parentId|[ModifierId](#schemamodifierid)|true|none|Base16-encoded 32 byte modifier id|
|votes|[Votes](#schemavotes)|true|none|Base16-encoded votes for a soft-fork and parameters|
|minerPk|string|false|none|none|

### AvlTreeData
<!-- backwards compatibility -->
<a id="schemaavltreedata"></a>
<a id="schema_AvlTreeData"></a>
<a id="tocSavltreedata"></a>
<a id="tocsavltreedata"></a>

=== "json"

    ```json
    {
      "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "treeFlags": 0,
      "keyLength": 0,
      "valueLength": 0
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|digest|[Digest32](#schemadigest32)|true|none|Base16-encoded 32 byte digest|
|treeFlags|integer(int32)|false|none|none|
|keyLength|integer(int32)|false|none|none|
|valueLength|integer(int32)¦null|false|none|none|

### ErgoLikeContext
<!-- backwards compatibility -->
<a id="schemaergolikecontext"></a>
<a id="schema_ErgoLikeContext"></a>
<a id="tocSergolikecontext"></a>
<a id="tocsergolikecontext"></a>

=== "json"

    ```json
    {
      "lastBlockUtxoRoot": {
        "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "treeFlags": 0,
        "keyLength": 0,
        "valueLength": 0
      },
      "headers": [
        {
          "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "timestamp": 1524143059077,
          "version": 2,
          "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "stateRoot": {
            "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "treeFlags": 0,
            "keyLength": 0,
            "valueLength": 0
          },
          "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "nBits": 19857408,
          "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extensionRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "height": 667,
          "size": 667,
          "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "powSolutions": {
            "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
            "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
            "n": "0000000000000000",
            "d": 987654321
          },
          "votes": "000000",
          "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
          "powOnetimePk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
          "powNonce": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "powDistance": 123456789
        }
      ],
      "preHeader": {
        "timestamp": 1524143059077,
        "version": 2,
        "nBits": 19857408,
        "height": 667,
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
      },
      "dataBoxes": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "boxesToSpend": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "spendingTransaction": {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ]
      },
      "selfIndex": 0,
      "extension": {},
      "validationSettings": "10e8070001e9070001ea070001eb070001ec070001ed070001ee070001ef070001f0070001f1070001f2070001f3070001f4070001f5070001f6070001f7070001",
      "costLimit": 0,
      "initCost": 0
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lastBlockUtxoRoot|[AvlTreeData](#schemaavltreedata)|true|none|state root before current block application|
|headers|[[SigmaHeader](#schemasigmaheader)]|true|none|fixed number of last block headers in descending order (first header is the newest one)|
|preHeader|[PreHeader](#schemapreheader)|true|none|fields of block header with the current `spendingTransaction`, that can be predicted by a miner before its formation|
|dataBoxes|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|boxes, that corresponds to id's of `spendingTransaction.dataInputs`|
|boxesToSpend|[[ErgoTransactionOutput](#schemaergotransactionoutput)]|true|none|boxes, that corresponds to id's of `spendingTransaction.inputs`|
|spendingTransaction|[ErgoLikeTransaction](#schemaergoliketransaction)|true|none|transaction that contains `self` box|
|selfIndex|integer(int64)|true|none|index of the box in `boxesToSpend` that contains the script we're evaluating|
|extension|object|true|none|prover-defined key-value pairs, that may be used inside a script|
|validationSettings|string|true|none|validation parameters passed to Interpreter.verify to detect soft-fork conditions|
|costLimit|integer(int64)|true|none|hard limit on accumulated execution cost, if exceeded lead to CostLimitException to be thrown|
|initCost|integer(int64)|true|none|initial value of execution cost already accumulated before Interpreter.verify is called|

### ExecuteScript
<!-- backwards compatibility -->
<a id="schemaexecutescript"></a>
<a id="schema_ExecuteScript"></a>
<a id="tocSexecutescript"></a>
<a id="tocsexecutescript"></a>

=== "json"

    ```json
    {
      "script": "string",
      "namedConstants": {},
      "context": {
        "lastBlockUtxoRoot": {
          "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "treeFlags": 0,
          "keyLength": 0,
          "valueLength": 0
        },
        "headers": [
          {
            "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "timestamp": 1524143059077,
            "version": 2,
            "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "stateRoot": {
              "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "treeFlags": 0,
              "keyLength": 0,
              "valueLength": 0
            },
            "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "nBits": 19857408,
            "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extensionRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "height": 667,
            "size": 667,
            "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "powSolutions": {
              "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
              "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
              "n": "0000000000000000",
              "d": 987654321
            },
            "votes": "000000",
            "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
            "powOnetimePk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
            "powNonce": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "powDistance": 123456789
          }
        ],
        "preHeader": {
          "timestamp": 1524143059077,
          "version": 2,
          "nBits": 19857408,
          "height": 667,
          "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "votes": "000000",
          "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
        },
        "dataBoxes": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "boxesToSpend": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "spendingTransaction": {
          "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "inputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "spendingProof": {
                "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "extension": {
                  "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                }
              }
            }
          ],
          "dataInputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
            }
          ],
          "outputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "value": 147,
              "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
              "creationHeight": 9149,
              "assets": [
                {
                  "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "amount": 1000
                }
              ],
              "additionalRegisters": {
                "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
              },
              "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "index": 0
            }
          ]
        },
        "selfIndex": 0,
        "extension": {},
        "validationSettings": "10e8070001e9070001ea070001eb070001ec070001ed070001ee070001ef070001f0070001f1070001f2070001f3070001f4070001f5070001f6070001f7070001",
        "costLimit": 0,
        "initCost": 0
      }
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|script|string|true|none|Sigma script to be executed|
|namedConstants|object¦null|true|none|Environment for compiler|
|context|[ErgoLikeContext](#schemaergolikecontext)|true|none|Interpreter context|

### SigmaBoolean
<!-- backwards compatibility -->
<a id="schemasigmaboolean"></a>
<a id="schema_SigmaBoolean"></a>
<a id="tocSsigmaboolean"></a>
<a id="tocssigmaboolean"></a>

=== "json"

    ```json
    {
      "op": 0,
      "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "condition": true
    }
    ```

Algebraic data type of sigma proposition expressions

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|op|integer(int8)|true|none|Sigma opCode|
|h|[HexString](#schemahexstring)|false|none|Base16-encoded bytes|
|g|[HexString](#schemahexstring)|false|none|Base16-encoded bytes|
|u|[HexString](#schemahexstring)|false|none|Base16-encoded bytes|
|v|[HexString](#schemahexstring)|false|none|Base16-encoded bytes|
|condition|boolean|false|none|none|

### SigmaBooleanAndPredicate
<!-- backwards compatibility -->
<a id="schemasigmabooleanandpredicate"></a>
<a id="schema_SigmaBooleanAndPredicate"></a>
<a id="tocSsigmabooleanandpredicate"></a>
<a id="tocssigmabooleanandpredicate"></a>

=== "json"

    ```json
    {
      "args": [
        {
          "op": 0,
          "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "condition": true
        }
      ]
    }
    ```

#### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[SigmaBoolean](#schemasigmaboolean)|false|none|Algebraic data type of sigma proposition expressions|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» args|[[SigmaBoolean](#schemasigmaboolean)]|false|none|[Algebraic data type of sigma proposition expressions]|

### SigmaBooleanOrPredicate
<!-- backwards compatibility -->
<a id="schemasigmabooleanorpredicate"></a>
<a id="schema_SigmaBooleanOrPredicate"></a>
<a id="tocSsigmabooleanorpredicate"></a>
<a id="tocssigmabooleanorpredicate"></a>

=== "json"

    ```json
    {
      "args": [
        {
          "op": 0,
          "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "condition": true
        }
      ]
    }
    ```

#### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[SigmaBoolean](#schemasigmaboolean)|false|none|Algebraic data type of sigma proposition expressions|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» args|[[SigmaBoolean](#schemasigmaboolean)]|false|none|[Algebraic data type of sigma proposition expressions]|

### SigmaBooleanThresholdPredicate
<!-- backwards compatibility -->
<a id="schemasigmabooleanthresholdpredicate"></a>
<a id="schema_SigmaBooleanThresholdPredicate"></a>
<a id="tocSsigmabooleanthresholdpredicate"></a>
<a id="tocssigmabooleanthresholdpredicate"></a>

=== "json"

    ```json
    {
      "args": [
        {
          "op": 0,
          "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "condition": true
        }
      ]
    }
    ```

#### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[SigmaBoolean](#schemasigmaboolean)|false|none|Algebraic data type of sigma proposition expressions|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» args|[[SigmaBoolean](#schemasigmaboolean)]|false|none|[Algebraic data type of sigma proposition expressions]|

### CryptoResult
<!-- backwards compatibility -->
<a id="schemacryptoresult"></a>
<a id="schema_CryptoResult"></a>
<a id="tocScryptoresult"></a>
<a id="tocscryptoresult"></a>

=== "json"

    ```json
    {
      "value": {
        "op": -45,
        "condition": true
      },
      "cost": 10
    }
    ```

Result of executeWithContext request (reduceToCrypto)

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|value|[SigmaBoolean](#schemasigmaboolean)|true|none|value of SigmaProp type which represents a statement verifiable via sigma protocol|
|cost|integer(int64)|true|none|Estimated cost of contract execution|

### ScanningPredicate
<!-- backwards compatibility -->
<a id="schemascanningpredicate"></a>
<a id="schema_ScanningPredicate"></a>
<a id="tocSscanningpredicate"></a>
<a id="tocsscanningpredicate"></a>

=== "json"

    ```json
    {
      "predicate": "string"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|predicate|string|true|none|none|

### ContainsPredicate
<!-- backwards compatibility -->
<a id="schemacontainspredicate"></a>
<a id="schema_ContainsPredicate"></a>
<a id="tocScontainspredicate"></a>
<a id="tocscontainspredicate"></a>

=== "json"

    ```json
    {
      "predicate": "string",
      "register": "string",
      "bytes": "string"
    }
    ```

#### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ScanningPredicate](#schemascanningpredicate)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» register|string|false|none|none|
|» bytes|string|false|none|none|

### EqualsPredicate
<!-- backwards compatibility -->
<a id="schemaequalspredicate"></a>
<a id="schema_EqualsPredicate"></a>
<a id="tocSequalspredicate"></a>
<a id="tocsequalspredicate"></a>

=== "json"

    ```json
    {
      "predicate": "string",
      "register": "string",
      "bytes": "string"
    }
    ```

#### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ScanningPredicate](#schemascanningpredicate)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» register|string|false|none|none|
|» bytes|string|false|none|none|

### ContainsAssetPredicate
<!-- backwards compatibility -->
<a id="schemacontainsassetpredicate"></a>
<a id="schema_ContainsAssetPredicate"></a>
<a id="tocScontainsassetpredicate"></a>
<a id="tocscontainsassetpredicate"></a>

=== "json"

    ```json
    {
      "predicate": "string",
      "assetId": "string"
    }
    ```

#### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ScanningPredicate](#schemascanningpredicate)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» assetId|string|false|none|none|

### AndPredicate
<!-- backwards compatibility -->
<a id="schemaandpredicate"></a>
<a id="schema_AndPredicate"></a>
<a id="tocSandpredicate"></a>
<a id="tocsandpredicate"></a>

=== "json"

    ```json
    {
      "predicate": "string",
      "args": [
        {
          "predicate": "string"
        }
      ]
    }
    ```

#### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ScanningPredicate](#schemascanningpredicate)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» args|[[ScanningPredicate](#schemascanningpredicate)]|false|none|none|

### OrPredicate
<!-- backwards compatibility -->
<a id="schemaorpredicate"></a>
<a id="schema_OrPredicate"></a>
<a id="tocSorpredicate"></a>
<a id="tocsorpredicate"></a>

=== "json"

    ```json
    {
      "predicate": "string",
      "args": [
        {
          "predicate": "string"
        }
      ]
    }
    ```

#### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ScanningPredicate](#schemascanningpredicate)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» args|[[ScanningPredicate](#schemascanningpredicate)]|false|none|none|

### ScanRequest
<!-- backwards compatibility -->
<a id="schemascanrequest"></a>
<a id="schema_ScanRequest"></a>
<a id="tocSscanrequest"></a>
<a id="tocsscanrequest"></a>

=== "json"

    ```json
    {
      "scanName": "Assets Tracker",
      "walletInteraction": "off",
      "removeOffchain": true,
      "trackingRule": {
        "predicate": "containsAsset",
        "assetId": "02dada811a888cd0dc7a0a41739a3ad9b0f427741fe6ca19700cf1a51200c96bf7"
      }
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scanName|string|false|none|none|
|removeOffchain|boolean|false|none|none|
|walletInteraction|string|false|none|none|
|trackingRule|[ScanningPredicate](#schemascanningpredicate)|false|none|none|

##### Enumerated Values

|Property|Value|
|---|---|
|walletInteraction|off|
|walletInteraction|shared|
|walletInteraction|forced|

### Scan
<!-- backwards compatibility -->
<a id="schemascan"></a>
<a id="schema_Scan"></a>
<a id="tocSscan"></a>
<a id="tocsscan"></a>

=== "json"

    ```json
    {
      "scanId": 2,
      "scanName": "Assets Tracker",
      "walletInteraction": "off",
      "removeOffchain": true,
      "trackingRule": {
        "predicate": "containsAsset",
        "assetId": "02dada811a888cd0dc7a0a41739a3ad9b0f427741fe6ca19700cf1a51200c96bf7"
      }
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scanName|string|false|none|none|
|scanId|integer|false|none|none|
|walletInteraction|string|false|none|none|
|removeOffchain|boolean|false|none|none|
|trackingRule|[ScanningPredicate](#schemascanningpredicate)|false|none|none|

##### Enumerated Values

|Property|Value|
|---|---|
|walletInteraction|off|
|walletInteraction|shared|
|walletInteraction|forced|

### ScanId
<!-- backwards compatibility -->
<a id="schemascanid"></a>
<a id="schema_ScanId"></a>
<a id="tocSscanid"></a>
<a id="tocsscanid"></a>

=== "json"

    ```json
    {
      "scanId": 0
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scanId|integer|false|none|none|

### ScanIdBoxId
<!-- backwards compatibility -->
<a id="schemascanidboxid"></a>
<a id="schema_ScanIdBoxId"></a>
<a id="tocSscanidboxid"></a>
<a id="tocsscanidboxid"></a>

=== "json"

    ```json
    {
      "scanId": 0,
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scanId|integer|true|none|none|
|boxId|[TransactionBoxId](#schematransactionboxid)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|

### ScanIdsBox
<!-- backwards compatibility -->
<a id="schemascanidsbox"></a>
<a id="schema_ScanIdsBox"></a>
<a id="tocSscanidsbox"></a>
<a id="tocsscanidsbox"></a>

=== "json"

    ```json
    {
      "scanIds": [
        0
      ],
      "box": {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    }
    ```

Ergo box with associated scans (their respective identifiers)

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scanIds|[integer]|true|none|none|
|box|[ErgoTransactionOutput](#schemaergotransactionoutput)|true|none|none|

### DlogCommitment
<!-- backwards compatibility -->
<a id="schemadlogcommitment"></a>
<a id="schema_DlogCommitment"></a>
<a id="tocSdlogcommitment"></a>
<a id="tocsdlogcommitment"></a>

=== "json"

    ```json
    {
      "r": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
      "a": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
    }
    ```

Randomness and commitment for the first step of the Schnorr protocol

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|r|string|true|none|Hex-encoded big-endian 256-bits secret exponent|
|a|string|true|none|Hex-encoded "g" generator for the Diffie-Hellman tuple (secp256k1 curve point)|

### HintExtractionRequest
<!-- backwards compatibility -->
<a id="schemahintextractionrequest"></a>
<a id="schema_HintExtractionRequest"></a>
<a id="tocShintextractionrequest"></a>
<a id="tocshintextractionrequest"></a>

=== "json"

    ```json
    {
      "tx": {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "size": 0
      },
      "real": [
        {
          "op": 0,
          "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "condition": true
        }
      ],
      "simulated": [
        {
          "op": 0,
          "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "condition": true
        }
      ],
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }
    ```

request to extract prover hints from a transaction

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tx|[ErgoTransaction](#schemaergotransaction)|true|none|Transaction to extract prover hints from|
|real|[[SigmaBoolean](#schemasigmaboolean)]|true|none|Real signers of the transaction|
|simulated|[[SigmaBoolean](#schemasigmaboolean)]|true|none|Simulated signers of the transaction|
|inputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|
|dataInputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|

### Commitment
<!-- backwards compatibility -->
<a id="schemacommitment"></a>
<a id="schema_Commitment"></a>
<a id="tocScommitment"></a>
<a id="tocscommitment"></a>

=== "json"

    ```json
    {
      "hint": "cmtWithSecret",
      "pubkey": {
        "op": 0,
        "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "condition": true
      },
      "position": "string",
      "type": "dlog",
      "a": "string",
      "b": "string"
    }
    ```

basic trait for prover commitments

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hint|string|true|none|none|
|pubkey|[SigmaBoolean](#schemasigmaboolean)|true|none|Algebraic data type of sigma proposition expressions|
|position|string|true|none|none|
|type|string|false|none|none|
|a|string|true|none|a group element of the commitment|
|b|string|false|none|b group element of the commitment (needed for DHT protocol only)|

##### Enumerated Values

|Property|Value|
|---|---|
|hint|cmtWithSecret|
|hint|cmtReal|
|hint|cmtSimulated|
|type|dlog|
|type|dht|

### CommitmentWithSecret
<!-- backwards compatibility -->
<a id="schemacommitmentwithsecret"></a>
<a id="schema_CommitmentWithSecret"></a>
<a id="tocScommitmentwithsecret"></a>
<a id="tocscommitmentwithsecret"></a>

=== "json"

    ```json
    {
      "hint": "cmtWithSecret",
      "pubkey": {
        "op": 0,
        "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "condition": true
      },
      "position": "string",
      "type": "dlog",
      "a": "string",
      "b": "string"
    }
    ```

commitment to secret along with secret (!) randomness

#### Properties

*None*

### SecretProven
<!-- backwards compatibility -->
<a id="schemasecretproven"></a>
<a id="schema_SecretProven"></a>
<a id="tocSsecretproven"></a>
<a id="tocssecretproven"></a>

=== "json"

    ```json
    {
      "hint": "proofReal",
      "challenge": "string",
      "pubkey": {
        "op": 0,
        "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "condition": true
      },
      "proof": "string",
      "position": "string"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hint|string|true|none|none|
|challenge|string|true|none|none|
|pubkey|[SigmaBoolean](#schemasigmaboolean)|true|none|Algebraic data type of sigma proposition expressions|
|proof|string|true|none|none|
|position|string|true|none|none|

##### Enumerated Values

|Property|Value|
|---|---|
|hint|proofReal|
|hint|proofSimulated|

### InputHints
<!-- backwards compatibility -->
<a id="schemainputhints"></a>
<a id="schema_InputHints"></a>
<a id="tocSinputhints"></a>
<a id="tocsinputhints"></a>

=== "json"

    ```json
    {
      "01": [
        {
          "hint": "cmtWithSecret",
          "pubkey": {
            "op": -51,
            "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
          },
          "position": "0-1",
          "type": "dlog",
          "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
          "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
        }
      ]
    }
    ```

hints for inputs, key is input index, values is a set of hints for the input

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|**additionalProperties**|[oneOf]|false|none|none|

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[CommitmentWithSecret](#schemacommitmentwithsecret)|false|none|commitment to secret along with secret (!) randomness|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[Commitment](#schemacommitment)|false|none|basic trait for prover commitments|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[SecretProven](#schemasecretproven)|false|none|none|

### TransactionHintsBag
<!-- backwards compatibility -->
<a id="schematransactionhintsbag"></a>
<a id="schema_TransactionHintsBag"></a>
<a id="tocStransactionhintsbag"></a>
<a id="tocstransactionhintsbag"></a>

=== "json"

    ```json
    {
      "secretHints": [
        {
          "01": [
            {
              "hint": "cmtWithSecret",
              "pubkey": {
                "op": -51,
                "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
              },
              "position": "0-1",
              "type": "dlog",
              "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
              "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
            }
          ]
        }
      ],
      "publicHints": [
        {
          "01": [
            {
              "hint": "cmtWithSecret",
              "pubkey": {
                "op": -51,
                "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
              },
              "position": "0-1",
              "type": "dlog",
              "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
              "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
            }
          ]
        }
      ]
    }
    ```

prover hints extracted from a transaction

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|secretHints|[[InputHints](#schemainputhints)]|false|none|Hints which contain secrets, do not share them!|
|publicHints|[[InputHints](#schemainputhints)]|false|none|Hints which contain public data only, share them freely!|

### GenerateCommitmentsRequest
<!-- backwards compatibility -->
<a id="schemageneratecommitmentsrequest"></a>
<a id="schema_GenerateCommitmentsRequest"></a>
<a id="tocSgeneratecommitmentsrequest"></a>
<a id="tocsgeneratecommitmentsrequest"></a>

=== "json"

    ```json
    {
      "tx": {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ]
      },
      "secrets": {
        "dlog": [
          "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
        ],
        "dht": [
          {
            "secret": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
            "g": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "h": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "u": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
            "v": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
          }
        ]
      },
      "inputsRaw": [
        "string"
      ],
      "dataInputsRaw": [
        "string"
      ]
    }
    ```

request to generate commitments to sign a transaction

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tx|[UnsignedErgoTransaction](#schemaunsignedergotransaction)|true|none|Unsigned transaction to sign|
|secrets|object|false|none|Optionally, external secrets used for signing|
|» dlog|[[DlogSecret](#schemadlogsecret)]|false|none|Sequence of secret exponents (DLOG secrets)|
|» dht|[[DhtSecret](#schemadhtsecret)]|false|none|Sequence of secret Diffie-Hellman tuple exponents (DHT secrets)|
|inputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|
|dataInputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|

### PaymentRequest
<!-- backwards compatibility -->
<a id="schemapaymentrequest"></a>
<a id="schema_PaymentRequest"></a>
<a id="tocSpaymentrequest"></a>
<a id="tocspaymentrequest"></a>

=== "json"

    ```json
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "value": 1,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "registers": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      }
    }
    ```

Request for generation of payment transaction to a given address

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|value|integer(int64)|true|none|Payment amount|
|assets|[[Asset](#schemaasset)]|false|none|Assets list in the transaction|
|registers|[Registers](#schemaregisters)|false|none|Ergo box registers|

### BurnTokensRequest
<!-- backwards compatibility -->
<a id="schemaburntokensrequest"></a>
<a id="schema_BurnTokensRequest"></a>
<a id="tocSburntokensrequest"></a>
<a id="tocsburntokensrequest"></a>

=== "json"

    ```json
    {
      "assetsToBurn": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ]
    }
    ```

Request for burning tokens in wallet

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|assetsToBurn|[[Asset](#schemaasset)]|true|none|Assets list to burn in the transaction|

### AssetIssueRequest
<!-- backwards compatibility -->
<a id="schemaassetissuerequest"></a>
<a id="schema_AssetIssueRequest"></a>
<a id="tocSassetissuerequest"></a>
<a id="tocsassetissuerequest"></a>

=== "json"

    ```json
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "ergValue": 0,
      "amount": 1000000,
      "name": "TST",
      "description": "Test token",
      "decimals": 8,
      "registers": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      }
    }
    ```

Request for generation of asset issue transaction

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|[ErgoAddress](#schemaergoaddress)|false|none|Optional, first address in the wallet will be used if not defined|
|ergValue|integer(int64)|false|none|Optional, amount of ergs to be put into box with issued assets|
|amount|integer(int64)|true|none|Supply amount|
|name|string|true|none|Assets name|
|description|string|true|none|Assets description|
|decimals|integer(int32)|true|none|Number of decimal places|
|registers|[Registers](#schemaregisters)|false|none|Optional, possible values for registers R7...R9|

### FullBlock
<!-- backwards compatibility -->
<a id="schemafullblock"></a>
<a id="schema_FullBlock"></a>
<a id="tocSfullblock"></a>
<a id="tocsfullblock"></a>

=== "json"

    ```json
    {
      "header": {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      },
      "blockTransactions": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactions": [
          {
            "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "inputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "spendingProof": {
                  "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "extension": {
                    "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                  }
                }
              }
            ],
            "dataInputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
              }
            ],
            "outputs": [
              {
                "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "value": 147,
                "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
                "creationHeight": 9149,
                "assets": [
                  {
                    "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                    "amount": 1000
                  }
                ],
                "additionalRegisters": {
                  "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
                },
                "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "index": 0
              }
            ],
            "size": 0
          }
        ],
        "size": 0
      },
      "adProofs": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "proofBytes": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "size": 0
      },
      "extension": {
        "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "fields": [
          [
            "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          ]
        ]
      },
      "size": 0
    }
    ```

Block with header and transactions

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|header|[BlockHeader](#schemablockheader)|true|none|Header of a block. It authenticates link to a previous block, other block sections (transactions, UTXO set transformation proofs, extension), UTXO set, votes for blockchain parameters to be changed and proof-of-work related data.|
|blockTransactions|[BlockTransactions](#schemablocktransactions)|true|none|Section of a block which contains transactions.|
|adProofs|[BlockADProofs](#schemablockadproofs)|true|none|none|
|extension|[Extension](#schemaextension)|true|none|Section of a block which contains extension data.|
|size|integer(int32)|true|none|Size in bytes|

### PowSolutions
<!-- backwards compatibility -->
<a id="schemapowsolutions"></a>
<a id="schema_PowSolutions"></a>
<a id="tocSpowsolutions"></a>
<a id="tocspowsolutions"></a>

=== "json"

    ```json
    {
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
      "n": "0000000000000000",
      "d": 987654321
    }
    ```

An object containing all components of pow solution

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pk|string|true|none|Base16-encoded public key|
|w|string|true|none|none|
|n|string|true|none|none|
|d|number|true|none|none|

### BlockHeaderWithoutPow
<!-- backwards compatibility -->
<a id="schemablockheaderwithoutpow"></a>
<a id="schema_BlockHeaderWithoutPow"></a>
<a id="tocSblockheaderwithoutpow"></a>
<a id="tocsblockheaderwithoutpow"></a>

=== "json"

    ```json
    {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "version": 2,
      "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "nBits": 19857408,
      "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "height": 667,
      "difficulty": 62,
      "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "votes": "000000",
      "size": 0,
      "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|[ModifierId](#schemamodifierid)|true|none|Base16-encoded 32 byte modifier id|
|timestamp|[Timestamp](#schematimestamp)|true|none|Basic timestamp definition|
|version|[Version](#schemaversion)|true|none|Ergo blockchain protocol version|
|adProofsRoot|[Digest32](#schemadigest32)|true|none|Base16-encoded 32 byte digest|
|stateRoot|[ADDigest](#schemaaddigest)|true|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|
|transactionsRoot|[Digest32](#schemadigest32)|true|none|Base16-encoded 32 byte digest|
|nBits|integer(int64)|true|none|none|
|extensionHash|[Digest32](#schemadigest32)|true|none|Base16-encoded 32 byte digest|
|height|integer(int32)|true|none|none|
|difficulty|integer(int32)|true|none|none|
|parentId|[ModifierId](#schemamodifierid)|true|none|Base16-encoded 32 byte modifier id|
|votes|[Votes](#schemavotes)|true|none|Base16-encoded votes for a soft-fork and parameters|
|size|integer(int32)|false|none|Size in bytes|
|extensionId|[ModifierId](#schemamodifierid)|false|none|Base16-encoded 32 byte modifier id|
|transactionsId|[ModifierId](#schemamodifierid)|false|none|Base16-encoded 32 byte modifier id|
|adProofsId|[ModifierId](#schemamodifierid)|false|none|Base16-encoded 32 byte modifier id|

### PopowHeader
<!-- backwards compatibility -->
<a id="schemapopowheader"></a>
<a id="schema_PopowHeader"></a>
<a id="tocSpopowheader"></a>
<a id="tocspopowheader"></a>

=== "json"

    ```json
    {
      "header": {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      },
      "interlinks": [
        "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      ]
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|header|[BlockHeader](#schemablockheader)|true|none|Header of a block. It authenticates link to a previous block, other block sections (transactions, UTXO set transformation proofs, extension), UTXO set, votes for blockchain parameters to be changed and proof-of-work related data.|
|interlinks|[[ModifierId](#schemamodifierid)]|true|none|Array of header interlinks|

### NipopowProof
<!-- backwards compatibility -->
<a id="schemanipopowproof"></a>
<a id="schema_NipopowProof"></a>
<a id="tocSnipopowproof"></a>
<a id="tocsnipopowproof"></a>

=== "json"

    ```json
    {
      "m": 0,
      "k": 0,
      "prefix": [
        {
          "header": {
            "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "timestamp": 1524143059077,
            "version": 2,
            "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "nBits": 19857408,
            "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "powSolutions": {
              "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
              "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
              "n": "0000000000000000",
              "d": 987654321
            },
            "height": 667,
            "difficulty": "9575989248",
            "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "votes": "000000",
            "size": 0,
            "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          },
          "interlinks": [
            "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          ]
        }
      ],
      "suffixHead": {
        "header": {
          "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "timestamp": 1524143059077,
          "version": 2,
          "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "nBits": 19857408,
          "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "powSolutions": {
            "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
            "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
            "n": "0000000000000000",
            "d": 987654321
          },
          "height": 667,
          "difficulty": "9575989248",
          "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "votes": "000000",
          "size": 0,
          "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        },
        "interlinks": [
          "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        ]
      },
      "suffixTail": [
        {
          "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "timestamp": 1524143059077,
          "version": 2,
          "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "nBits": 19857408,
          "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "powSolutions": {
            "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
            "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
            "n": "0000000000000000",
            "d": 987654321
          },
          "height": 667,
          "difficulty": "9575989248",
          "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "votes": "000000",
          "size": 0,
          "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ]
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|m|number|true|none|security parameter (min μ-level superchain length)|
|k|number|true|none|security parameter (min suffix length, >= 1)|
|prefix|[[PopowHeader](#schemapopowheader)]|true|none|proof prefix headers|
|suffixHead|[PopowHeader](#schemapopowheader)|true|none|none|
|suffixTail|[[BlockHeader](#schemablockheader)]|true|none|tail of the proof suffix headers|

### BlockHeader
<!-- backwards compatibility -->
<a id="schemablockheader"></a>
<a id="schema_BlockHeader"></a>
<a id="tocSblockheader"></a>
<a id="tocsblockheader"></a>

=== "json"

    ```json
    {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "version": 2,
      "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "nBits": 19857408,
      "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "powSolutions": {
        "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
        "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
        "n": "0000000000000000",
        "d": 987654321
      },
      "height": 667,
      "difficulty": "9575989248",
      "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "votes": "000000",
      "size": 0,
      "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
    ```

Header of a block. It authenticates link to a previous block, other block sections (transactions, UTXO set transformation proofs, extension), UTXO set, votes for blockchain parameters to be changed and proof-of-work related data.

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|[ModifierId](#schemamodifierid)|true|none|Block id|
|timestamp|[Timestamp](#schematimestamp)|true|none|Block generation time reported by a miner|
|version|[Version](#schemaversion)|true|none|Protocol version used to generate the block|
|adProofsRoot|[Digest32](#schemadigest32)|true|none|Digest of UTXO set transformation proofs|
|stateRoot|[ADDigest](#schemaaddigest)|true|none|AVL+ tree digest of UTXO set (after the block is applied)|
|transactionsRoot|[Digest32](#schemadigest32)|true|none|Merkle tree digest of transactions in the block (BlockTransactions section)|
|nBits|integer(int64)|true|none|Proof-of-work target (difficulty encoded)|
|extensionHash|[Digest32](#schemadigest32)|true|none|Merkle tree digest of the extension section of the block|
|powSolutions|[PowSolutions](#schemapowsolutions)|true|none|Solution for the proof-of-work puzzle|
|height|integer(int32)|true|none|Height of the block (genesis block height == 1)|
|difficulty|string|true|none|none|
|parentId|[ModifierId](#schemamodifierid)|true|none|Base16-encoded 32 byte modifier id|
|votes|[Votes](#schemavotes)|true|none|Votes for changing system parameters|
|size|integer(int32)|false|none|Size of the header in bytes|
|extensionId|[ModifierId](#schemamodifierid)|false|none|Hash of the extension section of the block == hash(modifier type id, header id, extensionHash)|
|transactionsId|[ModifierId](#schemamodifierid)|false|none|Hash of the transactions section of the block == hash(modifier type id, header id, transactionsRoot)|
|adProofsId|[ModifierId](#schemamodifierid)|false|none|Hash of the UTXO set transformation proofs section of the block == hash(modifier type id, header id, adProofsRoot)|

### BlockTransactions
<!-- backwards compatibility -->
<a id="schemablocktransactions"></a>
<a id="schema_BlockTransactions"></a>
<a id="tocSblocktransactions"></a>
<a id="tocsblocktransactions"></a>

=== "json"

    ```json
    {
      "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactions": [
        {
          "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "inputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "spendingProof": {
                "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "extension": {
                  "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                }
              }
            }
          ],
          "dataInputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
            }
          ],
          "outputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "value": 147,
              "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
              "creationHeight": 9149,
              "assets": [
                {
                  "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "amount": 1000
                }
              ],
              "additionalRegisters": {
                "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
              },
              "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "index": 0
            }
          ],
          "size": 0
        }
      ],
      "size": 0
    }
    ```

Section of a block which contains transactions.

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|headerId|[ModifierId](#schemamodifierid)|true|none|Identifier of a header of a corresponding block|
|transactions|[Transactions](#schematransactions)|true|none|Transactions of the block|
|size|integer(int32)|true|none|Size in bytes of all block transactions|

### BlockADProofs
<!-- backwards compatibility -->
<a id="schemablockadproofs"></a>
<a id="schema_BlockADProofs"></a>
<a id="tocSblockadproofs"></a>
<a id="tocsblockadproofs"></a>

=== "json"

    ```json
    {
      "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "proofBytes": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "size": 0
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|headerId|[ModifierId](#schemamodifierid)|true|none|Identifier of a header of the block which contains the proofs|
|proofBytes|[SerializedAdProof](#schemaserializedadproof)|true|none|Serialized bytes of the authenticated dictionary proof|
|digest|[Digest32](#schemadigest32)|true|none|Hash of the proofBytes|
|size|integer(int32)|true|none|Size in bytes|

### Extension
<!-- backwards compatibility -->
<a id="schemaextension"></a>
<a id="schema_Extension"></a>
<a id="tocSextension"></a>
<a id="tocsextension"></a>

=== "json"

    ```json
    {
      "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "fields": [
        [
          "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        ]
      ]
    }
    ```

Section of a block which contains extension data.

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|headerId|[ModifierId](#schemamodifierid)|true|none|Identifier of a header of a corresponding block|
|digest|[Digest32](#schemadigest32)|true|none|Root hash (aka digest) merkelized list of key-value records|
|fields|[[KeyValueItem](#schemakeyvalueitem)]¦null|true|none|List of key-value records|

### KeyValueItem
<!-- backwards compatibility -->
<a id="schemakeyvalueitem"></a>
<a id="schema_KeyValueItem"></a>
<a id="tocSkeyvalueitem"></a>
<a id="tocskeyvalueitem"></a>

=== "json"

    ```json
    [
      "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ]
    ```

Key-value record represented as a pair of hex strings in an array.

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[HexString](#schemahexstring)]|false|none|Key-value record represented as a pair of hex strings in an array.|

### CandidateBlock
<!-- backwards compatibility -->
<a id="schemacandidateblock"></a>
<a id="schema_CandidateBlock"></a>
<a id="tocScandidateblock"></a>
<a id="tocscandidateblock"></a>

=== "json"

    ```json
    {
      "version": 2,
      "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "nBits": 19857408,
      "adProofBytes": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsNumber": 2,
      "transactions": [
        {
          "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "inputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "spendingProof": {
                "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "extension": {
                  "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
                }
              }
            }
          ],
          "dataInputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
            }
          ],
          "outputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "value": 147,
              "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
              "creationHeight": 9149,
              "assets": [
                {
                  "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                  "amount": 1000
                }
              ],
              "additionalRegisters": {
                "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
              },
              "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "index": 0
            }
          ],
          "size": 0
        }
      ],
      "votes": "000000"
    }
    ```

Can be null if node is not mining or candidate block is not ready

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version|integer(int8)|false|none|none|
|extensionHash|[Digest32](#schemadigest32)|true|none|Base16-encoded 32 byte digest|
|timestamp|[Timestamp](#schematimestamp)|false|none|Basic timestamp definition|
|stateRoot|[ADDigest](#schemaaddigest)|false|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|
|nBits|integer(int64)|false|none|none|
|adProofBytes|[SerializedAdProof](#schemaserializedadproof)|false|none|Base16-encoded ad proofs|
|parentId|[ModifierId](#schemamodifierid)|true|none|Base16-encoded 32 byte modifier id|
|transactionsNumber|integer(int32)|false|none|none|
|transactions|[Transactions](#schematransactions)|false|none|List of ErgoTransaction objects|
|votes|[Votes](#schemavotes)|false|none|Base16-encoded votes for a soft-fork and parameters|

### PassphraseMatch
<!-- backwards compatibility -->
<a id="schemapassphrasematch"></a>
<a id="schema_PassphraseMatch"></a>
<a id="tocSpassphrasematch"></a>
<a id="tocspassphrasematch"></a>

=== "json"

    ```json
    {
      "matched": true
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|matched|boolean|true|none|true if passphrase matches wallet, false otherwise|

### WalletStatus
<!-- backwards compatibility -->
<a id="schemawalletstatus"></a>
<a id="schema_WalletStatus"></a>
<a id="tocSwalletstatus"></a>
<a id="tocswalletstatus"></a>

=== "json"

    ```json
    {
      "isInitialized": true,
      "isUnlocked": true,
      "changeAddress": "3WzCFq7mkykKqi4Ykdk8BK814tkh6EsPmA42pQZxU2NRwSDgd6yB",
      "walletHeight": 0,
      "error": "string"
    }
    ```

Status of the node wallet

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|isInitialized|boolean|true|none|true if wallet is initialized, false otherwise|
|isUnlocked|boolean|true|none|true if wallet is unlocked, false otherwise|
|changeAddress|string|true|none|address to send change to. Empty when wallet is not initialized or locked. By default change address correponds to root key address, could be set via /wallet/updateChangeAddress method.|
|walletHeight|integer|true|none|last scanned height for the wallet (and external scans)|
|error|string|true|none|last wallet error caught|

### InitWallet
<!-- backwards compatibility -->
<a id="schemainitwallet"></a>
<a id="schema_InitWallet"></a>
<a id="tocSinitwallet"></a>
<a id="tocsinitwallet"></a>

=== "json"

    ```json
    {
      "pass": "string",
      "mnemonicPass": "string"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pass|string|true|none|Password to encrypt wallet file with|
|mnemonicPass|string|false|none|Optional pass to password-protect mnemonic seed|

### InitWalletResult
<!-- backwards compatibility -->
<a id="schemainitwalletresult"></a>
<a id="schema_InitWalletResult"></a>
<a id="tocSinitwalletresult"></a>
<a id="tocsinitwalletresult"></a>

=== "json"

    ```json
    {
      "mnemonic": "string"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mnemonic|string|true|none|Mnemonic seed phrase|

### RestoreWallet
<!-- backwards compatibility -->
<a id="schemarestorewallet"></a>
<a id="schema_RestoreWallet"></a>
<a id="tocSrestorewallet"></a>
<a id="tocsrestorewallet"></a>

=== "json"

    ```json
    {
      "pass": "string",
      "mnemonic": "string",
      "mnemonicPass": "string",
      "usePre1627KeyDerivation": true
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pass|string|true|none|Password to encrypt wallet file with|
|mnemonic|string|true|none|Mnemonic seed|
|mnemonicPass|string|false|none|Optional pass to password-protect mnemonic seed|
|usePre1627KeyDerivation|boolean|true|none|use incorrect(previous) BIP32 key derivation (see https://github.com/ergoplatform/ergo/issues/1627 for details). It's recommended to set to 'true' if the original wallet was created by ergo node before v4.0.105.|

### CheckWallet
<!-- backwards compatibility -->
<a id="schemacheckwallet"></a>
<a id="schema_CheckWallet"></a>
<a id="tocScheckwallet"></a>
<a id="tocscheckwallet"></a>

=== "json"

    ```json
    {
      "mnemonic": "string",
      "mnemonicPass": "string"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mnemonic|string|true|none|Mnemonic seed (optional)|
|mnemonicPass|string|false|none|Optional pass to password-protect mnemonic seed|

### UnlockWallet
<!-- backwards compatibility -->
<a id="schemaunlockwallet"></a>
<a id="schema_UnlockWallet"></a>
<a id="tocSunlockwallet"></a>
<a id="tocsunlockwallet"></a>

=== "json"

    ```json
    {
      "pass": "string"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pass|string|true|none|Password to decrypt wallet file with|

### DeriveKey
<!-- backwards compatibility -->
<a id="schemaderivekey"></a>
<a id="schema_DeriveKey"></a>
<a id="tocSderivekey"></a>
<a id="tocsderivekey"></a>

=== "json"

    ```json
    {
      "derivationPath": "m/1/2"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|derivationPath|string|true|none|Derivation path for a new secret to derive|

### DeriveKeyResult
<!-- backwards compatibility -->
<a id="schemaderivekeyresult"></a>
<a id="schema_DeriveKeyResult"></a>
<a id="tocSderivekeyresult"></a>
<a id="tocsderivekeyresult"></a>

=== "json"

    ```json
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|

### DeriveNextKeyResult
<!-- backwards compatibility -->
<a id="schemaderivenextkeyresult"></a>
<a id="schema_DeriveNextKeyResult"></a>
<a id="tocSderivenextkeyresult"></a>
<a id="tocsderivenextkeyresult"></a>

=== "json"

    ```json
    {
      "derivationPath": "m/1/2",
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|derivationPath|string|true|none|Derivation path of the resulted secret|
|address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|

### MerkleProof
<!-- backwards compatibility -->
<a id="schemamerkleproof"></a>
<a id="schema_MerkleProof"></a>
<a id="tocSmerkleproof"></a>
<a id="tocsmerkleproof"></a>

=== "json"

    ```json
    {
      "leaf": "cd665e49c834b0c25574fcb19a158d836f3f2aad8e91ac195f972534c25449b3",
      "levels": [
        [
          "018b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337",
          0
        ]
      ]
    }
    ```

Merkle proof for a leaf, which is an array of bytes (e.g. a transaction identifier)

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|leaf|string|true|none|Base16-encoded Merkle tree leaf bytes|
|levels|[array]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|hash|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|side of hash|

### ProofOfUpcomingTransactions
<!-- backwards compatibility -->
<a id="schemaproofofupcomingtransactions"></a>
<a id="schema_ProofOfUpcomingTransactions"></a>
<a id="tocSproofofupcomingtransactions"></a>
<a id="tocsproofofupcomingtransactions"></a>

=== "json"

    ```json
    {
      "msgPreimage": "0112e03c6d39d32509855be7cee9b62ff921f7a0cf6883e232474bd5b54d816dd056f846980d34c3b23098bdcf41222f8cdee5219224aa67750055926c3a2310a483accc4f9153e7a760615ea972ac67911cff111f8c17f563d6147205f58f85133ae695d1d4157e4aecdbbb29952cfa42b75129db55bddfce3bc53b8fd5b5465f10d8be8ddda62ed3b86afb0497ff2d381ed884bdae5287d20667def224a28d2b6e3ebfc78709780702c70bd8df0e000000",
      "txProofs": [
        {
          "leaf": "cd665e49c834b0c25574fcb19a158d836f3f2aad8e91ac195f972534c25449b3",
          "levels": [
            [
              "018b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337",
              0
            ]
          ]
        }
      ]
    }
    ```

Proof that a block corresponding to given header without PoW contains some transactions

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msgPreimage|string|true|none|Base16-encoded serialized header without Proof-of-Work|
|txProofs|[[MerkleProof](#schemamerkleproof)]|true|none|Merkle proofs of transactions included into blocks (not necessarily all the block transactions)|

### WorkMessage
<!-- backwards compatibility -->
<a id="schemaworkmessage"></a>
<a id="schema_WorkMessage"></a>
<a id="tocSworkmessage"></a>
<a id="tocsworkmessage"></a>

=== "json"

    ```json
    {
      "msg": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "b": 987654321,
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "proof": {
        "msgPreimage": "0112e03c6d39d32509855be7cee9b62ff921f7a0cf6883e232474bd5b54d816dd056f846980d34c3b23098bdcf41222f8cdee5219224aa67750055926c3a2310a483accc4f9153e7a760615ea972ac67911cff111f8c17f563d6147205f58f85133ae695d1d4157e4aecdbbb29952cfa42b75129db55bddfce3bc53b8fd5b5465f10d8be8ddda62ed3b86afb0497ff2d381ed884bdae5287d20667def224a28d2b6e3ebfc78709780702c70bd8df0e000000",
        "txProofs": [
          {
            "leaf": "cd665e49c834b0c25574fcb19a158d836f3f2aad8e91ac195f972534c25449b3",
            "levels": [
              [
                "018b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337",
                0
              ]
            ]
          }
        ]
      }
    }
    ```

Block candidate related data for external miner to perform work

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|Base16-encoded block header bytes without PoW solution|
|b|integer|true|none|Work target value|
|pk|string|true|none|Base16-encoded miner public key|
|proof|[ProofOfUpcomingTransactions](#schemaproofofupcomingtransactions)|false|none|Proof that a block corresponding to given header without PoW contains some transactions|

### Peer
<!-- backwards compatibility -->
<a id="schemapeer"></a>
<a id="schema_Peer"></a>
<a id="tocSpeer"></a>
<a id="tocspeer"></a>

=== "json"

    ```json
    {
      "address": "127.0.0.1:5673",
      "restApiUrl": "https://example.com",
      "name": "mynode",
      "lastSeen": 1524143059077,
      "connectionType": "Incoming"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|string|true|none|none|
|restApiUrl|string¦null|false|none|none|
|name|string¦null|false|none|none|
|lastSeen|[Timestamp](#schematimestamp)|false|none|Basic timestamp definition|
|connectionType|string¦null|false|none|none|

##### Enumerated Values

|Property|Value|
|---|---|
|connectionType|Incoming|
|connectionType|Outgoing|

### PeersStatus
<!-- backwards compatibility -->
<a id="schemapeersstatus"></a>
<a id="schema_PeersStatus"></a>
<a id="tocSpeersstatus"></a>
<a id="tocspeersstatus"></a>

=== "json"

    ```json
    {
      "lastIncomingMessage": 1524143059077,
      "currentNetworkTime": 1524143059077
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lastIncomingMessage|[Timestamp](#schematimestamp)|true|none|Basic timestamp definition|
|currentNetworkTime|[Timestamp](#schematimestamp)|true|none|Basic timestamp definition|

### PeerMode
<!-- backwards compatibility -->
<a id="schemapeermode"></a>
<a id="schema_PeerMode"></a>
<a id="tocSpeermode"></a>
<a id="tocspeermode"></a>

=== "json"

    ```json
    {
      "state": "utxo",
      "verifyingTransactions": true,
      "fullBlocksSuffix": 2880
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|state|string|true|none|none|
|verifyingTransactions|boolean|true|none|none|
|fullBlocksSuffix|integer|true|none|none|

### SyncInfo
<!-- backwards compatibility -->
<a id="schemasyncinfo"></a>
<a id="schema_SyncInfo"></a>
<a id="tocSsyncinfo"></a>
<a id="tocssyncinfo"></a>

=== "json"

    ```json
    {
      "address": "127.0.0.1:5673",
      "mode": {
        "state": "utxo",
        "verifyingTransactions": true,
        "fullBlocksSuffix": 2880
      },
      "version": "4.0.16",
      "status": "Older",
      "height": 65780
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|string|true|none|none|
|mode|[PeerMode](#schemapeermode)|true|none|Peer operating mode parameters|
|version|string|true|none|none|
|status|string|true|none|none|
|height|integer|true|none|none|

### RequestedInfo
<!-- backwards compatibility -->
<a id="schemarequestedinfo"></a>
<a id="schema_RequestedInfo"></a>
<a id="tocSrequestedinfo"></a>
<a id="tocsrequestedinfo"></a>

=== "json"

    ```json
    {
      "address": "127.0.0.1:5673",
      "version": "4.0.26",
      "checks": 4
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|string|false|none|none|
|version|string|false|none|none|
|checks|integer|true|none|How many times we checked for modifier delivery status|

### RequestedInfoByModifierId
<!-- backwards compatibility -->
<a id="schemarequestedinfobymodifierid"></a>
<a id="schema_RequestedInfoByModifierId"></a>
<a id="tocSrequestedinfobymodifierid"></a>
<a id="tocsrequestedinfobymodifierid"></a>

=== "json"

    ```json
    {
      "property1": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "checks": 4
      },
      "property2": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "checks": 4
      }
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|**additionalProperties**|[RequestedInfo](#schemarequestedinfo)|false|none|none|

### ConnectedPeer
<!-- backwards compatibility -->
<a id="schemaconnectedpeer"></a>
<a id="schema_ConnectedPeer"></a>
<a id="tocSconnectedpeer"></a>
<a id="tocsconnectedpeer"></a>

=== "json"

    ```json
    {
      "address": "127.0.0.1:5673",
      "version": "4.0.26",
      "lastMessage": 1524143059077
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|string|true|none|none|
|version|string|false|none|none|
|lastMessage|[Timestamp](#schematimestamp)|false|none|Basic timestamp definition|

### ConnectedPeerByModifierId
<!-- backwards compatibility -->
<a id="schemaconnectedpeerbymodifierid"></a>
<a id="schema_ConnectedPeerByModifierId"></a>
<a id="tocSconnectedpeerbymodifierid"></a>
<a id="tocsconnectedpeerbymodifierid"></a>

=== "json"

    ```json
    {
      "property1": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "lastMessage": 1524143059077
      },
      "property2": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "lastMessage": 1524143059077
      }
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|**additionalProperties**|[ConnectedPeer](#schemaconnectedpeer)|false|none|none|

### TrackInfo
<!-- backwards compatibility -->
<a id="schematrackinfo"></a>
<a id="schema_TrackInfo"></a>
<a id="tocStrackinfo"></a>
<a id="tocstrackinfo"></a>

=== "json"

    ```json
    {
      "invalidModifierApproxSize": 65780,
      "requested": {
        "property1": {
          "property1": {
            "address": "127.0.0.1:5673",
            "version": "4.0.26",
            "checks": 4
          },
          "property2": {
            "address": "127.0.0.1:5673",
            "version": "4.0.26",
            "checks": 4
          }
        },
        "property2": {
          "property1": {
            "address": "127.0.0.1:5673",
            "version": "4.0.26",
            "checks": 4
          },
          "property2": {
            "address": "127.0.0.1:5673",
            "version": "4.0.26",
            "checks": 4
          }
        }
      },
      "received": {
        "property1": {
          "property1": {
            "address": "127.0.0.1:5673",
            "version": "4.0.26",
            "lastMessage": 1524143059077
          },
          "property2": {
            "address": "127.0.0.1:5673",
            "version": "4.0.26",
            "lastMessage": 1524143059077
          }
        },
        "property2": {
          "property1": {
            "address": "127.0.0.1:5673",
            "version": "4.0.26",
            "lastMessage": 1524143059077
          },
          "property2": {
            "address": "127.0.0.1:5673",
            "version": "4.0.26",
            "lastMessage": 1524143059077
          }
        }
      }
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|invalidModifierApproxSize|integer|true|none|none|
|requested|object|true|none|Currently requested modifiers|
|» **additionalProperties**|[RequestedInfoByModifierId](#schemarequestedinfobymodifierid)|false|none|none|
|received|object|true|none|Received modifiers|
|» **additionalProperties**|[ConnectedPeerByModifierId](#schemaconnectedpeerbymodifierid)|false|none|none|

### BlacklistedPeers
<!-- backwards compatibility -->
<a id="schemablacklistedpeers"></a>
<a id="schema_BlacklistedPeers"></a>
<a id="tocSblacklistedpeers"></a>
<a id="tocsblacklistedpeers"></a>

=== "json"

    ```json
    {
      "addresses": [
        "string"
      ]
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|addresses|[string]|true|none|none|

### NodeInfo
<!-- backwards compatibility -->
<a id="schemanodeinfo"></a>
<a id="schema_NodeInfo"></a>
<a id="tocSnodeinfo"></a>
<a id="tocsnodeinfo"></a>

=== "json"

    ```json
    {
      "name": "my-node-1",
      "appVersion": "0.0.1",
      "fullHeight": 667,
      "headersHeight": 667,
      "maxPeerHeight": 706162,
      "bestFullHeaderId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "previousFullHeaderId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "bestHeaderId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateRoot": "dab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateType": "digest",
      "stateVersion": "fab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "isMining": true,
      "peersCount": 327,
      "unconfirmedCount": 327,
      "difficulty": 667,
      "currentTime": 1524143059077,
      "launchTime": 1524143059077,
      "headersScore": 0,
      "fullBlocksScore": 0,
      "genesisBlockId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "parameters": {
        "height": 667,
        "storageFeeFactor": 100000,
        "minValuePerByte": 360,
        "maxBlockSize": 1048576,
        "maxBlockCost": 104876,
        "blockVersion": 2,
        "tokenAccessCost": 100,
        "inputCost": 100,
        "dataInputCost": 100,
        "outputCost": 100
      },
      "eip27Supported": true,
      "restApiUrl": "https://example.com"
    }
    ```

Data container for /info API request output. Contains information about node's state and configuration. Contains data about best block, best header, state, etc. Best block is the block with the maximum height.

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|Node's (peer) self-chosen name from config|
|appVersion|string|true|none|Node's application version|
|fullHeight|integer(int32)¦null|true|none|Height of the best block known to the node. Can be 'null' if state is empty (no full block is applied since node launch)|
|headersHeight|integer(int32)¦null|true|none|The height of the best header (i.e. the one with the maximum height). Can be 'null' if state is empty (no header applied since node launch)|
|maxPeerHeight|integer(int32)¦null|true|none|Maximum block height of connected peers. Can be 'null' if state is empty (no peer connected since node launch)|
|bestFullHeaderId|[ModifierId](#schemamodifierid)¦null|true|none|Best full-block id (header id of such block). Can be 'null' if no full block is applied since node launch.|
|previousFullHeaderId|[ModifierId](#schemamodifierid)¦null|true|none|Header id of the parent block of the best full-block (i.e. previous block in the blockchain). Can be 'null' if no full block is applied since node launch|
|bestHeaderId|[ModifierId](#schemamodifierid)¦null|true|none|Best header ID (hex representation). Can be 'null' if no header applied since node launch.|
|stateRoot|string¦null|true|none|Current UTXO set digest. Can be 'null' if state is empty (no full block is applied since node launch)|
|stateType|string|true|none|Whether the node is storing UTXO set or only its digest. Equals `digest` if only digest is stored, `utxo` if full UTXO set is stored.|
|stateVersion|string¦null|true|none|Id of a block where UTXO set digest is taken from. Can be 'null' if no full block is applied since node launch.|
|isMining|boolean|true|none|Whether the node is mining (i.e. generating blocks).|
|peersCount|integer(int32)|true|none|Number of peers this node is connected with.|
|unconfirmedCount|integer(int32)|true|none|Number of unconfirmed transactions in the mempool.|
|difficulty|integer¦null|true|none|Difficulty on current bestFullHeaderId. Can be 'null' if no full block is applied since node launch. Difficulty is a BigInt integer.|
|currentTime|[Timestamp](#schematimestamp)|true|none|Current internal node time|
|launchTime|[Timestamp](#schematimestamp)|true|none|When the node was launched (in Java time format, UNIX time * 1000).|
|headersScore|integer¦null|true|none|Cumulative difficulty of best headers-chain. Can be 'null' if no headers is applied since node launch. headersScore is a BigInt integer.|
|fullBlocksScore|integer¦null|true|none|Cumulative difficulty of best full blocks chain. Can be 'null' if no full block is applied since node launch. fullBlocksScore is a BigInt integer.|
|genesisBlockId|[ModifierId](#schemamodifierid)¦null|true|none|Header id of genesis block. Can be 'null' if genesis blocks is not produced yet.|
|parameters|[Parameters](#schemaparameters)|true|none|System parameters which could be readjusted via collective miners decision.|
|eip27Supported|boolean|false|none|Whether EIP-27 locked in|
|restApiUrl|string|false|none|Publicly accessible url of node which exposes restApi in firewall|

##### Enumerated Values

|Property|Value|
|---|---|
|stateType|digest|
|stateType|utxo|

### Parameters
<!-- backwards compatibility -->
<a id="schemaparameters"></a>
<a id="schema_Parameters"></a>
<a id="tocSparameters"></a>
<a id="tocsparameters"></a>

=== "json"

    ```json
    {
      "height": 667,
      "storageFeeFactor": 100000,
      "minValuePerByte": 360,
      "maxBlockSize": 1048576,
      "maxBlockCost": 104876,
      "blockVersion": 2,
      "tokenAccessCost": 100,
      "inputCost": 100,
      "dataInputCost": 100,
      "outputCost": 100
    }
    ```

System parameters which could be readjusted via collective miners decision.

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|height|integer(int32)|true|none|Height when current parameters were considered(not actual height). Can be '0' if state is empty|
|storageFeeFactor|integer(int32)|true|none|Storage fee coefficient (per byte per storage period ~4 years)|
|minValuePerByte|integer(int32)|true|none|Minimum value per byte of an output|
|maxBlockSize|integer(int32)|true|none|Maximum block size (in bytes)|
|maxBlockCost|integer(int32)|true|none|Maximum cumulative computational cost of input scripts in block transactions|
|blockVersion|[Version](#schemaversion)|true|none|Ergo blockchain protocol version|
|tokenAccessCost|integer(int32)|true|none|Validation cost of a single token|
|inputCost|integer(int32)|true|none|Validation cost per one transaction input|
|dataInputCost|integer(int32)|true|none|Validation cost per one data input|
|outputCost|integer(int32)|true|none|Validation cost per one transaction output|

### Version
<!-- backwards compatibility -->
<a id="schemaversion"></a>
<a id="schema_Version"></a>
<a id="tocSversion"></a>
<a id="tocsversion"></a>

=== "json"

    ```json
    2
    ```

Ergo blockchain protocol version

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|integer(int8)|false|none|Ergo blockchain protocol version|

### TransactionBoxId
<!-- backwards compatibility -->
<a id="schematransactionboxid"></a>
<a id="schema_TransactionBoxId"></a>
<a id="tocStransactionboxid"></a>
<a id="tocstransactionboxid"></a>

=== "json"

    ```json
    "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

Base16-encoded transaction box id bytes. Should be 32 bytes long

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|

### TransactionId
<!-- backwards compatibility -->
<a id="schematransactionid"></a>
<a id="schema_TransactionId"></a>
<a id="tocStransactionid"></a>
<a id="tocstransactionid"></a>

=== "json"

    ```json
    "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

Base16-encoded transaction id bytes

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base16-encoded transaction id bytes|

### ErgoTree
<!-- backwards compatibility -->
<a id="schemaergotree"></a>
<a id="schema_ErgoTree"></a>
<a id="tocSergotree"></a>
<a id="tocsergotree"></a>

=== "json"

    ```json
    "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041"
    ```

Base16-encoded ergo tree bytes

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base16-encoded ergo tree bytes|

### ErgoTreeObject
<!-- backwards compatibility -->
<a id="schemaergotreeobject"></a>
<a id="schema_ErgoTreeObject"></a>
<a id="tocSergotreeobject"></a>
<a id="tocsergotreeobject"></a>

=== "json"

    ```json
    {
      "tree": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
    }
    ```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tree|string|false|none|serialized Ergo tree|

### Transactions
<!-- backwards compatibility -->
<a id="schematransactions"></a>
<a id="schema_Transactions"></a>
<a id="tocStransactions"></a>
<a id="tocstransactions"></a>

=== "json"

    ```json
    [
      {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
              }
            }
          }
        ],
        "dataInputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
          }
        ],
        "outputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "value": 147,
            "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
            "creationHeight": 9149,
            "assets": [
              {
                "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
                "amount": 1000
              }
            ],
            "additionalRegisters": {
              "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
            },
            "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "index": 0
          }
        ],
        "size": 0
      }
    ]
    ```

List of ErgoTransaction objects

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ErgoTransaction](#schemaergotransaction)]|false|none|List of ErgoTransaction objects|

### FeeHistogramBin
<!-- backwards compatibility -->
<a id="schemafeehistogrambin"></a>
<a id="schema_FeeHistogramBin"></a>
<a id="tocSfeehistogrambin"></a>
<a id="tocsfeehistogrambin"></a>

=== "json"

    ```json
    {
      "nTxns": 0,
      "totalFee": 0
    }
    ```

Fee histogram bin

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nTxns|integer(int32)|false|none|none|
|totalFee|integer(int64)|false|none|none|

### FeeHistogram
<!-- backwards compatibility -->
<a id="schemafeehistogram"></a>
<a id="schema_FeeHistogram"></a>
<a id="tocSfeehistogram"></a>
<a id="tocsfeehistogram"></a>

=== "json"

    ```json
    [
      {
        "nTxns": 0,
        "totalFee": 0
      }
    ]
    ```

Fee histogram for transactions in mempool

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[FeeHistogramBin](#schemafeehistogrambin)]|false|none|Fee histogram for transactions in mempool|

### Asset
<!-- backwards compatibility -->
<a id="schemaasset"></a>
<a id="schema_Asset"></a>
<a id="tocSasset"></a>
<a id="tocsasset"></a>

=== "json"

    ```json
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
    ```

Token detail in the transaction

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tokenId|[Digest32](#schemadigest32)|true|none|Base16-encoded 32 byte digest|
|amount|integer(int64)|true|none|Amount of the token|

### Registers
<!-- backwards compatibility -->
<a id="schemaregisters"></a>
<a id="schema_Registers"></a>
<a id="tocSregisters"></a>
<a id="tocsregisters"></a>

=== "json"

    ```json
    {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    }
    ```

Ergo box registers

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|**additionalProperties**|[SValue](#schemasvalue)|false|none|Base-16 encoded serialized Sigma-state value|

### SValue
<!-- backwards compatibility -->
<a id="schemasvalue"></a>
<a id="schema_SValue"></a>
<a id="tocSsvalue"></a>
<a id="tocssvalue"></a>

=== "json"

    ```json
    "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    ```

Base-16 encoded serialized Sigma-state value

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base-16 encoded serialized Sigma-state value|

### Votes
<!-- backwards compatibility -->
<a id="schemavotes"></a>
<a id="schema_Votes"></a>
<a id="tocSvotes"></a>
<a id="tocsvotes"></a>

=== "json"

    ```json
    "000000"
    ```

Base16-encoded votes for a soft-fork and parameters

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base16-encoded votes for a soft-fork and parameters|

### ModifierId
<!-- backwards compatibility -->
<a id="schemamodifierid"></a>
<a id="schema_ModifierId"></a>
<a id="tocSmodifierid"></a>
<a id="tocsmodifierid"></a>

=== "json"

    ```json
    "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

Base16-encoded 32 byte modifier id

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base16-encoded 32 byte modifier id|

### Digest32
<!-- backwards compatibility -->
<a id="schemadigest32"></a>
<a id="schema_Digest32"></a>
<a id="tocSdigest32"></a>
<a id="tocsdigest32"></a>

=== "json"

    ```json
    "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

Base16-encoded 32 byte digest

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base16-encoded 32 byte digest|

### HexString
<!-- backwards compatibility -->
<a id="schemahexstring"></a>
<a id="schema_HexString"></a>
<a id="tocShexstring"></a>
<a id="tocshexstring"></a>

=== "json"

    ```json
    "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

Base16-encoded bytes

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base16-encoded bytes|

### ADDigest
<!-- backwards compatibility -->
<a id="schemaaddigest"></a>
<a id="schema_ADDigest"></a>
<a id="tocSaddigest"></a>
<a id="tocsaddigest"></a>

=== "json"

    ```json
    "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

Base16-encoded 33 byte digest - digest with extra byte with tree height

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|

### SerializedAdProof
<!-- backwards compatibility -->
<a id="schemaserializedadproof"></a>
<a id="schema_SerializedAdProof"></a>
<a id="tocSserializedadproof"></a>
<a id="tocsserializedadproof"></a>

=== "json"

    ```json
    "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

Base16-encoded ad proofs

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base16-encoded ad proofs|

### SpendingProofBytes
<!-- backwards compatibility -->
<a id="schemaspendingproofbytes"></a>
<a id="schema_SpendingProofBytes"></a>
<a id="tocSspendingproofbytes"></a>
<a id="tocsspendingproofbytes"></a>

=== "json"

    ```json
    "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

Base16-encoded spending proofs

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base16-encoded spending proofs|

### BlockSignature
<!-- backwards compatibility -->
<a id="schemablocksignature"></a>
<a id="schema_BlockSignature"></a>
<a id="tocSblocksignature"></a>
<a id="tocsblocksignature"></a>

=== "json"

    ```json
    "5ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ```

Base16-encoded block signature

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string(base16)|false|none|Base16-encoded block signature|

### Timestamp
<!-- backwards compatibility -->
<a id="schematimestamp"></a>
<a id="schema_Timestamp"></a>
<a id="tocStimestamp"></a>
<a id="tocstimestamp"></a>

=== "json"

    ```json
    1524143059077
    ```

Basic timestamp definition

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|integer(int64)|false|none|Basic timestamp definition|

### EmissionInfo
<!-- backwards compatibility -->
<a id="schemaemissioninfo"></a>
<a id="schema_EmissionInfo"></a>
<a id="tocSemissioninfo"></a>
<a id="tocsemissioninfo"></a>

=== "json"

    ```json
    {
      "minerReward": 0,
      "totalCoinsIssued": 0,
      "totalRemainCoins": 0,
      "reemitted": 0
    }
    ```

Emission info for height

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|minerReward|integer(int64)|false|none|none|
|totalCoinsIssued|integer(int64)|false|none|none|
|totalRemainCoins|integer(int64)|false|none|none|
|reemitted|integer(int64)|false|none|none|

### EmissionScripts
<!-- backwards compatibility -->
<a id="schemaemissionscripts"></a>
<a id="schema_EmissionScripts"></a>
<a id="tocSemissionscripts"></a>
<a id="tocsemissionscripts"></a>

=== "json"

    ```json
    {
      "emission": "string",
      "reemission": "string",
      "pay2Reemission": "string"
    }
    ```

Emission related scripts

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|emission|string|false|none|none|
|reemission|string|false|none|none|
|pay2Reemission|string|false|none|none|

### BalancesSnapshot
<!-- backwards compatibility -->
<a id="schemabalancessnapshot"></a>
<a id="schema_BalancesSnapshot"></a>
<a id="tocSbalancessnapshot"></a>
<a id="tocsbalancessnapshot"></a>

=== "json"

    ```json
    {
      "height": 0,
      "balance": 0,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ]
    }
    ```

Amount of Ergo tokens and assets

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|height|integer(int32)|true|none|none|
|balance|integer(int64)|true|none|none|
|assets|[[Asset](#schemaasset)]|false|none|[Token detail in the transaction]|

### AddressValidity
<!-- backwards compatibility -->
<a id="schemaaddressvalidity"></a>
<a id="schema_AddressValidity"></a>
<a id="tocSaddressvalidity"></a>
<a id="tocsaddressvalidity"></a>

=== "json"

    ```json
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "isValid": true,
      "error": "string"
    }
    ```

Validity status of Ergo address

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|[ErgoAddress](#schemaergoaddress)|true|none|Encoded Ergo Address|
|isValid|boolean|true|none|none|
|error|string|false|none|none|

### ApiError
<!-- backwards compatibility -->
<a id="schemaapierror"></a>
<a id="schema_ApiError"></a>
<a id="tocSapierror"></a>
<a id="tocsapierror"></a>

=== "json"

    ```json
    {
      "error": 500,
      "reason": "Internal server error",
      "detail": "string"
    }
    ```

Error response from API

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|error|integer|true|none|Error code|
|reason|string|true|none|Error message explaining the reason of the error|
|detail|string¦null|true|none|Detailed error description|

