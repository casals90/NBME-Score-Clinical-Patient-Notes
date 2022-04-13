from typing import Tuple

import numpy as np
import tensorflow as tf
from transformers import AutoConfig, TFAutoModel, AutoTokenizer


def create_model(
        model_name: str, sequence_length: int, activation: str = "sigmoid") \
        -> tf.keras.Model:
    """
    Given a name of pretrained model and sequence length, this function downloads
    pretrained model and also it adds a dropout and dense layers.

    Args:
        model_name (str): name of pretrained model to download
        sequence_length (int): sequence length tokens
        activation (Optional, str): last layer activation function. As default it is
            sigmoid.

    Returns:
        a keras model
    """
    input_tokens = tf.keras.layers.Input(
        shape=(sequence_length,), dtype=tf.int32)
    attention_mask = tf.keras.layers.Input(
        shape=(sequence_length,), dtype=tf.int32)

    config = AutoConfig.from_pretrained(model_name, output_hidden_states=True)
    backbone = TFAutoModel.from_pretrained(model_name, config=config)

    out = backbone(input_tokens, attention_mask=attention_mask)[0]
    out = tf.keras.layers.Dropout(.2)(out)
    out = tf.keras.layers.Dense(1, activation=activation)(out)

    return tf.keras.Model(inputs=[input_tokens, attention_mask], outputs=out)


def create_inputs(
        pn_history: str, feature_text: str, tokenizer: AutoTokenizer,
        max_length: int = 512, padding: str = "max_length",
        add_special_tokens: bool = True) -> Tuple[np.array, np.array]:
    """
    
    Args:
        pn_history (str):
        feature_text (str):
        tokenizer (AutoTokenizer):
        max_length (Optional, int):
        padding (Optional, str):
        add_special_tokens (Optional, bool):

    Returns:

    """
    tokens = tokenizer(
        pn_history,
        feature_text,
        max_length=max_length,
        padding=padding,
        add_special_tokens=add_special_tokens
    )

    input_ids = np.array(tokens["input_ids"])
    attention_mask = np.array(tokens["attention_mask"])

    return input_ids, attention_mask
