# Emoji 转中文

手动输入中文，并转化为 Emoji 表情。

## 文件

- inverse_emoji_dict:通过 emoji 检索对应的符号
- convertor：主程序，其中 method 为 emoji 产生方式，推荐使用方式 2
- emoji_dict_sim：为对 emoji_dict 进行谷歌翻译的结果。

## 示例

    Input: 文体两开花 弘扬中华文化
    Parameter: method=2, explain=Flase
    Input: 10 0 1 19 5 14 12 160 17 34 9
    Output: 📃📻🕑🔓🌺  📕🐑🏁📄📞

## 致谢

本代码参考了[ch2emoji](https://github.com/chroming/ch2emoji)