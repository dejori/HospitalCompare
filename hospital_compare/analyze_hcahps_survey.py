import matplotlib.pyplot as plt
import math
import numpy as np
import os
from hospital_compare.HCAHPSController import HCAHPSController
from hospital_compare.HospitalInformationController import HospitalInformationController

hcaphs_controller = HCAHPSController()
hospital_controller = HospitalInformationController()

RESULT_DIR = os.path.join(os.path.dirname(__file__), "..", 'results') # change this to wherever the results should be saved
if not os.path.isdir(RESULT_DIR):
    os.makedirs(RESULT_DIR)

def save_histogram(positive_questions, title, xlabel,filename):
    positives = []
    for hospitalnumber in hospital_controller.get_providernumbers():
        positive = sum([hcaphs_controller.get_answerpercentage(hospitalnumber, question) for question in positive_questions])
        if not math.isnan(positive):
            positives.append(positive)
    hist, bins = np.histogram(positives, bins=15)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar((bins[:-1] + bins[1:]) / 2, hist, align='center', width=(bins[1] - bins[0]), color='#333333', edgecolor='#333333')
    plt.ylabel('# of Hospitals')
    plt.xlabel(xlabel)
    plt.title(title)
    plt.xlim([0, 100])
    ax.set_xticks(range(0, 100 + 1, 20))
    ax.set_xticklabels(['', '20%', '40%', '60%', '80%', '100%'])
    plt.savefig(filename)


save_histogram(['Percent of patients who reported YES, they would probably recommend the hospital.','Patients who reported YES, they would definitely recommend the hospital.'],
                  'Would you recommend this hospital to your friends and family?',
                  'Patients who answered with \'YES\'',
                  os.path.join(RESULT_DIR,"recommend.png")
                  )

save_histogram(['Patients who reported that their doctors Always" communicated well."', 'Percent of patients who reported that their doctors Usually" communicated well."'],
                  'Did doctors communicated well?',
                  'Patients who answered with \'Always\' or \'Usually\'',
                   os.path.join(RESULT_DIR,"communication.png")
                   )

save_histogram(['Patients who reported that their nurses Always" communicated well."', 'Percent of patients who reported that their nurses Usually" communicated well."'],
                  'Did doctors communicated well?',
                  'Patients who answered with \'Always\' or \'Usually\'',
                   os.path.join(RESULT_DIR,"communication_nurses.png")
                   )

save_histogram(['Patients who gave their hospital a rating of 9 or 10 on a scale from 0 (lowest) to 10 (highest).', 'Percent of patients who gave their hospital a rating of 7 or 8 on a scale from 0 (lowest) to 10 (highest).'],
                  'What number would you use to rate this hospital during your stay?\n(0-10, worst-best) ',
                  'Patients who gave a rating of 7 or higher',
                  os.path.join(RESULT_DIR,"rating.png")
                  )

save_histogram(['Patients who reported that staff Always" explained about medicines before giving it to them."', 'Percent of patients who reported that staff Usually" explained about medicines before giving it to them."'],
                  'Before giving you any new medicine,\nhow often did hospital staff tell you what the medicine was for?',
                  'Patients who answered with \'Always\' or \'Usually\'',
                  os.path.join(RESULT_DIR,"explained.png")
                  )

save_histogram(['Percent of patients who reported that they Usually" received help as soon as they wanted."', 'Patients who reported that they Always" received help as soon as they wanted."'],
                  'After you pressed the call button,\nhow often did you get help as soon as you wanted it?',
                  'Patients who answered with \'Always\' or \'Usually\'',
                  os.path.join(RESULT_DIR,"help.png")
                  )

save_histogram(['Percent of patients who reported that their pain was Usually" well controlled."', 'Patients who reported that their pain was Always" well controlled."'],
                  'How often was your pain well controlled?',
                  'Patients who answered with \'Always\' or \'Usually\'',
                  os.path.join(RESULT_DIR,"pain.png")
                  )

save_histogram(['Percent of patients who reported that their room and bathroom were Usually" clean."', 'Patients who reported that their room and bathroom were Always" clean."'],
                  "How often were your room and bathroom kept clean",
                  'Patients who answered with \'Always\' or \'Usually\'',
                  os.path.join(RESULT_DIR,"clean.png")
                  )

save_histogram(['Patients who reported that the area around their room was Always" quiet at night."', 'Percent of patients who reported that the area around their room was Usually" quiet at night."'],
                  'How often was the area around your room quiet at night?',
                  'Patients who answered with \'Always\' or \'Usually\'',
                  os.path.join(RESULT_DIR,"quiet.png")
                  )

save_histogram(['Patients at each hospital who reported that YES, they were given information about what to do during their recovery at home.'],
                  "Did staff give you information about what to do\n during your recovery at home?",
                  'Patients who answered with \'YES\'',
                  os.path.join(RESULT_DIR,"information.png")
                  )


save_histogram(['Patients at each hospital who reported that YES, they were given information about what to do during their recovery at home.'],
                  "Did staff give information about what to do\n during your recovery at home?",
                  'Patients who answered with \'YES\'',
                  os.path.join(RESULT_DIR,"information.png")
                  )
