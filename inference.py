import torch
import time
from PIL import Image
from getModels import model_details
from transform import transform_norm
import streamlit as st
import config

# Reverse the dictionary to map indices to class names
index_to_class = config.INV_LABELS_CLASS


def inference(cnnmodel,image_path):
    
    if(cnnmodel[1] != None):
       
        image = Image.open(image_path).convert('RGB')
        
        cnnmodel[1].eval()
        input_tensor = transform_norm(image).unsqueeze(0)  # Add batch dimension
        
        # Measure inference time
        start_time = time.time()
        
        with torch.no_grad():
            output = cnnmodel[1](input_tensor)
            probs = torch.exp(output)
            # Get the predicted class index
            index = torch.argmax(output).item()
            
        end_time = time.time()
        inference_time = end_time - start_time
            
        predicted_class = index_to_class[index]
        predprob = round(probs[0][index].item(),2)
        if(predprob < 0.80) : predicted_class = 'None'
        
        st.markdown(f"🚀 Model: **{cnnmodel[0]}**")
        model_details(cnnmodel[1])
        st.markdown(f"🌱 Predicted Class: **{predicted_class}**")
        st.markdown(f"🎃 Accuracy: **{predprob:.2f}**")
        st.markdown(f"🌟 Inference Time: **{inference_time:.4f} seconds**")
            
    else:
        st.markdown(f"🚀 Model: **{cnnmodel[0]}**")
        st.markdown(f"☠️ No Model in Production..!!**")

      