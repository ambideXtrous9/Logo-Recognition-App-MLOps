import streamlit as st 
from inference import inference



def model_card(models):
    
    imgpath = st.file_uploader("Upload an Image containing Brand Logo", type=["jpg", "jpeg", "png"])
    
    
    if imgpath is not None:
        
        st.image(imgpath, caption="Uploaded Image", use_container_width=True)

        col1, col2, col3, col4 = st.columns(4)

        # Card 1: Model Name
        with col1:
            inference(models[0],image_path=imgpath)
        

        # Card 2: Model Details
        with col2:
            inference(models[1],image_path=imgpath)
            

        # Card 3: Predicted Class
        with col3:
            inference(models[2],image_path=imgpath)
            

        # Card 4: Inference Time
        with col4:
            inference(models[3],image_path=imgpath)
    
    st.write("""
    ### 🚀 **Exploring Image Classification Models with Transfer Learning!**
    - 🆕 **Models Evaluated**: We've assessed the following state-of-the-art models using the Flick27 dataset:
        - **Xception** 🤖
        - **InceptionV3** 🌈
        - **MobileNetV2** 📱
        - **EfficientNet** ⚡

    ### 🔍 **Performance Aspects Compared**
    - **⚡ Inference Time**: How quickly each model makes predictions.
    - **📦 Model Size**: The storage requirements of each model.
    - **🔢 Number of Parameters**: The complexity and capacity of each model.
    - **📈 Accuracy**: How well each model performs in classifying images.
    - **🏷️ Predicted Class**: The class each model predicts for the input images.

    - 📚 **Understanding Trade-Offs**: These comparisons will help us understand the trade-offs between speed, efficiency, and accuracy for each model.

    💡 **You can train your own model on any dataset following the link below:**
    [Train Your Model](https://github.com/ambideXtrous9/Brand-Logo-Classification-using-TransferLearning-Flickr27/tree/main/Final%20Model)
    """)