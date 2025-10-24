

1. Query: >> How do I authenticate requests to ScriptChain?
2025-10-23 16:22:22,125 | INFO | Top retrievals (weighted):
2025-10-23 16:22:22,125 | INFO | docs | getting_started.md | score 0.5450
2025-10-23 16:22:22,125 | INFO | docs | getting_started.md | score 0.4859
2025-10-23 16:22:22,125 | INFO | forums | thread_001.txt | score 0.4046
2025-10-23 16:22:22,125 | INFO | blogs | security_considerations.md | score 0.3554
2025-10-23 16:22:22,125 | INFO | blogs | deploying_at_scale.md | score 0.2698
2025-10-23 16:22:22,559 | INFO | Top reranked:
[forums] (thread_001.txt) final_score=-1.5466
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[docs] (getting_started.md) final_score=-2.1734
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=-2.6369
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[docs] (getting_started.md) final_score=-3.2080
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[forums] (thread_001.txt) final_score=-5.7475
UserC: I think the header should be Authorization: Bearer <token>.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

2. Query: >> What endpoint runs a script?
2025-10-23 16:24:43,555 | INFO | Top retrievals (weighted):
2025-10-23 16:24:43,561 | INFO | docs | getting_started.md | score 0.3640
2025-10-23 16:24:43,561 | INFO | docs | getting_started.md | score 0.2998
2025-10-23 16:24:43,561 | INFO | blogs | deploying_at_scale.md | score 0.2191
2025-10-23 16:24:43,561 | INFO | docs | features.md | score 0.1830
2025-10-23 16:24:43,561 | INFO | blogs | security_considerations.md | score 0.1698
2025-10-23 16:24:43,900 | INFO | Top reranked:
[docs] (getting_started.md) final_score=2.9548
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[docs] (getting_started.md) final_score=-4.1694
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=-4.7926
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[forums] (thread_001.txt) final_score=-5.7872
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[forums] (thread_001.txt) final_score=-6.1699
UserB: Make sure the header is X-API-Key, and that your key has 'run' permission.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

3. Query: >> I'm getting 429 errors; how to handle rate limits?
2025-10-23 16:25:28,399 | INFO | Top retrievals (weighted):
2025-10-23 16:25:28,400 | INFO | forums | thread_002.txt | score 0.4357
2025-10-23 16:25:28,400 | INFO | docs | getting_started.md | score 0.2121
2025-10-23 16:25:28,400 | INFO | blogs | deploying_at_scale.md | score 0.2061
2025-10-23 16:25:28,400 | INFO | forums | thread_002.txt | score 0.1609
2025-10-23 16:25:28,400 | INFO | forums | thread_002.txt | score 0.1366
2025-10-23 16:25:28,533 | INFO | Top reranked:
[forums] (thread_002.txt) final_score=5.6221
UserD: How to handle rate limits? I'm getting 429 frequently.
----------------------------------------
[docs] (getting_started.md) final_score=-2.1314
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[forums] (thread_002.txt) final_score=-6.3087
UserF: Alternatively, you can set parallelism to 1 to avoid bursts.
----------------------------------------
[docs] (getting_started.md) final_score=-6.3739
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=-6.4038
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

4. Query: >> Should I use Authorization: Bearer or X-API-Key?
2025-10-23 16:26:05,691 | INFO | Top retrievals (weighted):
2025-10-23 16:26:05,691 | INFO | forums | thread_001.txt | score 0.3127
2025-10-23 16:26:05,691 | INFO | blogs | security_considerations.md | score 0.3082
2025-10-23 16:26:05,691 | INFO | docs | getting_started.md | score 0.2922
2025-10-23 16:26:05,691 | INFO | forums | thread_001.txt | score 0.2883
2025-10-23 16:26:05,691 | INFO | forums | thread_001.txt | score 0.2684
2025-10-23 16:26:05,818 | INFO | Top reranked:
[forums] (thread_001.txt) final_score=4.1204
UserC: I think the header should be Authorization: Bearer <token>.
----------------------------------------
[forums] (thread_001.txt) final_score=0.6616
UserB: Make sure the header is X-API-Key, and that your key has 'run' permission.
----------------------------------------
[docs] (getting_started.md) final_score=-2.0467
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[forums] (thread_001.txt) final_score=-3.2022
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[blogs] (security_considerations.md) final_score=-4.0841
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

5. Query: >> How to deploy ScriptChain at scale?
2025-10-23 16:26:51,035 | INFO | Top retrievals (weighted):
2025-10-23 16:26:51,035 | INFO | blogs | deploying_at_scale.md | score 0.6419
2025-10-23 16:26:51,035 | INFO | docs | getting_started.md | score 0.4133
2025-10-23 16:26:51,035 | INFO | docs | getting_started.md | score 0.3582
2025-10-23 16:26:51,035 | INFO | forums | thread_001.txt | score 0.2173
2025-10-23 16:26:51,035 | INFO | docs | features.md | score 0.2086
2025-10-23 16:26:51,165 | INFO | Top reranked:
[blogs] (deploying_at_scale.md) final_score=6.1011
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[docs] (getting_started.md) final_score=-0.5195
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[docs] (getting_started.md) final_score=-1.5118
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[forums] (thread_001.txt) final_score=-2.9016
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[forums] (thread_002.txt) final_score=-6.1739
UserF: Alternatively, you can set parallelism to 1 to avoid bursts.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

6. Query: >> How to store API keys securely?
2025-10-23 16:27:55,995 | INFO | Top retrievals (weighted):
2025-10-23 16:27:55,995 | INFO | blogs | security_considerations.md | score 0.4637
2025-10-23 16:27:55,995 | INFO | forums | thread_001.txt | score 0.2688
2025-10-23 16:27:55,995 | INFO | docs | features.md | score 0.2427
2025-10-23 16:27:55,995 | INFO | docs | getting_started.md | score 0.2390
2025-10-23 16:27:55,995 | INFO | docs | getting_started.md | score 0.2191
2025-10-23 16:27:56,112 | INFO | Top reranked:
[blogs] (security_considerations.md) final_score=3.4665
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
[forums] (thread_001.txt) final_score=0.2737
UserB: Make sure the header is X-API-Key, and that your key has 'run' permission.
----------------------------------------
[forums] (thread_001.txt) final_score=-0.6903
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[docs] (getting_started.md) final_score=-2.1467
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[docs] (getting_started.md) final_score=-5.7307
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

7. Query: >> What endpoints provide job status?
2025-10-23 16:28:26,671 | INFO | Top retrievals (weighted):
2025-10-23 16:28:26,672 | INFO | docs | getting_started.md | score 0.3564
2025-10-23 16:28:26,672 | INFO | docs | features.md | score 0.2265
2025-10-23 16:28:26,672 | INFO | blogs | deploying_at_scale.md | score 0.1851
2025-10-23 16:28:26,673 | INFO | blogs | security_considerations.md | score 0.1680
2025-10-23 16:28:26,673 | INFO | docs | getting_started.md | score 0.1571
2025-10-23 16:28:26,743 | INFO | Top reranked:
[docs] (getting_started.md) final_score=2.5636
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=-6.4898
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[docs] (getting_started.md) final_score=-6.6976
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[blogs] (security_considerations.md) final_score=-6.7438
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
[docs] (features.md) final_score=-6.7485
# Features
- Secure sandboxing
- Versioned deployments
- Webhooks for events
- Role-based access control
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

8. Query: >> Is there role-based access control?
2025-10-23 16:28:53,905 | INFO | Top retrievals (weighted):
2025-10-23 16:28:53,905 | INFO | docs | features.md | score 0.5439
2025-10-23 16:28:53,905 | INFO | docs | getting_started.md | score 0.1893
2025-10-23 16:28:53,905 | INFO | blogs | security_considerations.md | score 0.1170
2025-10-23 16:28:53,905 | INFO | forums | thread_001.txt | score 0.0833
2025-10-23 16:28:53,905 | INFO | forums | thread_002.txt | score 0.0771
2025-10-23 16:28:54,031 | INFO | Top reranked:
[docs] (features.md) final_score=4.3691
# Features
- Secure sandboxing
- Versioned deployments
- Webhooks for events
- Role-based access control
----------------------------------------
[docs] (getting_started.md) final_score=-6.4500
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[forums] (thread_001.txt) final_score=-6.5349
UserB: Make sure the header is X-API-Key, and that your key has 'run' permission.
----------------------------------------
[forums] (thread_001.txt) final_score=-6.7078
UserC: I think the header should be Authorization: Bearer <token>.
----------------------------------------
[blogs] (security_considerations.md) final_score=-6.7486
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

9. Query: >> Does ScriptChain support webhooks?
2025-10-23 16:29:20,513 | INFO | Top retrievals (weighted):
2025-10-23 16:29:20,514 | INFO | docs | getting_started.md | score 0.5629
2025-10-23 16:29:20,514 | INFO | docs | features.md | score 0.4901
2025-10-23 16:29:20,514 | INFO | docs | getting_started.md | score 0.3804
2025-10-23 16:29:20,514 | INFO | blogs | deploying_at_scale.md | score 0.2820
2025-10-23 16:29:20,514 | INFO | forums | thread_001.txt | score 0.2624
2025-10-23 16:29:20,643 | INFO | Top reranked:
[docs] (getting_started.md) final_score=-1.2903
# ScriptChain App - Getting Started
ScriptChain is a fictional product for securely connecting scripts to healthcare workflows.
----------------------------------------
[docs] (features.md) final_score=-1.3558
# Features
- Secure sandboxing
- Versioned deployments
- Webhooks for events
- Role-based access control
----------------------------------------
[forums] (thread_001.txt) final_score=-2.8735
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=-3.3039
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[docs] (getting_started.md) final_score=-3.4842
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

10. Query: >> How frequently should I rotate API keys?
2025-10-23 16:29:48,929 | INFO | Top retrievals (weighted):
2025-10-23 16:29:48,930 | INFO | blogs | security_considerations.md | score 0.4689
2025-10-23 16:29:48,930 | INFO | docs | getting_started.md | score 0.2493
2025-10-23 16:29:48,930 | INFO | forums | thread_001.txt | score 0.1839
2025-10-23 16:29:48,930 | INFO | blogs | deploying_at_scale.md | score 0.1589
2025-10-23 16:29:48,930 | INFO | forums | thread_001.txt | score 0.1397
2025-10-23 16:29:49,002 | INFO | Top reranked:
[blogs] (security_considerations.md) final_score=5.3016
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
[forums] (thread_001.txt) final_score=-1.9970
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[forums] (thread_001.txt) final_score=-3.0219
UserB: Make sure the header is X-API-Key, and that your key has 'run' permission.
----------------------------------------
[docs] (getting_started.md) final_score=-3.5670
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[forums] (thread_002.txt) final_score=-4.4368
UserD: How to handle rate limits? I'm getting 429 frequently.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

11. Query: >> Are retries automatic or should I implement them?
2025-10-23 16:30:16,852 | INFO | Top retrievals (weighted):
2025-10-23 16:30:16,852 | INFO | blogs | security_considerations.md | score 0.1846
2025-10-23 16:30:16,852 | INFO | docs | features.md | score 0.1345
2025-10-23 16:30:16,852 | INFO | forums | thread_002.txt | score 0.1174
2025-10-23 16:30:16,852 | INFO | forums | thread_002.txt | score 0.1011
2025-10-23 16:30:16,852 | INFO | blogs | deploying_at_scale.md | score 0.0764
2025-10-23 16:30:16,920 | INFO | Top reranked:
[docs] (getting_started.md) final_score=-5.2874
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[forums] (thread_001.txt) final_score=-6.1359
UserC: I think the header should be Authorization: Bearer <token>.
----------------------------------------
[forums] (thread_001.txt) final_score=-6.4407
UserA: I tried scriptchain with API key but got 401. How do I fix?
----------------------------------------
[forums] (thread_002.txt) final_score=-6.5572
UserE: The docs say exponential backoff; I used 1s, 2s, 4s and it works.
----------------------------------------
[blogs] (security_considerations.md) final_score=-6.7520
# Security
Store API keys in environment variables; rotate them every 90 days.
For audit logging, enable request tracing.
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.

12. Query: >> Any tips on avoiding 429 bursts for batch jobs?
2025-10-23 16:30:39,297 | INFO | Top retrievals (weighted):
2025-10-23 16:30:39,297 | INFO | blogs | deploying_at_scale.md | score 0.4251
2025-10-23 16:30:39,297 | INFO | forums | thread_002.txt | score 0.2860
2025-10-23 16:30:39,297 | INFO | forums | thread_002.txt | score 0.2781
2025-10-23 16:30:39,297 | INFO | docs | getting_started.md | score 0.2283
2025-10-23 16:30:39,297 | INFO | forums | thread_002.txt | score 0.1451
2025-10-23 16:30:39,394 | INFO | Top reranked:
[forums] (thread_002.txt) final_score=-0.9310
UserF: Alternatively, you can set parallelism to 1 to avoid bursts.
----------------------------------------
[forums] (thread_002.txt) final_score=-3.9108
UserD: How to handle rate limits? I'm getting 429 frequently.
----------------------------------------
[docs] (getting_started.md) final_score=-5.2937
Installation: pip install scriptchain
Auth: API key in header X-API-Key
Endpoints:
- /v1/run : runs a script
- /v1/status : job status (id)
Retries: exponential backoff, status 429 means rate-limited
----------------------------------------
[blogs] (deploying_at_scale.md) final_score=-5.6585
# Deploying ScriptChain at Scale
When deploying in production, pin the runtime and use background workers to run long jobs.
Tip: use exponential backoff plus jitter to reduce synchronization.
----------------------------------------
[docs] (features.md) final_score=-6.5738
# Features
- Secure sandboxing
- Versioned deployments
- Webhooks for events
- Role-based access control
----------------------------------------
Contradiction check: no_contradiction
Logged query. Next.