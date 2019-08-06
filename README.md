# SMv2

基于 SM.MS 图床 API v2 的小程序。

## 安装方法

先安装我啦~

```bash
$ pip3 install smv2
```

## 使用方法

直接使用：

```bash
$ smv2 /path/to/image
```
例如：
```bash
➜ smv2 poster36.jpg 
Upload without Token.
┌SM.MS Upload Status───────────────────────────────────────────────┐
│ Status       │ True                                              │
├──────────────┼───────────────────────────────────────────────────┤
│ Image URL    │ https://i.loli.net/2019/08/04/slU3yuD1cr9hSNQ.jpg │
├──────────────┼───────────────────────────────────────────────────┤
│ Deletion URL │ https://sm.ms/delete/YDNzFTn1A4X3QORb9JCieM2ohs   │
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
│ Status       │ True                                              │
├──────────────┼───────────────────────────────────────────────────┤
│ Image URL    │ https://i.loli.net/2019/08/04/pgTkdFXm2IsORBx.jpg │
├──────────────┼───────────────────────────────────────────────────┤
│ Deletion URL │ https://sm.ms/delete/M8PCZ6fuW1br2qlswKyiTHRBUh   │
└──────────────┴───────────────────────────────────────────────────┘
```

![](https://i.loli.net/2019/08/04/3e8R1IAT4zsOlVu.png)

## TODOs

- [x] 支持基于 API Token 的图片上传
- [ ] 获得用户历史上传记录