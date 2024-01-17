# password complexity requirements: Disabled 
SeSecPwdComp -PasswordComplexity 0
#This command seems to be disabling password complexity requirements. The SeSecPwdComp might be a custom or external command/utility used to configure security settings, and setting the -PasswordComplexity parameter to 0 likely means that password complexity requirements are being disabled.

# SMBv1 client driver: Disabled
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart
# This command disables the SMBv1 client driver. SMBv1 is an older version of the Server Message Block protocol, and disabling it enhances security as it is considered a security risk.

# Force Restart
$restartRequired = Read-Host "Changes have been made. Do you want to restart now? (Y/N)"
# This part of the script prompts the user with a message indicating that changes have been made and asks whether the user wants to restart the computer. The response is stored in the $restartRequired variable.

if ($restartRequired -eq "Y") {
    Restart-Computer -Force
} else {
    Write-Host "Please restart the computer to apply the changes."
}
# Depending on the user's input (Y or y for yes), the script either forcefully restarts the computer using Restart-Computer -Force, or it informs the user to manually restart the computer to apply the changes.





From my classmate Israel Quirola Salas, he was helping me!
