import streamlit as st 
import warnings
from getModels import model_init
from modelCard import model_card
warnings.filterwarnings("ignore")

# UI configurations
st.set_page_config(page_title="ambideXtrous",
                   page_icon=":bridge_at_night:",
                   layout="centered")

st.title("🚀:rainbow[Brand Logo Recognition] :sunglasses:")


@st.cache_resource
def load_model():
    if 'models' not in st.session_state:
        st.session_state.models = model_init()
        return st.session_state.models


models = load_model()
    
model_card(models)        