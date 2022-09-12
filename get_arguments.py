'''
This function is using for set parameters(including super-parameters) for your model;
usage: python get_arguments.py --model_name=xxx --learning_rate=xxx --input_path=xxx --output_path=xxx
if you don't set any(or anyone) parameters, it will use default set
'''

import argparse
def get_arguments():
    # (1) 声明一个parser
    parser = argparse.ArgumentParser()#参数解析器

    # (2) 添加参数
    parser.add_argument("--model_name",default="transformer",type=str,help="the name of the model")
    parser.add_argument("--learning_rate",type=float,default=0.001) 
    parser.add_argument("--input_path",default="\d\myfile\input",help="the path of the input file") 
    parser.add_argument("--output_path",default="\d\myfile\output",help="the path of the output file") 

    # (3) 读取命令行参数
    args = parser.parse_args()
    return args

def main():
    myargs=get_arguments()
    print("model name:",myargs.model_name)
    print("learning rate:",myargs.learning_rate)
    print("input file path:",myargs.input_path)
    print("output file path:",myargs.output_path)

if __name__=="__main__":
    main()