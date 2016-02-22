import string

end = "  </circuit>\n</project>"

template = open("basic.txt", "rb")


class Labeler():
    def __init__(self):
        self.main()
    
    def make_label(self, number, pattern, letter=None):
        label_list = []
        if pattern == "single":
            for i in range(number):
                label_list.append(letter+str(number))
        if pattern == "upper":
            alpha = list(string.ascii_uppercase)
            for i in range(number):
                label_list.append(alpha[i])
        if pattern == "lower":
            alpha = list(string.ascii_lowercase)
            for i in range(number):
                label_list.append(alpha[i])
        
        return label_list

    def write(self, output, component):
        name = "Pin"
        if component == "tunnel":
            name = "Tunnel"
        if component == "out":
            pass
        elif component == "in":
            pass
            
        #labels = self.make_label()
        
        
    def main(self):
        output_name = "labelOutput.circ"
        output = open(output_name, "wb")
        for line in template:
            output.write(line)
        
        self.write(output, "out")
        
        output.write(end)
        output.close()

if __name__ == "__main__":
    Labeler()
    template.close()
