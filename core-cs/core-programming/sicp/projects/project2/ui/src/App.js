import React, { useState, useEffect, useRef } from "react";

const App = () => {
  const [message, setMessage] = useState("");
  const [username, setUsername] = useState("");
  const [receivedMessages, setReceivedMessages] = useState([]);
  const [isConnected, setIsConnected] = useState(false);
  const [isDarkMode, setIsDarkMode] = useState(false); 
  const socketRef = useRef(null);
  const messagesEndRef = useRef(null); // Ref for auto-scrolling

  useEffect(() => {
    socketRef.current = new WebSocket("ws://localhost:8080");
    socketRef.current.onopen = () => {
      console.log("Connected to WebSocket server");
      setIsConnected(true);
    };
    socketRef.current.onmessage = (event) => {
      console.log("Message from server:", event.data);
      setReceivedMessages((prevMessages) => [...prevMessages, event.data]); 
    };
  }, []);

  // Auto-scroll whenever new messages are received
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [receivedMessages]);

  const sendMessage = () => {
    if (isConnected && message.trim() !== "") {
      socketRef.current.send(`${username}: ${message}`);
      setMessage("");
    }
  };

  const handleInit = () => {
    setUsername(message);
    setMessage(""); 
  };

  const handleConnect = () => {
    if (!isConnected) {
      socketRef.current = new WebSocket("ws://localhost:8080");
      socketRef.current.onopen = () => {
        console.log("Reconnected to WebSocket server");
        setIsConnected(true);
      };
      socketRef.current.onmessage = (event) => {
        console.log("Message from server:", event.data);
        setReceivedMessages((prevMessages) => [...prevMessages, event.data]);
      };
    }
  };

  const handleDisconnect = () => {
    if (socketRef.current) {
      socketRef.current.close();
      setIsConnected(false);
      console.log("Disconnected from the server");
    }
  };

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
  };

  // Apply dark mode to the whole page body
  useEffect(() => {
    if (isDarkMode) {
      document.body.classList.add("dark");
    } else {
      document.body.classList.remove("dark");
    }
  }, [isDarkMode]);

  return (
    <div className={`container ${isDarkMode ? "dark" : ""}`}>
      <button className="dark-mode-toggle" onClick={toggleDarkMode}>
        Toggle Dark Mode
      </button>
      {!username ? (
        <div className="center">
          <div>Welcome to Chattato</div>
          <input
            className="my-input"
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleInit()}
            placeholder="Enter your username"
          />
          <button onClick={handleInit}>Ok</button>
        </div>
      ) : (
        <>
          <div className={`status-bar ${!isConnected ? "offline" : ""}`}>
            Status: {isConnected ? "Connected" : "Disconnected"}
          </div>
          <div className="input-area">
            <input
              type="text"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              placeholder="Type a message"
            />
            <button onClick={sendMessage}>Send</button>
            <button onClick={handleConnect} disabled={isConnected}>
              Connect
            </button>
            <button onClick={handleDisconnect} disabled={!isConnected}>
              Disconnect
            </button>
          </div>
          <div className="messages">
            <ul>
              {receivedMessages.map((msg, index) => (
                <li key={index}>{msg}</li>
              ))}
            </ul>
            <div ref={messagesEndRef} />
          </div>
        </>
      )}
    </div>
  );
};

export default App;
