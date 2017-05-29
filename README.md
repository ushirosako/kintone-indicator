# kintone-indicator

最新の異なるkintoneレコードの数値を集計し、その結果をメール送信するプログラムです。

It is a program to compile the numerical values of the latest different kintone records and e-mail the results.

# Environments

- Python 3.5.3
- PyYAML
- pykintone https://github.com/icoxfog417/pykintone
- kintone

# kintone App

| FieldCode       | FieldType       | DefaltValue          |
|:----------------|:----------------|---------------------:|
| Date            | Date            |                Today |
| Member          | Number          |                    0 |
| PV              | Number          |                    0 |
| UU              | Number          |                    0 |

# Sample of command

~~~less
$ sudo sh indicator/run.sh 
Between 2017-06-05 and 2017-05-29
Members: 5000 (+150)
PV: 5,000
UU: 300

Send to mail >>xxx@*****.***
~~~

# License

MIT
