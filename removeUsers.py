# Import the necessary Java libraries for file handling
from java.io import FileInputStream

# Open the "details.properties" file for reading
propInputStream = FileInputStream("details.properties")

# Create a Properties object and load the properties from the file
configProps = Properties()
configProps.load(propInputStream)

# Read the total number of domains to configure from the properties file
totalDomain_to_Configure = configProps.get("total.domain")

# Initialize a counter for the domains
counterDomain = 1

# Loop through each domain for configuration
while (counterDomain <= int(totalDomain_to_Configure)):
    # Read domain-specific properties from the properties file
    domainName = configProps.get("domain.name." + str(counterDomain))
    #adminURL = configProps.get("admin.url." + str(counterDomain))
    #adminUserName = configProps.get("admin.userName." + str(counterDomain))
    #adminPassword = configProps.get("admin.password." + str(counterDomain))
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
    x = 1

    # Loop through user deletion for the current domain
    while (x <= int(totalUsers_to_Remove)):
        userName = configProps.get("user.name." + str(x))
        try:
            # Attempt to remove a user
            cmo.removeUser(userName)
            print '-----------User Removed With Name : ', userName
        except:
            print '*************** Check If the User Name: ', userName, ' is correct...'

        x = x + 1

    print ' '
    counterDomain = counterDomain + 1
