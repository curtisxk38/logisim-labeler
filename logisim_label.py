import string
import sys


class Labeler():
    def __init__(self, component, number, pattern, letter):
        self.labels = self.make_label(int(number), pattern, letter)
        self.output = open("labelOutput.circ", "wt")
        self.comp = component
        
        self.x_initial = 100
        self.y_initial = 100
        self.x_change = 40
        self.y_change = 0

    def make_label(self, number, pattern, letter):
        label_list = []
        if pattern == "single":
            for i in range(number):
                label_list.append(letter+str(i))
        if pattern == "upper":
            alpha = list(string.ascii_uppercase)
            for i in range(number):
                label_list.append(alpha[i])
        if pattern == "lower":
            alpha = list(string.ascii_lowercase)
            for i in range(number):
                label_list.append(alpha[i])
        
        return label_list

    def write(self, component):
        name = "Pin"
        extra = ""
        if component == "tunnel":
            name = "Tunnel"
        if component == "out":
            extra = '\n      <a name="facing" val="west"/>'
            extra += '\n      <a name="output" val="true"/>'
            extra += '\n      <a name="labelloc" val="east"/>'
        elif component == "in":
            extra = '\n      <a name="tristate" val="false"/>'
        
        x = self.x_initial
        y = self.y_initial
        for i in self.labels:
            open_line = '\n    <comp lib="0" loc="({},{})" name="{}">'.format(x, y, name)
            label_line = '\n      <a name="label" val="{}"/>'.format(i)
            self.output.write(open_line)
            self.output.write(extra)
            self.output.write(label_line)
            self.output.write("\n    </comp>")
            x += self.x_change
            y += self.y_change
        
    def main(self):
        with open("basic.txt", "rt") as f:
            lines = f.readlines()
            self.output.writelines(lines)
        
        self.write(self.comp)
        
        self.output.write("\n  </circuit>\n</project>")
        self.output.close()

if __name__ == "__main__":
    comp = sys.argv[1]
    num = sys.argv[2]
    pattern = sys.argv[3]
    letter = None if pattern != "single" else sys.argv[4]
    Labeler(comp, num, pattern, letter).main()
    
