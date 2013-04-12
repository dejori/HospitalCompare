import matplotlib.pyplot as plt
import math
import os
import json
from hospital_compare.HCAHPSController import HCAHPSController
from hospital_compare.HospitalInformationController import HospitalInformationController
from numpy.ma.core import get_data

hcaphs_controller = HCAHPSController()
hospital_controller = HospitalInformationController()

RESULT_DIR = os.path.join(os.path.dirname(__file__), "..", 'results') # change this to wherever the results should be saved
if not os.path.isdir(RESULT_DIR):
    os.makedirs(RESULT_DIR)

def get_data(positive_questions):
    positives = []
    for hospitalnumber in hospital_controller.get_providernumbers():
        positive = sum([hcaphs_controller.get_answerpercentage(hospitalnumber, question) for question in positive_questions])
        if not math.isnan(positive):
            positives.append(positive)
    return positives
    
    
def save_boxplots(positives, xlabels, title,filename):
   
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.boxplot(positives,0,'')
    
    plt.title(title)
    plt.ylabel('Percentage of patients who gave a positive answer')
    plt.ylim([0, 110])
    ax.set_yticks(range(0, 100 + 1, 20))
    ax.set_yticklabels(['', '20%', '40%', '60%', '80%', '100%'])
    for idx, xlabel in enumerate(xlabels):
        ax.text(idx+1, 2, xlabel, rotation = 90, fontsize=8, va='bottom')
    ax.set_xticklabels([])
    ax.set_xticks([])
    plt.savefig(os.path.join(RESULT_DIR,filename))


questions_file = open(os.path.join(os.path.dirname(__file__), '..', 'data','hcahps_questions.json'))
question_groups = json.load(questions_file)
questions_file.close()

all_answer_data=[]
all_questions=[]
for question_category in question_groups.keys():
    print question_category
    questions = question_groups[question_category];
    
    answers_data = []
    
    for question in questions.keys():
        positive_questions = questions.get(question)
        print "\t"+question +" --> "+ str(positive_questions)
        answers_data.append(get_data(positive_questions))
        
    save_boxplots(answers_data, questions.keys(), question_category, question_category.replace(" ","_")+".png")
    all_answer_data.extend(answers_data)
    all_questions.extend(questions.keys())
    
save_boxplots(all_answer_data, all_questions, "HCAHPS Results", "all.png")
