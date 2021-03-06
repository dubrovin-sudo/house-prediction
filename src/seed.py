import os
import random
import numpy as np


def set_seed(seed_value: int = 12321) -> None:
    """
    Set a seed value
    :param seed_value:
    :return:
    """
    # 1. Set `PYTHONHASHSEED` environment variable at a fixed value
    os.environ['PYTHONHASHSEED'] = str(seed_value)

    # 2. Set `python` built-in pseudo-random generator at a fixed value
    random.seed(seed_value)

    # 3. Set `numpy` pseudo-random generator at a fixed value
    np.random.seed(seed_value)

    # 4. Set `tensorflow` pseudo-random generator at a fixed value
    # import tensorflow as tf
    # tf.set_random_seed(seed_value)
    # 5. For layers that introduce randomness like dropout
    # model.add(Dropout(0.25, seed=seed_value))
    # 6 Configure a new global `tensorflow` session
    # from keras import backend as K
    # session_conf = tf.ConfigProto(intra_op_parallelism_threads=1,
    #                               inter_op_parallelism_threads=1)
    # sess = tf.Session(graph=tf.get_default_graph(), config=session_conf)
    # K.set_session(sess)
