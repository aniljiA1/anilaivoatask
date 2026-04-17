import { useState } from "react";
import axios from "axios";

export default function ChatInterface() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    if (!message) return;

    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/chat`, {
        message: message,
      });

      setChat([...chat, { user: message, bot: res.data.reply }]);

      setMessage("");
    } catch (err) {
      console.error(err);
      setChat([
        ...chat,
        { user: message, bot: "Error: Unable to reach server" },
      ]);
    }
  };

  return (
    <div>
      <h3 className="text-xl font-semibold mb-3">AI Chat</h3>

      <div className="flex gap-2 mb-3">
        <input
          className="flex-1 p-2 border rounded-lg"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type message..."
        />

        <button
          onClick={sendMessage}
          className="bg-green-500 text-white px-4 rounded-lg hover:bg-green-600"
        >
          Send
        </button>
      </div>

      <div className="space-y-3 max-h-80 overflow-y-auto">
        {chat.map((c, index) => (
          <div key={index}>
            <p className="text-blue-600 font-medium">You: {c.user}</p>
            <p className="text-gray-700">AI: {c.bot}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
