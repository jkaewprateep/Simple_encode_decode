# Simple_encode_decode
Simple encoding-decoding transmisstion messages for model training results in parameters, you can add one or more input and keys there are many of algorithms including ACS that is default or DCS and many algorithms this one is simplest to learn from networks communciatoins such as TCP/IP and transcription messages.

## input ##

Create input as text vectorize, it is benefits you do it by using text vectorized or you can do it by token or simply dictionary method but it is not indicated the complexity except it is using for FF message ( fast forward message valid time is concern )
```
text = "I love cats"
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10000, oov_token='<oov>')
tokenizer.fit_on_texts([text])

vocab = [ "a", "b", "c", "d", "e", "f", "g", "h", "I", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_" ]
data = tf.constant([["_", "_", "_", "I"], ["l", "o", "v", "e"], ["c", "a", "t", "s"]])

layer = tf.keras.layers.StringLookup(vocabulary=vocab)
sequences_mapping_string = layer(data)
sequences_mapping_string = tf.constant( sequences_mapping_string, shape=(1,12) )
```

## Networks training ##
Model training for further prediction, if you do text vectorized mapping correct is part is very easy but you need to create of keys + input + variable from environment correctly and you do not need to make too much of the complex message composed that is because we need fast communicatons and it is only valid at the time they are in conversaition, salts or count number they telling space indicated or stikes.
```
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
: Model Initialize
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
model = tf.keras.models.Sequential([
	tf.keras.layers.InputLayer(input_shape=( 12 ), batch_size=1, name='layer_input'),
	tf.keras.layers.Dense(12, activation='relu', name='layer_dense_1')
])

model.summary()

prediction = model.predict(sequences_mapping_string) # an integer
```

## Background logics ##
The encode-decoder background logics you can add keys or multiple input.
```
decoder = tf.keras.layers.StringLookup(vocabulary=vocab, output_mode="int", invert=True)
result = decoder(sequences_mapping_string)
print( "encode: " + str( sequences_mapping_string ) )
print( "decode: " + str( result ) )

mapping_vocab = [ "_", "I", "l", "o", "v", "e", "c", "a", "t", "s" ]
string_matching = [ 27, 9, 12, 15, 22, 5, 3, 1, 20, 19 ]
string_matching_reverse = [ 1/27, 1/9, 1/12, 1/15, 1/22, 1/5, 1/3, 1/1, 1/20, 1/19 ]
```

## Files and Directory ##
```
1. AI - simple encryption alg found from books.png : result
2. simple_decoder.py : simple codes
3. README.md : readme file
```

## Result image ##
![Alt text](https://github.com/jkaewprateep/Simple_encode_decode/blob/main/AI%20-%20simple%20encryption%20alg%20found%20from%20books.png?raw=true "Title")


## From BAD BOY II Movies ##

| Name | to | Name |
| --- | --- | --- |
| DNILE | TOURS | ENGLAND |
| RICHEL | WILLAMS | HALE |
| SMITA | JONES | RAFLTTY |
| WATKINS | HARRINGTON | DELGAIRO |
| HASTINGS | DUNFACE | ABSENT |
| AMOUL | | |

| Name | to | Name | Tag |
| --- | --- | --- | --- |
| SMITA | GZOSY | FZZYL | GROZZY FENZZY |
| JONES | YKTUP | WBEJD | KATTUP WE EAT |
| RAFLTTY | XGLRZZE | ENWQEEZ | AGRACES EVY |
| WATKINS | YTOQZGC | TYTPKNJ | Y2000 TYPING |
| HARRINGTO | NGXXOTMZU | BRHYTWINU | NGXXOTMZU BTWEEN U |
| DELGAIRO | JKRMGOXU | MSTLLCRQ | JACKER GOXU MYSTIL CROWL |
