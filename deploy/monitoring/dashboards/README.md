把 Grafana 面板 JSON 以 ConfigMap 存这里(labels: grafana_dashboard: "1"), sidecar 自动加载。
必备三块:
1. DCGM GPU 面板: 官方 Dashboard ID 12239 导入后 Export JSON 存入
2. vLLM 面板: production-stack 仓库自带, 复制过来
3. 自建业务面板: QPS/P99/token用量/每千token成本
