from argparse import ArgumentParser

if __name__ == "__main__":
    #Initialize parser
    parser = ArgumentParser(description = "my math script")

    #Add the parameters positional/optional
    parser.add_argument("num1", help="Number 1", type=float)
    parser.add_argument("num2", help="Number 2", type=float)
    parser.add_argument("--operation", help="Provide Operator", default="+")
    #Parse the arguments
    args = parser.parse_args()
    result = None
    if args.operation == "+":
        result = args.num1+args.num2
    elif args.operation == "-":
        result = args.num1 - args.num2
    elif args.operation == "*":
        result = args.num1 * args.num2
    elif args.operation == "^":
        result = pow(args.num1, args.num2)
    print(result)
