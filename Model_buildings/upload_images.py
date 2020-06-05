
"""

This function will take the path of a folder and upload the images in that folder with the name of 
that folder as the concept label

"""

def upload_images(mainDIR):
    
    if mainDIR[-1] != '/':
        mainDIR = mainDIR + '/'
    else:
        mainDIR = mainDIR

    concept = mainDIR.split('/')[-2]

    print('Starting upload for concept named:', concept,'\n')
    for files in os.listdir(mainDIR):
        if not files. startswith('.'): # TO SKIP MAC SYSTEM FILES
            # print(files)
            
            img_path = mainDIR + files
            print("Uploading files at ", img_path, '\n with concept: ', concept,'\n')
            app.inputs.create_image_from_filename(img_path, concepts=[str(concept)])
            print('done\n\n')
