
import React, { useState, useRef, useEffect } from 'react';
import { ChatMessage } from '../types';
import { runChat } from '../services/geminiService';

const Chatbot: React.FC = () => {
  const [history, setHistory] = useState<ChatMessage[]>([
    { role: 'model', text: 'Welcome, Bilel. I am online and ready to assist. How can I help you today?' },
  ]);
  const [input, setInput] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const chatContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }
  }, [history]);

  const handleSendMessage = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage: ChatMessage = { role: 'user', text: input.trim() };
    setHistory(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const responseText = await runChat(input.trim(), history);
      const modelMessage: ChatMessage = { role: 'model', text: responseText };
      setHistory(prev => [...prev, modelMessage]);
    } catch (error) {
      const errorMessage: ChatMessage = { role: 'model', text: 'Sorry, an error occurred. Please check the console.' };
      setHistory(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      handleSendMessage();
    }
  };

  return (
    <div className="flex flex-col h-full bg-gray-950 border border-gray-700/50 rounded-lg overflow-hidden">
      <div className="p-4 border-b border-gray-700/50">
        <h3 className="font-semibold text-lg text-white">AI Assistant</h3>
        <p className="text-sm text-gray-400">System Status: <span className="text-green-400">Online</span></p>
      </div>
      <div ref={chatContainerRef} className="flex-1 p-4 space-y-4 overflow-y-auto">
        {history.map((msg, index) => (
          <div key={index} className={`flex items-start gap-3 ${msg.role === 'user' ? 'justify-end' : ''}`}>
            {msg.role === 'model' && (
              <div className="w-8 h-8 bg-indigo-600 rounded-full flex-shrink-0 flex items-center justify-center font-bold text-sm">AI</div>
            )}
            <div className={`max-w-md p-3 rounded-lg ${msg.role === 'user' ? 'bg-indigo-600 text-white' : 'bg-gray-800 text-gray-200'}`}>
              <p className="text-sm whitespace-pre-wrap">{msg.text}</p>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex items-start gap-3">
            <div className="w-8 h-8 bg-indigo-600 rounded-full flex-shrink-0 flex items-center justify-center font-bold text-sm">AI</div>
            <div className="max-w-md p-3 rounded-lg bg-gray-800 text-gray-200">
              <div className="flex items-center space-x-1">
                <span className="text-sm">Thinking</span>
                <div className="h-2 w-2 bg-gray-400 rounded-full animate-bounce [animation-delay:-0.3s]"></div>
                <div className="h-2 w-2 bg-gray-400 rounded-full animate-bounce [animation-delay:-0.15s]"></div>
                <div className="h-2 w-2 bg-gray-400 rounded-full animate-bounce"></div>
              </div>
            </div>
          </div>
        )}
      </div>
      <div className="p-4 border-t border-gray-700/50">
        <div className="flex items-center bg-gray-800 rounded-lg">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask me to code, query, or analyze..."
            className="flex-1 bg-transparent p-3 text-gray-200 placeholder-gray-500 focus:outline-none"
            disabled={isLoading}
          />
          <button
            onClick={handleSendMessage}
            disabled={isLoading}
            className="p-3 text-gray-400 hover:text-white disabled:text-gray-600 disabled:cursor-not-allowed transition-colors"
          >
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chatbot;
