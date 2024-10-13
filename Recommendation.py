import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def Recommendation():
        # Load the Excel file
    file_path = 'Potensi Kearifan Lokal.xlsx'
    df = pd.read_excel(file_path, sheet_name='Sheet1')

    # Combine relevant columns to create a corpus for the recommendation system
    df['combined_text'] = df['Kategori'] + " " + df['Nama'] + " " + df['Kearifan Lokal'] + " " + df['Konsep Sains']

    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer on the combined text
    tfidf_matrix = vectorizer.fit_transform(df['combined_text'])

    # Function to recommend P5 project themes based on a keyword search using AI (cosine similarity)
    def recommend_p5_theme_ai(keyword, df, tfidf_matrix):
        # Transform the input keyword into a vector
        keyword_vector = vectorizer.transform([keyword])
        
        # Compute cosine similarity between the keyword vector and the dataset's tfidf matrix
        cosine_sim = cosine_similarity(keyword_vector, tfidf_matrix)
        
        # Get the indices of the top 5 most similar entries
        top_indices = cosine_sim[0].argsort()[-5:][::-1]
        
        # Return the top 5 recommendations
        recommended_projects = df.iloc[top_indices][['Kategori', 'Nama', 'Kearifan Lokal', 'Konsep Sains', 'Potensi Tema Project P5']]
        return recommended_projects

    # Streamlit app
    st.title("AI-based P5 Project Theme Recommendation System")

    # Create dropdown options from unique values in 'Kategori', 'Nama', 'Kearifan Lokal', and 'Konsep Sains'
    category_options = df['Kategori'].unique().tolist()
    name_options = df['Nama'].unique().tolist()
    local_wisdom_options = df['Kearifan Lokal'].unique().tolist()
    science_concept_options = df['Konsep Sains'].unique().tolist()

    # Create dropdowns for user selection
    selected_category = st.selectbox("Select a Category:", category_options)
    #selected_name = st.selectbox("Select Local Wisdom Name:", name_options)
    #selected_local_wisdom = st.selectbox("Select Local Wisdom Type:", local_wisdom_options)
    #selected_science_concept = st.selectbox("Select Science Concept:", science_concept_options)

    # Combine the selected inputs into a single string for AI-based recommendation
    combined_input = f"{selected_category}"

    # Button to trigger recommendation
    if st.button('Recommend P5 Themes'):
        if combined_input:
            # Get AI-based recommendations
            result = recommend_p5_theme_ai(combined_input, df, tfidf_matrix)
            
            # Display the result in columns if any recommendations are found
            if not result.empty:
                st.subheader("Recommended P5 Project Themes")
                for idx, row in result.iterrows():
                    st.markdown("---")
                    col1, col2, col3, col4, col5 = st.columns(5)
                    
                    col1.write("**Kategori**")
                    col1.write(row['Kategori'])
                    
                    col2.write("**Nama**")
                    col2.write(row['Nama'])
                    
                    col3.write("**Kearifan Lokal**")
                    col3.write(row['Kearifan Lokal'])
                    
                    col4.write("**Konsep Sains**")
                    col4.write(row['Konsep Sains'])
                    
                    col5.write("**Potensi Tema Project P5**")
                    col5.write(row['Potensi Tema Project P5'])
            else:
                st.write("No themes found for the given keyword.")
        else:
            st.write("Please select all fields to get recommendations.")
# Panggil fungsi Recommendation
if __name__ == '__main__':
    Recommendation()