import { useState } from "react";
import ChatWindow from "./components/ChatWindow";
import Sidebar from "./components/Sidebar";
import "./App.css";

export default function App() {
  const [topK, setTopK] = useState(5);
  const [chatHistory, setChatHistory] = useState([]);

  const clearChat = () => {
    setChatHistory([]);
  };

  return (
    <div className="app-container">
      <Sidebar topK={topK} setTopK={setTopK} clearChat={clearChat} />
      <main className="main-content">
        <header className="header">
          <h1>🏥 Medical Research Assistant</h1>
          <p>Answers grounded in medical research papers</p>
        </header>
        <ChatWindow
          topK={topK}
          chatHistory={chatHistory}
          setChatHistory={setChatHistory}
        />
      </main>
    </div>
  );
}