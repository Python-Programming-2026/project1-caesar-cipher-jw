# 凯撒密码加密/解密工具

## 小组分工
- 代码：王惠乔
- README：姜怡柔

## 功能介绍

本工具实现了凯撒密码的加密和解密功能，支持对英文字母进行指定偏移量的加密/解密操作，同时保留非字母字符不变。

## 原理说明

凯撒密码是一种简单的替换加密技术，通过将字母按顺序移动固定位数来实现加密。例如，偏移量为3时，A会变成D，B会变成E，以此类推。

### 加密过程
1. 输入未加密文本
2. 输入偏移位数
3. 对文本中的每个字符进行处理：
   - 小写字母：将其转换为对应的ASCII码，计算偏移后的值，再转换回字符
   - 大写字母：同上
   - 非字母字符：保持不变
4. 输出加密后的文本

### 解密过程
1. 输入已加密文本
2. 输入偏移位数（与加密时使用的偏移位数相同）
3. 对文本中的每个字符进行处理：
   - 小写字母：将其转换为对应的ASCII码，计算偏移前的值，再转换回字符
   - 大写字母：同上
   - 非字母字符：保持不变
4. 输出解密后的文本

## 使用方法

1. 确保已安装Python环境
2. 运行 `caesar.py` 文件
3. 根据提示输入操作类型（加密或解密）
4. 输入相应的文本和偏移位数
5. 查看输出结果

## 示例

### 加密示例
```
请输入加密或解密：加密
请输入未加密文本：Hello, World!
请输入偏移位数：3
Khoor, Zruog!
```

### 解密示例
```
请输入加密或解密：解密
请输入已加密文本：Khoor, Zruog!
请输入偏移位数：3
Hello, World!
```

## 注意事项

- 偏移位数可以是任意整数，程序会自动处理超出26的情况（使用取模运算）
- 只对英文字母进行加密/解密，其他字符保持不变
- 区分大小写，大写字母和小写字母分别处理

## 代码结构

- `caesar_encryption()`: 实现加密功能
- `caesar_decryption()`: 实现解密功能
- 主程序：根据用户输入调用相应的函数

## 运行环境

- Python 3.x
- 无第三方依赖

## 所用知识点

1. 函数定义与调用（def 定义函数）
2. 输入输出（input、print、end=''）
3. 数据类型转换（int() 转整数）
4. for 循环遍历字符串
5. 条件判断（if-elif-else）
6. 内置函数（ord()、chr()）
7. 算术与取模运算（+、-、%）

## 参考资料

- [CSDN博客 - 凯撒密码实现](https://blog.csdn.net/mxlmhgzw/article/details/8042273?fromshare=blogdetail&sharetype=blogdetail&sharerId=8042273&sharerefer=PC&sharesource=2401_87388105&sharefrom=from_link)
- [CSDN博客 - 凯撒密码详解](https://blog.csdn.net/libaiup/article/details/135978923?fromshare=blogdetail&sharetype=blogdetail&sharerId=135978923&sharerefer=PC&sharesource=2401_87388105&sharefrom=from_link)
- [CSDN博客 - Python实现凯撒密码](https://python4u.blog.csdn.net/article/details/147730288?fromshare=blogdetail&sharetype=blogdetail&sharerId=147730288&sharerefer=PC&sharesource=2401_87388105&sharefrom=from_link)
- [CSDN博客 - 凯撒密码原理与实现](https://blog.csdn.net/dzh0622/article/details/80977810?fromshare=blogdetail&sharetype=blogdetail&sharerId=80977810&sharerefer=PC&sharesource=2401_87388105&sharefrom=from_link)
