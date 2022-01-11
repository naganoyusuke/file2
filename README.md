# file2
システムの課題２です
# リポジトリの説明
Rosを使いノードを5つ用いて2倍,3倍,4倍,5倍にするリポジトリです。
# 開発環境の説明
Ubuntu20.04

Raspberry Pi 4(ubuntu os)
# 実行方法
```
chmod +x count.py
```
```
rosrun mypkg count.py
```
別の端末を立ち上げる

```
chmod +x twice.py
```
```
rosrun mypkg twice.py
```
別の端末を立ち上げる
```
chmood +x third.py
```
```
rosrun mypkg third.py
```
別の端末を立ち上げる

```
chmod +x fourth.py
```
```
rosrun mypkg fourth.py
```

別の端末を立ち上げる

```
chmod +x fifth.py
```
```
rosrun mypkg fifth.py
```

別の端末を立ち上げる

```
rostopic echo /fifth
```

# ライセンス
ライセンスファイルがありますのでそちらをご覧ください。





