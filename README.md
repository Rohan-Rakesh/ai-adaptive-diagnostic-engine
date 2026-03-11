# ai-adaptive-diagnostic-engine
# AI-Driven Adaptive Diagnostic Engine

## Overview

This project implements a **1-Dimensional Adaptive Testing System** that dynamically adjusts question difficulty based on a student's responses.
The system estimates a learner’s ability level and selects questions that best match their proficiency.

The goal of this project is to demonstrate how **adaptive assessment systems** can be built using modern backend tools and AI models to create **smarter learning platforms**.

The engine begins with a baseline ability score and continuously updates it using an **Item Response Theory (IRT)-inspired approach**, allowing the system to present increasingly appropriate questions.

---

## Key Features

• Adaptive question selection based on user performance
• Ability estimation using an IRT-inspired algorithm
• MongoDB-based question and session storage
• REST API built with FastAPI
• AI-generated personalized study recommendations
• Modular and scalable project architecture
• Unit testing for algorithm validation
• Docker support for easy deployment

---

## Tech Stack

Backend Framework
FastAPI

Programming Language
Python

Database
MongoDB

AI Integration
OpenAI API

Testing
Pytest

Deployment
Docker (optional)

---

## System Architecture

```
Client Application
       │
       ▼
    FastAPI API
       │
       ├── Adaptive Engine (Ability estimation)
       │
       ├── MongoDB Database
       │
       └── AI Study Plan Generator
              │
              ▼
          OpenAI API
```

---

## Adaptive Algorithm

The system uses a simplified **Item Response Theory (IRT)** model to estimate the probability that a student answers a question correctly.

Probability of a correct response:

P(correct) = 1 / (1 + e^(−(ability − difficulty)))

After each answer, the student's **ability score is updated** based on the difference between the expected probability and the actual outcome.

Correct answer → ability increases
Incorrect answer → ability decreases

The next question is selected by choosing the question whose difficulty is **closest to the updated ability score**.

---

## Project Structure

```
ai-adaptive-diagnostic-engine
│
├── app
│   ├── api
│   ├── core
│   ├── models
│   ├── services
│   ├── utils
│   └── main.py
│
├── scripts
│   └── seed_questions.py
│
├── tests
│   └── test_adaptive_engine.py
│
├── docs
│   └── API.md
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .env.example
```

---

## Installation

Clone the repository

```
git clone https://github.com/yourusername/ai-adaptive-diagnostic-engine.git
cd ai-adaptive-diagnostic-engine
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file using the example:

```
MONGO_URI=mongodb://localhost:27017
OPENA
```
