# LLM Inference Platform — 企业级 GPU 推理平台(个人实战)

## 使用方法(仓库先行,服务器后置)
1. 本地循环:改模板 → 运行 `make lint`(或推到 GitHub 触发 CI)→ 通过再进下一步
2. kind 循环:`kind create cluster` 跑通监控/日志/网关/业务层(无 GPU)
3. GPU 循环:租 GPU 机器,只做 GPU Operator + vLLM + 压测/故障演练

## 目录说明
- `bootstrap/`      Argo CD 根应用(App-of-Apps 入口)
- `argocd/apps/`    每个组件一个 Application,编号 = 部署顺序(sync-wave)
- `deploy/`         各组件的 values 和自写 YAML(你主要改这里)
- `apps/chat-api/`  自研 FastAPI 业务服务源码
- `docs/`           week0 练习、runbook、故障复盘

## 约定
- 所有 `# TODO(你来改)` 的字段必须自己填,填之前先回答注释里的问题
- 禁止 kubectl apply 手工改集群(阶段 7 接入 Argo 后)
- 每天在 docs/journal.md 记一条:做了什么/坑/怎么解决
