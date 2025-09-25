Ergo Platform documentation
=======================================

[docs.ergoplatform.com](https://docs.ergoplatform.com/)

## Contributing

Please submit a pull request. 

## Running locally

Install required packages

```
python -m pip install -r requirements.txt
```

```
mkdocs serve
```

## Continuous deployment

Every pull request runs the documentation build on GitHub Actions. The workflow publishes an ephemeral GitHub Pages preview so
reviewers can click through the rendered site without touching production. Look for the **Deploy preview to GitHub Pages** job
in the PR checks and follow the environment URL that GitHub surfaces after the job succeeds.

Merges to `main` continue to build on the runner and push the generated site to the self-hosted server via SSH, keeping the
existing docs site at [docs.ergoplatform.com](https://docs.ergoplatform.com/) unchanged.

