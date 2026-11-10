import http from 'k6/http';
import { sleep, check } from 'k6';

// Configured for Deliverable 3 requirements: 500 VUs for 60 seconds
export const options = {
  vus: 500,
  duration: '60s',
};

export default function () {
  // Target the active kubectl port-forward tunnel on port 3000
  const url = 'http://127.0.0.1:3000/tasks/';

  const response = http.get(url);

  check(response, {
    'status is 200': (r) => r.status === 200,
    'API returns JSON array': (r) => r.body.startsWith('['),
  });

  sleep(1);
}