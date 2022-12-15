"""
如果 chat GPT 出现错误，很可能就是 config 有问题，比如过期，需要 debug
"""
config = {
  # "Authorization": "<API-KEY>",  # This is optional
  # "Authorization": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJoYmNoZW4xMjFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJVUyJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItSmtlVWVBTW5HaE1NdDhUS21RcmJkZ212In0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTcyMTAzMTEyMzk1OTQ3MDYyMSIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY3MDU4Mzc2NywiZXhwIjoxNjcwNjI2OTY3LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.Xo-r5ij43_id6jNJAdQwXxnYuWw_aQ4P-dnvRCBOGGFWx46OVGbRfDZ03mAiX6Ux2umFHQ6YsAhBmNNahuj3hX3hONq03GxpcDVK-YE3qTYx3gNnWhm-tsX2HOmHKKjmxXBowID4RwGO7ftKiW2FOOW-Dn8__W4sPMumm-mndWPQtq38nNXvOWmf1qdKjP5Fd6YY_HhW6c1AuU_7FrYC4eL1l_B9b2AZTNwgsjOdssM-X8eGz0jj0v6JBoQc5yuYhnUHcL-RL2y9K727uGLezAJi4Jhl7IS0q7p1AIUTE5Hcf2dJ9m90Qh2vUK3DkPFxuhTuAGIu1rxETrAliRMq4A",  # This is optional
  "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..rOc-Tyv2Fq3Uh57y.kgChyhv9D1rzjtlUxtSJ9DRgHDpM-19dyZ6cY3agQ8WOWUiYs9m9x2Eox3GLtpx7PVGXGwWw2FAB51jwYrYBMgkISG5Sx-bLKtp1Gw1XceboGfMoLsf3Z1ZMLLEqaSEQYKN9YeWeb3akLABUEm5agoEJazv_DfajhzGWiblX_ILsgITOmurOg562LDyRGWjejCiWASdc8ZfLUZ2MkpbhLhtzez7asUugSoGj9_tvTpSUQD7gNFWqYUY0EIOysHL2H96V8Vb2LDgeUconNbFHatcgi_pEaDP7lEXL5rb6KHt5LDGcCL4ggMTXmYUm7O-AFCfaYO0ePMt6ikCfn-OSzLJOMxCUsaPgOm8urrJhzV1egHqlvsmvkwPN9D7Ms3O-sFVxgqCTsQ1ip48TZjr9YqY4ETnIFNb-N_5WhziBqKuO4n49uU9vjg4cTM-4hiW7V1cUNW9HOKgf6sr2HgvTExU3V6PowkEr8FsQNAxCTPYX16r75ZdEXvJqAmGRNerLRpzSfF_NvM4CU-rBn3m1NxUskPfwr5q2ocHVVi5jdfD8rid-5tMvdu2JoIESGfqNPPn8xhzghqZ_GOD5k6F9vTENXDhpxH4L_nqlKHDMNDsPqO6b5UsQt0-uhLXKjfr6SISq2K6sxqPgJElrERhHPAXYbk7Y-wJh7PyJhDpvZC3CBxbXb_mwyHKok_D8E2Co27z13F9yYF9fxv__PLFr7sbJdHlC0kkCHLUPe-cz4JCghPEGK0xMqvvXSUZdpVRm4fg2AsScJEWluUH5z1EbVkosuK8pNcmwP2EIR80wRL8-ZUlXK_HufdvAfn-PK55XxY2tmnjTL5Dof8DNCR2x0MawAWzv8oRiL4O4_6299q6yYDfa9PZYiSc0MQ-mmUy4qaVcKFSnpcsJlv8uDts0R6RjIKd220KiYx4_QH3hP-oLATC0iRtbK7FKxQRBzKVW-td9QHdePoe4Qk6D79aNupNrLWFUrM5anJE2lWRrfj3T4NavfK0f-MOhCDZZUgkvKvyQFYf5Pz3xvapVJSyFDGZhDHhAaIBvqZ80n2g1GXRxIQg-9jrpFiNfgij1wWglke61aWe6AMrB7cK0CXddvgL6v4z01sBQdNv9VG4mR7QN20iqmVVULrPCMuedH-B9i9fAzNE9kfnOsXiqeDma3mDIerNqK1jayd-_s6Gb8H5Zi0grdRzddWJtdSkPVB7MHmu4hfAPIjc5BsOjpf6Jsdc5MkTpsqp8g7GKVqKUjTJJbqHYSH9VCZL9HRfZyq_I6rTXDBzcW435kpdPaTHuRVCAzzjXEgIZdizCJLvkcN084DX3REZaUhabKldNm9YE5QJvUGr5MUqfDl-zE18xjQV-NVbhbv2nJu63Y14GU6OT6Sdf2a2MylpzcyxnBKAB9hWp4OjRFN1CKKnY7m6ExNNWgNghK-YkiyGOhZFynVd6nnBf-YnaqZp58GCznsTOvBfMOi8YEyw1BuOsGGsGIIBHDhRY1U43iyf4BH-9NdyA0mpBt-SQqQQikfH3iONB-Vmzd2BawySSdLlosk81WvaLZBMTNBt4s_SO3vzOzPLno8ZX0dxGxAd5QXo4jcvNbn6loZePTJzELvVeeXayA1GqXvclUHFqHOZv846Y7ymlGN4gMP7hsgPDNO0P6VIznJY03rxx2YIwu5VNCZvH_HUG6-XEFi0wSy3SzB5guhKSWem0t-YVhT3-PsAbqe-rhijdFIXTV4vvKvpN9Z3Yo96rvTAaFTkmBsvFGo7mp6FRHvVrKxbuaKg3YgWVAyJKo_8SvDz3GMwyFlUDDk6IFMyHdVnHYFqgosIXct6ZHZ3cjkNQudHTdUiuBpG7D6oxyLqZfSLgkByu5MmwOC0vI7j7JMa5-boptzb5fhFuJffqRQH8Cp8nulQ6i-NGDLfKsRQAOlje4WYgXgo23GQD1vi6nfk1iEJG12dhRl-DyZHtlN-PctI_HkDsjLzYGu90IOqpSsezQT-MKOiStMQkRlwSnJxeRryNSYpwGrq8yXBNYB75MU4TdZoaNnwal7x1ULMPS0nqL_dbnnIOGPneuEnzcYsqwdXT4yy9GCrMkxM70zWMN9hmoybQVzBFzvTgx5xcU1O247A5tm-GTx6GUSnOt6__9YtPdaf907Smo096OCqURRPakYTlDyd84Ao7wqojgpus7V5q_CtULbvA5j-w74XW4CfR2_iaLXI-xzHRNuoxfmWQHnXJsMtTmCRlVeS4bcU.7k7YXYkiBtTppmhhCBuDQA",
  # "cf_clearance": "nJzoli8bqevHNJEKaffVZyigaRJtfkV6TxQI5qfCm2A-1670938074-0-1-f6b513dd.563fcc3c.a1b44c3d-160",
  # "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
  # "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
  "accept_language": "en-US,en",
  "proxy": "http://127.0.0.1:8001/",  # 建议填一个不冲突的
}
