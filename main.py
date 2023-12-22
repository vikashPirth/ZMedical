welcome_prompt = "Welcome Doctor! What would you like to do today?\n - To List all patients press 1. \n To run a diagnosis press 2.\n To press quit q.\n"
name_prompt  = "What is the patient's name?"
appearence_prompt = "How is the patient's general apperance?\n  1. Normal appeearnce\n 2. Irritable or lethargic\n"


def assess_eyes():
    print("Ask the question for eyes")

def assess_skin():
    print("ask the question for skin")

def list_patients():
    print("List all patients and diagnosis")

def start_new_diagnosis():
    name = input(name_prompt)
    appearence =  input(appearence_prompt)
    
    if appearence == "1" :
        assess_eyes()
    elif appearence == "2":
        assess_skin()
    else:
        print("input is not valid")



def main():
   
   while (True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            return

main()