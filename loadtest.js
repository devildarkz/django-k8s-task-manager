import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 500 }, // Ramp up to 500 virtual users over 30 seconds
    { duration: '30s', target: 500 }, // Stay at 500 users
    { duration: '30s', target: 0 },   // Ramp down to 0 users
  ],
  noConnectionReuse: false,
};

export default function () {
  const url = 'http://127.0.0.1:3000/tasks';

  // Test READ (Get all tasks)
  const resGet = http.get(url);
  check(resGet, { 'get status is 200': (r) => r.status === 200 });

  // Test CREATE (Add a new task)
  const payload = JSON.stringify({ title: 'Load Test Task' });
  const params = { headers: { 'Content-Type': 'application/json' } };
  const resPost = http.post(url, payload, params);
  check(resPost, { 'post status is 200': (r) => r.status === 200 });

  sleep(1); // Wait 1 second between requests per user
}