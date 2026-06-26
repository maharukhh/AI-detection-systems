# AI Fake Profile Detector

A simple Python application that analyzes basic social media profile information and identifies whether a profile is likely to be real or fake using rule-based detection. 

## Objective

The objective of this project is to demonstrate a basic fake profile detection system by evaluating common profile characteristics such as followers, following count, posts, and account age.

## Detection Parameters

The application analyzes:

* Number of followers
* Number of following
* Total posts
* Account age (in months)

## Technologies Used

* Python


## How It Works

1. Accept profile information from the user.
2. Evaluate the profile using predefined rules.
3. Assign a risk score based on suspicious characteristics.
4. Classify the profile as either **Likely Fake** or **Appears Real**.


## Installation

Clone the repository:

```bash
git clone https://github.com/maharukhh/fake-profile-detector.git
cd fake-profile-detector
```

## Run the Project

```bash
python main.py
```

## Sample Output

```text
=== Fake Profile Detector ===

Enter number of followers: 20
Enter number of following: 1500
Enter number of posts: 2
Enter account age (months): 1

Analysis Result:

Profile is likely FAKE
```

## Project Structure

```text
Fake-Profile-Detector/
│
├── main.py
├── output.png
└── README.md
```

## Concepts Used

* Rule-Based Classification
* Conditional Statements
* User Input Handling
* Decision Making
* Python Programming

  
## Future Improvements

* Train a Machine Learning classification model.
* Use a real-world social media dataset.
* Analyze profile images and account activity.
* Add confidence scores for predictions.
* Build a graphical user interface (GUI).
* Deploy as a web application.

  
## Author

**Mahrukh**

Robotics & Intelligence Systems Student passionate about Artificial Intelligence, Machine Learning, Computer Vision, and Software Development.
