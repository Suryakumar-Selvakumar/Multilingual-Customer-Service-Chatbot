# Development of a Multilingual Customer Service Chatbot

This is my **MS Course Project**, aligned with the course - **Natural Language Processing and Generative AI**, and associated with my **Master's Degree in Computer Science** at the **University of Colorado Denver**. 

## Project Description

This project aimed to develop a seamless multilingual single-turn customer service chatbot capable of accurately responding to
inquiries in English, French, and Spanish. 

The chatbot was built by fine-tuning the **mBART-large-50** model (which is designed to handle multiple languages within a single framework) on a **Multilingual Customer Support Training Dataset** which includes customer service interactions in the aforementioned three languages. 

This multilingual dataset was obtained by using **MarianMT models - *opus-mt-en-fr & opus-mt-en-es*** to translate **Bitext Customer Support LLM Chatbot Training Dataset** (which contains only English interactions) into French and Spanish. 

*Note: More info may be added upon completion of Project Report works.*

## Instructions to Run the Project (IMPORTANT: Read all the instructions once before following them)

**1. Clone the repo locally using:** <br>
`git clone https://github.com/yourusername/your-repo.git`

**2. Download the models folder from this Drive [Link](https://drive.google.com/drive/folders/1Or6SQIoqOEhYCPT2Jrtaha3_OsyKc9xp?usp=sharing)**
- The size of the folder is around `9.2GB`.  
- The download may occur in parts as the large files may not get zipped together with the smaller files. In that case, ensure the following large files are placed in the following paths:

    i) `05d892bf4a3e34b9a4de239109387d43107b2a8c55ad34b73a929ca6c1ede24e` - `models/comet/models--Unbabel--wmt20-comet-qe-da/blobs/`
    
    ii) `model.ckpt` - `models/comet/models--Unbabel--wmt20-comet-qe-da/snapshots/2e7ffc84fb67d99cf92506611766463bb9230cfb/checkpoints`

    iii) `model.safetensors` - `models/final_mbart_model/`

    iv) `pytorch_model.bin` - `models/mbart-large-50/`

- Once done, place the `models` folder inside the cloned repo in the same directory as the project notebooks.
- NOTE: I had to store my models on Google Drive as `git-lfs` upload kept failing because it was unreliable with my slow internet speed.

**3. Use `conda` and `environment.yml` to create a virtual env with all required dependencies:**

- `conda env create -f environment.yml`
- activate conda env with `conda activate chatbot-env`

**4. Steps to run the project files:**

- Create an ipykernel with your conda env using `python -m ipykernel install --user --name=chatbot-env`
- Now, use `jupyter notebook` command to launch the jupyter notebook server, from which you can run the notebooks. Make sure to switch to `chatbot-env` kernel before running the notebooks.
- To interact with the Chatbot, run `python chatbot_interface_gradio.py`.

## Additional instructions for running the project that may be helpful:

**1. Run times for the notebooks and Response times for the Chatbot may vary *drastically* depending on your system specs. Below is the System that was used to build the project:**
- CPU: *12th Gen Intel(R) Core(TM) i9-12900KF*
- RAM: *32GB* 
- GPU: *NVIDIA GeForce RTX 4070 Ti*
- Driver Version: *560.35.03*  
- CUDA Version: *12.5* 

**2. NOTE:** <br>
The code in the notebooks are setup in such a way that new data won't be created if that data already exists. If you wish to regenerate any data using any of the models, ensure to delete the respective pre-existing files. Be careful not to delete `Bitext_Sample_Customer_Support_Training_Dataset.csv` as it's the original training dataset.

**3. Additional File-Specific Information:**
- *Notebook - 1 - Multilingual Dataset Creation:* Translation of the original dataset to `French` and `Spanish` took around `5.14 hrs` on my System.
- *Notebook - 2 - Multilingual Dataset Analysis:* This notebook should run fairly quickly, the last code cell may take a while depending on your `GPU`.
- *Notebook - 3 - MBart Model Trainer:* You will need an extremely powerful GPU to run this notebook, I opted to use Google Colab Pro which provided the `NVIDIA A100-SXM4-40GB` GPU.
- *Notebook - 4 - MBart Model Evaluation:* This notebook took `11 hrs` to run on my System. Depending on your system specs, it may run faster or much slower.
- *chatbot_interface_gradio:* The response times for the user instructions will vary depending on your system. More powerful the System = Faster response times.