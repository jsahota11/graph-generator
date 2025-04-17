async function sendData() {
  const response = await fetch('/api/data', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: "Hello from frontend!" })
  });

  const result = await response.json();
  console.log(result);
}
