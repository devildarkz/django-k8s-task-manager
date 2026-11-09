import http from 'k6/http';
import { sleep, check } from 'k6';

// Restrict to a single virtual user and one iteration for a quick health check
export const options = {
  vus: 1,
  iterations: 1,
};

export default function () {
// Use your active Minikube tunnel URL
const url = 'http://127.0.0.1:51132/tasks';

const response = http.get(url);
  
  check(response, {
    'status is 200': (r) => r.status === 200,
    'API returns JSON array': (r) => r.body.startsWith('['),
  });

  sleep(1);
}