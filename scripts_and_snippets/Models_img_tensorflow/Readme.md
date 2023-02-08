## Build The image
```bash
docker build -t lukeroy/dbe-models-eval:latest .
```

## Get Results as csv file
```bash
docker run -i lukeroy/dbe-models-eval:latest >results.csv
```


## how to check result
```python
reloaded_model = tf.saved_model.load(model)
reloaded_results = tf.sigmoid(reloaded_model(tf.constant(["This TF Hub model uses the implementation of BERT from the TensorFlow Models repository on GitHub."])))
print(reloaded_results)
```
