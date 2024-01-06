## <b> Chat with your Image data using using LangChain Framework. </b>

## System Setup:
Step 1. Create a virtual environment
  > conda create -p myenv python=3.9 -y

step 2. Activate the environment:
  > conda activate myenv/

step 3. Install all the requirements:
  > pip install -r requirements.txt
 
step 4. start writing the code, with standard file name as main.py

## <b> Flow </b>
![image](https://github.com/Chandrakant817/Chat-with-PDF-using-LangChain/assets/69152112/40d04d29-5a66-4d49-9e85-e84dec172c3b)

### <b> High Level Architecture </b>
![image](https://github.com/Chandrakant817/Chat-with-your-Image-data-using-using-LangChain/assets/69152112/db16ecfd-7574-4bd9-b67c-5959a665db21)

### <b> Steps: </b>
1. Upload the Image
2. Extract the content from the Image using easyocr (this is a python Library)
3. Extract the text into raw text variable
4. Split content into Chunk
5. Do Embeddings of the data (Download embeddings from the OpenAI)
6. Store Data into Vector Store (eg: FAISS)
7. User can pass a Prompt
8. Get the Output.

## <b> Output </b>





