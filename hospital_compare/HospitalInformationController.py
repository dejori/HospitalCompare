import csv
import os

class HospitalInformationController(object):
    
    lines=[]
    hospital_information={}
    
    def __init__(self):
        hospitalinfo_filename = 'HQI_HOSP.csv'
        data_folder = os.path.join(os.path.dirname(__file__), "..", 'data')
        with open(os.path.join(data_folder, hospitalinfo_filename), 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            self.lines = [line for line in reader]
            self.hospital_information = {line['Provider Number']: line for line in self.lines}
                
    def get_providernumbers(self):
        return self.hospital_information.keys()
        
    def get_hospitaltypes(self):
        return list(set([line['Hospital Type'] for line in self.lines]))
    
    def get_ownershiptypes(self):
        return list(set([line['Hospital Ownership'] for line in self.lines]))
    
    def get_hospitaltype(self,hospitalnumber):
        return self.hospital_information.get(hospitalnumber)['Hospital Type']

    def get_ownershiptype(self,hospitalnumber):
        return self.hospital_information.get(hospitalnumber)['Hospital Ownership']
    
    def get_information(self, hospitalnumber):
        return self.hospital_information.get(hospitalnumber)

    
if  __name__ =='__main__':
    controller = HospitalInformationController()
        