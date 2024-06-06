from typing import List

def get_requirements(file_path: str) -> list[str]:
    encodings = [  'UTF-16 LE','cp1252','windows-1252']  # Add more encodings as needed
    
    for encoding in encodings:
        
        with open(file_path, 'r', encoding=encoding) as file_obj:
                requirements = file_obj.readlines()
                requirements = [i.strip() for i in requirements if i.strip()]
                print(requirements)
                return requirements
                
# Example usage
requirements_list = get_requirements('requirements.txt')
print(requirements_list)

f =open('hell.txt','r') 
print("hello",f.readlines())

