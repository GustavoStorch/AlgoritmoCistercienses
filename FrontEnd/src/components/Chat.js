import React, { useState } from "react";
import "../App.css";

const API_URL = "http://127.0.0.1:5000";

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [imageUrl, setImageUrl] = useState(null);
  const [auxImages, setAuxImages] = useState([]);

  const handleSendMessage = async () => {
    if (input.trim() !== "" && !isNaN(input)) {
      const numero = parseInt(input, 10);

      setMessages([{ sender: "Usuário", text: input }]);
      setInput("");

      try {
        const response = await fetch(`${API_URL}/gerar/${numero}`);
        const data = await response.json();

        if (response.ok && data.imagem_principal) {
          setImageUrl(`${API_URL}/imagem/${data.imagem_principal}?t=${Date.now()}`);
          setAuxImages(data.imagens_auxiliares.map(nome => `${API_URL}/imagem/${nome}`));

          setMessages([
            { sender: "Usuário", text: input },
            { sender: "Sistema" }
          ]);
        } else {
          setMessages([
            { sender: "Usuário", text: input },
            { sender: "Sistema", text: "Erro ao gerar a imagem." }
          ]);
        }
      } catch (error) {
        setMessages([
          { sender: "Usuário", text: input },
          { sender: "Sistema", text: "Falha ao conectar com a API." }
        ]);
      }
    } else {
      setMessages([{ sender: "Sistema", text: "Por favor, digite um número válido." }]);
    }
  };

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        const imageBase64 = reader.result;
        setMessages((prev) => [
          ...prev,
          {
            sender: "Usuário",
            text: "Imagem enviada:",
            image: imageBase64,
          },
        ]);
      };
      reader.readAsDataURL(file);
    }
  };
  

  return (
    <div id="chat-container">
      <div id="chat-header">Chat dos Números Cistercienses 🔢</div>
      <div id="chat-box">
        {messages.map((msg, index) => (
          <div key={index} className={`message-container ${msg.sender}`}>
            <div className="message-content">
              <i className={msg.sender === "Usuário" ? "fas fa-user" : "fas fa-robot"}></i>
              <b>{msg.sender}:</b> {msg.text}

              {msg.sender === "Sistema" && imageUrl && (
                <div className="image-container">
                  <img src={imageUrl} alt="Número Cisterciense" className="numero-imagem" />
                  <div className="image-actions">
                    <button onClick={() => window.open(imageUrl, "_blank")}>
                    <i className="fas fa-search-plus"></i>
                    </button>
                    <button
                      className="image-button"
                      onClick={async () => {
                        try {
                          const response = await fetch(imageUrl);
                          const blob = await response.blob();
                          const url = window.URL.createObjectURL(blob);
                          const link = document.createElement("a");
                          link.href = url;
                          link.download = `numero_cisterciense.png`;
                          document.body.appendChild(link);
                          link.click();
                          document.body.removeChild(link);
                          window.URL.revokeObjectURL(url);
                        } catch (error) {
                          alert("Erro ao baixar a imagem.");
                        }
                      }}
                    >
                      <i className="fas fa-download"></i>
                    </button>
                  </div>

                  {auxImages.length > 0 && (
                    <div className="aux-images">
                      {auxImages.map((imgUrl, i) => (
                        <img
                          key={i}
                          src={imgUrl}
                          alt={`Parte ${i + 1}`}
                          className="aux-imagem"
                          style={{ margin: "5px", height: "120px" }}
                        />
                      ))}
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      <div className="input-container">
        <input
          type="text"
          className="input-teclado"
          placeholder="Digite um número..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && handleSendMessage()}
        />

        <button className="clip-button" title="Enviar imagem">
          <label htmlFor="upload-image" style={{ cursor: "pointer", margin: 0 }}>
            <i className="fas fa-paperclip"></i>
          </label>
        </button>
        <input
          type="file"
          id="upload-image"
          style={{ display: "none" }}
          accept="image/*"
          onChange={(e) => handleImageUpload(e)}
        />

        <button className="btn-enviar" onClick={handleSendMessage}>
          <i className="fas fa-paper-plane"></i> Enviar
        </button>
      </div>
    </div>
  );
};

export default Chat;
