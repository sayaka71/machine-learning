import numpy as np  

def crop_img(im, crop_size = 60):
  '''
  画像周りをcrop_sizeだけ切り落とす
  params
  ------------------------------
  im: image(Numpy Array)
  crop_size: crop size (int)
  ------------------------------
  returns
  ------------------------------
  im: coropped image(Numpy Array)
  '''

  im = im[crop_size:-crop_size, crop_size:-crop_size, :]

  return im
  