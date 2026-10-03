async function post(url, data) {
  const res = await fetch(url, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  });
  return res.json();
}

async function chat() {
  const output = document.getElementById("output");
  output.textContent = "Denke...";
  const data = await post("/api/chat", {
    message: document.getElementById("message").value
  });
  output.textContent = data.reply || data.error;
}

async function quantum() {
  const output = document.getElementById("qoutput");
  const data = await post("/api/quantum", {
    input: document.getElementById("qinput").value
  });
  output.textContent = JSON.stringify(data, null, 2);
}
