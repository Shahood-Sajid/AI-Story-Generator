import streamlit as st
import requests
import json
import markdown

def main():
    st.set_page_config(
        page_title="Story Generator",
        page_icon="📚",
        layout="centered"
    )
    
    st.title("📚 AI Story Generator")
    st.write("Enter your story requirements below and let AI create a captivating story for you!")
    
    # User input section
    user_prompt = st.text_area(
        "Describe the story you want:",
        height=150,
        placeholder="Example: Write a short adventure story set in a futuristic city with a teenage protagonist who discovers a hidden power..."
    )
    
    # Advanced options (collapsible)
    with st.expander("Advanced Options"):
        col1, col2 = st.columns(2)
        with col1:
            story_length = st.select_slider(
                "Story Length:",
                options=["Very Short", "Short", "Medium", "Long", "Very Long"],
                value="Medium"
            )
        with col2:
            story_genre = st.selectbox(
                "Genre:",
                ["Any", "Fantasy", "Sci-Fi", "Mystery", "Adventure", "Romance", "Horror", "Comedy"]
            )
    
    # Generate button
    if st.button("Generate Story", type="primary", use_container_width=True):
        if not user_prompt:
            st.error("Please enter a story description!")
        else:
            with st.spinner("Generating your story..."):
                try:
                    # Create full prompt with advanced options
                    full_prompt = f"{user_prompt}\n\nLength: {story_length}"
                    if story_genre != "Any":
                        full_prompt += f"\nGenre: {story_genre}"
                    
                    # Call backend API
                    response = requests.post(
                        "http://localhost:5000/StoryGenerator",
                        json={"message": full_prompt},
                        timeout=60
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        
                        # Display the story with styling
                        st.subheader("Your Generated Story")
                        story_container = st.container(height=400, border=True)
                        with story_container:
                            story_html = markdown.markdown(result["story"])
                            st.markdown(story_html, unsafe_allow_html=True)
                        
                        # Download button
                        st.download_button(
                            label="Download Story",
                            data=result["story"],
                            file_name="generated_story.md",
                            mime="text/markdown"
                        )
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"Failed to generate story: {e}")
    
    # Footer
    st.divider()
    st.caption("AI Story Generator powered by Gemini 2.0")

if __name__ == "__main__":
    main()