import os
import re
import glob

itch_project_path = ""


# Find directory with latest version in current directory
def find_latest_version(OS):
    all_directories = glob.glob("./Exports/" + OS + "/*")
    latest_version_major = 0
    latest_version_minor = 0
    latest_version_patch = 0

    for directory in all_directories:
        match = re.match(r"./Exports/" + OS + "[\\/\\\\](\d+)\.(\d+)\.(\d+)", directory)

        if match:
            major = int(match.group(1))
            minor = int(match.group(2))
            patch = int(match.group(3))

            if major > latest_version_major:
                latest_version_major = major
                latest_version_minor = minor
                latest_version_patch = patch
            elif major == latest_version_major:
                if minor > latest_version_minor:
                    latest_version_minor = minor
                    latest_version_patch = patch
                elif minor == latest_version_minor:
                    if patch > latest_version_patch:
                        latest_version_patch = patch

    return str(latest_version_major) + "." + str(latest_version_minor) + "." + str(latest_version_patch)


def publish(platform):
    platformFolder = ""

    if platform == "windows":
        platformFolder = "Windows"
    elif platform == "linux":
        platformFolder = "Linux"
    elif platform == "html5":
        platformFolder = "Web"

    version = find_latest_version(platformFolder)
    itch_project = itch_project_path + ":" + platform
    command = "butler push --userversion " + version + " ./Exports/" + platformFolder + "/" + version + " " + itch_project

    print("Pushing " + platformFolder + " Build " + version + " to " + itch_project)
    print("Command: " + command)
    os.system(command)

##################################################################################
##################################################################################
###################################  MAIN CODE  ##################################

publish("html5")
publish("windows")
publish("linux")