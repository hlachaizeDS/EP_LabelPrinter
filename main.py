from LabelPrinter import *
import easygui
import time

#Connection to the printer
host = "192.168.1.103"
port = 9100
label_printer=LabelPrinter(host,port)

#Variables
label_dict = {
    "$enzyme" : "",
    "$full_batch_name" : "",
    "$short_batch_name" : "",
    "$label_number" : "0"
}

#Messages
query_dict = {
    "$enzyme" : "Enzyme (TDT, PAP, EndoV or EndoQ)",
    "$full_batch_name" : "Full batch name",
    "$short_batch_name" : "Short batch name",
    "$label_number" : "Number of labels to print"
}

#template_paths
path_dict = {
    "TDT" : "TDT_EPlabel.cmd",
    "PAP" : "PAP_EPlabel.cmd",
    "EndoV" : "EndoV_EPlabel.cmd",
    "EndoQ" : "EndoQ_EPlabel.cmd"
}

#Get infos from the user, by printing out desired Messages
for key in label_dict:
    label_dict[key]=easygui.enterbox(msg=query_dict[key])
    #if the wrong enzyme is selected, send an error message
    if key=="$enzyme" and label_dict[key] not in list(path_dict.keys()):
        easygui.msgbox(msg="Wrong enzyme type")
        exit()
    #if the user has cancelled, exit
    if label_dict[key]==None:
        exit()


for label_number in range(int(label_dict["$label_number"])):
    label_file = open(path_dict[label_dict["$enzyme"]], 'r')
    label_lines = label_file.readlines()

    for line in label_lines:

        line = line.replace("$full_batch_name",label_dict["$full_batch_name"])
        line = line.replace("$short_batch_name",label_dict["$short_batch_name"])
        line = line.replace("$bottle_number",str(label_number))
        r = label_printer.send(line, 0)
        print(line)

    time.sleep(0.5)
