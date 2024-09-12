import streamlit as st
import tempfile
import os
from faster_whisper import WhisperModel

def get_model_name(base_model, english_only):
    if base_model == "large-v3" or not english_only:
        return base_model
    return f"{base_model}.en"

def transcribe_audio(file_path, output_type, model_size, english_only, device, compute_type):
    model_name = get_model_name(model_size, english_only)
    model = WhisperModel(model_name, device=device, compute_type=compute_type)
    segments, _ = model.transcribe(file_path, language="en" if english_only else None)
    
    if output_type == "text":
        return "\n".join([segment.text for segment in segments])
    elif output_type == "srt":
        srt_content = ""
        for i, segment in enumerate(segments, start=1):
            srt_content += f"{i}\n"
            srt_content += f"{format_time(segment.start)} --> {format_time(segment.end)}\n"
            srt_content += f"{segment.text}\n\n"
        return srt_content

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

st.title("Audio/Video Transcription App")

uploaded_file = st.file_uploader("Choose an audio or video file", type=["mp3", "wav", "mp4", "avi", "mov"])
output_type = st.selectbox("Select output type", ["text", "srt"])

col1, col2 = st.columns(2)

with col1:
    model_size = st.selectbox(
        "Select model size", 
        ["tiny", "base", "small", "medium", "large-v3"]
    )
    english_only = st.checkbox("English only")

with col2:
    device = st.selectbox("Select device", ["cpu", "cuda"])
    if device == "cuda":
        compute_type = st.selectbox("Select compute type", ["float16", "int8_float16"])
    else:
        compute_type = "int8"
        st.text("Compute type: int8 (CPU)")

if st.button("Run Transcription"):
    if uploaded_file is not None:
        with st.spinner("Transcribing..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix="." + uploaded_file.name.split(".")[-1]) as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file_path = temp_file.name

            result = transcribe_audio(temp_file_path, output_type, model_size, english_only, device, compute_type)

            if output_type == "text":
                st.text_area("Transcription Result", result, height=300)
            elif output_type == "srt":
                st.download_button(
                    label="Download SRT file",
                    data=result,
                    file_name="transcription.srt",
                    mime="text/srt"
                )

            os.unlink(temp_file_path)
    else:
        st.error("Please upload a file first.")

# Display the actual model name being used
actual_model_name = get_model_name(model_size, english_only)
st.info(f"Using model: {actual_model_name}")