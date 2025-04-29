import json
import agentclinic
from agentclinic import ScenarioNEJMExtended
cases = [
    {
        "image_url": "https://csvc.nejm.org/ContentServer/images?id=IC20250424&width=1500&height=4000",
        "question": "A 26-year-old man presented with sudden onset of severe pain in the legs and inability to move the left leg. On physical examination, he had complete loss of motor function in the left leg. Bedside ultrasonographic examination with color Doppler showed no blood flow in the distal aorta. Computed tomographic angiography of the abdomen revealed a saddle embolus at the aortoiliac junction (left). Emergency aortoiliac embolectomy was performed, and a gelatinous mass was removed. A subsequent transthoracic echocardiogram identified a heterogeneous mass in the left atrium (middle). On hospital day 2, cardiothoracic surgery was performed to remove the left atrial mass, and a villous, friable lesion was excised (right). Histopathology of the cardiac mass showed abundant mucopolysaccharide matrix with scattered nests of lepidic cells. What is the diagnosis?",
        "patient_info": "As a patient actor, you are a 26-year-old man who presented with sudden onset of severe pain in the legs and inability to move the left leg. You also have complete loss of motor function in the left leg. This pain and immobility came on rapidly, and you have been unable to walk due to the condition. You don't have any known medical history of vascular disease, but you were recently experiencing discomfort in your legs. You are not aware of any specific test results or prior conditions contributing to this problem.",
        "physical_exams": "On physical examination, you had complete loss of motor function in the left leg. Bedside ultrasonographic examination with color Doppler showed no blood flow in the distal aorta. Computed Tomographic Angiography (CTA) of the abdomen revealed a saddle embolus at the aortoiliac junction on the left side. Emergency aortoiliac embolectomy was performed, and a gelatinous mass was removed. A subsequent transthoracic echocardiogram identified a heterogeneous mass in the left atrium. On hospital day 2, cardiothoracic surgery was performed to remove the left atrial mass, which was a villous, friable lesion. Histopathology of the cardiac mass showed abundant mucopolysaccharide matrix with scattered nests of lepidic cells.",
        "answers": [
            {"text": "Cardiac myxoma", "correct": True},
            {"text": "Cardiac sarcoma", "correct": False},
            {"text": "Intracardiac thrombus", "correct": False},
            {"text": "Marantic endocarditis", "correct": False},
            {"text": "Papillary fibroelastoma", "correct": False},
        ],
    },
]

with open("nejm_subset.jsonl", "w") as f:
    for case in cases:
        f.write(json.dumps(case) + "\n")
        

with open("nejm_subset.jsonl", "r") as f:
    for line in f:
        # Load each line (case) into a dictionary
        case_dict = json.loads(line)
        
        # Create an instance of ScenarioNEJMExtended with the case data
        scenario = ScenarioNEJMExtended(case_dict)
        
        # Print patient information (
        print("Patient Information:")
        print(scenario.patient_information())
        print("\nExam Information:")
        print(scenario.exam_information())
        print("\nDiagnosis Information:")
        print(scenario.diagnosis_information())
        print("-" * 50)
        