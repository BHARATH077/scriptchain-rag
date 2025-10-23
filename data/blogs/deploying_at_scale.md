# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
