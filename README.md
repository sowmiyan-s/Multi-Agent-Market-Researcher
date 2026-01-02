# Multi-Agent Market Researcher

A sophisticated financial and market research system powered by **Mistral AI** and **CrewAI**. This application deploys a team of specialized AI agents to perform deep-dive analysis on any company using real-time search capabilities.

## 🚀 Overview

The **Multi-Agent Market Researcher** automates the complex process of gathering financial data and market trends. It leverages a sequential process where:
1.  **Financial Analyst**: Researches stock performance, key ratios, and earnings data.
2.  **Market Research Analyst**: Analyzes competitive landscapes and industry trends.
3.  **Reporting Analyst**: Synthesizes all findings into a professional, structured report.

## 🛠️ Technology Stack

*   **LLM**: Mistral AI (Medium/Large models)
*   **Orchestration**: CrewAI
*   **Search**: Serper.dev (Google Search API)
*   **UI**: Streamlit
*   **Framework**: LangChain

## 📥 Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/YOUR_USERNAME/Multi-Agent-Market-Researcher.git
    cd Multi-Agent-Market-Researcher
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**
    You need two API keys to run this system. Create a file named `.env` in the root of the project:
    
    *   **MISTRAL_API_KEY**: Get it from the [Mistral AI Console](https://console.mistral.ai/).
    *   **SERPER_API_KEY**: Get it from [Serper.dev](https://serper.dev/) (provides 2,500 free Google searches).

    **Your `.env` file should look like this:**
    ```env
    MISTRAL_API_KEY=your_actual_key_here
    SERPER_API_KEY=your_actual_key_here
    ```

## 🎮 Usage

1.  **Start the Application**
    ```bash
    streamlit run app.py
    ```

2.  **Generate a Report**
    *   Enter the name of any company (e.g., "NVIDIA").
    *   Monitor the **Agent Reasoning Logs** to see the "thought process" of each agent.
    *   Download the final plain-text report once the analysis is complete.

## 📋 Features

*   **Log Isolation**: Technical agent logs are separated from the final report for a clean reading experience.
*   **Search Integration**: Agents use the Serper tool to fetch real-world, real-time data.
*   **Minimalist Interface**: A distraction-free, professional UI focused solely on result generation.
*   **Downloadable Reports**: Export your strategic analysis in one click.

## 🤝 Credits

*   [CrewAI](https://www.crewai.com/) - Multi-agent orchestration.
*   [Mistral AI](https://mistral.ai/) - Powerful open-weights LLMs.
*   [Serper.dev](https://serper.dev/) - Fast Google Search API.

## 📄 License

This project is licensed under the MIT License.
