lint:
	helm lint deploy/apps/chat-api || true
	@command -v kubeconform >/dev/null && find deploy -name '*.yaml' ! -name 'values*.yaml' -exec kubeconform -ignore-missing-schemas -summary {} + || echo "tip: 安装 kubeconform 做 schema 校验"
