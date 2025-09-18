
import { GoogleGenAI, GenerateContentResponse } from "@google/genai";
import { ChatMessage } from '../types';
import { SYSTEM_PROMPT } from '../constants';

const API_KEY = process.env.API_KEY;

if (!API_KEY) {
  console.warn("API_KEY not found. AI Chatbot will be disabled.");
}

const ai = new GoogleGenAI({ apiKey: API_KEY! });

export const runChat = async (prompt: string, history: ChatMessage[]): Promise<string> => {
  if (!API_KEY) {
    return "I am currently offline. The API key is missing.";
  }

  try {
    const chatHistory = history.map(msg => ({
      role: msg.role,
      parts: [{ text: msg.text }]
    }));

    const response: GenerateContentResponse = await ai.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: [
            ...chatHistory,
            { role: 'user', parts: [{text: prompt}] }
        ],
        config: {
            systemInstruction: SYSTEM_PROMPT,
        }
    });

    const text = response.text;
    if (!text) {
        return "I couldn't generate a response. Please try again.";
    }
    return text;
  } catch (error) {
    console.error("Gemini API error:", error);
    return `An error occurred while communicating with the AI. Details: ${error instanceof Error ? error.message : 'Unknown error'}`;
  }
};
