document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const form = document.getElementById("chat-form");
    const input = document.getElementById("user-input");
    let messages = [];

    function appendMessage(role, text) {
        const msgDiv = document.createElement("div");
        msgDiv.className = `message ${role}`;
        const textSpan = document.createElement("span");
        textSpan.className = "text";
        textSpan.textContent = text;
        msgDiv.appendChild(textSpan);
        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const userText = input.value.trim();
        if (!userText) return;
        appendMessage("user", userText);
        messages.push({ role: "user", content: userText });
        input.value = "";

        try {
            const response = await fetch("/chat/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ messages }),
            });
            const data = await response.json();
            if (data.reply) {
                appendMessage("assistant", data.reply);
                messages.push({ role: "assistant", content: data.reply });
            } else {
                appendMessage("assistant", "Error: " + data.error);
            }
        } catch (err) {
            appendMessage("assistant", "Network error");
        }
    });
});
