// API Service for connecting frontend to backend

// Base API URL - defaults to localhost:8000 during development
// For Docusaurus, environment variables are processed at build time
const API_BASE_URL =
  typeof process.env.REACT_APP_API_BASE_URL !== 'undefined'
    ? process.env.REACT_APP_API_BASE_URL
    : 'http://localhost:8000/api/v1';

// Common headers for API requests
const getHeaders = (): HeadersInit => ({
  'Content-Type': 'application/json',
});

// Generic API request function
const apiRequest = async <T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> => {
  try {
    const url = `${API_BASE_URL}${endpoint}`;
    const response = await fetch(url, {
      headers: getHeaders(),
      ...options,
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error(`API request failed for ${endpoint}:`, error);
    throw error;
  }
};

// API service class with methods for different endpoints
class ApiService {
  // Books API methods
  async getAllBooks(skip: number = 0, limit: number = 100) {
    return apiRequest(`/books?skip=${skip}&limit=${limit}`);
  }

  async getBookById(id: string) {
    return apiRequest(`/books/${id}`);
  }

  async createBook(bookData: { title: string; author: string; content?: string }) {
    return apiRequest('/books', {
      method: 'POST',
      body: JSON.stringify(bookData),
    });
  }

  async updateBook(id: string, bookData: Partial<{ title: string; author: string; content: string }>) {
    return apiRequest(`/books/${id}`, {
      method: 'PUT',
      body: JSON.stringify(bookData),
    });
  }

  async deleteBook(id: string) {
    return apiRequest(`/books/${id}`, {
      method: 'DELETE',
    });
  }

  // AI API methods
  async generateSummary(text: string, options: {
    model?: string;
    length?: string;
    format?: string;
    extractiveness?: string;
    temperature?: number;
  } = {}) {
    return apiRequest('/ai/summarize', {
      method: 'POST',
      body: JSON.stringify({
        text,
        ...options
      }),
    });
  }

  async generateEmbeddings(texts: string[], options: {
    model?: string;
    input_type?: string;
  } = {}) {
    return apiRequest('/ai/embeddings', {
      method: 'POST',
      body: JSON.stringify({
        texts,
        ...options
      }),
    });
  }

  async generateText(prompt: string, options: {
    model?: string;
    max_tokens?: number;
    temperature?: number;
  } = {}) {
    return apiRequest('/ai/generate', {
      method: 'POST',
      body: JSON.stringify({
        prompt,
        ...options
      }),
    });
  }

  // Health check
  async healthCheck() {
    return apiRequest('/health');
  }
}

// Export singleton instance
export const apiService = new ApiService();

// Export types if needed
export type {
  apiRequest
};