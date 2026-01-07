 🏏 Virat Kohli — Test Career Dismissal Analysis

A data-driven analysis of **when and why Virat Kohli struggled in Test cricket**, using **ball-by-ball match data** and **cricket-informed statistical reasoning**.

This project focuses on **interpretability and context**, prioritizing clear insights over black-box prediction.



 📌 Project Objective

To understand the **conditions and match situations** under which Virat Kohli was more likely to be dismissed in Test cricket, particularly during the later phase of his career.

Rather than predicting dismissals, the goal is to **explain patterns** in:

* early-phase vulnerability
* impact of the new ball
* pace vs spin
* pressure and fatigue across innings



 🔍 Key Questions Addressed

* Is Kohli more vulnerable early in his innings?
* How does the new ball affect dismissal risk?
* Does pace pose a greater challenge than spin?
* Do pressure situations increase dismissals?
* Was the decline technical, contextual, or physical?



 📊 Key Insights

* **Early-phase vulnerability**: Dismissal rates are higher in the first 10 overs, before settling.
* **New ball impact**: The highest dismissal risk occurs during the new-ball phase.
* **Pace vs spin**: Pace bowling consistently leads to higher dismissal rates than spin.
* **Pressure & fatigue**: Later innings show increased dismissals, indicating physical and contextual decline.
* **No single technical flaw**: Patterns suggest situational factors rather than a fundamental batting weakness.



 🧠 Analytical Approach

   Data

* Ball-by-ball Test match data (Cricsheet)
* All matches involving Virat Kohli in Test cricket

 Methodology

* Feature engineering grounded in cricket context
* Avoidance of cumulative or leakage-prone variables
* Use of machine learning **only to identify important factors**
* Final explanations derived from **real dismissal rates and distributions**

 Why no black-box explainability?

The project deliberately avoids fragile post-hoc explainability tools and instead relies on:

* interpretable statistics
* transparent visualizations
* domain-driven reasoning

This mirrors how insights are communicated in professional sports analytics environments.



 🛠️ Tech Stack

* **Python**
* **Pandas**
* **Matplotlib**
* **Streamlit**



 🚀 Live Application

👉 **Streamlit App:**
*(Link will appear here after deployment)*

The app presents:

* interactive filters
* dismissal-rate visualizations
* cricket-focused explanations for each pattern



 📁 Project Structure


kohli-test-analysis/
│
├── app.py
├── data/
│   └── kohli_test_ball_by_ball.csv
├── requirements.txt
├── README.md
└── .gitignore



 📈 What This Project Demonstrates

* Correct problem framing in sports analytics
* Avoidance of data leakage and exposure bias
* Clean separation of modeling and interpretation
* End-to-end delivery: data → analysis → visualization → deployment

This project was built to reflect **real-world analytics standards**, not notebook-only experimentation.



 🔮 Possible Extensions

* Opposition-specific analysis
* Venue-based comparisons
* Phase-by-phase career breakdown
* Integration with ball-tracking data


 👤 Author

Built by ME - Saigireesh 
Passionate in sports analytics, applied machine learning, and interpretable data storytelling.

