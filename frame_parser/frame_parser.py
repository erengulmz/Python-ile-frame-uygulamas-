import cv2
import os
import uuid
import glob
#get video name and video directory
video_list=glob.glob("video_main/*.mp4")
#if video_main folder cannot be reached, create new one 
if(len(video_list)==0):
    print("The video_main folder cannot be reached.")
    video_folder_check=input("Do you want a create video_folder? [y/n]:")
    if(video_folder_check == 'y' or video_folder_check == 'Y'):
        os.makedirs('video_main',exist_ok=True)
        print("The folder has been created. Please embed your videos in it. Then run the program again.")
        exit()        
    elif(video_folder_check == 'n' or video_folder_check == 'N'):
        print("Folder creation denied. In order to use the program, create a folder named video_main, place your videos in it and try again.")
        exit()
    else:
        print("Wrong Input. Please Try Again")
        exit()       
else:
    print("Your Video List:" + str(video_list))
    print("Default Frame Number:10")
#frame-folder counter 
frame_counter=0
counter=0
#the number of frames the video will be divided into
###frame_number=input('Enter a Frame Number:') ### if the user asked for the frame number
frame_number=5
#create the folder
while(len(video_list)>counter):
    os.makedirs('frames/'+video_list[counter][11::],exist_ok=True)
    counter+=1
counter=0
#create the .jpg files
while(len(video_list)>counter):
    cap=cv2.VideoCapture(video_list[counter])
    while(cap.isOpened()):
        flag,frame=cap.read()
        if (flag==False):
            break
        if(frame_counter%int(frame_number)==0):
            unique_filename=str(uuid.uuid1())
            path='frames/'+video_list[counter][11::]+'/'+str(frame_counter)+'_'+str(unique_filename)[:8]+'.jpg'
            cv2.imwrite(path,frame)
        frame_counter+=1   
    counter+=1
    frame_counter=0
    cap.release()
print("Process Success. Please Check the Frames Folder")
cv2.destroyAllWindows