# python3-pyinstaller-base-app-codesigning
Base project example to create an application with Python3 and PyInstaller, including all necessary build scripts.

This Repo creates a project that you can clone to streamline MacOS python desktop app development. It contains all necessary scripts to build your final project, as well as code-sign them from Apple (Developer Account required).

# Setup
## Part 1: Developer Account
Note: This section is taken from: https://gist.github.com/txoof/0636835d3cc65245c6288b2374799c43
### (1/2) Create a developer account with Apple
- Go to https://developer.apple.com and shell out $99 for a developer account
- Download and install X-Code from the Apple App Store
- Open and run X-Code app and install whatever extras it requires
- Open the preferences pane (cmd+,)
- click the + in the lower right corner
choose Apple ID
- enter your apple ID and password
### (2/2) Create an App-Specific password for altool to use
- Instructions from Apple to create: https://support.apple.com/en-us/HT204397
- Open KeyChain Access
- Create a "New Password Item"
- Keychain Item Name: Developer-altool
- Account Name: your developer account email
- Password: the application-specific password you just created

## Part 2: Get Your Hashes
### (1/2) Create Certificates with XCode
- Open XCode
- In the top-apple Menu, go to XCode > Preferences > Accounts > Your Account > In the team, chose the Admin team > Manage Certificates in the bottom-right
- click the plus in the bottom corner
- choose "Developer ID Application"
- repeating, click the plus in the bottom corner
- choose "Developer ID Installer"
### (2/2) Get Certificates and Add to Project
- run:
> security find-identity -p basic -v
- your output will look like:
> 1) HASH_OF_ID_HERE "Developer ID Application: ..."
> 2) HASH_OF_ID_HERE "Developer ID Installer: ..."
> 
>    2 valid identities found
- copy the appropriate hashes into the build file in 
> ./build-scripts/build
## Step 3: Configure the ./build-scripts/build File
There are explanatory comments next to each variable at the top of the ```./build-scripts/build``` as to what they represent. You must fill these out for this to work.
Additionally, you will need to configure two settings in the .spec file:
### Create your Identifiers
- developer.apple.com
- choose "account" in top right
- login
- "Certificates, IDs, and Profiles"
- on the left, switch to "Identifiers"
- create two App IDs, one for your .app and one for your .pkg
- it may be helpful to do something like ```com.your-domain.app-name``` for the .app and ```com.your-domain.app-name.pkg``` for the .pkg
### In the .SPEC file
- at the way bottom, set the 'name' to the same as 'APP' in the ./build-scripts/build file
- at the way bottom, set bundle_identifier=```bundle_id_for_your_app``` using the identifier for the .app
> app = BUNDLE(coll,
>              name='My New App.app',
>              icon=None,
>              bundle_identifier=bundle_id)
# Coding Your App
Begin to code your application in the ```./app/app.py``` file. When you are satisfied, proceed to the next section.
# Building & Packaging Your App
Individual scripts are provided in the ```./build-scripts/``` directory. Here, you can customize the individual level scripts so you can choose which process to run (i.e., you may want to build your .app for testing purposes and therefore do not want a .pkg or to notorize)
The main workflow is in ```./build-scripts/build``` and can be run with ```bash ./build-scripts/build```.
