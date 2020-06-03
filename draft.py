from rnnoise_wrapper import RNNoise


denoiser = RNNoise(path_to_lib='rnnoise_wrapper/rnnoise-windows.exe')

audio = denoiser.read_wav('test.wav')
filtered_audio = denoiser.filter(audio)
denoiser.write_wav('test_denoised.wav', filtered_audio)

signal=0
i=0
win_len=0
threshold=0

window = signal[i:(i+win_len)]
energy = ((window - window.mean()) ** 2).sum()
voice = energy > threshold



