import cv2
import os

path = os.getcwd()

def take_photo(name: str):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise 'cannot open camera'
        exit(1)

    while True:

        ret, frame = cap.read()
        if not ret:
            raise 'cannot receive frame (stream end?)'
        
        cv2.imshow('frame', frame)

        key = cv2.waitKey(1)
        if key == ord('c'):
            _save_photo(name,  frame)
            print('Foto guardada!')
            print('Presiona "Q" Para salir!')
        elif key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def _save_photo(name: str, frame):
    dir_photo = os.path.join(path, 'fotos', name)

    if not os.path.exists(dir_photo):
        os.mkdir(dir_photo)

    photo_name = os.path.join(dir_photo, name + '.png')
    cv2.imwrite(photo_name, frame)

if __name__ == '__main__':
    name = input("Ingrese su nombre: ")
    take_photo(name)
