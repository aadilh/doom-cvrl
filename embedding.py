import os
# import input_data
import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector
import numpy as np

LOG_DIR = "embedding/"
# mnist = input_data.read_data_sets("data/", one_hot=True)
data = np.load('embedding.npy')
print data.shape

with tf.device('/cpu:0'):
    embedding_var = tf.Variable(tf.stack(data, axis=0), trainable=False, name='embedding')
# Format: tensorflow/contrib/tensorboard/plugins/projector/projector_config.proto
config = projector.ProjectorConfig()

# with open(LOG_DIR+'metadata.tsv', 'w') as f:
#             for i in range(10000):
#                 c = np.nonzero(mnist.test.labels[::1])[1:][0][i]
#                 f.write('{}\n'.format(c))

# You can add multiple embeddings. Here we add only one.
embedding = config.embeddings.add()
embedding.tensor_name = embedding_var.name
# Link this tensor to its metadata file (e.g. labels).
# embedding.metadata_path = os.path.join(LOG_DIR, 'metadata.tsv')
embedding.sprite.image_path = os.path.join('master.png')
embedding.sprite.single_image_dim.extend([84, 84])
# Use the same LOG_DIR where you stored your checkpoint.
summary_writer = tf.summary.FileWriter(LOG_DIR)

session = tf.Session()
init = tf.global_variables_initializer()
session.run(init)
session.run(embedding_var)
saver = tf.train.Saver()
saver.save(session, os.path.join(LOG_DIR,"model.ckpt"), 1)


# The next line writes a projector_config.pbtxt in the LOG_DIR. TensorBoard will
# read this file during startup.
projector.visualize_embeddings(summary_writer, config)
