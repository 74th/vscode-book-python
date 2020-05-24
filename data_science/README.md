Using Python 3.7.2

```
curl -lO https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv
```

## 環境構築

### 環境分離に pyenv virtualenv を使う場合

```
# using MacOS mojave
# https://qiita.com/zreactor/items/c3fd04417e0d61af0afe
brew install python pyenv pyenv-virtualenv

# Python 3.8.2 のインストール
pyenv install 3.8.2

# 環境名 data_science の作成
pyenv virtuenv 3.8.2 data_science

pyenv local data_science
```

### 環境分離に venv を使う場合

VSCode は.venv を直接認識してくれます。

```
# Python はHomebrewなどパッケージマネージャを使用してインストール
brew install python

# .venv に環境を作成
python -m venv .venv

# bash で以後使えるようにする
source .venv/bin/activate
```

### パッケージ管理に requirements.txt を使う場合

```
pip install -r requirements.txt
```

### パッケージ管理に Poetry を使う場合

```
pip install --user poetry
```

```
# .venv ディレクトリが既にある場合、それを自動で読み込むようになる
poetry install
```
