import { useEffect, useState } from "react";
import Hyperspeed from './components/Hyperspeed';

const API_URL = window.location.origin + "/api";

function App() {
  const [status, setStatus] = useState("Carregando...");

  useEffect(() => {
    fetch(`${API_URL}/health/ready`)
      .then((res) => {
        if (!res.ok) throw new Error("Backend não está pronto");
        return res.json();
      })
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("Erro ao conectar com backend"));
  }, []);

  return (
    <div style={{ width: "100vw", height: "100vh", position: "relative", backgroundColor: "black", overflow: "hidden" }}>
      
      <div style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%", zIndex: 0 }}>
        <Hyperspeed/>
      </div>

      <div style={{ 
        position: "relative",
        zIndex: 1,
        display: "flex",
        height: "100vh",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        fontFamily: "Arial",
        color: "white", // Texto branco para aparecer no fundo preto
      }}>
        <h1 style={{ textShadow: "2px 2px 10px rgba(0,0,0,0.8)" }}>Agenda App 🚀</h1>
        <h2>Status do Backend:</h2>
        <p style={{ 
          fontSize: "24px", 
          fontWeight: "bold", 
          color: status === "ok" ? "#00ff00" : "#ff4444",
          textShadow: "2px 2px 10px rgba(0,0,0,0.8)"
        }}>
          {status}
        </p>
      </div>
    </div>
  );
}

export default App;