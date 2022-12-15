
import tensorflow as tf

text = "I love cats"
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10000, oov_token='<oov>')
tokenizer.fit_on_texts([text])

vocab = [ "a", "b", "c", "d", "e", "f", "g", "h", "I", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_" ]
data = tf.constant([["_", "_", "_", "I"], ["l", "o", "v", "e"], ["c", "a", "t", "s"]])

layer = tf.keras.layers.StringLookup(vocabulary=vocab)
sequences_mapping_string = layer(data)
sequences_mapping_string = tf.constant( sequences_mapping_string, shape=(1,12) )
print( 'result: ' + str( sequences_mapping_string ) )

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
: Model Initialize
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
model = tf.keras.models.Sequential([
	tf.keras.layers.InputLayer(input_shape=( 12 ), batch_size=1, name='layer_input'),
	tf.keras.layers.Dense(12, activation='relu', name='layer_dense_1')
])

model.summary()

prediction = model.predict(sequences_mapping_string) # an integer

print( "text: " + str( text ) )
print( "seqs: " + str( [ sequences_mapping_string ] ) )
print( "prediction: " + str( prediction[0] ) )

decoder = tf.keras.layers.StringLookup(vocabulary=vocab, output_mode="int", invert=True)
result = decoder(sequences_mapping_string)
print( "encode: " + str( sequences_mapping_string ) )
print( "decode: " + str( result ) )

mapping_vocab = [ "_", "I", "l", "o", "v", "e", "c", "a", "t", "s" ]
string_matching = [ 27, 9, 12, 15, 22, 5, 3, 1, 20, 19 ]
string_matching_reverse = [ 1/27, 1/9, 1/12, 1/15, 1/22, 1/5, 1/3, 1/1, 1/20, 1/19 ]

print( tf.math.multiply( tf.constant(string_matching, dtype=tf.float32), tf.constant(string_matching_reverse, dtype=tf.float32 ), name=None ) )
