# -*- coding: UTF-8 -*-

#  参数
# 以下是调用函数时可使用的正式参数类型：
#
# 必备参数
# 关键字参数
# 默认参数
# 不定长参数

#=====================================================================#
# 必备参数
# 必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

#可写函数说明
def printme( str ):
    "打印任何传入的字符串"
    print(str);
    return;
#调用printme函数
# printme();
printme("11");

#=====================================================================#

# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
#
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
#
# 以下实例在函数 printme() 调用时使用参数名：

def printme1( str ):
    "打印任何传入的字符串"
    print(str);
    return;
#调用printme函数
printme1( str = "My string");



def printinfo( name, age ):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age);
    return;
#调用printinfo函数
printinfo( age=50, name="miki" );

#=====================================================================#

# 缺省参数
# 调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：


#可写函数说明
def printinfo( name, age = 35 ):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return;
#调用printinfo函数
printinfo( age=50, name="miki" );
printinfo( name="miki" );

#=====================================================================#
# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：


# 可写函数说明
def printinfo2( arg1, *vartuple ):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return;
# 调用printinfo 函数
printinfo2( 10 );
printinfo2( 70, 60, 50 );

#=====================================================================#