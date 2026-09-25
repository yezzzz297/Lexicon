# Part 4 - Unique information

topics = {"Python", "Web", "AI", "Security", "Testing"}

ada = {"Python", "AI"}
sarah = {"Python", "APIs"}
abel = {"AI", "LLMs"}
david = {"Linux", "Security"}
anna = {"Testing", "Python"}
skills = ada | sarah | abel | david | anna

workshop_a = {"Anna", "David", "Sara", "Leo"}
workshop_b = {"Sara", "Leo", "Mia", "Noah"}

print("Topics:", topics)
print("All skills:", skills)
print("Both workshops:", workshop_a & workshop_b)
print("Only A:", workshop_a - workshop_b)
print("Only B:", workshop_b - workshop_a)
print("Everyone:", workshop_a | workshop_b)

# & means both, - means difference, and | joins the sets.
