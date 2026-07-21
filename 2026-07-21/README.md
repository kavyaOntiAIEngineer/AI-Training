# End-to-End Understanding of Fine-Tuning LLMs
## Practical 01 – Dataset Exploration & Tokenization with Hugging Face

##  Overview

This practical demonstrates the first step in the Large Language Model (LLM) fine-tuning pipeline. The objective is to understand how to download a dataset from Hugging Face, explore its structure, perform basic data analysis, and tokenize the text using a pretrained BERT tokenizer.

The IMDb Movie Review dataset is used for sentiment analysis, where reviews are classified as either **Positive** or **Negative**.

---

##  Objectives

- Download the IMDb dataset from Hugging Face
- Explore dataset splits and structure
- Analyze dataset features and labels
- Convert the dataset into a Pandas DataFrame
- Perform basic Exploratory Data Analysis (EDA)
- Calculate review statistics
- Download a pretrained BERT tokenizer
- Tokenize individual reviews
- Tokenize the complete dataset
- Understand Input IDs and Attention Masks

---

##  Technologies Used

- Python 3.x
- Hugging Face Datasets
- Hugging Face Transformers
- Pandas
- BERT Base Uncased Tokenizer
- VS Code
- Jupyter Notebook

---

##  Dataset

**Dataset Name:** IMDb Movie Reviews

Source:
https://huggingface.co/datasets/stanfordnlp/imdb

Dataset contains:

- 25,000 Training Reviews
- 25,000 Testing Reviews
- 50,000 Unsupervised Reviews

Labels

- 0 → Negative
- 1 → Positive

---

##  Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate into the folder

```bash
cd Fine_Tuning_Practical_01
```

Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install transformers datasets pandas torch jupyter
```

---

## ▶ Running the Notebook

Open the project in VS Code.

Launch the Jupyter Notebook.

Select the appropriate Python kernel.

Run all cells sequentially.

---

##  Practical Workflow

### Step 1

Install required libraries

### Step 2

Import Python libraries

### Step 3

Download IMDb dataset

### Step 4

Explore dataset information

### Step 5

View available dataset splits

### Step 6

Count training, testing, and unsupervised samples

### Step 7

Display the first training sample

### Step 8

Display the first three movie reviews

### Step 9

Understand dataset features and labels

### Step 10

Convert numeric labels into readable text

### Step 11

Display a random review

### Step 12

Convert dataset into a Pandas DataFrame

### Step 13

Display dataset shape

### Step 14

View column names

### Step 15

Check for missing values

### Step 16

Analyze label distribution

### Step 17

Create a sentiment column

### Step 18

Calculate review lengths

### Step 19

Find average review length

### Step 20

Display the longest review

### Step 21

Display the shortest review

### Step 22

Download the pretrained BERT tokenizer

### Step 23

Tokenize a single review

### Step 24

Display Input IDs

### Step 25

Display Token Names

### Step 26

Tokenize the complete dataset

### Step 27

Inspect the tokenized dataset

### Step 28

Display the first tokenized sample

### Step 29

Display Input IDs

### Step 30

Display Attention Mask

---

##  Key Concepts Learned

- Hugging Face Datasets
- DatasetDict
- Dataset Splits
- Feature Inspection
- Sentiment Analysis Dataset
- Pandas Integration
- Data Exploration
- Tokenization
- BERT Tokenizer
- Input IDs
- Attention Mask
- Padding
- Truncation
- Maximum Sequence Length

---

## Expected Learning Outcomes

After completing this practical, you will be able to:

- Load datasets directly from Hugging Face Hub
- Explore and analyze NLP datasets
- Understand dataset labels and features
- Perform basic EDA on text datasets
- Use pretrained tokenizers
- Convert text into model-readable tokens
- Prepare datasets for LLM fine-tuning

---

##  References

- Hugging Face Datasets Documentation
  https://huggingface.co/docs/datasets

- Hugging Face Transformers Documentation
  https://huggingface.co/docs/transformers

- IMDb Dataset
  https://huggingface.co/datasets/stanfordnlp/imdb

