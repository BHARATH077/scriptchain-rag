1. Query: >> How do I authenticate requests to ScriptChain?
2025-10-23 12:15:26,709 | INFO | Top retrievals (weighted):
2025-10-23 12:15:26,710 | INFO | docs | getting_started.md | score 0.5450
2025-10-23 12:15:26,710 | INFO | docs | getting_started.md | score 0.4859
2025-10-23 12:15:26,710 | INFO | forums | thread_001.txt | score 0.4046
2025-10-23 12:15:26,710 | INFO | blogs | security_considerations.md | score 0.3554
2025-10-23 12:15:26,710 | INFO | blogs | deploying_at_scale.md | score 0.2698
2025-10-23 12:15:26,710 | INFO | Top reranked:
[forums] (thread_001.txt) final_score=1.5553
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[forums] (thread_002.txt) final_score=0.8147
UserD: How to handle rate limits? I'm getting 429 frequently.
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=0.6836
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[docs] (getting_started.md) final_score=0.5996
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[forums] (thread_001.txt) final_score=0.5036
UserC: I think the header should be Authorization: Bearer <token>.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

2. Query: >> What endpoint runs a script?
2025-10-23 12:17:25,336 | INFO | Top retrievals (weighted):
2025-10-23 12:17:25,336 | INFO | docs | getting_started.md | score 0.3640
2025-10-23 12:17:25,336 | INFO | docs | getting_started.md | score 0.2998
2025-10-23 12:17:25,336 | INFO | blogs | deploying_at_scale.md | score 0.2191
2025-10-23 12:17:25,336 | INFO | docs | features.md | score 0.1830
2025-10-23 12:17:25,336 | INFO | blogs | security_considerations.md | score 0.1698
2025-10-23 12:17:25,336 | INFO | Top reranked:
[docs] (getting_started.md) final_score=0.8432
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[docs] (getting_started.md) final_score=0.5271
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=0.0876
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[docs] (features.md) final_score=0.0732
# Features
- Secure sandboxing
- Versioned deployments
- Webhooks for events
- Role-based access control
----------------------------------------
[blogs] (security_considerations.md) final_score=0.0679
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

3. Query: >> I'm getting 429 errors; how to handle rate limits?
2025-10-23 12:18:42,288 | INFO | Top retrievals (weighted):
2025-10-23 12:18:42,288 | INFO | forums | thread_002.txt | score 0.4357
2025-10-23 12:18:42,288 | INFO | docs | getting_started.md | score 0.2121
2025-10-23 12:18:42,288 | INFO | blogs | deploying_at_scale.md | score 0.2061
2025-10-23 12:18:42,288 | INFO | forums | thread_002.txt | score 0.1609
2025-10-23 12:18:42,288 | INFO | forums | thread_002.txt | score 0.1366
2025-10-23 12:18:42,288 | INFO | Top reranked:
[forums] (thread_002.txt) final_score=3.3430
UserD: How to handle rate limits? I'm getting 429 frequently.
----------------------------------------
[docs] (getting_started.md) final_score=0.7623
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[forums] (thread_002.txt) final_score=0.6892
UserF: Alternatively, you can set parallelism to 1 to avoid bursts.
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=0.6581
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[docs] (getting_started.md) final_score=0.4465
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

4. Query: >> Should I use Authorization: Bearer or X-API-Key?
2025-10-23 12:19:13,948 | INFO | Top retrievals (weighted):
2025-10-23 12:19:13,948 | INFO | forums | thread_001.txt | score 0.3127
2025-10-23 12:19:13,948 | INFO | blogs | security_considerations.md | score 0.3082
2025-10-23 12:19:13,948 | INFO | docs | getting_started.md | score 0.2922
2025-10-23 12:19:13,948 | INFO | forums | thread_001.txt | score 0.2883
2025-10-23 12:19:13,948 | INFO | forums | thread_001.txt | score 0.2684
2025-10-23 12:19:13,948 | INFO | Top reranked:
[forums] (thread_001.txt) final_score=1.7094
UserC: I think the header should be Authorization: Bearer <token>.
----------------------------------------
[forums] (thread_001.txt) final_score=0.7234
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[forums] (thread_002.txt) final_score=0.3915
UserE: The docs say exponential backoff; I used 1s, 2s, 4s and it works.
----------------------------------------
[blogs] (security_considerations.md) final_score=0.1233
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
[docs] (getting_started.md) final_score=0.1169
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

5. Query: >> How to deploy ScriptChain at scale?
2025-10-23 12:23:47,846 | INFO | Top retrievals (weighted):
2025-10-23 12:23:47,848 | INFO | blogs | deploying_at_scale.md | score 0.6419
2025-10-23 12:23:47,848 | INFO | docs | getting_started.md | score 0.4133
2025-10-23 12:23:47,848 | INFO | docs | getting_started.md | score 0.3582
2025-10-23 12:23:47,848 | INFO | forums | thread_001.txt | score 0.2173
2025-10-23 12:23:47,848 | INFO | docs | features.md | score 0.2086
2025-10-23 12:23:47,848 | INFO | Top reranked:
[blogs] (deploying_at_scale.md) final_score=1.5589
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[docs] (getting_started.md) final_score=1.1516
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[forums] (thread_001.txt) final_score=0.8643
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[forums] (thread_002.txt) final_score=0.8331
UserD: How to handle rate limits? I'm getting 429 frequently.
----------------------------------------
[forums] (thread_002.txt) final_score=0.6525
UserF: Alternatively, you can set parallelism to 1 to avoid bursts.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

6. Query: >> How to store API keys securely?
2025-10-23 12:24:55,626 | INFO | Top retrievals (weighted):
2025-10-23 12:24:55,626 | INFO | blogs | security_considerations.md | score 0.4637
2025-10-23 12:24:55,626 | INFO | forums | thread_001.txt | score 0.2688
2025-10-23 12:24:55,626 | INFO | docs | features.md | score 0.2427
2025-10-23 12:24:55,626 | INFO | docs | getting_started.md | score 0.2390
2025-10-23 12:24:55,626 | INFO | docs | getting_started.md | score 0.2191
2025-10-23 12:24:55,627 | INFO | Top reranked:
[blogs] (security_considerations.md) final_score=1.3249
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
[forums] (thread_001.txt) final_score=0.8849
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[forums] (thread_002.txt) final_score=0.8142
UserD: How to handle rate limits? I'm getting 429 frequently.
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=0.6275
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[docs] (getting_started.md) final_score=0.4692
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

7. Query: >> What endpoints provide job status?
2025-10-23 12:24:23,622 | INFO | Top retrievals (weighted):
2025-10-23 12:24:23,622 | INFO | docs | getting_started.md | score 0.3564
2025-10-23 12:24:23,622 | INFO | docs | features.md | score 0.2265
2025-10-23 12:24:23,622 | INFO | blogs | deploying_at_scale.md | score 0.1851
2025-10-23 12:24:23,622 | INFO | blogs | security_considerations.md | score 0.1680
2025-10-23 12:24:23,622 | INFO | docs | getting_started.md | score 0.1571
2025-10-23 12:24:23,622 | INFO | Top reranked:
[docs] (getting_started.md) final_score=0.5042
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[docs] (features.md) final_score=0.0906
# Features
- Secure sandboxing
- Versioned deployments
- Webhooks for events
- Role-based access control
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=0.0740
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[blogs] (security_considerations.md) final_score=0.0672
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
[docs] (getting_started.md) final_score=0.0628
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

8. Query: >> Is there role-based access control?
2025-10-23 12:25:34,729 | INFO | Top retrievals (weighted):
2025-10-23 12:25:34,729 | INFO | docs | features.md | score 0.5439
2025-10-23 12:25:34,729 | INFO | docs | getting_started.md | score 0.1893
2025-10-23 12:25:34,729 | INFO | blogs | security_considerations.md | score 0.1170
2025-10-23 12:25:34,729 | INFO | forums | thread_001.txt | score 0.0833
2025-10-23 12:25:34,729 | INFO | forums | thread_002.txt | score 0.0771
2025-10-23 12:25:34,729 | INFO | Top reranked:
[docs] (features.md) final_score=0.9877
# Features
- Secure sandboxing
- Versioned deployments
- Webhooks for events
- Role-based access control
----------------------------------------
[docs] (getting_started.md) final_score=0.4573
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[forums] (thread_001.txt) final_score=0.3952
UserB: Make sure the header is X-API-Key, and that your key has 'run' permission.
----------------------------------------
[blogs] (security_considerations.md) final_score=0.0468
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
[forums] (thread_001.txt) final_score=0.0333
UserC: I think the header should be Authorization: Bearer <token>.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

9. Query: >> Does ScriptChain support webhooks?
2025-10-23 12:26:13,583 | INFO | Top retrievals (weighted):
2025-10-23 12:26:13,584 | INFO | docs | getting_started.md | score 0.5629
2025-10-23 12:26:13,584 | INFO | docs | features.md | score 0.4901
2025-10-23 12:26:13,584 | INFO | docs | getting_started.md | score 0.3804
2025-10-23 12:26:13,584 | INFO | blogs | deploying_at_scale.md | score 0.2820
2025-10-23 12:26:13,584 | INFO | forums | thread_001.txt | score 0.2624
2025-10-23 12:26:13,584 | INFO | Top reranked:
[docs] (getting_started.md) final_score=0.8299
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[docs] (getting_started.md) final_score=0.5138
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[forums] (thread_001.txt) final_score=0.4937
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=0.4760
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[docs] (features.md) final_score=0.1960
# Features
- Secure sandboxing
- Versioned deployments
- Webhooks for events
- Role-based access control
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

10. Query: >> How frequently should I rotate API keys?
2025-10-23 12:26:48,282 | INFO | Top retrievals (weighted):
2025-10-23 12:26:48,282 | INFO | blogs | security_considerations.md | score 0.4689
2025-10-23 12:26:48,282 | INFO | docs | getting_started.md | score 0.2493
2025-10-23 12:26:48,282 | INFO | forums | thread_001.txt | score 0.1839
2025-10-23 12:26:48,283 | INFO | blogs | deploying_at_scale.md | score 0.1589
2025-10-23 12:26:48,283 | INFO | forums | thread_001.txt | score 0.1397
2025-10-23 12:26:48,283 | INFO | Top reranked:
[forums] (thread_001.txt) final_score=1.4670
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[blogs] (security_considerations.md) final_score=0.9472
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
[docs] (getting_started.md) final_score=0.4614
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[forums] (thread_002.txt) final_score=0.4380
UserD: How to handle rate limits? I'm getting 429 frequently.
----------------------------------------
[forums] (thread_002.txt) final_score=0.4165
UserE: The docs say exponential backoff; I used 1s, 2s, 4s and it works.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

11. Query: >> Are retries automatic or should I implement them?
2025-10-23 12:27:27,862 | INFO | Top retrievals (weighted):
2025-10-23 12:27:27,863 | INFO | blogs | security_considerations.md | score 0.1846
2025-10-23 12:27:27,863 | INFO | docs | features.md | score 0.1345
2025-10-23 12:27:27,863 | INFO | forums | thread_002.txt | score 0.1174
2025-10-23 12:27:27,863 | INFO | forums | thread_002.txt | score 0.1011
2025-10-23 12:27:27,863 | INFO | blogs | deploying_at_scale.md | score 0.0764
2025-10-23 12:27:27,864 | INFO | Top reranked:
[forums] (thread_001.txt) final_score=0.7713
UserC: I think the header should be Authorization: Bearer <token>.
----------------------------------------
[forums] (thread_001.txt) final_score=0.6066
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[forums] (thread_002.txt) final_score=0.4356
UserE: The docs say exponential backoff; I used 1s, 2s, 4s and it works.
----------------------------------------
[blogs] (security_considerations.md) final_score=0.0739
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
[docs] (features.md) final_score=0.0538
# Features
- Secure sandboxing
- Versioned deployments
- Webhooks for events
- Role-based access control
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

12. Query: >> Any tips on avoiding 429 bursts for batch jobs?
2025-10-23 12:27:53,101 | INFO | Top retrievals (weighted):
2025-10-23 12:27:53,102 | INFO | blogs | deploying_at_scale.md | score 0.4251
2025-10-23 12:27:53,102 | INFO | forums | thread_002.txt | score 0.2860
2025-10-23 12:27:53,102 | INFO | forums | thread_002.txt | score 0.2781
2025-10-23 12:27:53,102 | INFO | docs | getting_started.md | score 0.2283
2025-10-23 12:27:53,102 | INFO | forums | thread_002.txt | score 0.1451
2025-10-23 12:27:53,102 | INFO | Top reranked:
[forums] (thread_002.txt) final_score=0.5073
UserD: How to handle rate limits? I'm getting 429 frequently.
----------------------------------------
[docs] (getting_started.md) final_score=0.4530
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[docs] (features.md) final_score=0.4142
# Features
- Secure sandboxing
- Versioned deployments
- Webhooks for events
- Role-based access control
----------------------------------------
[blogs] (security_considerations.md) final_score=0.4138
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
[docs] (getting_started.md) final_score=0.3958
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.