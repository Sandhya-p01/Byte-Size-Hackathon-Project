import streamlit as st
from moviepy.editor import VideoFileClip

st.set_page_config(page_title="PulsePoint AI")

st.title("🎬 PulsePoint AI")
st.write("Turn long videos into short reels")

uploaded_video = st.file_uploader("Upload a video", type=["mp4"])

if uploaded_video:
    with open("input_video.mp4", "wb") as f:
        f.write(uploaded_video.read())

    st.success("Video uploaded!")

    if st.button("Generate Reels"):
        video = VideoFileClip("input_video.mp4")

        clips = [(0, 30), (30, 60), (60, 90)]

        for i, (start, end) in enumerate(clips):
            clip = video.subclip(start, end)
            output = f"reel_{i+1}.mp4"
            clip.write_videofile(output)
            st.video(output)
