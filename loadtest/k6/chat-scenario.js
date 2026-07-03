// [压测|E类] 端到端: 走网关(鉴权+限流+路由全链路)。kind循环打mock同样有效
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  scenarios: {
    ramp: {
      executor: 'ramping-vus',
      startVUs: 1,
      stages: [
        { duration: '__TODO__', target: __TODO__ },  // 爬坡: 到"预估安全并发"
        { duration: '__TODO__', target: __TODO__ },  // 稳态: 观测窗口, 盯Grafana
        { duration: '__TODO__', target: __TODO__ },  // 突发: 设为几倍才能触发KEDA+429?
        { duration: '2m', target: 0 },
      ],
    },
  },
  thresholds: {
    http_req_failed: ['rate<__TODO__'],   // 你的可用性目标; 注意429在check里不算失败
  },
};

const URL = __ENV.URL || '__TODO__';       // 走网关的完整URL
const KEY = __ENV.API_KEY || '__TODO__';

export default function () {
  const res = http.post(URL, JSON.stringify({
    messages: [{ role: 'user', content: '用一句话解释PagedAttention' }],
    max_tokens: __TODO__,                  // 输出长度直接决定压测强度, 依据什么定?
  }), { headers: { 'Content-Type': 'application/json', 'x-api-key': KEY } });
  check(res, {
    'status 2xx/429': (r) => r.status === 200 || r.status === 429,
    'has usage': (r) => r.status !== 200 || !!r.json('usage'),
  });
}
