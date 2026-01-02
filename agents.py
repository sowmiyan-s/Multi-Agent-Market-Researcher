from crewai import Agent, LLM
import os
from dotenv import load_dotenv
from tools import tools_list

load_dotenv()

# Base LLM - Using Mistral Medium for balanced speed and reasoning
llm = LLM(
    model="mistral/mistral-medium-latest",
    api_key=os.environ.get("MISTRAL_API_KEY"),
    temperature=0.2
)

# Market Research Analyst
market_research_analyst = Agent(
    role="Market Research Analyst",
    goal="Provide insights about {company} through market analysis",
    verbose=True,
    memory=False,
    backstory=(
        "You are an expert Market Research Analyst. Your goal is to find market trends, "
        "competitor data, and consumer insights for {company}. "
        "When using the search tool, ALWAYS provide a simple string as the search query."
    ),
    tools=tools_list,
    llm=llm,
    allow_delegation=False
)

# Financial Analyst
financial_analyst = Agent(
    role="Financial Analyst",
    goal="Provide comprehensive financial insights about {company}",
    verbose=True,
    memory=False,
    backstory=(
        "You are a Senior Financial Analyst. You specialize in analyzing stock performance, "
        "financial ratios, and earnings reports for {company}. "
        "When using the search tool, ALWAYS provide a simple string as the search query."
    ),
    tools=tools_list,
    llm=llm,
    allow_delegation=False
)

# Reporting Analyst
reporting_analyst = Agent(
    role="Reporting Analyst",
    goal="Create detailed reports based on financial and market research for {company}",
    verbose=True,
    memory=False,
    backstory=(
        "You are a professional Technical Writer and Reporting Analyst. "
        "Your job is to take raw financial and market data and turn it into a polished report. "
        "When using the search tool, ALWAYS provide a simple string as the search query."
    ),
    tools=tools_list,
    llm=llm,
    allow_delegation=False
)
