import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("Carregando...");

  useEffect(() => {
    fetch("http://localhost:30007/health/ready")
      .then((res) => {
        if (!res.ok) throw new Error("Backend não está pronto");
        return res.json();
      })
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("Erro ao conectar com backend"));
  }, []);

  return (
    <div style={{ 
      display: "flex",
      height: "100vh",
      justifyContent: "center",
      alignItems: "center",
      flexDirection: "column",
      fontFamily: "Arial"
    }}>
      <h1>Agenda App 🚀</h1>
      <h2>Status do Backend:</h2>
      <p style={{ fontSize: "24px", fontWeight: "bold" }}>
        {status}
      </p>
    </div>
  );
}

export default App;
