# ErgoScript Compiler

The [ErgoScript Compiler](https://github.com/ergoplatform/ergoscript-compiler) is a Command Line Interface (CLI) tool designed to compile ErgoScript code into an Ergo address.

## User Guide

### Setup and Compilation

1. If you're starting from source, compile the ErgoScript compiler using these steps:
    - Clone the repository by executing `git clone https://github.com/scalahub/ErgoScriptCompiler.git`.
    - Make sure SBT is installed and correctly set up in your path.
    - Use the command `sbt assembly` in the project root folder to compile the JAR file.

       Upon successful compilation, a JAR file is generated in the following path: `target/scala-2.12/ErgoScriptCompiler-assembly-0.1.jar`. In the steps below, `<jarFile>` refers to this JAR.

       If you're using the precompiled JAR, proceed directly to the next step.

2. Compiling ErgoScript code involves the following steps:
    - Save your ErgoScript code in a text file, for example, `myScript.es`. You can choose any file extension.
    - If your code references any symbols (constants), save them in a separate file, for instance, `mySymbols.json`. Refer to the section below on how to write this file. 
    - This symbols file is optional and is only required if your code references any symbols.
    - Use the command `java -cp <jarFile> Compile <ergoScriptFile> <optionalSymbolsFile>` to compile the file. For example:
        - `java -cp ErgoScriptCompiler.jar Compile myScript.es mySymbols.json`
        - `java -cp ErgoScriptCompiler.jar Compile myScript.es`

Refer to the example below for a sample output.

### Integration in Your Project

To use ErgoScript Compiler in your project, add the following to your build.sbt:

```
libraryDependencies += "io.github.ergoplatform" %% "ergoscriptcompiler" % "1.0"
```

Then call: `util.Compiler.compile(ergoScriptFile: String,  symbolsFile: Option[String])`

## Examples and Outputs

The `src/test/resources` directory contains sample ErgoScript and symbol files. Here's an example execution:

```bash
java -cp \
      target/scala-2.12/ErgoScriptCompiler-assembly-0.1.jar \
      Compile \
      src/test/resources/AgeUSD.es \
      src/test/resources/AgeUSD_symbols.json 
```

The output includes:
1. The ErgoTree corresponding to the Script, serialized and hex-encoded.
2. The Blake2b256 hash of the ErgoTree, hex-encoded.
3. The address corresponding to the ErgoTree.

## Symbol File Format

If your ErgoScript code references token IDs or script hashes, encode such values in a "symbols" file as follows (any file extension is permissible):

```json
{
  "symbols":[
    {
      "name":"poolTokenId",
      "type":"CollByte",
      "value":"0fb1eca4646950743bc5a8c341c16871a0ad9b4077e3b276bf93855d51a042d1"
    },
    {
      "name":"epochPrepScriptHash",
      "type":"CollByte",
      "value":"d998e06e0c093b0990fa3da4f3bea4364546803551ea9cac02623e9675ba4522"
    },
    {
      "name":"buffer",
      "type":"Int",
      "value":"4"
    }
  ]


}
```

## Generating Payment Requests

Apart from compiling ErgoScript, this tool can generate a "payment request". It replaces register values from human-understandable forms to serialized-hex needed by the Ergo client's REST API. For instance, to store the integer 1, you would provide the register value as `0402`. 

The command to generate payment requests is: `java -cp <jarFile> Payment <humanRequest.json> <symbolsFile.json>`

