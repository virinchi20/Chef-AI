import os
import cv2
import agents as ag



def main():

    food = ag.extract_food_name("Grilled Cheese")
    print(food.food_to_cook)
    
    video = cv2.VideoCapture(0)

    if not video.isOpened():
        print("Error: Could not access camera")
        exit()
    
    while True:
        ret, frame = video.read()

        if not ret:
            print("Error: Could not capture video")
    


        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    video.release()
    cv2.destroyAllWindows()
        


if __name__ == "__main__":
    main()