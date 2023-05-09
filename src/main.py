from __future__ import unicode_literals
import youtube_dl
import Draw

Draw
print('Iniciar ferramenta de downlods D.V.S On ?')
option = 'y' 
option = input('Y/n:')

if option == 'y':
	print('Downlodo do videos ou apenas o audio?')
	print('1:Video')
	print('2:Apenas audio')
	print('3:Sair')
	tipo = input('>>>:')
	if tipo == '1':
		link = [input('Link: ')]
		with youtube_dl.YoutubeDL() as ydl:
			ydl.download(link)
	elif tipo == '2':
		link = [input('Link: ')]
		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
			}],
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download(link)
	elif tipo == '3':
		print('Ate uma proxima')
	else:
		print('Função inesistente')
		print('Exit Force')
elif option == 'n':
    print ('Ate uma proxima')
else:
	print('Função inesistente')
	print('Exit Force')
