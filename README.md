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

# Settings
## account.yaml
kintone subdomain, appliction id, api token

```yaml
domain: *****
apps:
    send:
        id: *****
        token: **********************************
```

## settings.yaml
mail settings

```yaml
mail:
    smtp: *****.*****.com
    port: 587 
    to: *****@****.***
    from: *****@****.***
    bcc: []
    #ex) [xxxx@domain.com, xxx@domain.com,..]
    password: *****
```

# Sample of command

```less
$ sudo sh indicator/run.sh 
Between 2017-06-05 and 2017-05-29
Members: 7,000 (+2,150)
PV: 6,000
UU: 400

Send to mail >>xxx@*****.***
```

# License

MIT
