---
tags:
  - JavaScript
---

# Ledger

## Side Loading

The Ledger application is currently being reviewed by the Ledger team and should be available via the Ledger Manager shortly, in the meantime you can follow these steps below to side-load the application onto your Ledger S or Ledger S+ device. 



### Download & Extract

Go to the ['Actions'](https://github.com/tesseract-one/ledger-app-ergo/actions/runs/3613041599) section on the ledger-app-ergo repository and scroll down to **Artifacts**. 

Click on the artifact matching your ledger device (i,e. ergo-app-debug-nanos) and it should start downloading. 

Next, open your command line and navigate to the extracted Ledger App folder.

### Setup 

**install virtualenv**

=== "OSX"

    ```
    sudo apt install python3-pip
    pip3 install virtualenv
    ```

=== "Windows"

    ```
    py -m ensurepip –upgrade
    pip3 install virtualenv
    ```

**Run & activate**

=== "OSX"

    ```
    virtualenv -p python3 ledger
    source ledger/bin/activate
    pip3 install ledgerblue
    ```

=== "Windows"

    ```
    python -m venv .\venv
    venv\Scripts\activate
    pip install ledgerblue
    ```



### Deploy

Now it's time to deploy the binary file `app.hex` into the Ledger device:

Make sure your ledger is connected, but the Ledger Manager is **closed**. 

```
python -m ledgerblue.loadApp --targetId 0x31100004 --apdu --tlv --fileName app.hex --appName Ergo --appFlags 0xe0
```

While the process is running, follow the instructions on the device screen to validate and accept the app installation.




## Resources 
> For wallet developers


There is a [Binding Library](https://github.com/anon-br/ledgerjs-hw-app-ergo) available, for anything else, you will need to implement a biding API using [this documentation](https://docs.google.com/document/d/1z8nIlRmPhwcKzyZ2jZYYkaFDtLt8pgvnRWrT5zJJ_Tw/edit?pli=1#heading=h.hag83gqtujji)

- [ledger4j - Ledger HID Communityions Library](https://github.com/aionnetwork/ledger4j) 
- [tesseract-one/ledger-app-ergo](https://github.com/tesseract-one/ledger-app-ergo)
- [lib-ledger-core](https://github.com/LedgerHQ/lib-ledger-core)
