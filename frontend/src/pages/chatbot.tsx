import React from 'react';
import Layout from '@theme/Layout';
import ChatWidget from '@site/src/components/ChatBot';

function ChatBotPage(): React.ReactElement {
  return (
    <Layout
      title="AI Assistant"
      description="Your AI-powered robotics and physical AI assistant">
      <div style={{ padding: '2rem', minHeight: '80vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <div style={{ maxWidth: '800px', width: '100%' }}>
          <h1>AI Assistant for Robotics & Physical AI</h1>
          <p>Welcome to your AI assistant. This tool can help you with questions about robotics, humanoid control, simulation environments, and physical AI concepts. Try asking about:</p>
          <ul>
            <li>How to implement robot control algorithms</li>
            <li>Simulation environments for robotics</li>
            <li>Embodied AI principles</li>
            <li>NVIDIA Isaac Sim techniques</li>
            <li>ROS 2 integration</li>
          </ul>
          <div style={{ marginTop: '2rem', height: '500px' }}>
            <ChatWidget />
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default ChatBotPage;