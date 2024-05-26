import os
import laion_clap

audio_dir = os.path.join(os.path.dirname(__file__), os.pardir, 'audio')

model = laion_clap.CLAP_Module(enable_fusion=False)
model.load_ckpt() # download the default pretrained checkpoint.

classes = [
  "plastic bottle",
  "can",
  "glass",
  "paper",
]

class_embeds = model.get_text_embedding(classes)

audio_path = 'glass/glass2.mp3'
audio_file = [
  os.path.join(audio_dir, audio_path)
]
audio_embed = model.get_audio_embedding_from_filelist(x = audio_file, use_tensor=False)

max_sim = 0
idx = 0

for i in range(class_embeds.shape[0]):
  class_embed = class_embeds[i]

  sim = audio_embed @ class_embed.T
  print([classes[i], sim])

  if (sim > max_sim):
    max_sim = sim
    idx = i

print(classes[idx])