# Asking the user for different types of words to create a funny story
adj : str = input("Enter an adjective: ")  # Describes something (e.g., happy, sad)
verb : str = input("Enter a verb: ")  # Action word (e.g., run, jump)
adv : str = input("Enter an adverb: ")  # Describes how something is done (e.g., quickly, slowly)
noun : str = input("Enter a noun: ")  # A person, place, or thing (e.g., dog, car)
place  : str = input("Enter a place: ")  # Any location (e.g., park, beach)
number : str = input("Enter a number: ")  # Any number
body_part : str = input("Enter a body part: ")  # A part of the body (e.g., hand, leg)
past_tense_verb : str = input("Enter a past-tense verb: ")  # A verb in the past form (e.g., jumped, ran)
emotion : str = input("Enter an emotion: ")  # Feeling (e.g., excited, angry)
color : str = input("Enter a color: ")  # Any color (e.g., red, blue)
food : str = input("Enter a food: ")  # Any type of food (e.g., pizza, burger)

# Printing the completed Mad Libs story using the user's inputs
print(f"Sarah is so {adj}. She {verb} in the park. She goes there {adv}. \
She has a {noun}. She went with her pet to the {place} yesterday and \
she found {number} more cats there. She picked them up with her {body_part}. \
Then she {past_tense_verb} away. The cats were really {emotion} and they were \
{color} in color. Then she fed them with {food}.")
