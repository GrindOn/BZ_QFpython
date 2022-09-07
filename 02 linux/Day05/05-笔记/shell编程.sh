#!/bin/bash
# 第一行的注释，电脑在运行脚本时，会解析，用来表示默认的脚本命令
a=10  # shell里定义了一个变量a,它的值是10. 注意:等号两端不能有空格
# 使用 $ 获取变量的值
echo 下午好$a
echo "good afternoon$a"
# 单引号里的内容会原样输出
echo 'hi$a'
# echo `good`  反引号里的内容会被当做命令来执行
echo `whoami`

# shell 里使用=赋值运算符来定义变量，需要注意的是等号两端不能有空格
a=hello   # 定义了一个变量a,它的值是hello

# 使用 $ 来获取变量的值
echo $a

# shell里 $ 功能比较强大
a=1000

# ${变量名} 可以用来取值。 {} 大多数情况下可以省略
echo $a  # 使用$可以取值
echo ${a}  # 也可以用来取值

# 特殊的值
echo '$0的值是'$0  # $0 表示脚本文件的名字

# $1 ~ $n 表示第1到第n个参数
echo '$1的值是'$1
echo '$2的值是'$2

# $* 和 $@ 表示所有的参数
echo '$*的值是'$*
echo '$@的值是'$@

# $# 表示参数的个数
echo '$#的值是'$#

# $(cmd)  执行小括号里的命令
echo $(whoami) # 等价于  `whoami`

# $((表达式))
echo $((1+1))

# read 命令用来接收用户的输入
# read -p '请输入您的年龄' age
# echo $age


# 条件判断语句
if ls /;then   # if 可以来一个命令
    echo '命令执行成功了'  # 如果命令成功，执行这个语句
else
    echo '命令执行失败了'  # 如果命令不成功，执行else语句
fi

# 数值的比较
# >:-gt  <:-lt  >=:-ge  <=:-le ==:-eq  !=:ne
if [ 3 -gt 2 ];then
	echo '3>2'
else
	echo '3不大于2'
fi

#read -p '输入一段内容' x
#read -p '再输入一段内容' y
#if [ $x = $y ];then
#	echo "$x等于$y"
#else
#	echo '不等于'
#fi

# if [ $x != $y ];then
#	echo '不等于'
#else
#	echo '等于'
#fi

#if [ $x -gt $y ];then  # 此写法仅支持数字比较

#if [[ $x > $y ]];then
#	echo $x大于$y
#else
#	echo $x不大于$y
#fi

# read -p '请输入一个路径' path

#if [ -d $path ];then
#	echo $path是一个文件夹
#else
#	echo $path不是一个文件夹
#fi

#case语句的使用，条件判断语句，用来判断相等的情况
#read -p '请输入您要执行的操作' op
#case $op in
#	1)
#		echo 添加用户
#		;;
#	2)
#		echo 删除用户
#		;;
#	3)
#		echo 查询用户
#		;;
#	*)
#		echo 输入的操作不正确
#		;;
#esac

# shell里的for循环
for i in `seq 1 10`  # for...in循环，相当于Python for in in range(1,11)
do
	echo $i
done

# C语言风格的for循环
for((j=0;j<=10;j++))
do
	echo $j
done

#function foo()
foo(){  # function 可以省略不写
	echo 'foo里$0'$0
	echo 'foo里$1'$1
	echo 'foo里$2'$2
	echo 'foo里的$#'$#
	echo 'hello'
	echo 'good'
}
foo 10 12 34 58 74

# 数组的使用，可以理解为Python里的列表
names=(hello 12 34 good 8)

# $names取出这个值以后，再 [3]
echo $names  # 默认获取数组里的 0 个数据
echo $names[3]  # hello[3]而不是 good
echo ${names[3]}  # 需要加 {} 

# * 和 @ 都能获取到所有的数据
echo ${names[*]}
echo ${names[@]}

# 获取数组长度
echo ${#names[*]}
echo ${#names[@]}

# 遍历数组
for n in ${names[@]}
do
	echo $n
done

for((x=0;x<${#names[@]};x++))
do
	echo ${names[x]}
done

