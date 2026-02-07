import streamlit as st
from summarizer import generate_summary

st.title("📞 Call Summary Generator")

transcript = st.text_area("Paste call transcript here")

if st.button("Generate Summary"):
    if transcript.strip():
        output = generate_summary(transcript)

        st.subheader("Summary")
        st.write(output["summary"])

        st.subheader("Key Points")
        for p in output["key_points"]:
            st.markdown(f"- {p}")

        st.subheader("Action Items")
        for a in output["action_items"]:
            st.markdown(f"- {a}")
    else:
        st.error("Please paste transcript")
