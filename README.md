# E-commerce Customer Retention Analysis (2024)

**Author:** Senior Data Analyst  
**Contact / Verification Email:** 23f2003790@ds.study.iitm.ac.in

## Summary
The company is experiencing declining customer loyalty. Quarterly retention rates for 2024 are:

- Q1: 65.47  
- Q2: 73.85  
- Q3: 73.61  
- Q4: 77.49  

**Average retention (2024): 72.61**

Industry benchmark target: **85**

**Solution focus:** implement targeted retention campaigns.

---

## Key findings
1. The retention rate improved steadily from Q1 (65.47) to Q4 (77.49) but remains below the industry target of 85.  
2. The computed average retention for 2024 is **72.61**, which is **12.39 percentage points** below the target 85.  
3. The largest quarter-over-quarter jump was Q1 → Q2 (+8.38 pts), suggesting that certain initiatives mid-year may have positively influenced retention. However, growth plateaued between Q2 and Q3.  
4. While the trend is positive, the pace of improvement is insufficient to meet the target within the year without new interventions.

---

## Business implications
- A sustained gap of ~12.4 percentage points implies significant lost customer lifetime value (CLV) relative to competitors.  
- If average order value and purchase frequency remain constant, increasing retention to 85 would materially increase revenue and reduce marketing acquisition costs over time.  
- The plateau between Q2 and Q3 signals potential issues with mid-funnel or post-purchase experience (e.g., onboarding, product quality, delivery, returns, or loyalty incentives).

---

## Recommendations (to reach 85)
**Strategic approach: targeted retention campaigns (high-priority).**
1. **Segmented win-back campaigns**  
   - Identify customers who churned or reduced purchase frequency in the last 6-12 months.  
   - Deploy personalized offers (discounts, free shipping, product recommendations) and measure lift via A/B tests.
2. **Onboarding & education for new customers**  
   - Implement a 30–90 day onboarding drip with product tips, reviews, and tailored recommendations to accelerate habit formation.
3. **Loyalty program redesign**  
   - Move from a points-only system to tiered benefits that emphasize status and exclusivity (exclusive access, early drops).
4. **Post-purchase experience optimization**  
   - Improve delivery/update communications, simplify returns, and request feedback proactively to reduce friction.
5. **Predictive retention modeling**  
   - Build models to score churn risk and trigger interventions (e.g., coupon, outreach). Prioritize high CLV users.
6. **Measure & iterate**  
   - Set short-term targets (e.g., +2 ppt per quarter) and use controlled experiments (holdout and treatment groups) to estimate ROI before scaling.

---

## Specific tactical example (6-month playbook)
- Month 0–1: Deploy churn scoring model; design 3 segmented campaigns (high-value, mid-value, low-value).  
- Month 1–3: Run A/B tests for messaging and offer structure; prioritize high-value segment.  
- Month 3–6: Scale winners; introduce loyalty tier benefits and onboarding automation.  
- Expected impact: if interventions produce +3 to +5 ppt lift in 6 months, iterative scaling can approach the 85 target over successive quarters.

---

## Files in this PR / repo
- `analysis.py` — Python script to compute statistics and generate the trend plot.  
- `retention_trend.png` — Visualization of quarterly retention with industry benchmark and average.  
- `README.md` — This data story (you are reading it).

---

## How to reproduce locally (commands)
1. Clone repo (replace `<your-repo>`):  
```bash
git clone <your-repo>
cd <your-repo>
```
2. (Optional) Create virtual env and install deps:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install pandas matplotlib
```
3. Run the analysis:
```bash
python analysis.py
# This saves retention_trend.png
```
4. Create a branch, commit, push, and open a Pull Request:
```bash
git checkout -b feature/retention-analysis
git add analysis.py retention_trend.png README.md
git commit -m "Add retention analysis, plot, and data story"
git push origin feature/retention-analysis
# Then create a PR via GitHub UI or gh CLI
```

---

## Notes and limitations
- Analysis is descriptive and based on 4 quarterly data points — limited sample size; stronger conclusions require user-level transaction data, cohorts, and more features (channel, product, region).  
- Recommendation prioritization should be driven by ROI estimates, available engineering resources, and expected CLV per segment.

---

**Verified contact:** 23f2003790@ds.study.iitm.ac.in
