import React from "react";
import Chat from "./components/Chat";
import logo from "../src/resources/catolica.png";

function App() {
  return (
    <div className="App">
      <Chat />
      <img src={logo} alt="Católica SC" className="logo"/>
    </div>
  );
}

export default App;
