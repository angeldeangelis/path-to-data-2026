# Task 02: Project Budget Analysis
# Goal: Categorize projects based on their financial scale

project_names = ["Road Rehab", "Bridge Repair", "Sewer Line", "Street Lights"]
budgets = [500000, 120000, 85000, 45000]

high_priority = []
standard_priority = []

# Iterating through the lists using index
for i in range(len(project_names)):
    name = project_names[i]
    amount = budgets[i]
    
    # Logic: Projects over 100,000 are high priority
    if amount > 100000:
        print(f"CRITICAL: {name} requires senior supervision. Budget: ${amount}")
        high_priority.append(name)
    else:
        print(f"NOTICE: {name} managed by standard protocol. Budget: ${amount}")
        standard_priority.append(name)

# Final Summary
print("--- Final Report ---")
print(f"High Priority Projects: {high_priority}")
print(f"Standard Priority Projects: {standard_priority}")