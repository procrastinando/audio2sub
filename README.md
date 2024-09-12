# audio2sub: Generate Transcription or Subtitles with Faster Whisper in a GUI

**audio2sub** is a user-friendly graphical web application that utilizes the power of [Faster Whisper](https://github.com/ggerganov/whisper) to generate accurate transcriptions and subtitles from audio files. 

## Requirements

* **Python**: Version 3.8 or higher

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/procrastinando/audio2sub
    cd audio2sub
    ```

2.  **Create a Conda Environment:**
    ```bash
    conda create --name audio2sub python=3.8 -y
    conda activate audio2sub
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Run the GUI

Start the application using Streamlit:

```bash
streamlit run app.py
```


## Running on Nvidia GPU (Optional)

To leverage the power of your Nvidia GPU for faster processing, follow these steps:

**1. Install CUDA and Drivers:**

   * **Find the latest CUDA 12.2 version**: https://developer.nvidia.com/cuda-toolkit-archive
   * **Download and Install:**  Replace `cuda_12.2.2_535.104.05_linux.run` with your downloaded CUDA installer.

      ```bash
      wget https://developer.download.nvidia.com/compute/cuda/12.2.2/local_installers/cuda_12.2.2_535.104.05_linux.run
      chmod +x cuda_12.2.2_535.104.05_linux.run 
      ```

   * **Configure Environment:**

      ```bash
      nano ~/.bashrc  # Edit your .bashrc file
      ```
      Add these lines at the end and save the file:

      ```bash
      export PATH=/usr/local/cuda-12.2/bin:$PATH
      export LD_LIBRARY_PATH=/usr/local/cuda-12.2/lib64:$LD_LIBRARY_PATH
      ```

   * **Reload your .bashrc:**

      ```bash
      source ~/.bashrc 
      ```

   * **Follow the instructions for installing drivers and CUDA toolkit.**

**2. Install cuDNN:**

   * **Download the latest cuDNN8:** https://developer.nvidia.com/rdp/cudnn-archive

   * **Install:** 

     ```bash
     sudo dpkg -i cudnn-local-repo-ubuntu2204-8.9.7.29_1.0-1_amd64.deb
     sudo cp /var/cudnn-local-repo-ubuntu2204-8.9.7.29/cudnn-local-08A7D361-keyring.gpg /usr/share/keyrings/
     sudo apt-get install libcudnn8
     sudo apt-get install libcudnn8-dev
     ```

**3. Verify Installation:**

* **Drivers:** `nvidia-smi`
* **CUDA:** `nvcc --version`
* **cuDNN:** `dpkg -l | grep libcudnn`