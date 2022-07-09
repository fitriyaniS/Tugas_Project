{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "58b0c275-3e89-4058-9eb6-b5b943b2a849",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_12412\\3784041276.py\u001b[0m in \u001b[0;36m<cell line: 49>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     49\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mfile_video_stream\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0misOpened\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     50\u001b[0m     \u001b[1;31m#get the current frame from the video stream as an image\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 51\u001b[1;33m     \u001b[0mret\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mcurrent_frame\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfile_video_stream\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     52\u001b[0m     \u001b[1;31m#resize the current frame to 1/4 size to proces faster\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     53\u001b[0m     \u001b[0mcurrent_frame_small\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mresize\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcurrent_frame\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mfx\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0.25\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mfy\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0.25\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "# -*- coding: utf-8 -*-\n",
    "\"\"\"\n",
    "@author: abhilash\n",
    "\"\"\"\n",
    "\n",
    "#importing the required libraries\n",
    "import cv2\n",
    "import face_recognition\n",
    "\n",
    "#capture the video from default camera \n",
    "file_video_stream = cv2.VideoCapture('vid.mp4')\n",
    "\n",
    "#load the sample images and get the 128 face embeddings from them\n",
    "zahra_image = face_recognition.load_image_file('zahra.jpg')\n",
    "zahra_face_encodings = face_recognition.face_encodings(zahra_image)[0]\n",
    "\n",
    "wina_image = face_recognition.load_image_file('wina.jpg')\n",
    "wina_face_encodings = face_recognition.face_encodings(wina_image)[0]\n",
    "\n",
    "pitri_image = face_recognition.load_image_file('pitri.jpg')\n",
    "pitri_face_encodings = face_recognition.face_encodings(pitri_image)[0]\n",
    "\n",
    "lendi_image = face_recognition.load_image_file('lendi.jpg')\n",
    "lendi_face_encodings = face_recognition.face_encodings(lendi_image)[0]\n",
    "\n",
    "yevan_image = face_recognition.load_image_file('yevan.jpg')\n",
    "yevan_face_encodings = face_recognition.face_encodings(yevan_image)[0]\n",
    "\n",
    "aldi_image = face_recognition.load_image_file('aldi.jpg')\n",
    "aldi_face_encodings = face_recognition.face_encodings(aldi_image)[0]\n",
    "\n",
    "johar_image = face_recognition.load_image_file('johar.jpg')\n",
    "johar_face_encodings = face_recognition.face_encodings(johar_image)[0]\n",
    "\n",
    "urip_image = face_recognition.load_image_file('urip.jpg')\n",
    "urip_face_encodings = face_recognition.face_encodings(urip_image)[0]\n",
    "\n",
    "#save the encodings and the corresponding labels in seperate arrays in the same order\n",
    "known_face_encodings = [zahra_face_encodings, wina_face_encodings, pitri_face_encodings, lendi_face_encodings, yevan_face_encodings, aldi_face_encodings, johar_face_encodings, urip_face_encodings]\n",
    "known_face_names = [\"zahra\", \"wina\", \"pitri\", \"lendi\", \"yevan\", \"aldi\", \"johar\", \"urip\"]\n",
    "\n",
    "\n",
    "#initialize the array variable to hold all face locations, encodings and names \n",
    "all_face_locations = []\n",
    "all_face_encodings = []\n",
    "all_face_names = []\n",
    "\n",
    "#loop through every frame in the video\n",
    "while (file_video_stream.isOpened):\n",
    "    #get the current frame from the video stream as an image\n",
    "    ret,current_frame = file_video_stream.read()\n",
    "    #resize the current frame to 1/4 size to proces faster\n",
    "    current_frame_small = cv2.resize(current_frame,(0,0),fx=0.25,fy=0.25)\n",
    "    #detect all faces in the image\n",
    "    #arguments are image,no_of_times_to_upsample, model\n",
    "    all_face_locations = face_recognition.face_locations(current_frame_small,number_of_times_to_upsample=1,model='hog')\n",
    "    \n",
    "    #detect face encodings for all the faces detected\n",
    "    all_face_encodings = face_recognition.face_encodings(current_frame_small,all_face_locations)\n",
    "\n",
    "\n",
    "    #looping through the face locations and the face embeddings\n",
    "    for current_face_location,current_face_encoding in zip(all_face_locations,all_face_encodings):\n",
    "        #splitting the tuple to get the four position values of current face\n",
    "        top_pos,right_pos,bottom_pos,left_pos = current_face_location\n",
    "        \n",
    "        #change the position maginitude to fit the actual size video frame\n",
    "        top_pos = top_pos*4\n",
    "        right_pos = right_pos*4\n",
    "        bottom_pos = bottom_pos*4\n",
    "        left_pos = left_pos*4\n",
    "        \n",
    "        #find all the matches and get the list of matches\n",
    "        all_matches = face_recognition.compare_faces(known_face_encodings, current_face_encoding)\n",
    "       \n",
    "        #string to hold the label\n",
    "        name_of_person = 'Unknown face'\n",
    "        \n",
    "        #check if the all_matches have at least one item\n",
    "        #if yes, get the index number of face that is located in the first index of all_matches\n",
    "        #get the name corresponding to the index number and save it in name_of_person\n",
    "        if True in all_matches:\n",
    "            first_match_index = all_matches.index(True)\n",
    "            name_of_person = known_face_names[first_match_index]\n",
    "        \n",
    "        #draw rectangle around the face    \n",
    "        cv2.rectangle(current_frame,(left_pos,top_pos),(right_pos,bottom_pos),(255,0,0),2)\n",
    "        \n",
    "        #display the name as text in the image\n",
    "        font = cv2.FONT_HERSHEY_DUPLEX\n",
    "        cv2.putText(current_frame, name_of_person, (left_pos,bottom_pos), font, 0.5, (255,255,255),1)\n",
    "    \n",
    "    #display the video\n",
    "    cv2.imshow(\"Webcam Video\",current_frame)\n",
    "    \n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "        break\n",
    "\n",
    "#release the stream and cam\n",
    "#close all opencv windows open\n",
    "file_video_stream.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0234bb39-613f-466a-88d0-7289f0073204",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
