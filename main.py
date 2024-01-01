welcome_prompt = "Welcome Doctor! What would you like to do today?\n - To List all patients press 1. \n To run a diagnosis press 2.\n To press quit q.\n"
name_prompt  = "What is the patient's name?"
appearence_prompt = "How is the patient's general apperance?\n  1. Normal appeearnce\n 2. Irritable or lethargic\n"
eye_prompt = "How are the patient's eyes?\n  1. Eves Normal or Slightly sunken\n 2. Eyes really Sunken\n"
skin_promopt = "How is the patient's skin when you pinch?\n  1.Normal skin pinch \n 2.Slow skin pinch.\n"
sever_dehydration = "Server Dehydration"
some_dehydration  = "Some Dehydration"
no_dehydration = "No Dehydration"
error_message = "Could not save the patients diagnosis due to invalid input"

patients_and_diagnosis = [

    "Mike: Severe Dehydration", 
    "Vikash: No Dehydration",
    "Ali: Some Dehydration"
]

def assess_eyes(eyes: str):
    if eyes == "1" :
        return no_dehydration
    elif eyes == "2":
        return sever_dehydration
    else:
        return ""

def assess_skin(skin: str):
    if skin == "1" :
        return some_dehydration
    elif skin == "2":
        return sever_dehydration
    else:
        return ""

def list_patients():
    for patient in patients_and_diagnosis:
        print(patient)

def save_new_diagnosis(name, diagnosis):
    if name == "" or diagnosis == "":
        print(error_message)
        return
    final_diagnosis = f'{name}:{diagnosis}'
    patients_and_diagnosis.append(final_diagnosis)
    print("Final diagnosis:" , final_diagnosis, "\n")

def access_appearence():
    appearence =  input(appearence_prompt)
    if appearence == "1" :
        eyes = input(eye_prompt)
        return assess_eyes(eyes=eyes)
    elif appearence == "2":
        skin = input(skin_promopt)
        return assess_skin(skin=skin)
    else:
        return ""

def start_new_diagnosis():
    name = input(name_prompt)
    diagnosis = access_appearence()
    save_new_diagnosis(name=name, diagnosis=diagnosis)
    
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