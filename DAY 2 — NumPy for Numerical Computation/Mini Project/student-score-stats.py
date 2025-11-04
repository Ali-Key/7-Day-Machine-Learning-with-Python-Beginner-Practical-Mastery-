# Day 2 Mini-Project — Student Score Stats Using NumPy
# In this mini-project, we will use NumPy to analyze a set of student scores and compute basic statistics.

# Step 1 — Import NumPy
import numpy as np

# Step 2 — Create Student Scores Array
scores = np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])
print("\n--- Student Scores ---")
print("Scores:", scores)

# Step 3 — Calculate Basic Statistics
print("\n--- Basic Statistics ---")
print("Mean Score:", np.mean(scores))          # Average score
print("Median Score:", np.median(scores))      # Middle value of scores
print("Standard Deviation:", np.std(scores))   # How spread out scores are from the mean
print("Variance:", np.var(scores))             # Square of standard deviation (average squared distance from the mean)
print("Maximum Score:", np.max(scores))        # Highest score 
print("Minimum Score:", np.min(scores))        # Lowest score

# Step 4 — Calculate Total Score
print("\n--- Total Score ---")

total_score = np.sum(scores)
print("Total Score:", total_score)  # Sum of all scores

# Step 5 — Calculate Percentiles
print("\n--- Percentiles ---")
print("25th Percentile:", np.percentile(scores, 25))  # Score below which 25% of scores fall
print("50th Percentile (Median):", np.percentile(scores, 50))  # Median score
print("75th Percentile:", np.percentile(scores, 75))  # Score below which 75% of scores fall

# Step 6 — Conclusion
print("\n✅ Student Score Statistics Computation Complete!")
print("You have successfully computed basic statistics for student scores using NumPy.")    
print("Feel free to modify the scores array and explore more statistics!")
