import json
from csv import writer



# load json file
with open ('data.json', 'r') as openfile:

    jsonObject = json.load(openfile)
    #print(jsonObject)


# define function for set overlap
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    # check length
    if len(a_set.intersection(b_set)) > 0:
        return(a_set.intersection(b_set))
    else:
        return("no common elements")

#make list of civs

CivNameList = list(jsonObject.keys())
#print(CivNameList)

# make list of opponents for each civs

civIndex = 0
for civ in CivNameList:
    opponentsList = []
    CurrentCivIndex = civIndex
    while CurrentCivIndex < len(CivNameList):
        opponentsList.append(CivNameList[CurrentCivIndex])
        CurrentCivIndex = CurrentCivIndex + 1
    #print(opponentsList)
    civIndex = civIndex + 1
    for oppo in opponentsList:

        CivA = civ
        CivB = oppo

        #Buildings

        listABuild = []
        listBBuild = []
        JointListBuild = []

        # create list of ids
        for i in jsonObject[CivA]['buildings']:
            listABuild.append(i['id'])
            #print(listA)

        for i in jsonObject[CivB]['buildings']:
            listBBuild.append(i['id'])
            #print(listB)

        a = listABuild
        b = listBBuild

        commonListBuild = common_member(a, b)
        print(CivA, " building count = ", len(listABuild))
        print(CivB, " building count = ", len(listBBuild))
        print("Common building count = ", len(commonListBuild))


        #techs

        listATech = []
        listBTech = []
        JointListTech = []

        # create list of ids
        for i in jsonObject[CivA]['techs']:
            listATech.append(i['id'])
            #print(listA)

        for i in jsonObject[CivB]['techs']:
            listBTech.append(i['id'])
            #print(listB)


        a = listATech
        b = listBTech

        commonListTech = common_member(a, b)
        print(CivA, " tech count = ", len(listATech))
        print(CivB, " tech count = ", len(listBTech))
        print("Common tech count = ", len(commonListTech))

        #Units

        listAUnit = []
        listBUnit = []
        JointListUnit = []

        # create list of ids
        for i in jsonObject[CivA]['units']:
            listAUnit.append(i['id'])
            #print(listA)

        for i in jsonObject[CivB]['units']:
            listBUnit.append(i['id'])
            #print(listB)


        a = listAUnit
        b = listBUnit

        commonListUnit = common_member(a, b)
        print(CivA, " Unit count = ", len(listAUnit))
        print(CivB, " Unit count = ", len(listBUnit))
        print("Common Unit count = ", len(commonListUnit))

        # Overall

        CivACountAll = len(listABuild) + len(listATech) + len(listAUnit)
        CivBCountAll = len(listBBuild) + len(listBTech) + len(listBUnit)
        CommonCountAll = len(commonListBuild) + len(commonListTech) + len(commonListUnit)

        print( CivA, " all tech tree count = ", CivACountAll)
        print( CivB, " all tech tree count = ", CivBCountAll)
        print("Number of shared Tech Tree Items = ", CommonCountAll)

        #format the data to be saved to the csv

        csvNewLine = [CivA, CivB, CivACountAll, CivBCountAll, CommonCountAll ]
        #print(csvNewLine)
        with open('results.csv', 'a') as f_object:

            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)

            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(csvNewLine)

            # Close the file object
            f_object.close()
