student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# highest_score = max(student_scores)
# print(highest_score)

highest_in_for = 0
for score in student_scores:
    if score > highest_in_for:
        highest_in_for = score

print(f"Highest score of the list is: {highest_in_for}")
