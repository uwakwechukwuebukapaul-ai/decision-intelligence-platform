def build_career_prompt(profile, recommendations):

    prompt = f"""

You are a professional career decision intelligence assistant.

Analyze this user profile:

Name:
{profile.name}

Education:
{profile.education}

Experience:
{profile.experience}

Skills:
{profile.skills}

Goals:
{profile.goals}


Recommended career paths:

{recommendations}


Generate:

1. Career recommendation explanation
2. Why these paths fit the user
3. Skill gaps to improve
4. A 90-day action plan

Make the response practical and personalized.

"""


    return prompt