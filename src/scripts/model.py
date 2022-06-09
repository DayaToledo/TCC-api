import tensorflow as tf

def get_model(X_train):
    shape = X_train.shape[1:]
    # Define model layers
    input_layer = tf.keras.Input(shape=shape)

    # Y1 output will be fed from the first dense
    first_dense = tf.keras.layers.Dense(units='128', activation='relu')(input_layer)
    y1_output = tf.keras.layers.Dense(units='1', name='EXT_PER')(first_dense)

    # Y2 output will be fed from the second dense
    second_dense = tf.keras.layers.Dense(units='128',activation='relu')(first_dense)
    y2_output = tf.keras.layers.Dense(units='1',name='AGR_PER')(second_dense)

    # Y3 output will be fed from the third dense
    third_dense = tf.keras.layers.Dense(units='128',activation='relu')(second_dense)
    y3_output = tf.keras.layers.Dense(units='1',name='CSN_PER')(third_dense)

    # Y4 output will be fed from the fourth dense
    fourth_dense = tf.keras.layers.Dense(units='128',activation='relu')(third_dense)
    y4_output = tf.keras.layers.Dense(units='1',name='EST_PER')(fourth_dense)

    # Y5 output will be fed from the fifth dense
    fifth_dense = tf.keras.layers.Dense(units='128',activation='relu')(fourth_dense)
    y5_output = tf.keras.layers.Dense(units='1',name='OPN_PER')(fifth_dense)

    # Define the model with the input layer and a list of output layers
    model = tf.keras.Model(inputs=input_layer,outputs=[y1_output, y2_output, y3_output, y4_output, y5_output])

    return model


def compile_model(model):
    # Specify the optimizer, and compile the model with loss functions for both outputs
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(
        optimizer=optimizer,
        loss={
            'EXT_PER': 'mse', 
            'AGR_PER': 'mse',
            'CSN_PER': 'mse',
            'EST_PER': 'mse',
            'OPN_PER': 'mse'
        },
        metrics={
            'EXT_PER':tf.keras.metrics.RootMeanSquaredError(),
            'AGR_PER':tf.keras.metrics.RootMeanSquaredError(),
            'CSN_PER':tf.keras.metrics.RootMeanSquaredError(),
            'EST_PER':tf.keras.metrics.RootMeanSquaredError(),
            'OPN_PER':tf.keras.metrics.RootMeanSquaredError(),
        }
    )
    return model


def train_model(X_train, X_test, y_train, y_test, model):
    model.fit(
        X_train, 
        y_train,
        epochs=10, 
        batch_size=10, 
        validation_data=(X_test, y_test)
    )
    return