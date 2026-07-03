#!/usr/bin/env bash
# 引擎层基准: 绕过网关直打 router, 得到 TTFT/TPOT 与容量拐点
# 用法: PORT_FORWARD 先开 -> BASE=http://127.0.0.1:30080 bash run-vllm-bench.sh
set -euo pipefail
BASE=${BASE:-http://127.0.0.1:30080}
MODEL=${MODEL:-facebook/opt-125m}   # TODO(你来改)
for C in 1 8 16 32 64; do
  echo "== concurrency $C =="
  vllm bench serve --backend openai-chat --base-url "$BASE" \
    --model "$MODEL" --num-prompts $((C*10)) --max-concurrency "$C" \
    --random-input-len 512 --random-output-len 128
done
# 产出物: 每档并发的 TTFT P50/P99、吞吐 -> 填进 docs/ 压测报告, 反推 KEDA threshold
