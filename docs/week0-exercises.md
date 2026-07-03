# 第 0 周:K8s 手感练习(kind 集群,免费)

每题都按四步做:抄 → 改一个参数 → 故意改坏 → 自己修好。修的过程记到 docs/journal.md。

## 准备
kind create cluster --name lab
kubectl get nodes   # 验收: Ready

## 练习1: Deployment + Service
- 部署 nginx (2副本) + ClusterIP Service,port-forward 后 curl 通
- 验收: kubectl get endpoints nginx 有 2 个 IP
- 破坏实验: 把 Service selector 改错 → endpoints 变空 → curl 失败 → 修好
- 必答: labels/selector/endpoints 三者关系?

## 练习2: 探针
- 给 nginx 加 readiness (path=/),改成 /wrong 观察 Pod Running 但 NotReady
- 验收: 能用 describe pod 找到探针失败事件
- 必答: readiness 失败和 liveness 失败,后果有什么不同?

## 练习3: ConfigMap + 资源限制
- 用 ConfigMap 挂一个自定义 index.html;给容器加 memory limit 并制造 OOMKilled
- 验收: kubectl describe pod 看到 OOMKilled + restart 计数增加
- 必答: requests 和 limits 分别影响什么?(调度 vs 运行时)

## 练习4: Helm
- helm create demo,读懂生成的模板;helm install 后改 values 里副本数 upgrade
- 验收: helm diff(装插件)能看出变更;helm rollback 回滚成功
- 必答: helm template 和 helm install 的区别?

## 练习5: 监控栈
- helm 装 kube-prometheus-stack,给练习1的 nginx 配 ServiceMonitor(需 nginx-exporter 或换 podinfo 应用)
- 验收: Grafana 里查到该应用指标;Prometheus targets 页面状态 UP
- 必答: ServiceMonitor 是怎么被 Prometheus 发现的?(Operator/CRD 机制)

全部完成 → 你已经具备启动主项目阶段 0 的全部前置能力。
