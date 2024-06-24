def evalRPN(self, tokens: List[str]) -> int:
        
        stack =[]
        operator_map = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: y - x,
        "*": lambda x, y: x * y,
        "/": lambda x, y: y / x
        }

        for i in tokens:
            stack.append(i)
            if stack[-1] in operator_map and len(stack) >2: 
                operator = stack.pop()
                operand1 = stack.pop()
                operand2 = stack.pop()
                res = operator_map[operator](int(operand1),int(operand2))
                stack.append(res)
            
    
        return int(stack[0])