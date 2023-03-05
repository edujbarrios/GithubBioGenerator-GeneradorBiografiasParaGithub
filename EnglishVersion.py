# Script to generate biographies for GitHub

print("👋 Welcome to the GitHub biography generation tool!")
print("Please select the type of biography you would like to generate:")
print("1. Short biography (10 words or less)")
print("2. Simple biography (1-2 sentences)")
print("3. Detailed biography")

# Ask user what type of biography they want to generate
bio_type = input("Select 1, 2, or 3: ")

# User prompts
username = input("👤 What is your GitHub username? ")
profession = input("💼 What is your profession or field of work? ")
experience = input("🎓 How many years of experience do you have in your profession? ")
hobbies = input("🎨 What are your hobbies or interests? ")
short_term_goals = input("🏆 What is your primary short-term professional goal? ")
long_term_goals = input("🚀 What is your primary long-term professional goal? ")
technologies = input("💻 What are the technologies that you most like or use in your work? ")
featured_projects = input("🌟 What is the most notable project you've worked on? ")
achievements = input("🏅 What is your biggest accomplishment in your career? ")
collaborations = input("🤝 Have you collaborated on other open-source projects? If so, which ones? ")
current_job = input("🏢 Where are you currently employed? ")
current_position = input("👨‍💼 What is your current position at your job? ")
education = input("🎓 What is your educational background? ")

# Generate the biography
if bio_type == "1":
    bio = f"{username}, {profession} with {experience} years of experience. {hobbies} enthusiast. 🏆{short_term_goals} 🚀{long_term_goals}"
elif bio_type == "2":
    bio = f"{username}, {profession}. 🏆{short_term_goals} 🚀{long_term_goals}. {hobbies} enthusiast. 🌟{featured_projects}"
elif bio_type == "3":
    bio = f"I'm {username}, a {profession} with {experience} years of experience. I'm passionate about {hobbies} and constantly looking for ways to improve my skills in the technologies I use, such as {technologies}. My most notable project so far has been 🌟{featured_projects} and my biggest accomplishment has been 🏅{achievements}. Currently, my short-term goal is 🏆{short_term_goals} and my long-term goal is to 🚀{long_term_goals}. I have collaborated on several open-source projects, such as {collaborations}. I'm currently employed at 🏢{current_job} as a 👨‍💼{current_position} and have a {education} in my field of study."

# Print the generated biography
print("\n📝 Here's your GitHub biography:\n")
print(bio)
