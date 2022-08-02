The application is inside LabGui_v1.4 folder, just cick on LabGui_v1.4.exe to run it.
Do not move or remove anything from this folder, otherwise the app will not run properly.
If you want to use the app without having to search the .exe file inside the folder, 
right click on the folder, select "Create a shortcut" and then move the shortcut wherever you want. 
Do not move the .exe file itself, it needs to be in the same folder as the bunch of .dll files to run properly. 

With LabGui_v1.4, you can now perofom in silico digestion on proteins.
several enzymes are already implemented: Trypsin as well as some GENOVIS enzymes: FabRICATOR, FabULOUS and GingisKHAN. 
This module is fully functional with open, save and save as functions.
as an output, you will find the MW of the digested fragment in its identifier.
Please note that in current state, in silico digestion cannot be used to digest a complete proteome.
It will slow down the app in a best case scenario, completely freeze it in the worst case. 
A limit of 100,000 character has been implemented to prevent freezing, you can still try to open it, but a warning will be displayed before.

PATCHNOTE:

1.1
# Corrected a bug which prevent the SSPC logo to be displayed correctly on the second window.
# Open, Save, Save as, and Manual actions are now available.
# Searches can be saved in .pdf format or .txt format.

1.2
# HTTPError and URLError are now indicated if something wrong happened during search
# Searches can now be saved and loaded in .xlsx format
# Spaces in the beginning and at the end of the component name input will not bring an error anymore. 
# Find Weight Form is now scrollable, which allow to display more than 20 values to the screen without resizing the window to
  access the bottom of the form.
# following the previous patch, the number of component has been increased to 99 (seriously, is there a buffer where you will need to
  use that much components?). 
# Edit menu removed because useless.
# View menu added with possibility to switch between Light mode and Dark mode (yeah, also useless but fun at least :D)
# Find Protein tab implemented: allows to quickly access the .fasta of a protein using its uniprot ID.

1.3
# You can now access to Uniprot information about the protein via the radiobutton.
# fasta output has been reworked in order to be scrollable, huge proteins will not be truncated anymore.
# fasta and info from Uniprot can now be saved.
# corrected an issue of keeping an empty value as a save filename when cancelling Save window which cause bug during the next save attempt.
# Tool Buttons with functional shortcuts on now available for each actions (Open, Save, Save as, View, Help) in the forms.
# View mode (light or dark) will stay in memory and will be displayed on the next session.

1.4
# in Silico Digestion tab implemented.
# enzymes implemented: Trypsin, FabRICATOR IdeS, FabULOUS SpeB, GingisKHAN Kgp.
# MW calculation implemented for the module in Silico Digestion.


You can report bugs and send your advices at this address:
stanislas.helle@ul.ie

Hope you will find this app usefull! :)