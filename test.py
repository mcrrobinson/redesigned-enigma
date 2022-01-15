from posixpath import split


content = ["0,Adam,Garvey,211.34.105.81",
"1,Brittany,Adams,81.239.71.65",
"2,Loyd,Calico,134.73.13.229",
"3,Samuel,Coulter,18.89.183.177",
"4,Wayne,Strong,25.158.249.68",
"5,Mark,Cage,212.190.30.27",
"6,Ramona,Dingle,90.6.170.139",
"7,Kathleen,Cutter,143.7.106.149",
"8,Christopher,Smith,217.132.99.42",
"9,Douglas,Peck,3.1.251.41",
"10,Maria,Pies,220.236.96.97",
"11,Maria,Pies,220.236.96.97,this throw off",
"12,Maria,Pies,220.236.96.97",
"13,Maria,Pies,220.236.96.97",
"14,Maria,Pies,220.236.96.97",
"14,Maria,Pies,220.236.96.97",
"14,Maria,Pies,220.236.96.97",
"14,Maria,Pies,220.236.96.97"]

previous_row_length = None
current_incrementation_counter = 0
for index, item in enumerate(content):
    split_row = item.split(',')
    current_row_length = len(split_row)
    
    if index == current_incrementation_counter:
        
        if current_row_length == previous_row_length or previous_row_length == None:
            print("Same", current_row_length)
        else:
            print("Pickle in the mix.")
            
        previous_row_length = current_row_length
        current_incrementation_counter = 2 ** index