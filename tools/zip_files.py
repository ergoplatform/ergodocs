import os                                                                                                                                           
import zipfile                                                                                                                                      
                                                                                                                                                    
# Function to find all .md files in the given directory                                                                                             
def get_md_files(dir_path):                                                                                                                         
    md_files = []                                                                                                                                   
    for root, _, files in os.walk(dir_path):                                                                                                        
        for file in files:                                                                                                                          
            if file.endswith(".md"):                                                                                                                
                md_files.append(os.path.join(root, file))                                                                                           
    return md_files                                                                                                                                 
                                                                                                                                                    
# Get all .md files from the child directories                                                                                                      
md_files = get_md_files(os.getcwd())                                                                                                                
                                                                                                                                                    
# Create a zip file and add .md files to it                                                                                                         
with zipfile.ZipFile("md_files.zip", "w") as archive:                                                                                               
    for md_file in md_files:                                                                                                                        
        archive.write(md_file, os.path.relpath(md_file, os.getcwd()))                                                                               
                                                                                                                                                    
print("md_files.zip created with all .md files from child directories.")      