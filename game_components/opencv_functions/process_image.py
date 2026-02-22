import cv2 as cv
import pygame
import argparse

def detectAndDisplay(frame,faces):
    #-- Detect faces
    #faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        frame = cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0 ), 4)
        #cv.imshow('Capture - Face detection', frame)
        if w*h<25000:  
            if (x + (w // 2))<(250): 
                return pygame.K_UP #esquerda
            elif (x + (w // 2))>(400):
                return pygame.K_DOWN #direita
        #zona de segurança
        return None
        