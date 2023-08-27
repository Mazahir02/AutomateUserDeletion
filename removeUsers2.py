# Import the necessary Java libraries for file handling
from java.io import FileInputStream, BufferedReader, InputStreamReader, File
from java.util import ArrayList
from java.lang import String

import sys  # Import the sys module

# Open the "details.properties" file for reading
propInputStream = FileInputStream("details.properties")

# Create a Properties object and load the properties from the file
configProps = Properties()
configProps.load(propInputStream)

# Read the total number of domains to configure from the properties file
totalDomain_to_Configure = configProps.get("total.domain")

# Initialize empty lists to store usernames
usernames = []

# Open the CSV file for reading
csvfile = File('<path for CSV File>/userDetails.csv')
reader = BufferedReader(InputStreamReader(FileInputStream(csvfile)))

# Read the CSV file line by line
line = reader.readLine()
while line is not None:
    # Split the line into parts using a comma as the delimiter
    parts = line.split(",")
    if len(parts) >= 0 :
        # Assuming the first part contains usernames(modify as needed)
        username = parts[0]
        # Append the username to its respective list
        usernames.append(username)
    # Read the next line
    line = reader.readLine()

# Close the CSV file when you're done with it
reader.close()

# Initialize a counter for the domains
counterDomain = 1

# Loop through each domain for configuration
while (counterDomain <= int(totalDomain_to_Configure)):
    # Read domain-specific properties from the properties file
    domainName = configProps.get("domain.name." + str(counterDomain))
    #adminURL = configProps.get("admin.url." + str(counterDomain))
    #adminUserName = configProps.get("admin.userName")
    #adminPassword = configProps.get("admin.password")
    realmName = configProps.get("security.realmName")
    totalUsers_to_Remove = configProps.get("total.username")

    try:
        # Attempt to connect to the WebLogic Server with admin credentials
        #connect(adminUserName, adminPassword, adminURL)
        connect()
        serverConfig()

        # Construct the authenticator path
        authenticatorPath = '/SecurityConfiguration/' + domainName + '/Realms/' + realmName + '/AuthenticationProviders/DefaultAuthenticator'
        print authenticatorPath

        # Change the current working directory to the authenticator path
        cd(authenticatorPath)
    except:
        print 'Exception Raised'

    print ' '
    print ' '


    print 'Deleting Users . . .'

    # Loop through user deletion for the current domain
    for i in range(len(usernames)):
        userName = usernames[i]
        try:
            if userName == 'abc_456':
                print 'Dont remove Application Admin user : ', userName,'!!!'
                sys.exit(0)
            else:
            # Attempt to remove a user
                cmo.removeUser(userName)
                print 'User Removed With Name : ', userName
        except:
            print 'Check If the User Name: ', userName, ' is correct...'


    print ' '
    counterDomain = counterDomain + 1
