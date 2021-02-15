configfile = open("C:\TEMP\haproxy.cfg","r")

global_section = ""
defaults_section = ""
frontend_sections = {}
backend_sections = {}

currentsection = ""
sectionname = ""
for line in configfile:
    #print("Processing", line)
    parseline = line.split()

    # need a check here if the line has just spaces or tabs, parseline will be empty
    if len(parseline) > 0:
        # check for start of the global section
        if parseline[0].lower() == "global":
            print("End of", currentsection, sectionname)
            currentsection = "GLOBAL"
            print("\nStart of", currentsection, "section")

        # check for start of the defaults section
        elif parseline[0].lower() == "defaults":
            print("End of", currentsection, sectionname)
            currentsection = "DEFAULTS"
            print("\nStart of", currentsection, "section")

        # check for start of a frontend section
        elif parseline[0].lower() == "frontend":
            print("End of", currentsection, sectionname)
            currentsection = "FRONTEND"
            sectionname = parseline[1]
            frontend_sections[sectionname] = ""
            print("\nStart of", currentsection, "section named", sectionname)

        # check for start of a backend section
        elif parseline[0].lower() == "backend":
            print("End of", currentsection, sectionname)
            currentsection = "BACKEND"
            sectionname = parseline[1]
            backend_sections[sectionname] = ""
            print("\nStart of", currentsection, "section named", sectionname)

    # the line is empty, so add the line to whatever section we are currently in (if any)
    if currentsection == "GLOBAL":
        global_section += line
        print("Adding to", currentsection)
    elif currentsection == "DEFAULTS":
        defaults_section += line
        print("Adding to", currentsection)
    elif currentsection == "FRONTEND":
        try:
            print("Adding to", currentsection, sectionname)
            frontend_sections[sectionname] += line
        except ValueError:
            print("FRONTEND", sectionname, "not found")
    elif currentsection == "BACKEND":
        try:
            print("Adding to", currentsection, sectionname)
            backend_sections[sectionname] += line
        except ValueError:
            print("BACKEND", sectionname, "not found")
    # end if len(parseline) > 0
# end for line in configfile

# print out some results for troublshooting and development
print("")
print("Parsing complete.")
print("GLOBAL section has ", len(global_section), " characters")
#print(global_section)
print("DEFAULTS section has ", len(defaults_section), " characters")
#print(defaults_section)
print("There are ", len(frontend_sections), " FRONTEND sections ")
#print(frontend_sections)
print("There are ", len(backend_sections), " BACKEND sections ")
#print(backend_sections)
