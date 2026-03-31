README
# Spam Email Classifier

A command-line tool that uses Machine Learning (Naive Bayes) to classify emails as **SPAM** or **HAM** (legitimate). Trained on a labeled CSV dataset, it can detect spam in real time right from your terminal.

---

## What It Does

- Loads a labeled email dataset from a CSV file
- Automatically detects which column is the text and which is the label
- Trains a Multinomial Naive Bayes classifier using Bag-of-Words features
- Saves the trained model so it doesn't retrain every time
- Lets you type in any email text and instantly get a SPAM / HAM result

---

## Project Structure

```
spam-classifier/
├── spam_classifier.py   # Main application file
├── emails.csv           # Labeled dataset (you provide this)
├── model.pkl            # Auto-generated after first run
└── README.md
```

---

## Requirements

- Python 3.7 or above
- pandas
- scikit-learn

Install dependencies with:

```bash
pip install pandas scikit-learn
```

---

## Dataset Format

The program expects a CSV file named `emails.csv` in the same folder as the script.

The CSV should have at least two columns — one for the email text and one for the label. Column names don't matter, the program figures them out automatically.

Labels can be either:
- `spam` / `ham`
- `1` / `0`

**Example:**

| text | label |
|------|-------|
| Congratulations! You won a free iPhone. Click here! | spam |
| Hey, are you coming to the meeting tomorrow? | ham |
| URGENT: Your account has been compromised. Verify now. | spam |
| Please find the attached report for your review. | ham |

A good free dataset to use: [UCI SMS Spam Collection](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)

---

## How to Run

1. Clone or download the project files
2. Place your `emails.csv` in the same folder
3. Open a terminal in that folder
4. Run:

```bash
python spam_classifier.py
```

---

## Usage

When the program starts, it trains the model (first time) or loads the saved model, then shows a menu:

```
Spam Classifier Running

1 classify
2 retrain
3 exit
enter:
```

**Option 1 — Classify an email:**
```
enter: 1
enter email: You have been selected for a cash prize. Call now!
result: SPAM
```

```
enter: 1
enter email: Can we reschedule our call to Thursday?
result: HAM
```

**Option 2 — Retrain the model** (useful if you update your dataset):
```
enter: 2
training model...
training done: 5572
```

**Option 3 — Exit:**
```
enter: 3
bye
```

---

## How It Works

1. **Text Cleaning** — Input is lowercased for consistency
2. **Vectorization** — Text is converted to word count vectors using `CountVectorizer`
3. **Classification** — A `MultinomialNB` model predicts SPAM (1) or HAM (0)
4. **Model Saving** — The trained model and vectorizer are saved to `model.pkl` using pickle
5. **Auto-load** — On next run, the saved model is loaded instead of retraining

---

## Notes

- The `model.pkl` file is created automatically after the first run — don't delete it if you want to skip retraining
- If you update `emails.csv`, use option `2` from the menu to retrain
- Empty inputs are handled gracefully — the program will ask again
- The program works with different CSV formats as long as there are at least two columns

---

## Course Info

**Course:** Fundamentals of AI and ML — CSA2001  
**Project Type:** Bring Your Own Project (BYOP)  
**Deadline:** March 31, 2026
