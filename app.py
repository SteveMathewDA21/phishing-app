import streamlit as st
import pandas as pd

# Sample dataframe
data = pd.read_excel('Metrics table.xlsx')
df = pd.DataFrame(data)

def display_content(dataset, model):
    st.write(f"Selected Dataset: {dataset}")
    st.write(f"Selected Model: {model}")


    if dataset == 'Mendeley' and model == 'FNN':
        st.image("Images/Mendeley_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Mendeley+FNN_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Mendeley+FNN_ROC.png", caption='ROC Curve', use_column_width=True)
    elif dataset == 'Mendeley' and model == 'Perceptron':
        st.image("Images/Mendeley_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Mendeley+Perceptron_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Mendeley+Perceptron_ROC.png", caption='ROC Curve', use_column_width=True)
    elif dataset == 'Mendeley' and model == 'Perceptron+SHAP':
        st.image("Images/Mendeley_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Mendeley+Perceptron+SHAP_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Mendeley+Perceptron+SHAP_Features.png", caption='Important Features', use_column_width=True)
        st.image("Images/Mendeley+Perceptron+SHAP_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Mendeley' and model == 'KNN':
        st.image("Images/Mendeley_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Mendeley+KNN_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Mendeley+KNN_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Mendeley' and model == "Naïve Bayes":
        st.image("Images/Mendeley_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Mendeley+NB_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Mendeley+NB_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Mendeley' and model == "Logistic Regression":
        st.image("Images/Mendeley_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Mendeley+LR_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Mendeley+LR_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Mendeley' and model == "Decision Tree":
        st.image("Images/Mendeley_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Mendeley+DT_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Mendeley+DT_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Mendeley' and model == "Decision Tree+SHAP":
        st.image("Images/Mendeley_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Mendeley+DT+SHAP_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Mendeley+DT+SHAP_Features.png", caption='Important Features', use_column_width=True)
        st.image("Images/Mendeley+DT+SHAP_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Kaggle' and model == 'FNN':
        st.image("Images/Kaggle_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Kaggle+FNN_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Kaggle+FNN_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Kaggle' and model == 'Perceptron':
        st.image("Images/Kaggle_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Kaggle+Perceptron_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Kaggle+Perceptron_ROC.png", caption='ROC Curve', use_column_width=True)
    elif dataset == 'Kaggle' and model == 'Perceptron+SHAP':
        st.image("Images/Kaggle_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Kaggle+Perceptron+SHAP_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Kaggle+Perceptron+SHAP_Features.png", caption='Important Features', use_column_width=True)
        st.image("Images/Kaggle+Perceptron+SHAP_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Kaggle' and model == 'KNN':
        st.image("Images/Kaggle_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Kaggle+KNN_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Kaggle+KNN_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Kaggle' and model == "Naïve Bayes":
        st.image("Images/Kaggle_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Kaggle+NB_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Kaggle+NB_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Kaggle' and model == "Logistic Regression":
        st.image("Images/Kaggle_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Kaggle+LR_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Kaggle+LR_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Kaggle' and model == "Decision Tree":
        st.image("Images/Kaggle_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Kaggle+DT_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Kaggle+DT_ROC.png", caption='ROC Curve', use_column_width=True)

    elif dataset == 'Kaggle' and model == "Decision Tree+SHAP":
        st.image("Images/Kaggle_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Kaggle+DT+SHAP_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Kaggle+DT+SHAP_Features.png", caption='Important Features', use_column_width=True)
        st.image("Images/Kaggle+DT+SHAP_ROC.png", caption='ROC Curve', use_column_width=True)

    #
    elif dataset == 'Kaggle' and model == "SHAP (Kaggle-specific)":
        st.image("Images/Kaggle_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Kaggle+SHAP_Waterfall.png", use_column_width=True)
        st.image("Images/Kaggle+SHAP_Waterfall(2).png", use_column_width=True)
        st.image("Images/Kaggle+SHAP_Waterfall(3).png", use_column_width=True)
        st.image("Images/Kaggle+SHAP_Waterfall(4).png", use_column_width=True)
        st.image("Images/Kaggle+SHAP_Mean.png", caption='Mean Values', use_column_width=True)
        st.image("Images/Kaggle+SHAP_Values.png", caption='SHAP Values', use_column_width=True)
        st.image("Images/Kaggle+SHAP_BeeswarmValues.png", caption='Beeswarm Plot', use_column_width=True)
        st.image("Images/Kaggle+SHAP_CM.png", caption='Confusion Matrix', use_column_width=True)

    elif dataset == 'Kaggle' and model == "LIME (Kaggle-specific)":
        st.image("Images/Kaggle_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Prob.jpeg", caption='Probability of each class label', use_column_width=True)
        st.image("Images/Kaggle+LIME_CM.png", caption='Confusion Matrix', use_column_width=True)
        st.image("Images/Kaggle+LIME(1).png", caption='Local Explanation', use_column_width=True)

    elif dataset == 'Mendeley' and model == "EBM (Mendeley-specific)":
        st.image("Images/Mendeley_dist.png", caption='Distribution of Target Values', use_column_width=True)
        st.image("Images/Mendeley+EBM_CM.png", caption='Confusion Matrix', use_column_width=True)
    

st.title('Prediction of Phishing Attacks using XAI: Results')
st.write('### CSE3502 J Component by 20MIS0047, 20MIS0054 and 20MIS0137')
# Display the dataframe as a table
st.write('## Result Summary')
st.write(df)

st.write('### Select dataset and model to view more details')

# Dropdown menus for dataset and model selection
dataset = st.selectbox('Dataset', ['Mendeley', 'Kaggle'])
model = st.selectbox('Model', ['SHAP (Kaggle-specific)','EBM (Mendeley-specific)','LIME (Kaggle-specific)','FNN', 'Perceptron', 'Perceptron+SHAP', 'KNN', 'Naïve Bayes', 'Logistic Regression', 'Decision Tree', 'Decision Tree+SHAP'])

if st.button('Submit'):
    # Display text and image based on selected options
    display_content(dataset, model)
