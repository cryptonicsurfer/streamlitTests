try:
    import streamlit as st
    import cv2
    import requests
    import numpy as np
    from PIL import Image
    from io import BytesIO
    import tempfile
    print("All required packages are installed!")
except ImportError as e:
    print(f"Error: {e}")
