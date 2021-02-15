configfile = open("C:\TEMP\haproxy.cfg","r")

global_section = ""
defaults_section = ""
frontend_section_name = []
frontend_section_value = []
backend_section_name = []
backend_section_value = []

currentsection = ""
sectionname = ""
for line in configfile:
    #print("Processing", line)
    parseline = line.split()

    # need a check here if the line has just spaces or tabs, parseline will be empty
    if len(parseline) > 0:
        # start of the global section
        if parseline[0].lower() == "global":
            print("End of", currentsection, sectionname)
            currentsection = "GLOBAL"
            print("")
            print("Start of", currentsection, "section")

        # start of the defaults section
        elif parseline[0].lower() == "defaults":
            print("End of", currentsection, sectionname)
            currentsection = "DEFAULTS"
            print("")
            print("Start of", currentsection, "section")

        # start of a frontend section
        elif parseline[0].lower() == "frontend":
            print("End of", currentsection, sectionname)
            currentsection = "FRONTEND"
            sectionname = parseline[1]
            frontend_section_name.append(sectionname)
            frontend_section_value.append("")
            print("")
            print("Start of", currentsection, "section named", sectionname)

        # start of a backend section
        elif parseline[0].lower() == "backend":
            print("End of", currentsection, sectionname)
            currentsection = "BACKEND"
            sectionname = parseline[1]
            backend_section_name.append(sectionname)
            backend_section_value.append("")
            print("")
            print("Start of", currentsection, "section named", sectionname)

        # not start of any section, so add the line to whatever section we are currently in
        else:
            if currentsection == "GLOBAL":
                global_section += line
                print("Adding to", currentsection)
            elif currentsection == "DEFAULTS":
                defaults_section += line
                print("Adding to", currentsection)
            elif currentsection == "FRONTEND":
                try:
                    #print("Adding to", currentsection, sectionname, line)
                    print("Adding to", currentsection, sectionname)
                    sectionindex = frontend_section_name.index(sectionname)
                    frontend_section_value[sectionindex] += line
                except ValueError:
                    print("FRONTEND", sectionname, "not found")
            elif currentsection == "BACKEND":
                try:
                    print("Adding to", currentsection, sectionname)
                    sectionindex = backend_section_name.index(sectionname)
                    backend_section_value[sectionindex] += line
                except ValueError:
                    print("BACKEND", sectionname, "not found")
    # end if len(parseline) > 0
# end for line in configfile

# print out some results for troublshooting and development
print("Parsing complete.")
print("GLOBAL section has ", len(global_section), " characters")
#print(global_section)
print("DEFAULTS section has ", len(defaults_section), " characters")
#print(defaults_section)
print("There are ", len(frontend_section_name), " FRONTEND sections ", frontend_section_name)
#print(frontend_section_name)
#print(frontend_section_value)
print("There are ", len(backend_section_name), " BACKEND sections ", backend_section_name)
#print(backend_section_name)
#print(backend_section_value)

print("BACKEND section ", backend_section_name[10], " contains the text:")
print(backend_section_value[10])