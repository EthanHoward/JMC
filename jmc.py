import os

def packTotalJSONFile(pkgdimgJSON, dir):
    head = '{\n"directory":"' + dir + '",\n'   
    schema = head + '"files_list":\n    {\n' + pkgdimgJSON + '    }\n}'
    return schema 

def returnJSONSchema(ordr, name, last):
    schema = ""
    if last == True:
        schema = '        "' + str(ordr) +pc '":"' + str(name) + '"\n'
    else:
        schema = '        "' + str(ordr) + '":"' + str(name) + '",\n'
    return schema



def init():
    print(" -------------------------------------------------------------------------------------")
    print(" ---------------------------------- JSON META CREATOR --------------------------------")
    print(" -------------------------------------------------------------------------------------")
    header  =   """ -------------------------------------- CHOICES --------------------------------------"""
    print(" ----Please enter the path of the folder that the meta will be built around [./]------")
    path = input(" --- ? ")
    if ("./" in path) == True & (len(path) == 2) == True:
        header += "\n ----PATH: ./"
        pass
    elif len(str(path)) <= 2:
        header += "\n ----PATH: ./" 
        path += "./"
        pass
    elif len(str(path)) >= 2:
        header += "\n    PATH: " + str(path)
        pass
    try:
        files = os.listdir(path)
    except IOError:
        mainloop()
    print(" ----Please enter the meta file name [JSON]-------------------------------------------")
    imagelist_name = input(" --- ? ")
    if len(str(imagelist_name)) <= 2:
        imagelist_name = "META.JSON"
        header += "\n ----FILE LIST NAME: " + str(imagelist_name)
    elif len(str(imagelist_name)) >= 2:
        header += "\n ----FILE LIST NAME: " + str(imagelist_name + ".JSON") 
        pass
    packaged_images_json = str('')
    imglist              = open(imagelist_name + ".JSON", 'a+')

    amount_of_files = 0
    for i, img in enumerate(files, start=1):
        amount_of_files = i
    for i, img in enumerate(files, start=1):
        if i >= amount_of_files:
            packaged_images_json += returnJSONSchema(i, img, True)
        else:
            packaged_images_json += returnJSONSchema(i, img, False)
    
    packed = packTotalJSONFile(packaged_images_json, path)
    
    imglist.write(packed)
    imglist.close()
    
    header += "\n ----N0 OF FILES: " + str(amount_of_files)


    print(" -------------------------------------------------------------------------------------")
    print(header)
    print(" -------------------------------------------------------------------------------------")

def mainloop():
    while True:
        try:
            init()
        except KeyboardInterrupt:
            print("---------- KeyboardInterrupt ---------")
            exit()

mainloop()
