FROM python:3.9

WORKDIR /home

# Install deps
ADD requirements.txt /home/
RUN pip3 install -r requirements.txt

# Add files
ADD fm_postly_public_st.py /home/

# Expose port
EXPOSE 80

# Start App
CMD [ "streamlit","run" ,"fm_postly_public_st.py","--server.port","80"]
