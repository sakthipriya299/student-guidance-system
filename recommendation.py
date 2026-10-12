 def get_recommendations(interest, skills, preferred_course, career_goal):
interest = interest.lower()
skills = skills.lower()
preferred_course = preferred_course.lower()
career_goal = career_goal.lower()

recommendations = []

if any(word in interest + skills + preferred_course + career_goal
       for word in ["programming", "computer", "technology", "coding"]):
    recommendations.append({
        "course": "Computer Science / IT",
        "careers": "Software Developer, Web Developer, IT Support",
        "reason": "Your interests or skills relate to computers and technology."
    })

if any(word in interest + skills + preferred_course + career_goal
       for word in ["business", "commerce", "account", "finance"]):
    recommendations.append({
        "course": "Commerce / Business Administration",
        "careers": "Accountant, Business Analyst, Finance Executive",
        "reason": "Your interests or goals relate to business and finance."
    })

if any(word in interest + skills + preferred_course + career_goal
       for word in ["biology", "medical", "health", "medicine"]):
    recommendations.append({
        "course": "Life Sciences / Healthcare",
        "careers": "Lab Technician, Research Assistant, Healthcare Professional",
        "reason": "Your interests or goals relate to biology or healthcare."
    })

if any(word in interest + skills + preferred_course + career_goal
       for word in ["design", "art", "creative", "drawing"]):
    recommendations.append({
        "course": "Design / Creative Arts",
        "careers": "Graphic Designer, UI Designer, Illustrator",
        "reason": "Your interests or skills relate to creativity and design."
    })

if not recommendations:
    recommendations.append({
        "course": "Explore courses related to your preferred subject",
        "careers": "Research careers that match your interests and strengths",
        "reason": "More information about your interests can help narrow down suitable options."
    })

return recommendations