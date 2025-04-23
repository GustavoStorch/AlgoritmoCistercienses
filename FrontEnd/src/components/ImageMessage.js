import React from "react";
import "../App.css";

const ImageMessage = ({ imageUrl, auxImages, numeroSolicitado }) => {
  const downloadImage = async () => {
    try {
      const response = await fetch(imageUrl);
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = `${numeroSolicitado}.png`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
    } catch (error) {
      alert("Erro ao baixar a imagem.");
    }
  };

  return (
    <div className="image-container">
      <img src={imageUrl} alt="Número Cisterciense" className="numero-imagem" />
      <div className="image-actions">
        <button onClick={() => window.open(imageUrl, "_blank")}>
          <i className="fas fa-search-plus"></i>
        </button>
        <button className="image-button" onClick={downloadImage}>
          <i className="fas fa-download"></i>
        </button>
      </div>
      {auxImages?.length > 0 && (
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
  );
};

export default ImageMessage;
