# Fake News Detector

A machine learning application that detects whether a news article is real or fake using Natural Language Processing (NLP) techniques.

## Objective

The objective of this project is to classify news articles as **REAL** or **FAKE** by analyzing textual content using machine learning and text vectorization techniques.

## Features

* Fake and real news classification
* Text preprocessing and vectorization
* TF-IDF feature extraction
* Machine learning-based prediction
* Accuracy evaluation
* User input prediction

## Dataset

The project uses two datasets:

* `Fake.csv` – Fake news articles
* `True.csv` – Real news articles

The datasets are combined and shuffled before training the model.


## Technologies Used

* Python
* Pandas
* Scikit-learn
* Natural Language Processing (NLP)


## Machine Learning Model

* **Feature Extraction:** TF-IDF Vectorizer
* **Classification Algorithm:** Passive Aggressive Classifier

## Installation

Clone the repository:

```bash
git clone https://github.com/maharukhh/fake-news-detector.git
cd fake-news-detector
```

Install the required libraries:

```bash
pip install pandas scikit-learn
```

## Run the Project

```bash
python main.py
```

## How It Works

1. Load the fake and real news datasets.
2. Combine and shuffle the data.
3. Convert text into numerical features using TF-IDF.
4. Train the Passive Aggressive Classifier.
5. Evaluate model accuracy.
6. Predict whether user-entered news is real or fake.

## Sample Output

```text
Loading datasets...
Training model...
Accuracy: 98.75 %

Enter news:
Scientists discover water on Mars.

Prediction: REAL
```

## Project Structure

```text
Fake-News-Detector/
│
├── main.py
├── Fake.csv
├── True.csv
├── output.png
└── README.md
```

## Concepts Used

* Natural Language Processing (NLP)
* Text Classification
* TF-IDF Vectorization
* Supervised Machine Learning
* Binary Classification

## Future Improvements

* Implement BERT and Transformer models.
* Add news source credibility analysis.
* Build a web application.
* Support batch predictions.
* Save trained models.
* Deploy using Flask or FastAPI.

## Author

**Mahrukh**

Robotics & Intelligence Systems Student passionate about Artificial Intelligence, Machine Learning, Natural Language Processing, and Software Development.
