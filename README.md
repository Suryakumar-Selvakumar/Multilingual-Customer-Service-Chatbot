# Development of a Multilingual Customer Service Chatbot

This is my **MS Course Project**, aligned with the course - **Natural Language Processing and Generative AI**, and associated with my **Master's Degree in Computer Science** at the **University of Colorado Denver**.

## Project Description

Today’s globalized business environments demand the provision of consistent and efficient customer service across multiple languages, and companies around the world are struggling to provide it reliably. The aim of this project is to develop an efficient & seamless **Multilingual Single-turn Customer Service Chatbot** capable of accurately responding to customer inquiries in multiple languages, namely, **English**, **French**, and **Spanish**.

The **Multilingual Customer Support Dataset** required to train the chatbot was created by using **MarianMT models – _opus-mt-en-fr_ & _opus-mt-en-es_** and translating **Bitext Customer Support LLM Chatbot Training Dataset** containing English interactions, into French and Spanish. This dataset was then used to fine-tune the **mBART-large-50** model to respond to customer service queries in the aforementioned three languages. A web interface was built with **Gradio**, to allow interaction with the chatbot, which is fast and capable of handling customer queries and providing high-quality formatted responses in multiple languages within the same chat interaction.

_For a comprehensive report of the Project, please refer to the [MS Course Project Report](./Docs/Suryakumar%20Selvakumar%20-%20MS%20Course%20Project%20Report.pdf)_

## Sample Output

<div align="center">
   <h3 align="left">English:</h3>
   <img width=auto height=auto src="./Output Samples/en.png" alt="Chatbot response in English">
   <h3 align="left">French:</h3>
   <img width=auto height=auto src="./Output Samples/fr.png" alt="Chatbot response in French">
   <h3 align="left">Spanish:</h3>
   <img width=auto height=auto src="./Output Samples/es.png" alt="Chatbot response in Spanish">
</div>

## Instructions to Run the Project

**IMPORTANT: Read all the instructions once before following them**

**1. Fork & Clone the repo:** <br>
`git clone https://github.com/your-username/your-forked-repo.git`

**2. Download the models folder from this Drive [Link](https://drive.google.com/drive/folders/1Or6SQIoqOEhYCPT2Jrtaha3_OsyKc9xp?usp=sharing)**

- The size of the folder is around `9.2GB`.
- If `COMET` evaluation is not a concern or the user wishes to download the `COMET` model themselves, then please skip that model.
- The download may occur in parts as the large files may not get zipped together with the smaller files. In that case, ensure the following large files are placed in the following paths:

  i) `05d892bf4a3e34b9a4de239109387d43107b2a8c55ad34b73a929ca6c1ede24e` - `models/comet/models--Unbabel--wmt20-comet-qe-da/blobs/`

  ii) `model.ckpt` - `models/comet/models--Unbabel--wmt20-comet-qe-da/snapshots/2e7ffc84fb67d99cf92506611766463bb9230cfb/checkpoints/`

  iii) `model.safetensors` - `models/final_mbart_model/`

  iv) `pytorch_model.bin` - `models/mbart-large-50/`

- Once done, place the `models` folder inside the cloned repo in the same directory as the project notebooks.
- NOTE: I had to store my models on Google Drive as `git-lfs` upload kept failing because my slow internet speed was unreliable.

**3. Create a virtual env with Conda and Install all required dependencies:**

_Approach #1: Use provided `environment.yml`_

- `conda env create -f environment.yml`
- activate conda env with `conda activate chatbot-env`
- It is highly recommended to run this project on a Linux system. If that is not an option, please follow Approach #2.

_Approach #2: Use provided `requirements.txt`_

- `conda create -n your-env-name python=3.9`
- `conda activate your-env-name`
- `pip install -r requirements.txt`
- OS-specific Conda libraries that may be needed for the project may have to be installed manually.

**4. Steps to run the project files:**

- Create an ipykernel with your conda env using `python -m ipykernel install --user --name=chatbot-env`
- Now, use `jupyter notebook` command to launch the jupyter notebook server, from which you can run the notebooks. Make sure to switch to `chatbot-env` kernel before running the notebooks.
- To interact with the Chatbot, run `python chatbot_interface_gradio.py`. Feel free to use any instructions from the [dataset](./data/Multilingual_Customer_Support_Training_Dataset_Cleaned.csv) or the [sample questions](./Docs/sample-questions.md) provided.

## Information pertaining to running the project that may be helpful:

**1. Run times for the notebooks and Response times for the Chatbot may vary _drastically_ depending on your system specs. Below is the System that was used to build the project:**

- CPU: _12th Gen Intel(R) Core(TM) i9-12900KF_
- RAM: _32GB_
- GPU: _NVIDIA GeForce RTX 4070 Ti_
- Driver Version: _560.35.03_
- CUDA Version: _12.5_

**2. NOTE:** <br>
The code in the notebooks are setup in such a way that new data won't be created if that data already exists. If you wish to regenerate any data using any of the models, ensure to delete the respective pre-existing files or change the name of the files. Be careful not to delete `Bitext_Sample_Customer_Support_Training_Dataset.csv` as it's the original training dataset.

**3. File-Specific Information:**

- _Notebook - 1 - Multilingual Dataset Creation:_ Translation of the original dataset to `French` and `Spanish` took around `5.14 hrs` on my System.
- _Notebook - 2 - Multilingual Dataset Analysis:_ This notebook should run fairly quickly, the last code cell may take a while depending on your `GPU`.
- _Notebook - 3 - MBart Model Trainer:_ The user will need an extremely powerful GPU to run this notebook, I opted to use Google Colab Pro which provided the `NVIDIA A100-SXM4-40GB` GPU.
- _Notebook - 4 - MBart Model Evaluation:_ This notebook took `11 hrs` to run on my System. Depending on the user's system specs, it may run faster or much slower. Try lowering the `num_beams` parameter in the `generate_response()` function by one or two values if the run time is too long but the metrics may get worse. For a comprehensive report of the metrics I achieved, please refer to the [Performance Log document](./Docs/Performance-Log.md).
- _chatbot_interface_gradio:_ The response times of the chatbot will vary depending on the user's system. More powerful the System = Faster response times. As before, lowering `num_beams` may help with the response times but the response quality may get worse.
