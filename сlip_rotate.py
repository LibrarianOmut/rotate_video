import cv2
import os

def rotate_video(input_path, output_path):
    # Открываем видеофайл
    cap = cv2.VideoCapture(input_path)
    
    # Получаем параметры видео
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Кодек для сохранения видео
    
    # Меняем ширину и высоту местами для поворота на 90 градусов
    out = cv2.VideoWriter(output_path, fourcc, fps, (height, width))
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Поворачиваем кадр на 90 градусов
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        
        # Записываем повернутый кадр в выходное видео
        out.write(rotated_frame)
    
    # Освобождаем ресурсы
    cap.release()
    out.release()

def process_videos(input_folder, output_folder):
    # Проверяем, существует ли папка base_videos
    if not os.path.exists(input_folder):
        print(f"Папка {input_folder} не найдена!")
        return
    
    # Создаем папку для сохранения повернутых видео, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Получаем список всех файлов в папке base_videos
    video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]
    
    if not video_files:
        print(f"В папке {input_folder} нет видеофайлов в формате MP4!")
        return
    
    # Обрабатываем каждое видео
    for video_file in video_files:
        input_path = os.path.join(input_folder, video_file)
        output_path = os.path.join(output_folder, video_file)
        
        print(f"Обработка видео: {input_path}")
        rotate_video(input_path, output_path)
        print(f"Видео сохранено: {output_path}")

if __name__ == "__main__":
    # Папка с исходными видео
    input_folder = "base_videos"
    
    # Папка для сохранения повернутых видео
    output_folder = "rotated_videos"
    
    # Обрабатываем видео
    process_videos(input_folder, output_folder)