# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
