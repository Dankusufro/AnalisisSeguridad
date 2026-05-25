# Hallazgos Grype

| Repositorio | Paquete | Version | Vulnerabilidad | Severidad | Mensaje |
| --- | --- | --- | --- | --- | --- |
| DeepSeek-TUI | actions/download-artifact | v4 | GHSA-cxww-7g56-2vh6 | low | @actions/download-artifact has an Arbitrary File Write via artifact extraction |
| DeepSeek-TUI | aws-lc-sys | 0.38.0 | GHSA-394x-vwmw-crm3 | low | AWS-LC X.509 Name Constraints Bypass via Wildcard/Unicode CN |
| DeepSeek-TUI | aws-lc-sys | 0.38.0 | GHSA-9f94-5g5w-gf6r | low | CRL Distribution Point Scope Check Logic Error in AWS-LC |
| DeepSeek-TUI | bytes | 1.11.0 | GHSA-434x-w66g-qw3r | low | bytes has integer overflow in BytesMut::reserve |
| DeepSeek-TUI | lru | 0.12.5 | GHSA-rhfx-m35p-ff5j | low | `IterMut` violates Stacked Borrows by invalidating internal pointer |
| DeepSeek-TUI | quinn-proto | 0.11.13 | GHSA-6xvm-j4wr-6v98 | low | Quinn affected by unauthenticated remote DoS via panic in QUIC transport parameter parsing |
| DeepSeek-TUI | rand | 0.9.2 | GHSA-cq8v-f236-94qc | low | Rand is unsound with a custom logger using rand::rng() |
| DeepSeek-TUI | rustls-webpki | 0.103.8 | GHSA-82j2-j2ch-gfr8 | low | rustls-webpki: Denial of service via panic on malformed CRL BIT STRING |
| DeepSeek-TUI | rustls-webpki | 0.103.8 | GHSA-pwjx-qhcg-rvj4 | low | webpki: CRLs not considered authoritative by Distribution Point due to faulty matching logic |
| DeepSeek-TUI | rustls-webpki | 0.103.8 | GHSA-965h-392x-2mh5 | low | webpki: Name constraints for URI names were incorrectly accepted |
| DeepSeek-TUI | rustls-webpki | 0.103.8 | GHSA-xgp8-3hg3-c2mh | low | webpki: Name constraints were accepted for certificates asserting a wildcard name |
| DeepSeek-TUI | time | 0.3.46 | GHSA-r6v5-fh4h-64xc | low | time vulnerable to stack exhaustion Denial of Service attack |
| TradingAgents | aiohttp | 3.12.13 | GHSA-c427-h43c-vf67 | low | AIOHTTP accepts duplicate Host headers |
| TradingAgents | aiohttp | 3.12.13 | GHSA-6mq8-rvhq-8wgg | low | AIOHTTP's HTTP Parser auto_decompress feature is vulnerable to zip bomb |
| TradingAgents | aiohttp | 3.12.13 | GHSA-p998-jp59-783m | low | AIOHTTP affected by UNC SSRF/NTLMv2 Credential Theft/Local File Read in static resource handler on Windows |
| TradingAgents | aiohttp | 3.12.13 | GHSA-6jhg-hg63-jvvf | low | AIOHTTP vulnerable to  denial of service through large payloads |
| TradingAgents | aiohttp | 3.12.13 | GHSA-jj3x-wxrx-4x23 | low | AIOHTTP vulnerable to DoS when bypassing asserts |
| TradingAgents | aiohttp | 3.12.13 | GHSA-m5qp-6w8w-w647 | low | AIOHTTP has a Multipart Header Size Bypass |
| TradingAgents | aiohttp | 3.12.13 | GHSA-w2fm-2cpv-w7v5 | low | aiohttp allows unlimited trailer headers, leading to possible uncapped memory usage |
| TradingAgents | aiohttp | 3.12.13 | GHSA-g84x-mcqj-x9qq | low | AIOHTTP vulnerable to DoS through chunked messages |
| TradingAgents | aiohttp | 3.12.13 | GHSA-63hf-3vf5-4wqf | low | AIOHTTP's C parser (llhttp) accepts null bytes and control characters in response header values - header injection/secur |
| TradingAgents | aiohttp | 3.12.13 | GHSA-9548-qrrj-x5pj | low | AIOHTTP is vulnerable to HTTP Request/Response Smuggling through incorrect parsing of chunked trailer sections |
| TradingAgents | aiohttp | 3.12.13 | GHSA-54jq-c3m8-4m76 | low | AIOHTTP vulnerable to brute-force leak of internal static ﬁle path components |
| TradingAgents | aiohttp | 3.12.13 | GHSA-hcc4-c3v8-rx92 | low | AIOHTTP Affected by Denial of Service (DoS) via Unbounded DNS Cache in TCPConnector |
| TradingAgents | aiohttp | 3.12.13 | GHSA-3wq7-rqq7-wx6j | low | AIOHTTP has late size enforcement for non-file multipart fields causes memory DoS |
| TradingAgents | aiohttp | 3.12.13 | GHSA-966j-vmvw-g2g9 | low | AIOHTTP leaks Cookie and Proxy-Authorization headers on cross-origin redirect |
| TradingAgents | aiohttp | 3.12.13 | GHSA-mqqc-3gqh-h2x8 | low | AIOHTTP has unicode match groups in regexes for ASCII protocol elements |
| TradingAgents | aiohttp | 3.12.13 | GHSA-69f9-5gxw-wvc2 | low | AIOHTTP's unicode processing of header values could cause parsing discrepancies |
| TradingAgents | aiohttp | 3.12.13 | GHSA-2vrm-gr82-f7m5 | low | AIOHTTP has CRLF injection through multipart part content type header construction |
| TradingAgents | aiohttp | 3.12.13 | GHSA-mwh4-6h8g-pg8w | low | AIOHTTP has HTTP response splitting via \r in reason phrase |
| TradingAgents | aiohttp | 3.12.13 | GHSA-fh55-r93g-j68g | low | AIOHTTP Vulnerable to Cookie Parser Warning Storm |
| TradingAgents | chainlit | 2.5.5 | GHSA-2g59-m95p-pgfq | low | Chainlit contain a server-side request forgery (SSRF) vulnerability |
| TradingAgents | chainlit | 2.5.5 | GHSA-v492-6xx2-p57g | low | Chainlit contains an authorization bypass vulnerability |
| TradingAgents | curl-cffi | 0.11.3 | GHSA-qw2m-4pqf-rmpp | low | curl_cffi: Redirect-based SSRF leads to internal network access in curl_cffi (with TLS impersonation bypass) |
| TradingAgents | filelock | 3.18.0 | GHSA-w853-jp5j-5j7f | low | filelock has a TOCTOU race condition which allows symlink attacks during lock file creation |
| TradingAgents | filelock | 3.18.0 | GHSA-qmgc-5h2g-mvrw | low | filelock Time-of-Check-Time-of-Use (TOCTOU) Symlink Vulnerability in SoftFileLock |
| TradingAgents | langchain-community | 0.3.25 | GHSA-pc6w-59fv-rh23 | low | Langchain Community Vulnerable to XML External Entity (XXE) Attacks |
| TradingAgents | langchain-core | 0.3.83 | GHSA-qh6h-p6c9-ff54 | low | LangChain Core has Path Traversal vulnerabilites in legacy `load_prompt` functions |
| TradingAgents | langchain-core | 0.3.83 | GHSA-2g6r-c272-w58r | low | LangChain affected by SSRF via image_url token counting in ChatOpenAI.get_num_tokens_from_messages |
| TradingAgents | langchain-openai | 0.3.23 | GHSA-r7w7-9xr2-qq2r | low | langchain-openai: Image token counting SSRF protection can be bypassed via DNS rebinding |
| TradingAgents | langchain-text-splitters | 0.3.8 | GHSA-m42m-m8cr-8m58 | low | LangChain Text Splitters is vulnerable to XML External Entity (XXE) attacks due to unsafe XSLT parsing |
| TradingAgents | langchain-text-splitters | 0.3.8 | GHSA-fv5p-p927-qmxr | low | LangChain Text Splitters: HTMLHeaderTextSplitter.split_text_from_url SSRF Redirect Bypass |
| TradingAgents | langgraph | 0.4.8 | GHSA-g48c-2wqr-h844 | low | LangGraph checkpoint loading has unsafe msgpack deserialization |
| TradingAgents | langgraph-checkpoint | 2.0.26 | GHSA-wwqv-p2pp-99h5 | low | LangGraph Checkpoint affected by RCE in "json" mode of JsonPlusSerializer |
| TradingAgents | langgraph-checkpoint | 2.0.26 | GHSA-mhr3-j7m5-c7c9 | low | LangGraph: BaseCache Deserialization of Untrusted Data may lead to Remote Code Execution |
| TradingAgents | langsmith | 0.3.45 | GHSA-rr7j-v2q5-chgv | low | LangSmith SDK: Streaming token events bypass output redaction |
| TradingAgents | lxml | 5.4.0 | GHSA-vfmq-68hx-4jfw | low | lxml: Default configuration of iterparse() and ETCompatXMLParser() allows XXE to local files |
| TradingAgents | marshmallow | 3.26.1 | GHSA-428g-f7cq-pgp5 | low | Marshmallow has DoS in Schema.load(many) |
| TradingAgents | mcp | 1.9.4 | GHSA-j975-95f5-7wqh | low | MCP Python SDK has Unhandled Exception in Streamable HTTP Transport, Leading to Denial of Service |
| TradingAgents | mcp | 1.9.4 | GHSA-9h52-p55h-vw2f | low | Model Context Protocol (MCP) Python SDK does not enable DNS rebinding protection by default |
| TradingAgents | orjson | 3.10.18 | GHSA-hx9q-6w63-j58v | low | orjson does not limit recursion for deeply nested JSON documents |
| TradingAgents | protobuf | 5.29.5 | GHSA-7gcm-g887-7qv7 | low | protobuf affected by a JSON recursion depth bypass |
| TradingAgents | pyasn1 | 0.6.1 | GHSA-jr27-m4p2-rc6r | low | Denial of Service in pyasn1 via Unbounded Recursion |
| TradingAgents | pyasn1 | 0.6.1 | GHSA-63vm-454h-vhhq | low | pyasn1 has a DoS vulnerability in decoder |
| TradingAgents | pygments | 2.19.1 | GHSA-5239-wwwm-4pmq | low | Pygments has Regular Expression Denial of Service (ReDoS) due to Inefficient Regex for GUID Matching |
| TradingAgents | pyjwt | 2.10.1 | GHSA-752w-5fwx-jx9f | low | PyJWT accepts unknown `crit` header extensions |
| TradingAgents | python-dotenv | 1.1.0 | GHSA-mf9w-mj56-hr94 | low | python-dotenv: Symlink following in set_key allows arbitrary file overwrite via cross-device rename fallback |
| TradingAgents | python-multipart | 0.0.18 | GHSA-wp53-j4wj-2cfg | low | Python-Multipart has Arbitrary File Write via Non-Default Configuration |
| TradingAgents | python-multipart | 0.0.18 | GHSA-mj87-hwqh-73pj | low | python-multipart affected by Denial of Service via large multipart preamble or epilogue data |
| TradingAgents | python-socketio | 5.13.0 | GHSA-g8c6-8fjj-2r4m | low | python-socketio vulnerable to arbitrary Python code execution (RCE) through malicious pickle deserialization in certain  |
| TradingAgents | requests | 2.32.4 | GHSA-gc5v-m9x4-r6x2 | low | Requests has Insecure Temp File Reuse in its extract_zipped_paths() utility function |
| TradingAgents | starlette | 0.41.3 | GHSA-7f5h-v6xp-fcq8 | low | Starlette vulnerable to O(n^2) DoS via Range header merging in ``starlette.responses.FileResponse`` |
| TradingAgents | starlette | 0.41.3 | GHSA-2c2j-9gv5-cj73 | low | Starlette has possible denial-of-service vector when parsing large files in multipart forms |
| TradingAgents | urllib3 | 2.4.0 | GHSA-pq67-6m6q-mj2v | low | urllib3 redirects are not disabled when retries are disabled on PoolManager instantiation |
| TradingAgents | urllib3 | 2.4.0 | GHSA-48p4-8xcf-vxj5 | low | urllib3 does not control redirects in browsers and Node.js |
| TradingAgents | urllib3 | 2.4.0 | GHSA-38jv-5279-wg99 | low | Decompression-bomb safeguards bypassed when following HTTP redirects (streaming API) |
| TradingAgents | urllib3 | 2.4.0 | GHSA-gm62-xv2j-4w53 | low | urllib3 allows an unbounded number of links in the decompression chain |
| TradingAgents | urllib3 | 2.4.0 | GHSA-2xpw-w6gg-jr37 | low | urllib3 streaming API improperly handles highly compressed data |
| Understand-Anything | brace-expansion | 2.0.2 | GHSA-f886-m6hf-6m8v | low | brace-expansion: Zero-step sequence causes process hang and memory exhaustion |
| Understand-Anything | brace-expansion | 5.0.5 | GHSA-jxxr-4gwj-5jf2 | low | brace-expansion: Large numeric range defeats documented `max` DoS protection |
| Understand-Anything | brace-expansion | 5.0.5 | GHSA-jxxr-4gwj-5jf2 | low | brace-expansion: Large numeric range defeats documented `max` DoS protection |
| Understand-Anything | devalue | 5.6.4 | GHSA-77vg-94rm-hx3p | low | Svelte devalue: DoS via sparse array deserialization |
| Understand-Anything | picomatch | 2.3.1 | GHSA-3v7f-55p6-f55p | low | Picomatch: Method Injection in POSIX Character Classes causes incorrect Glob Matching |
| Understand-Anything | picomatch | 4.0.3 | GHSA-3v7f-55p6-f55p | low | Picomatch: Method Injection in POSIX Character Classes causes incorrect Glob Matching |
| Understand-Anything | picomatch | 2.3.1 | GHSA-c2c7-rcm5-vvqj | low | Picomatch has a ReDoS vulnerability via extglob quantifiers |
| Understand-Anything | picomatch | 4.0.3 | GHSA-c2c7-rcm5-vvqj | low | Picomatch has a ReDoS vulnerability via extglob quantifiers |
| Understand-Anything | postcss | 8.5.8 | GHSA-qx2v-qp2m-jg93 | low | PostCSS has XSS via Unescaped </style> in its CSS Stringify Output |
| Understand-Anything | postcss | 8.5.8 | GHSA-qx2v-qp2m-jg93 | low | PostCSS has XSS via Unescaped </style> in its CSS Stringify Output |
| Understand-Anything | smol-toml | 1.6.0 | GHSA-v3rj-xjv7-4jmq | low | smol-toml: Denial of Service via TOML documents containing thousands of consecutive commented lines |
| Understand-Anything | vite | 6.4.1 | GHSA-p9ff-h696-f583 | low | Vite Vulnerable to Arbitrary File Read via Vite Dev Server WebSocket |
| Understand-Anything | vite | 7.3.1 | GHSA-p9ff-h696-f583 | low | Vite Vulnerable to Arbitrary File Read via Vite Dev Server WebSocket |
| Understand-Anything | vite | 7.3.1 | GHSA-v2wj-q39q-566r | low | Vite: `server.fs.deny` bypassed with queries |
| Understand-Anything | vite | 6.4.1 | GHSA-4w7w-66w2-5vf9 | low | Vite Vulnerable to Path Traversal in Optimized Deps `.map` Handling |
| Understand-Anything | vite | 7.3.1 | GHSA-4w7w-66w2-5vf9 | low | Vite Vulnerable to Path Traversal in Optimized Deps `.map` Handling |
| claude-code-action | undici | 5.29.0 | GHSA-v9p9-hfj2-hcw8 | low | Undici has Unhandled Exception in WebSocket Client Due to Invalid server_max_window_bits Validation |
| claude-code-action | undici | 5.29.0 | GHSA-vrm6-8vpv-qv8q | low | Undici has Unbounded Memory Consumption in WebSocket permessage-deflate Decompression |
| claude-code-action | undici | 5.29.0 | GHSA-g9mf-h72j-4rw9 | low | Undici has an unbounded decompression chain in HTTP responses on Node.js Fetch API via Content-Encoding leads to resourc |
| claude-code-action | undici | 5.29.0 | GHSA-2mjp-6q6p-2qxm | low | Undici has an HTTP Request/Response Smuggling issue |
| claude-code-action | undici | 5.29.0 | GHSA-4992-7rv2-5pvq | low | Undici has CRLF Injection in undici via `upgrade` option |
| claude-plugins-official | actions/download-artifact | v4 | GHSA-cxww-7g56-2vh6 | low | @actions/download-artifact has an Arbitrary File Write via artifact extraction |
| codegraph | picomatch | 4.0.3 | GHSA-3v7f-55p6-f55p | low | Picomatch: Method Injection in POSIX Character Classes causes incorrect Glob Matching |
| codegraph | picomatch | 4.0.3 | GHSA-c2c7-rcm5-vvqj | low | Picomatch has a ReDoS vulnerability via extglob quantifiers |
| dexter | file-type | 21.3.0 | GHSA-j47w-4g3g-c36v | low | file-type: ZIP Decompression Bomb DoS via [Content_Types].xml entry |
| dexter | file-type | 21.3.0 | GHSA-5v7r-6r5c-r473 | low | file-type affected by infinite loop in ASF parser on malformed input with zero-size sub-header |
| dexter | langsmith | 0.4.12 | GHSA-fw9q-39r9-c252 | low | LangSmith Client SDKs has Prototype Pollution in langsmith-sdk via Incomplete `__proto__` Guard in Internal lodash `set( |
| dexter | langsmith | 0.5.13 | GHSA-fw9q-39r9-c252 | low | LangSmith Client SDKs has Prototype Pollution in langsmith-sdk via Incomplete `__proto__` Guard in Internal lodash `set( |
| dexter | langsmith | 0.4.12 | GHSA-rr7j-v2q5-chgv | low | LangSmith SDK: Streaming token events bypass output redaction |
| dexter | langsmith | 0.5.13 | GHSA-rr7j-v2q5-chgv | low | LangSmith SDK: Streaming token events bypass output redaction |
| dexter | music-metadata | 11.12.0 | GHSA-v6c2-xwv6-8xf7 | low | music-metadata has an infinite loop vulnerability in ASF parser |
| dexter | protobufjs | 6.8.8 | GHSA-xq3m-2v4x-88gg | low | Arbitrary code execution in protobufjs |
