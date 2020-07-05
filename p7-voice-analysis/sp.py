from pocketsphinx import Pocketsphinx

ps = Pocketsphinx(verbose=True)
ps.decode()

print(ps.hypothesis())