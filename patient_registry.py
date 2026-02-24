# Requirements
#   1. REQ-01: The system shall allow the creation of a new patient record with a name and a
#      unique Patient ID.
#   2. REQ-02: The system shall retrieve a patient's record using their unique Patient ID.
#   3. REQ-03: The system shall ensure data integrity by preventing the modification of a
#      Patient ID once it has been assigned.
#   4. REQ-04: The system shall allow updating a patient’s name using their Patient ID, while
#      keeping the Patient ID unchanged.
#   5. REQ-05: The system shall allow deleting a patient record using their Patient ID. If the ID
#      does not exist, the system shall display an appropriate error message.

class PatientRegistry:
    '''
    Manage patient names and IDs in a dictionary

    This class provides methods to register, retrieve, update, delete, and list patients.

    Data Fields:
        _database (dict[str, str]) - maps patient IDs to names
        _next_id (int) - tracks entries for unique patient IDs
    '''
    # Needs name and ID stored in simulated database
    def __init__(self):
        # Simulated Database
        self._database = {}
        # Unique ID - incremented for each user
        self._next_id = 101
    
    # Methods
    def register_patient(self, name:str) -> str:
        '''
        Creates a unique ID for a patient and creates a new entry in the database give name
        
        Requirements:
            REQ-01 - The system shall allow the creation of a new patient record with a name and a unique Patient ID.
            REQ-03 - The system shall ensure data integrity by preventing the modification of a Patient ID once it has been 
                     assigned.
        
        Args:
            name (str) - name of patient
        
        Returns: 
            patient_id (str) - unique ID of patient
        '''
        #Test input
        if not name:
            raise ValueError("Name cannot be empty")
        
        # Create unique patient ID
        patient_id = f"P-{self._next_id}"
        # Increcemnt ID so next one is unique
        self._next_id += 1
        
        #Store name and ID in database
        self._database[patient_id] = { "patient_id": patient_id, "name": name }

        return patient_id

    def get_patient(self, patient_id:str) -> dict:
        '''
        Retrieves patient name from database given ID

        Requirements:
            REQ-02 - The system shall retrieve a patient's record using their unique Patient ID.
        
        Args:
            patient_id - name of patient
        
        Returns: 
            dictionary entry of patient
        '''
        #Test input
        if not patient_id:
            raise ValueError("Patient ID cannot be empty")
        elif patient_id not in self._database:
            raise LookupError(f"No patient found with ID \'{patient_id}\'")
        

        return self._database.get(patient_id, "ID Not Found")
    

    def update_patient_name(self, patient_id:str) -> dict:
        '''
        Updates the name of a patient in the database to given name
        
        Requirements:
            REQ-02 - The system shall allow updating a patient’s name using their Patient ID, while keeping the Patient ID 
                     unchanged.
        
        Parameters:
            patient_id (str) - id of patient to be changed

        Returns: 
            dictionary entry of patient
        '''
        #Test input
        if not patient_id:
            raise ValueError("Patient ID cannot be empty")
        elif patient_id not in self._database:
            raise LookupError(f"No patient found with ID \'{patient_id}\'")
        
        new_name = input("Enter New Name of " + patient_id + ": ").strip()

        self._database[patient_id] = { "patient_id": patient_id, "name": new_name }
        
        return self._database.get(patient_id, "ID Not Found")


    def delete_patient(self, patient_id) -> bool:
        '''
        Delete an entry in the dataset given patient ID
        
        Requirements:
            REQ-05 - The system shall allow deleting a patient record using their Patient ID. If the ID does not exist, the 
                     system shall display an appropriate error message.
        
        Args:
            patient_id (str) - id of patient to be changed
            
        Returns: 
            new name & old ID of patient
        '''
        #Test input
        if not patient_id:
            raise ValueError("Patient ID cannot be empty")
        elif patient_id not in self._database:
            raise LookupError(f"No patient found with ID \'{patient_id}\'")
        else:
            del self._database[patient_id]
            return True

    def list_patients(self) -> list:
        return list(self._database.values())