# Zipper :
## How it's Work :
### A specific dictionnary type :
- {"str":"SOME_STRING","LM":["KEY_1",.....]}
- "str" can only be composed of "0" and "1" of any length
- "LM" is empty before encryption and filled with key after

## Functions Description :
### Generate(x) :
- Return an dictionnary : {"str":"SOME_STRING","LM":[]}
- "str" will be fiiled with a random ammount of 0 and 1
- "LM" will be empty

### Compress(Hm,X,xmax)
- Return an dictionnary : {"str":YOUR_ENCODED_STRING,"LM":["KEY_1",...,"KEY_X"]}
- Hm is a dictionnary like : {"str":SOME_STRING,"LM":[]}
- X is the number of key
- xmax is the lentgh max of the key use to encrypt

### UnCompress(Hm)
- Return a string of the decrypted string of the dictionnary given
- Hm is a dictionnary like : {"str":SOME_STRING,"LM":[]}
