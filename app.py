import streamlit as st
import re
import sys
import logging
import warnings

# Suppress Streamlit threading warnings and Pydantic serialization noise
logging.getLogger('streamlit').setLevel(logging.ERROR)
warnings.filterwarnings("ignore", message="missing ScriptRunContext")
warnings.filterwarnings("ignore", message="serialized value may not be as expected")
from crewai import Crew, Process
from agents import reporting_analyst, market_research_analyst, financial_analyst
from tasks import reporting_analysis, market_analysis, financial_analysis

# Handle different Streamlit versions for ScriptRunContext
try:
    from streamlit.runtime.scriptrunner import get_script_run_ctx as get_script_run_context
    from streamlit.runtime.scriptrunner import add_script_run_ctx as add_script_run_context
except ImportError:
    try:
        from streamlit.runtime.scriptrunner import get_script_run_context, add_script_run_context
    except ImportError:
        get_script_run_context = lambda: None
        add_script_run_context = lambda ctx: None

# Minimalist CSS
st.set_page_config(page_title="Market Researcher", page_icon="None", layout="wide")

st.markdown("""
    <style>
    .stMarkdown, .stText {
        font-family: 'Inter', sans-serif;
    }
    .report-container {
        border-top: 1px solid #ddd;
        padding-top: 20px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Stream sys output to a dedicated console box
class StreamToContainer:
    def __init__(self, container):
        self.container = container
        self.buffer = []
        self.log_area = self.container.empty()
        self.full_log = ""
        self.context = get_script_run_context()
    
    def write(self, data):
        if self.context:
            add_script_run_context(self.context)
        
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)
        if cleaned_data.strip():
            self.full_log += cleaned_data
            # Display logs in a code block for better formatting
            self.log_area.code(self.full_log, language="bash")

# Streamlit UI
st.title("Multi-Agent Market Researcher")

company = st.text_input("Enter Company Name", placeholder="e.g. NVIDIA, Tesla, Apple")
submitted = st.button("Generate Report", use_container_width=True)

if submitted and company:
    log_expander = st.expander("Agent Reasoning Logs", expanded=True)
    with log_expander:
        console_container = st.container()
        
    with st.status("Agents are working...", expanded=True) as status:
        sys.stdout = StreamToContainer(console_container)
        
        try:
            crew = Crew(
                agents=[financial_analyst, market_research_analyst, reporting_analyst],
                tasks=[financial_analysis, market_analysis, reporting_analysis],
                process=Process.sequential,
                verbose=True
            )
            result = crew.kickoff(inputs={"company": company})
            final_output = str(result)
            
            status.update(label="Analysis Complete", state="complete", expanded=False)
            log_expander.update(expanded=False)
        except Exception as e:
            status.update(label="Error Occurred", state="error")
            st.error(f"Error: {e}")
            final_output = None

    if final_output:
        st.markdown("---")
        st.markdown(f"## Research Report: {company}")
        st.markdown(final_output)
            
        st.download_button(
            label="Download Report",
            data=final_output,
            file_name=f"{company}_Report.txt",
            mime="text/plain"
        )
elif submitted and not company:
    st.warning("Please enter a company name first.")
