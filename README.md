# SMv2

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

基于 SM.MS 图床 API v2 的小程序。

## 安装方法

直接用 pip 安装我啦~

```bash
$ pip3 install smv2
```

## 使用方法

### 查看用户基本信息

在指定了 API Token 的情况下使用 `smv2 profile` 查看当前用户基本信息，例如:

```
┌SM.MS User Profile─┬────────────────────────┐
│ username          │ noc@nova.moe           │
├───────────────────┼────────────────────────┤
│ Role              │ user                   │
├───────────────────┼────────────────────────┤
│ Group Expire Time │ 2020-02-18             │
├───────────────────┼────────────────────────┤
│ Disk Usage        │ 2.12 MB                │
├───────────────────┼────────────────────────┤
│ Disk Limit        │ 5.00 GB                │
└───────────────────┴────────────────────────┘
```

### 上传图片

直接使用：

```bash
$ smv2 /path/to/image
```
例如：
```bash
➜ smv2 poster36.jpg
Upload without Token.
┌SM.MS Upload Status───────────────────────────────────────────────┐
│ Image URL    │ https://i.loli.net/2019/02/18/Q123f2TWhtnk1FR.jpg │
├──────────────┼───────────────────────────────────────────────────┤
│ Deletion URL │ https://sm.ms/delete/8Ymbq218218XlPIDg4ReE2rcTi   │
└──────────────┴───────────────────────────────────────────────────┘
```

若有 API Token，则可以在 `~/.smms` 文件中以如下形式写入后使用：

```ini
[sm.ms]
api_token=<Enter Your Token Here>
```

此时上传的文件就可以在 [sm.ms](https://sm.ms) 后台看到了，例如：

```
➜ smv2 potw1144a.jpg
Upload with Token:1A0G******IhBV
┌SM.MS Upload Status───────────────────────────────────────────────┐
│ Image URL    │ https://i.loli.net/2019/02/18/Q123f2TWhtnk1FR.jpg │
├──────────────┼───────────────────────────────────────────────────┤
│ Deletion URL │ https://sm.ms/delete/8Ymbq218218XlPIDg4ReE2rcTi   │
└──────────────┴───────────────────────────────────────────────────┘

```

![](https://i.loli.net/2019/08/04/3e8R1IAT4zsOlVu.png)

### 查看历史图片

对于用户已经上传的图片，可以在指定了 API Token 的情况下使用 `smv2 history` 进行查看，例如：

```
┌SM.MS User History─────────────────────────────────┬─────────────────────────────────────────────────┐
│ Image URL                                         │ Delete URL                                      │
├───────────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ https://i.loli.net/2019/02/18/Q123f2TWhtnk1FR.jpg │ https://sm.ms/delete/8Ymbq218218XlPIDg4ReE2rcTi │
├───────────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ https://i.loli.net/2019/02/18/Q123f2TWhtnk1FR.jpg │ https://sm.ms/delete/8Ymbq218218XlPIDg4ReE2rcTi │
├───────────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ https://i.loli.net/2019/02/18/Q123f2TWhtnk1FR.png │ https://sm.ms/delete/8Ymbq218218XlPIDg4ReE2rcTi │
├───────────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ https://i.loli.net/2019/02/18/Q123f2TWhtnk1FR.jpg │ https://sm.ms/delete/8Ymbq218218XlPIDg4ReE2rcTi │
└───────────────────────────────────────────────────┴─────────────────────────────────────────────────┘
```
