import pygame

# Инициализировать PyGame
pygame.init()

# Установить громкость
volume = 0.5
pygame.mixer.music.set_volume(volume)

# Загрузить музыкальный файл
filename = 'C:/Users/drago/Desktop/kazakhstan-ugrozhaet-nam-bombardirovkoi.mp3'
pygame.mixer.music.load(filename)

# Воспроизвести музыку
pygame.mixer.music.play()

# Запустить основной цикл
running = True
while running:
    # Обработать события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Остановить музыку и закрыть PyGame
pygame.mixer.music.stop()
pygame.quit()
