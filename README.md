# google-cloud-icons-for-plantuml

### docker imageのビルド

```
docker image build -t google-cloud-icons-for-plantuml:latest .
```

# 実行

```
docker run --rm -v ${PWD}:/app google-cloud-icons-for-plantuml scripts/icon-builder.py
```


```
# コンテナ内のpip freeze結果を吐き出す
docker run --rm -v ${PWD}:/app google-cloud-icons-for-plantuml -m pip freeze > requirements-on-container.txt
```