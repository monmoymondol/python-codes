import React from "react";
import WebcamStream from "./components/WebcamStream";

export default function App() {
  return (
    <div className="app">
      <header>
        <h1>Live Face Recognition</h1>
      </header>
      <main>
        <WebcamStream
          apiEndpoint="http://localhost:5000/recognize"
          captureInterval={500}
          sendSize={{ width: 320, height: 240 }}
        />
      </main>
      <footer>
        <small>Camera feed is processed locally and sent to the recognition API.</small>
      </footer>
    </div>
  );
}
