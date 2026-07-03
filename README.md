# LLM Inference Platform — 企业级 GPU 推理平台(个人实战)

架构: 用户 -> Envoy(AI)Gateway [鉴权/Token限流] -> chat-api/Dify [RAG] -> vLLM Router -> vLLM GPU Pods
观测: DCGM+vLLM+Envoy+业务指标 -> Prometheus -> Grafana/Alertmanager; 日志 -> Alloy -> Loki
弹性: KEDA(推理队列) + HPA(业务CPU); 交付: GitHub Actions -> GitOps(Argo CD)

## 目录 <-> 方案章节 <-> 部署阶段
| 目录 | 方案章节 | 阶段 |
|---|---|---|
| bootstrap/, argocd/apps/ | §6 GitOps 组织 | 7 |
| deploy/gpu-operator/ | §7 GPU接入 | 1 |
| deploy/monitoring/ (values/servicemonitors/rules/dashboards) | §11 §13 | 2 |
| deploy/logging/ | §12 日志 | 2 |
| deploy/data/ | §3 数据层 | 4 |
| deploy/inference/ | §8 vLLM部署 + §14 KEDA | 3,6 |
| deploy/apps/ (chat-api chart, dify) | §3 业务层 | 4 |
| deploy/gateway/routes/ | §9 §10 网关三件套 | 5 |
| deploy/chaos/ | §15 故障场景 | 8 |
| apps/chat-api/ | 自研服务源码 | 4 |
| loadtest/ | §16 压测 | 8 |
| docs/runbook, docs/postmortem | §13 §15 产出物 | 全程 |

## 使用节奏(仓库先行)
1. 本地循环: 改模板 -> push -> Actions 绿
2. kind 循环: 无GPU跑通 monitoring/logging/data/chat-api/gateway (inference 用 mock 顶替)
3. GPU 循环: gpu-operator + inference + loadtest + chaos

## 铁律
- 每个 TODO(你来改) 先回答旁边的"问题:"再填; TODO(验证) 必须 kubectl 核对后填
- 阶段7后禁止 kubectl apply; 版本号一律固定, 禁止 latest/*
- 每天一条 docs/journal.md; 每条告警一篇 runbook; 每次演练一篇 postmortem

## 填参路线图(__TODO__共约90处, 按此顺序消灭, 每层填完发review)
1. local/kind-config -> 2. monitoring/values -> 3. servicemonitors(3个) -> 4. rules(4个)
-> 5. logging(2个) -> 6. data(3个) -> 7. mock/vllm-mock -> 8. apps/chat-api values
-> 9. gateway/routes(7个) -> 10. gpu-operator -> 11. inference -> 12. keda -> 13. chaos+k6 -> 14. argocd/apps里的repoURL与版本号
规则: TODO(验证)类必须kubectl核对后填; 每个__TODO__旁写一句依据; 装完组件回填真实名称
