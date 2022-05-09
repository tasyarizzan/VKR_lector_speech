**EN**
A desktop application for assessing the expressiveness of a lecturer's speech.
Desctop app for assessing teacher's expressiveness.
/ * A desktop application written in Python. The ability to analyze speech as from a microphone in real time. The estimated indicators of the expressiveness of speech and their dynamics: loudness, monotony, spatial impression (acoustics), tonal balance (ratio of high and low frequencies), silence / speech ratio, tempo, speech-to-noise ratio (sound transparency), noticeable interference and distortion.

Possible solutions
Interference and Distortion Visibility: Confidence score / number of words recognized.

Pace: number of words / duration in minutes.

Structure
The audio_classification.py module analyzes audio recording for speech and non-speech. The voice2vec.py module describes the voice2VecModel class, which parses and displays the result of the analysis of the recording on the screen. It is also possible to get the results in the form of an excel file for further use and calculations. The Voice2VecModel class contains functions that receive parameters when the class is initialized. Each of the functions get_volume (), get_silent_sg (), get_monotone (), get_tempo (), get_otnosh (), get_tone_balance (), get_intfrnce_distn (), get_noise (), get_spat_imprsn () impression are returned (values: acoustics), mono balance (treble to bass ratio), treble to bass ratio, sound-to-sound ratio, noticeable interference and distortion.

For the get_volume () functions, the thresholds for quiet and loud speech are configured (Figure 18) using attributes such as THRESHOLD_LW and THRESHOLD_LD. These attributes, in turn, depend on the local settings of the hardware (speaker and microphone).

Rice. 18. Setting thresholds

The logical function for classifying the language "speech - not speech" is_speech (), imported from the audio_classify.py module, includes what is analyzed and whether the audio file is speech. The input is the path of the audio file in the system.



**RU**
# Десктопное приложение для оценки показателей выразительности речи лектора.
# Desktop app for evaluating expressiveness indicators of lecturer speech.

#### Десктопное приложение, написанное на языке Python. Возможность анализа речи как с микрофона в режиме реального времени, так и из аудио и видео файлов. Оцениваемые показатели выразительности речи и их динамики: ~~громкость~~, ~~монотонность~~, пространственное впечатление (акустика), тональный баланс (соотношения высоких и низких частот), ~~соотношение тишина/речь~~, ~~темп~~, соотношение речи и шума (прозрачность звука), заметность помех и искажений.

# Возможные решения
Заметность помех и искажений: показатель уверенности / количество слов, которые распознались.

Темп: количество слов / на длительность в минутах.


# Структура 
Модуль audio_classification.py анализирует звукозапись на речь и не речь. В модуле voice2vec.py описан класс voice2VecModel, который анализирует и выдает результат анализа аудиозаписи на экран. Также есть возможность получить результаты в виде excel файла для дальнейшего использования и вычислений. Класс Voice2VecModel содержит функции, получающие параметры при инициализации класса. Каждая из функций get_volume(), get_silent_sg(), get_monotone(), get_tempo(), get_otnosh(), get_tone_balance(), get_intfrnce_distn(), get_noise(), get_spat_imprsn() возвращаются значения: громкость, монотонность, пространственное впечатление (акустика), тональный баланс (соотношения высоких и низких частот), соотношение тишина/речь, темп, соотношение речи и шума (прозрачность звука), заметность помех и искажений.в виде свойств класса соответственно.

Для функции get_volume() настраиваются пороги для тихой и громкой речи (Рис. 18), с использованием таких атрибутов, как THRESHOLD_LW и THRESHOLD_LD. Данные атрибуты в свою очередь зависят от локальных настроек аппаратной части (динамика и микрофона).

Рис. 18. Настройка порогов

Логическая функция для классификации файла на «речь – не речь» is_speech(), импортируется из модуля audio_classify.py, вследствие чего проводится анализ и определяется является ли аудио файл речью. На вход подается путь аудиофайла в системе.
