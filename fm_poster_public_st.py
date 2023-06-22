"""
Purpose:
    BuildOn Poster
"""

import os

# 3rd party imports
import numpy as np
import requests
import streamlit as st
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth

IMAGE_API = os.environ["IMAGE_API"]
TEXT_API = os.environ["TEXT_API"]

st.set_page_config(layout="wide")


def gen_summary(text):
    data = {"text": text}

    auth_url = TEXT_API.replace("https://", "").replace("/", "")

    auth = BotoAWSRequestsAuth(
        aws_host=auth_url,
        aws_region="us-east-1",  # HARDCODED to us-east-1
        aws_service="lambda",
    )

    headers = {
        "Content-Type": "application/json",
    }

    resp = requests.post(TEXT_API, json=data, headers=headers, auth=auth)
    # print(resp.json())
    return resp.json()["text"]


def gen_image(text):
    headers = {
        "Content-Type": "application/json",
    }

    data = {"text": text}

    auth_url = IMAGE_API.replace("https://", "").replace("/", "")

    auth = BotoAWSRequestsAuth(
        aws_host=auth_url,
        aws_region="us-east-1",  # HARDCODED to us-east-1
        aws_service="lambda",
    )

    resp = requests.post(IMAGE_API, json=data, headers=headers, auth=auth)
    # print(resp.json())

    return np.array(resp.json()["generated_image"])


def app() -> None:
    """
    Purpose:
        Controls the app flow
    Args:
        N/A
    Returns:
        N/A
    """
    col1, col2 = st.columns(2)

    article = col1.text_area("Input article", height=900)

    styles = col2.multiselect(
        "Image Style",
        [
            "Cloud",
            "Pixel Art",
            "Landscape",
            "Cityscape",
            "Futuristic",
            "Watercolor",
            "Technology",
            "Computer",
            "Cyberpunk",
            "Realistic",
            "Retro",
            "Abstract",
            "Geometric",
            "Network",
        ],
    )

    if col2.button("Generate"):
        with st.spinner("In progress..."):
            summary_text = gen_summary(article)

            style_string = ""
            for style in styles:
                style_string += style + " "

            summary_image = gen_image(summary_text + style_string)

            col2.subheader(summary_text)
            col2.image(summary_image)


def main() -> None:
    """
    Purpose:
        Controls the flow of the streamlit app
    Args:
        N/A
    Returns:
        N/A
    """

    # Start the streamlit app

    st.markdown(
        "<h1 style='text-align: center;'>BuildOn Poster</h1>", unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align: center;'>Sharing your article or idea with the world? Make your content pop with a great tagline and image</h3>",
        unsafe_allow_html=True,
    )

    app()


if __name__ == "__main__":
    main()
