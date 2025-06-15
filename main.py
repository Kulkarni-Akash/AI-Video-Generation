import streamlit as st
from src.video_generator import VideoGeneration

st.set_page_config(
    page_title="GenVids",
)

st.title("GenVids")
st.markdown("GenVids is a video generation app that creates videos from text prompts.")

text_prompt=st.text_input("Enter your text prompt here:", placeholder="e.g. A cat playing with a ball")

st.button("Generate Video", on_click=lambda: st.write("Video generation started..."))

if text_prompt:
    with st.spinner("Generating video...", show_time=True):
        video_gen=VideoGeneration()
        job_id = video_gen.video_generation_job(text_prompt)
        status, status_response = video_gen.job_status(job_id)
        video_gen.get_video(status, status_response)

    st.video("output/output.mp4", format="video/mp4", start_time=0)
    st.toast("Video generation completed!", icon="✅")