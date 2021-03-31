myDetails = ["I am ambitious and driven.",
             "I thrive on challenge and constantly set goals for myself, so I have something to strive toward.",
             "Im not comfortable with settling and Im always looking for an opportunity to do better and achieve .",
             "In my previous role, I was promoted three times in less than two years.",
             "I find this skill is especially helpful when kicking off projects with new clients."]
myFile = open("sample.txt", "w+")
for i in range(int(len(myDetails))):
    myFile.write(myDetails[i])
    myFile.write("\n")
myFile.close()

