import numpy as np

# ==============================
# Task 1 — Generate and Inspect
# ==============================

np.random.seed(42)

# Generate scores (5 students, 4 subjects)
scores = np.random.randint(50, 101, size=(5, 4))

print("Original Scores:\n", scores)

# 1. Score of 3rd student in 2nd subject
print("\nScore of 3rd student in 2nd subject:")
print(scores[2, 1])

# 2. All scores of last 2 students
print("\nScores of last 2 students:")
print(scores[-2:, :])

# 3. First 3 students in subjects 2 and 3 only
print("\nFirst 3 students in subjects 2 and 3:")
print(scores[:3, 1:3])


# ==============================
# Task 2 — Analyze with Broadcasting
# ==============================

# Column-wise mean (rounded to 2 decimals)
column_mean = np.round(scores.mean(axis=0), 2)
print("\nColumn-wise Mean (per subject):")
print(column_mean)

# Add curve using broadcasting
curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve

# Ensure no score exceeds 100
curved_scores = np.clip(curved_scores, None, 100)

print("\nCurved Scores:")
print(curved_scores)

# Row-wise max (best subject per student)
row_max = curved_scores.max(axis=1)
print("\nBest score per student:")
print(row_max)


# ==============================
# Task 3 — Normalize and Identify
# ==============================

# Min-max normalization per row
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)

normalized = (curved_scores - row_min) / (row_max - row_min)

print("\nNormalized Scores (0–1 scale):")
print(normalized)

# Find index of highest value in normalized array
max_index = np.unravel_index(np.argmax(normalized), normalized.shape)

print("\nStudent index and Subject index of highest normalized value:")
print(max_index)

# Extract all scores strictly above 90
above_90 = curved_scores[curved_scores > 90]

print("\nScores strictly above 90:")
print(above_90)