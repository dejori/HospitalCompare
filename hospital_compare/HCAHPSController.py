import csv
import os
from hospital_compare.HospitalInformationController import HospitalInformationController

class HCAHPSController(object):
    
    hospitalinformation_controller = HospitalInformationController()
    
    lines=[]
    records={}
   

    def __init__(self):
        data_folder = os.path.join(os.path.dirname(__file__), "..", 'data','Hospital_flatfiles')
        self.consumer_perspective_filename = 'HQI_HOSP_HCAHPS_MSR.csv'
        
        with open(os.path.join(data_folder, self.consumer_perspective_filename), 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            self.lines =[line for line in reader]
            self.records = {line['Provider Number']+'_'+line['HCAHPS Question']: line  for line in self.lines}
    
    def get_record(self, hospitalnumber, question):
        return self.records[hospitalnumber+'_'+question]
            
    def get_answerpercentage(self, hospitalnumber, question):
        record = self.records.get(hospitalnumber+'_'+question)
        if record and record['HCAHPS Answer Percent'].isdigit() and record['Number of Completed Surveys'] == '300 or more':
            return int(record['HCAHPS Answer Percent']);
        else:
            return float('NaN')
                
    def get_questions(self):
        return list(set([line['HCAHPS Question'] for line in self.lines]))

        
